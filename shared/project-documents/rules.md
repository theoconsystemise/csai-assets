# Shared project-document policy contract

Contract version: 1.2.0

Use the existing [canonical email skill](../../project-document-control/SKILL.md)
as the single owner of the following reusable rule sections. Read their full text,
not this index as a substitute:

| Policy | Required section |
|---|---|
| Project identity and linked records | Project matching |
| Purpose, disciplines, exclusions and live destinations | Folder selection |
| Identity, conflicts, revisions and immutable records | Duplicate and revision rules |
| Tender basis, originals, extracts and lineage | Tender packages and derived documents |
| Eligibility, upload/readback and partial failures | Filing and verification |
| Tenant-scoped state, identity cache, checkpoints and concurrency | Persistent queue and audit |
| Decision reuse, changed proposals and correction authority | Decisions, corrections and learning |
| Exact approval for replacements, folders, sharing and corrections | Configuration and authority |

Do not copy these rules into a second independently edited policy. The email
workflow owns ordinary document rules; both intake routes use the separate quote policy. Project Document Import consumes
the named sections as policy, not as a command to run email intake.

Scope adapters explicitly differ:

- Import uses nominated folder access instead of mailbox access; source file/version
  IDs supplement message/attachment IDs. A processed ID alone never proves filing.
- Import always starts read-only and requires subsequent explicit bounded approval.
  Email automatic-clear-match permission does not transfer.
- Import uses its item-table audit contract; email builder presentation remains unchanged.
- Import does not inherit email menus, installation claims, cadence, schedules or
  morning emails. No source mutation is permitted.
- Quote exclusions route to [Quote Filing](../../supplier-subcontractor-quote-filing/SKILL.md);
  that workflow's exact estimation/QR/invited-response, price, GST, attachment, status,
  approval and readback rules remain its own. Both intake routes use the
  [source-neutral handoff contract](quote-handoff.md) 1.1.0 for automatic read-only
  assessment. A handoff does not authorise writes. Quote Filing 0.6.0 accepts email
  and folder sources; no second quote skill is required.

If a rule conflict or omitted edge case prevents a safe conclusion, hold it and
record the ambiguity. Never weaken immutable evidence, tenant separation, exact
identity, approval or stored-byte verification.

Maintenance: update methodology in the canonical email policy sections first.
For every policy change, review both workflows, update the import manifest dependency
hash and validated section anchors in the same release, bump the import release when
behaviour changes and rerun structural checks. A changed policy hash is a compatibility
review gate, not permission to silently load an unreviewed dependency.

Canonical baseline: `theoconsystemise/csai-assets` commit
`32afa24ef5f195498b9417cc3d7f9de3a75ff5a0`, including Quote Filing 0.5.0 and its
API reference 0.5.0. This release extends the current files; it must not restore
historical runtime profiles or narrower retired quote rules. Quote Filing owns the
approved missing-supplier/contact, missing-QR and association paths, automatic
Requested-to-Submitted save effects, attachment-preserving API sequence and
content-verification limits. The generic job-document stored-byte rule does not
override Quote Filing's explicit evidence-strength rules for supplier responses.
