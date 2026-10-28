#!/usr/bin/env python3
"""Offline release structure/integrity checks; no service calls or runtime claim."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "project-document-import"


def validate(root=ROOT):
    base = root / "project-document-import"
    manifest = json.loads((base / "manifest.json").read_text())
    assert manifest["version"] == "0.3.0"
    assert manifest["repository"] == "theoconsystemise/csai-assets"
    assert manifest["runtime_validation"] == "NOT TESTED"
    assert manifest["providers"]["onedrive"] == "NOT IMPLEMENTED"
    for path, expected in manifest["sha256"].items():
        actual = hashlib.sha256((root / path).read_bytes()).hexdigest()
        assert actual == expected, f"Checksum mismatch: {path}"
    skill = (base / "SKILL.md").read_text()
    assert skill.startswith("---\n")
    front = skill.split("---", 2)[1]
    assert re.search(r"^name: project-document-import$", front, re.M)
    assert re.search(r"^description: .+", front, re.M)
    assert "Version: " + manifest["version"] in skill
    for dep in manifest["policies"]:
        text = (root / dep["path"]).read_text()
        for heading in dep["required_sections"]:
            assert "\n## " + heading + "\n" in text, f"Missing policy: {heading}"
    quote = (root / "supplier-subcontractor-quote-filing/SKILL.md").read_text()
    email = (root / "project-document-control/SKILL.md").read_text()
    handoff = (root / "shared/project-documents/quote-handoff.md").read_text()
    assert "name: supplier-subcontractor-quote-filing" in quote and "Version: 0.6.0" in quote
    assert "Version: 2026-10-28.2" in email
    assert manifest["shared_contract_version"] == "1.2.0"
    assert manifest["quote_handoff_version"] == "1.1.0"
    for text in (quote, email, skill):
        assert "quote-handoff.md" in text, "Missing shared quote contract reference"
    for heading in ("Routing and authority", "Required input envelope",
                    "Assessment and execution", "Required result and parent reconciliation"):
        assert "\n## " + heading + "\n" in handoff
    assert "current quote skill is email-based" not in skill
    for heading in ("Missing supplier", "Missing Quote Request or supplier response"):
        assert "\n## " + heading + "\n" in quote
    api_path = "supplier-subcontractor-quote-filing/references/wunderbuild-api.md"
    assert api_path in manifest["sha256"] and "Version: 0.5.0" in (root / api_path).read_text()
    for active in (skill, quote, email, handoff):
        assert "consystemai-openmaus-skills" not in active
    checked = 0
    for path in manifest["sha256"]:
        file = root / path
        if file.suffix != ".md":
            continue
        for dest in re.findall(r"\]\(([^)]+)\)", file.read_text()):
            if "://" in dest or dest.startswith("#"):
                continue
            target = (file.parent / dest.split("#")[0]).resolve()
            assert target.is_relative_to(root.resolve()), f"Escaping link: {dest}"
            assert target.is_file(), f"Broken link: {file}: {dest}"
            checked += 1
    return manifest, checked


if __name__ == "__main__":
    release, links = validate()
    print(json.dumps({"result": "PASS", "version": release["version"],
                      "checksummed_files": len(release["sha256"]),
                      "relative_links": links, "runtime": "NOT TESTED"}))
