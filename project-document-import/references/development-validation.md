# Development validation and source correction

Release: Project Document Import 0.3.0, 28 October 2026.
Canonical repository: theoconsystemise/csai-assets.
Baseline: 32afa24ef5f195498b9417cc3d7f9de3a75ff5a0.
Quote Filing: 0.6.0, extending canonical 0.5.0.
Project Document Control routing edition: 2026-10-28.2.
Shared document contract: 1.2.0. Quote handoff: 1.1.0.

## Source correction

The earlier Import 0.1.0/0.2.0 and Quote Filing 0.3.0 integration was written against
a retired private repository. Those prompts/releases are withdrawn for this work.
Do not install or run them, mix dependencies with this repository, or resolve their
access problem by publishing them. Load this release and every dependency from one
resolved canonical commit; report the exact versions and stop on retrieval failure
before customer access. Do not silently substitute an installed release.

This corrected build starts from the current canonical Project Document Control and
Quote Filing 0.5.0 files and API reference, not from the retired quote implementation.
It adds folder-source acceptance, shared handoff evidence and version reporting while
preserving Chief/specialist ownership, exact inherited approval, missing-supplier/contact
and missing-QR/response creation/association approval paths, no-send checks, original
attachment retention, MCP-first execution, permitted automatic status/timestamp changes,
partial-result reconciliation and the recorded content-verification limits.
The API reference 0.5.0 remains byte-for-byte unchanged.

Ordinary email intake, commands, builder presentation, stable display numbers,
completion-delivery state, classifications, folder rules and scheduling boundary remain
unchanged apart from explicit quote routing and dependency loading. Shared policy reads
the current email skill's named rule sections; no independent classification copy exists.
Builder configuration, source links, decisions and audit data stay outside this repository.

## Checks and runtime boundary

Run `python3 checks/validate_project_document_import.py`.
The check verifies manifest file hashes, policy/contract headings, canonical repository,
skill versions, required companion API reference and relative links. Validate frontmatter
separately against repository conventions; the existing Quote Filing frontmatter uses a
version field, which is retained for compatibility. A generic validator that rejects
that established field is not the repository contract.

Verify all saved files by readback at one final commit. Compare unchanged email sections
and the complete supplier API reference to the baseline. These are structure/integrity
checks, not live classification or execution tests.

Historical Grok G1/H1/I1 evidence for the API reference is preserved with its original
limitations; it does not prove the new folder-origin integration. New source-to-quote
assessment, transport, repeat/cross-source handling and approved execution remain
Grok NOT TESTED. No bot, scheduler, connector or delegation service is created here.
The same assistant can apply both skills; separate-specialist transport requires real
runtime capability and cannot be assumed from a handoff document.

No customer Drive or Wunderbuild access or filing occurs during development. No access
changes, customer messages, template sharing or production rollout are authorised.

## Next read-only acceptance

Reload this release at its verified canonical commit and report loaded skill/dependency
versions. Audit a nominated authorised folder; assess any quotes through Quote Filing
and return exact existing-response or create/associate-and-file proposals for review,
without writes. Missing email context is recorded and only blocks conclusions requiring
it. Report source/target coverage honestly and quote assessment separately from filing.
If no quotes are present, that branch remains NOT TESTED. Return observed output and
errors to the developer before a separately authorised bounded write test.
