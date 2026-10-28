# Google Drive source adapter

Adapter contract: 0.1.0. Instruction-level implementation; Grok execution NOT TESTED.
Other providers, including OneDrive and Dropbox: extension points only, NOT IMPLEMENTED.
Do not claim a connector or SDK has been supplied by these instructions.

Use the runtime's authorised Drive connector/API where capable. Verify its actual
capabilities rather than assuming attachment/download/export or recursive traversal.
Verify the nominated folder ID, account and access; record shared-drive context when
applicable. Do not change permissions or request broader source access automatically.

Record the explicit root, recursion/depth, exclusions, shortcut policy and runtime
limits in the scope. List each scoped folder with all pages, child IDs and parent
relationships. Retain continuation tokens and folder-level failures. Include a
traversal ledger with listed/failed/limited folders and completion flags. A failed
branch means unknown unenumerated children; never report a zero count for them.
Source changes during a scan make it a time-bounded observation, not an atomic
snapshot; record changed versions and revisit unstable items before proposals.

Preserve provider, source account, file ID, parent IDs/path, original name, MIME type,
web link, size when supplied, version/revision/checksum tokens when exposed and
observed timestamps. Resolve links from retrieved metadata; mark unavailable links
explicitly rather than inventing them. A move/rename may preserve identity; a changed
file at the same path may not. Modified time/name/size alone cannot prove unchanged
content. Record both original and canonical identity when a shortcut is encountered.

Default: do not follow shortcuts outside the scoped root, arbitrary embedded links
or external download redirects. List them as excluded/held with reason. Follow an
internal shortcut only if explicitly in scope, with target access verified and
visited-ID deduplication preventing cycles; never expand the scope implicitly.

For ordinary binary files, obtain authorised original bytes; calculate SHA-256 with
a deterministic tool. Provider checksums using other algorithms are supporting
metadata, not a source SHA-256. Text previews are not original bytes. Record each
failed download, unsupported type, password/corruption/security hold, size/time limit
or unavailable OCR/render separately. Do not pretend unknown content was inspected.

Native Docs/Sheets/Slides have no original downloadable binary equivalent. If export
is technically available, treat it as a derived snapshot with native ID/version,
export MIME, export time and SHA-256, retaining native name/link separately. Preview
and recommend only until the exact export/format/derived filename is approved.
Do not call an export an unchanged original or infer native duplicate status from
its exported bytes. If export is unsupported, record unsupported and hold.

Archives: preserve parent identity and safe member paths, enumerate within explicit
expansion limits, prevent path traversal/cycles/decompression abuse, hash and inspect
members independently. Never flatten away lineage or execute content. Record unexpanded
members/archives and incomplete coverage. Hold unsupported archive handling.

For future providers require the same list/page/traversal, metadata identity,
authorised byte retrieval, version/change detection, link, error and checkpoint
contract. Add a separate tested adapter before enabling one; do not treat a generic
URL as an implemented integration.
