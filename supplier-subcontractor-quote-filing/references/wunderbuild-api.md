# Wunderbuild supplier-response API execution reference

Version: 0.5.0
Scope: estimation Quote Requests only. Companion to supplier-subcontractor-quote-filing/SKILL.md; it grants no authority beyond that skill and the builder's exact approval.
Evidence basis: builder-supplied Grok G1, H1 and I1 reports, October 2026. Revalidate current tool documentation in the executing runtime. These reports are not proof of support in every runtime.

## Execution sequence

1. Resolve the authorised estimation, quoteRequestId and supplier-response/subcontractor identifier from live records. Do not assume IDs or transplant identifiers from another account.
2. Read get_quote_request and obtain complete current response items, GST basis, attachments and status.
3. Inspect the live manage_estimation_quote_requests contract for update_subcontractor_response_items, its target parameter and exact item schema. Do not invent outer payload or item field names from this illustrative fragment.
4. Preserve existing attachment entries by sending each as {_id: existingAttachmentId}. Include the new file with name, type, actual byte size and newFile: true. I1 reported that omitted existing IDs are deleted: the list replaces the collection; a new-only list does not append.
5. Use the current item IDs and approved amounts; preserve unchanged lines. Set gstInc according to the evidenced price basis. The tested examples used ex-GST amounts and gstInc: false.
6. Call update_subcontractor_response_items. Use the returned signed upload URL to PUT the actual corresponding PDF bytes with the documented headers/content type. Treat the URL as a credential; do not log or publish it. Never use a guessed upload endpoint.
7. Read get_quote_request and get_attachment_content (or the runtime's documented equivalents). Confirm that the new PDF is on the selected supplier response and all previous attachments survive. Do not substitute request-header or estimation Documents attachments.
8. On ambiguous outcomes, read back before retrying. Preserve partial-success evidence; do not repeat the whole creation or upload sequence blindly.

Illustrative attachment fragment, not a complete request:

```json
{
  "attachments": [
    {"_id": "<each current attachment ID to retain>"},
    {
      "name": "<original filename.pdf>",
      "type": "application/pdf",
      "size": 12345,
      "newFile": true
    }
  ],
  "gstInc": false
}
```

Read all existing attachment IDs freshly. Do not copy placeholder values, infer actual byte size, or reuse a historical attachment list. For an initially empty collection, only the approved new-file descriptor is required.

## Supplier and Quote Request preflight

Inspect the supplier create/update and contact contracts. Supplier creation can permit omitted email while Quote Request association rejects it. Validate the supplier primary email or the selected linked contact's email before the full operation. Quote Request creation takes supplierId and optionally supplierContactId; do not add an undocumented email field to that request. Never send invitations merely to create or file.

Use documented estimation-level create_quote_request / add_suppliers_to_quote_request actions and verify each saved record. Do not substitute job-level schemas. Obtain required dates from evidence or the builder.

## Status and verification

G1/H1 reported automatic Submitted status after saving costs; I1 retained Submitted but refreshed dateSubmitted. Record these normal save effects. Do not infer an invitation was sent from status alone or deliberately alter acceptance state.

I1 retained the original attachment ID, added the second once and preserved prices. Its stored raw-byte hashes were unavailable: extracted-text/rendered-image fingerprints reportedly matched recovery copies. This supports content/identity preservation with a verification limitation, not byte-for-byte PDF equality. Source SHA-256 values must be labelled as source hashes.

Do not use the browser simply because a response already exists or is Requested. Retain browser execution as a fallback only for a specifically unsupported action.
