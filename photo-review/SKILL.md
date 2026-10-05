---
name: consystemai-photo-review
description: Review, deduplicate and recommend client-suitable Site Diary photos for a Weekly Client Update. Use within the Weekly Client Update Specialist by default, when a runtime delegates photo review to a separate worker, or when the builder asks to inspect or revise the photo selection.
---

# ConsystemAI Photo Review

Review the qualifying Site Diary photos for one named Wunderbuild Job and reporting period. This Skill provides the visual evidence-control and photo-selection method. It may run inside the Weekly Client Update Specialist or in a separate delegated worker where the runtime benefits from delegation.

## Scope

You may:
- read the named Job and Site Diaries;
- retrieve Site Diary attachment content;
- visually assess photos;
- deduplicate photos;
- number the unique reviewable set;
- mark photos Recommended or Available;
- revise the recommended set when asked; and
- make the selected source identifiers available to the calling Weekly Client Update workflow or delegated worker.

You must not:
- draft or send the client email;
- write to Wunderbuild;
- create schedules/routines;
- change project data;
- infer unsupported progress facts; or
- use browser/computer access for normal photo retrieval.

## Inputs

Accept:
- Job number or name;
- inclusive reporting period; and
- the Job timezone when supplied by the calling workflow or delegated worker.

If the Job or period is ambiguous, ask only for the missing clarification.

## Runtime portability

This Skill defines the canonical photo-review logic and required handoff. Keep runtime-specific tool names, browser mechanics, image rendering methods, navigation instructions and bot-to-bot transfer mechanics outside the canonical Skill where practical.

Use the runtime's supported authorised Wunderbuild and file/image capabilities without changing the evidence standard, selection rules or builder-facing outcome. If the runtime cannot retrieve or visually inspect the actual photo content, report the limitation rather than selecting from metadata alone.

## Retrieve photos

1. Resolve the Job and use its authoritative IANA timezone if not supplied.
2. List Site Diaries for the requested inclusive Job-local date range, widening the timestamp query where needed so UTC boundaries do not omit a qualifying diary.
3. Fetch each qualifying diary's detail and attachment metadata.
4. For every image attachment, retrieve the actual image content through the runtime's supported authorised Wunderbuild attachment/image capability, using the source Site Diary id and attachment id or equivalent stable identifiers.
5. Obtain a visually reviewable image representation, preferably JPEG where the runtime supports format choice, and visually assess the actual image content. Never select from filenames or metadata alone.
6. Prefer the structured Wunderbuild connection/API for attachment retrieval. Use browser/computer fallback only when the structured path cannot retrieve the required image content and the runtime's approved execution path supports that fallback.

## Deduplicate before review

Deduplicate the complete retrieved set before assigning builder-facing numbers.

Use exact underlying-content identity or deterministic digest where possible. Preserve all source provenance for duplicate groups, but show each unique image only once in the builder-facing review set.

Do not number duplicate copies separately.

## Build the unique-photo review set

For every unique usable photo, assign a stable review number for this review run:

- Photo 1
- Photo 2
- Photo 3
- etc.

Classify each as:

- **Recommended** — clear, client-suitable and representative of meaningful visible progress; or
- **Available** — usable and relevant, but not needed in the recommended set.

Exclude entirely:
- exact duplicates;
- blurred/unusable images;
- safety/privacy-sensitive images;
- irrelevant images; and
- images that materially pre-date or contradict the reported stage.

Prefer a representative recommended set, normally three to six photos, without forcing a target.

## Photo-review state and builder inspection

During a normal Weekly Client Update run, keep the full unique-photo review as internal workflow state and return only the Recommended set to the builder-facing Weekly Client Update result.

Retain for every unique usable photo:
- the actual visually reviewed image;
- stable review number;
- plain-language description;
- Recommended or Available status;
- source diary local date; and
- complete source identifiers/provenance.

If the runtime displays raw attachment/image results during retrieval, identify internally which displayed images are duplicates/excluded and which unique review number corresponds to each retained photo.

If the builder explicitly asks to inspect the wider photo set, present a clearly titled `Full Photo Review — [JOB]` containing the unique usable photo count, Recommended numbers, Available numbers and the actual unique image previews where supported.

The builder may revise the selection in ordinary language, for example:
- `Remove Photo 2 from the recommended set.`
- `Add Photo 6.`
- `Replace Photo 3 with the best Available alternative.`
- `Show me the alternatives for landscaping.`
- `Use Photos 1, 4 and 7.`

Maintain the current review selection within the active workflow so later revisions refer to the same numbering unless a brand-new review run is requested.
## Return to the Weekly Client Update workflow

When this Skill runs inside the Weekly Client Update Specialist, retain the following information in the active workflow state. When the Skill is delegated to a separate worker, return the same information as a concise machine-usable handoff:

- Job number/name;
- reporting period;
- unique review count;
- recommended review numbers;
- for every Recommended photo:
  - review number;
  - plain-language description;
  - source Site Diary id;
  - source Site Diary local date;
  - attachment id;
  - original attachment filename; and
- up to three Available alternatives with the same identifiers.

When running inside the same bot, reuse already retrieved image content where available. When delegated, transfer raw image content only if the runtime explicitly supports it; otherwise return the stable source identifiers so the calling Weekly Client Update workflow can retrieve only the Recommended images it needs to present.

## Selection revisions

If the builder changes the selection, update the current Recommended set and keep the revised selection available to the active Weekly Client Update workflow or delegated worker.

Never silently change the builder's explicit selection.
