# Import audit and state contract

Contract: 0.3.0. Use JSON/CSV plus a readable table when the runtime supports artifacts;
otherwise provide the complete table in chat and state the persistence limitation.
Audit export/storage must be in the authorised builder's configured private destination;
never upload customer audits or configuration to the skill repository or source folder.
Local audit/checkpoint persistence is allowed for a read-only run; no source/Wunderbuild
write or external communication is implied. If durable state is unavailable, report it;
filing is blocked until state and safe serialization exist.

## Run record

Record run ID, tenant, operator, skill/version/commit/dependency hashes, adapter/runtime
versions if known, mode, source account/root/link, scope/exclusions/limits, start/end
times/timezone, verified Wunderbuild workspace, project candidate chain/link evidence,
selected entity IDs and links, folder-map observation, traversal pages/tokens/errors,
comparison coverage, state availability and missing email context.

## One row per discovered document occurrence

Include these fields even when unknown (use null plus reason, never invented values):

| Field | Contents |
|---|---|
| Item/source identity | Stable item ID, tenant, provider/account, source file ID/version, parent/path, archive/member or native/export lineage |
| Source link and name | Verified source link, original filename, MIME, byte size and deterministic SHA-256 where obtained |
| Target project | Candidate evidence, linked lead/estimate/job IDs/links, selected entity or Unconfirmed |
| Existing Wunderbuild match | Every relevant document ID/link/folder, verified identity/content evidence, coverage gaps |
| Classification | Purpose, discipline, lifecycle, historical/tender/contract protection |
| Duplicate/revision finding | Already present / Exact duplicate / Missing / Possible revision / Conflict / Historical / Unresolved; old/new references and reason |
| Proposed destination/action | Live folder ID/path/access, No action / File original / Review / Quote handoff / Approved derivative; each copy separately |
| Supporting evidence | Observed page/title block, number/revision/issue, hashes/cache provenance, links, builder-provided statements clearly labelled |
| Decision required | Exact missing question or proposal version/action/approver; unresolved context including missing email |
| Processing status | Discovered / Inspected / Proposed / Held / Quote handoff / Already present / Duplicate skipped / Inaccessible / Unsupported / Unprocessed / Uploading / Uploaded — verification incomplete / Filed and verified / Failed before upload |
| Quote routing and result | Handoff ID, transport/receipt state, Quote Filing loaded version, exact estimate/QR/response, price/currency/GST/item mapping, proposal version and separate quote result; see [handoff contract](../../shared/project-documents/quote-handoff.md) |
| Execution history | Approval/cancellation, actor/time, intent, attempts, returned IDs, stored-hash/location/access verification, correction history |

Use append-only events plus current status; preserve earlier proposals and outcomes.
Distinguish inspection completion from filing status. One occurrence can be inspected
and held, or historical and already present. A duplicate within the source is not
already filed: identify a representative to propose and link other occurrences to it.
Same content in a different project is not proof of presence in the target project.

## Summary and coverage reconciliation

Report discovered document occurrences and unique identities separately; exclude folders
from document counts. Record archive-member counts separately from top-level files.
Assign exactly one primary outcome bucket per occurrence:

1. Already present (include verified exact-duplicate skips as a labelled subset).
2. Proposed for filing (no write yet).
3. Held (including unresolved revisions, conflicts and historical routing).
4. Quote handoff (all quote occurrences, with separate proposed/already-present/held/blocked/partial/filed subtotals; never double-count as ordinary filed documents).
5. Inaccessible.
6. Unsupported.
7. Unprocessed (including limit/interruption).
8. Filed and verified (only after a subsequent authorised run).
9. Uploaded — verification incomplete.
10. Failed before upload.

The buckets sum to discovered occurrences. Also report inspected count separately
(a coverage measure, not an additive bucket); count cached revalidated inspections
and newly inspected separately. Show historical/revision findings as additional labels.
Report all required totals, including zero counts; identify unknown counts for
unlisted inaccessible branches. Preserve excluded-item counts/reasons separately.

State source enumeration and content-inspection coverage independently from Wunderbuild
comparison coverage. Mark overall Complete only when every in-scope branch/page and
discovered relevant item is accounted for and required inspection/comparison succeeded.
Otherwise state Partial or Blocked, exact gaps and checkpoint/next action. An enumerated
but unreadable item is not inspected. Never call an interrupted listing complete or
say nothing is missing when inaccessible branches or target records remain unchecked.
