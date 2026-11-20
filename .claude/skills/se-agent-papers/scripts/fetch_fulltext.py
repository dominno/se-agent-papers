#!/usr/bin/env python3
"""Retrieve open-access source texts for subsequent human/model review.

NOT a paper-reading or claim-verification system. Saves source HTML/PDF text
with origin + hash; it NEVER sets a review status to fulltext_reviewed.

Examples:
  python scripts/fetch_fulltext.py --id 2404.16130
  python scripts/fetch_fulltext.py --all --delay 3
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, os, re, sys, tempfile, time
from pathlib import Path
import requests


from paper_storage import FULLTEXT as OUT, METADATA, WIKI

CATALOG = WIKI / 'catalog' / 'papers.jsonl'
HEADERS={'User-Agent':'ResearchKnowledgeWiki/1.0 (personal research, polite rate limits)'}

def write_text(id,body,url,kind,version):
    if len(body.strip())<3500:
        raise RuntimeError(f'Parsed text is too small: {len(body)} chars')
    title=f'# Source full-text capture: {id}\n\nSource: {url}\nFormat: {kind}\nDocument: {version}\n\n'
    full=title+body
    data=full.encode('utf-8')
    file=OUT/f'{id}.md'
    file.write_bytes(data)
    meta={'arxiv_id':id,'retrieved_at':dt.datetime.now(dt.timezone.utc).isoformat(),
          'source_url':url,'source_format':kind,'captured_bytes':len(data),
          'sha256':hashlib.sha256(data).hexdigest(),
          'review_status':'retrieved_not_reviewed',
          'warning':'Machine-retrieved text is unreviewed. No fulltext_reviewed approval.'}
    (OUT/f'{id}.metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return file

def fetch(url):
    for attempt in range(3):
        try:
            response=requests.get(url,headers=HEADERS,timeout=(15,60),allow_redirects=True)
            if response.status_code in (429,500,502,503,504):
                time.sleep(4*(attempt+1));continue
            response.raise_for_status();return response
        except (requests.Timeout,requests.ConnectionError):
            if attempt==2:raise
            time.sleep(4*(attempt+1))
    raise RuntimeError('HTTP blocked or rate limited: '+url)

def parse_html(html):
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(html,'html.parser')
    for node in soup(['script','style','nav','footer','header']):node.decompose()
    main=soup.select_one('article') or soup.select_one('div.ltx_page_main') or soup.select_one('main')
    if main is None: raise RuntimeError('Cannot identify paper body')
    output=[];last=''
    for node in main.find_all(['h1','h2','h3','h4','p','li','figcaption'],recursive=True):
        if node.find_parent('li') and node.name!='li':continue
        content=' '.join(node.stripped_strings)
        content=re.sub(r'\s+',' ',content).strip()
        if not content or content==last:continue
        last=content
        if node.name.startswith('h'):output.append('\n'+'#'*int(node.name[1])+' '+content+'\n')
        elif node.name=='li':output.append('- '+content)
        elif node.name=='figcaption':output.append('_'+content+'_')
        else:output.append(content+'\n')
    return '\n'.join(output)

def read_pdf(data):
    try: import fitz
    except ImportError as e:raise RuntimeError('Install pymupdf for PDF extraction') from e
    import io
    doc=fitz.open(stream=data,filetype='pdf')
    output=[]
    for i,page in enumerate(doc,1):
        txt=page.get_text('text')
        output.append(f'\n## PDF page {i}\n\n{txt.strip()}\n')
    return '\n'.join(output)

def atomic_write(path, data):
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        tmp = Path(handle.name)
        try:
            handle.write(data)
            handle.close()
            os.replace(tmp, path)
        finally:
            tmp.unlink(missing_ok=True)


def matches_version(extract, version):
    if not extract.is_file():
        return False
    with extract.open("rb") as source:
        header = source.read(512).splitlines()
    return f"Document: {version}".encode() in header and b"## PDF page 1" in header


def restore_pinned(article, meta, force=False, batch=False):
    """Fetch the catalogued version and verify the audit digest when available."""
    version = meta["version"]
    if not re.fullmatch(re.escape(article) + r"v[1-9]\d*", version):
        raise ValueError(f"Invalid review version for {article}")
    pdf = OUT / (version + ".pdf")
    extract = OUT / (article + ".md")
    url = "https://arxiv.org/pdf/" + version
    downloaded = force or not pdf.is_file()
    download_url = f"https://export.arxiv.org/pdf/{version}" if batch else url
    data = fetch(download_url).content if downloaded else pdf.read_bytes()
    if not data.startswith(b"%PDF-"):
        raise ValueError(f"Expected a PDF for {version}")
    if meta.get("original_sha256") and hashlib.sha256(data).hexdigest() != meta["original_sha256"]:
        raise ValueError(f"PDF checksum differs from the audit for {version}")
    if downloaded or not matches_version(extract, version):
        body = read_pdf(data)
        heading = f"# Source full-text capture: {article}\n\nSource: {url}\nFormat: pdf-extracted\nDocument: {version}\n\n"
        capture = (heading + body).encode("utf-8")
        # PDF extraction may vary between PyMuPDF releases. The recorded digest
        # continues to describe the original audit copy.
        if downloaded:
            atomic_write(pdf, data)
        atomic_write(extract, capture)
        if meta.get("sha256") and hashlib.sha256(capture).hexdigest() != meta["sha256"]:
            print(f"{version}: PDF verified; local extraction differs from the archived text digest.", file=sys.stderr)
    return extract


def retrieve(id):
    htmls=[f'https://arxiv.org/html/{id}',f'https://ar5iv.labs.arxiv.org/html/{id}']
    errors=[]
    for url in htmls:
        try:
            res=fetch(url);parsed=parse_html(res.text)
            if len(parsed)<5000:raise RuntimeError('HTML too short for full text')
            return write_text(id,parsed,url,'html','version-unpinned-check-source')
        except Exception as ex:errors.append(f'{url}: {ex}')
    url=f'https://arxiv.org/pdf/{id}'
    try:
        res=fetch(url)
        if not res.content.startswith(b'%PDF'):raise RuntimeError('Not PDF payload')
        parsed=read_pdf(res.content)
        return write_text(id,parsed,url,'pdf-extracted','version-unpinned-check-source')
    except Exception as ex:errors.append(f'{url}: {ex}')
    raise RuntimeError('; '.join(errors))

def main():
    ap=argparse.ArgumentParser()
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--id',help='arxiv id, e.g. 2404.16130')
    group.add_argument('--all',action='store_true')
    ap.add_argument('--delay',type=float,default=3.0,help='minimum seconds between source requests')
    ap.add_argument('--force',action='store_true',help='redownload existing full text')
    args=ap.parse_args()
    if args.delay < 3:
        ap.error('--delay must be at least 3 seconds')
    OUT.mkdir(parents=True, exist_ok=True)
    ids=[json.loads(x)['arxiv_id'] for x in CATALOG.read_text().splitlines() if x.strip()] if args.all else [args.id]
    successes=0;errors=[]
    for ix,id in enumerate(ids,1):
        if not re.fullmatch(r'\d{4}\.\d{4,5}',id):raise ValueError(id)
        target=OUT/f'{id}.md'
        metadata = METADATA / f'{id}.metadata.json'
        meta = json.loads(metadata.read_text(encoding='utf-8')) if metadata.is_file() else {}
        pinned = bool(meta.get('version'))
        try:
            force = args.force
            if not force:
                if pinned:
                    pdf = OUT / (meta['version'] + '.pdf')
                    if pdf.is_file() and meta.get('original_sha256'):
                        force = hashlib.sha256(pdf.read_bytes()).hexdigest() != meta['original_sha256']
                    ready = pdf.is_file() and matches_version(target, meta['version'])
                else:
                    ready = target.is_file()
                if ready and not force:
                    print(f'[{ix}/{len(ids)}] skip existing {id}');continue
            if ix>1:time.sleep(max(args.delay,0))
            result=restore_pinned(id, meta, force, args.all) if pinned else retrieve(id);successes+=1
            print(f'[{ix}/{len(ids)}] downloaded (not reviewed) {result.name}',flush=True)
        except Exception as ex:
            print(f'[{ix}/{len(ids)}] failed {id}: {ex}',file=sys.stderr)
            errors.append({'arxiv_id':id,'error':str(ex)})
    if errors:
        (OUT/'download_errors.json').write_text(json.dumps(errors,ensure_ascii=False,indent=2)+'\n')
    print(f'Completed: new={successes} errors={len(errors)} total_requested={len(ids)}')
    return 1 if errors else 0

if __name__=='__main__':raise SystemExit(main())
