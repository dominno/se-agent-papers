"""Paths shared by the wiki and its optional external collection of papers."""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
METADATA = WIKI / "raw" / "metadata"
default_cache = Path.home() / ".local" / "share" / "se-agent-papers" / "fulltext"
FULLTEXT = Path(os.environ.get("SE_AGENT_PAPERS_FULLTEXT_DIR") or default_cache).expanduser().resolve()
project = ROOT
if ROOT.parent.name == "skills" and ROOT.parent.parent.name in {".agents", ".claude"}:
    project = ROOT.parents[2]
    if project == Path.home():
        project = ROOT
if FULLTEXT.is_relative_to(project):
    raise ValueError("SE_AGENT_PAPERS_FULLTEXT_DIR must point outside the skill repository.")
