---
name: consystemai-weekly-client-update
description: Prepare an evidence-backed Weekly Client Update from a named Wunderbuild Job's Site Diaries and photos for an inclusive reporting period. Use when asked to generate, revise or prepare delivery of a weekly client update, client progress update or Site Diary-based client report. Keep generation read-only, require builder review, and never send anything automatically.
---

# ConsystemAI Weekly Client Update

Prepare one builder-reviewable Weekly Client Update from live Wunderbuild evidence. Treat Wunderbuild as the source of truth and keep project contexts separate.

## Required inputs

Require only:

- Wunderbuild Job number or name; and
- either an explicit inclusive reporting-period start and end date, or an unambiguous natural-language period such as `last week`.

Manual operation examples include `Prepare last week's client update for J-01084` and `Prepare the client update for J-01084 from 21 September to 27 September`.

Ask only for genuinely missing or ambiguous inputs. Never ask the user for internal IDs, Site Diary IDs, timezone, photo choices, output format or delivery method before generation.

## Manual invocation

This release is manual-only. Installing or loading this skill must not create, enable or depend on a routine, schedule, startup trigger, watcher or automatic inbox process. Run only after an explicit builder request in the bot conversation. Once invoked, carry out the permitted workflow steps without asking for approval at every read-only step; stop only for a genuinely ambiguous input, a reserved builder decision or an external write requiring the explicit delivery choice defined below.

## Safety boundary

- Search the named Job before using an ID.
- Use read-only Wunderbuild operations during generation.
- Never create, alter, publish, share or delete anything in Wunderbuild.
- Never fabricate records, images, files, retrievals or support for a statement.
- Treat every result as a draft requiring builder review.
- Never send an email or Wunderbuild communication automatically.
- Create an unsent email draft only after a separate explicit user instruction and confirmed sender, recipient and subject.
- If a connector cannot guarantee draft-only behaviour, stop without creating anything.

## Resolve the Job and reporting period

1. Search using the supplied Job number or name. Prefer an exact Job-number match.
2. Continue automatically when exactly one Job resolves.
3. If several Jobs genuinely match, show up to three Job-number/name choices.
4. If no Job matches, request a corrected reference.
5. Read the resolved Job's authoritative IANA timezone. Stop if it is missing or invalid.
6. Resolve any relative period in the Job timezone. `Last week` means the previous Monday through Sunday, inclusive, in that timezone. Do not use the computer's local timezone unless it is the same as the Job timezone.
7. Treat all reporting dates as Job-local calendar dates, not UTC dates.
8. If a natural-language period could reasonably mean more than one date range, show the interpreted inclusive range and ask for confirmation before retrieval. Do not ask when the range is unambiguous under these rules.
9. Validate that the start date is not later than the end date.

## Retrieve Site Diaries and photos

1. Query a widened timestamp window so UTC boundaries cannot omit a qualifying diary: local start minus one day through local end plus two days, using an exclusive upper boundary where required.
2. Paginate until retrieval is complete.
3. Convert each reliable `entryDateTime` into the Job timezone and retain only diaries whose local dates fall inside the inclusive period.
4. Retrieve diary details before filtering when a list row lacks a reliable timestamp.
5. Flag title, timestamp or diary-date inconsistencies in the audit.
6. Retrieve every qualifying diary's full questions, answers and attachment metadata using the Site Diary detail operation.
7. For every photo/file attachment on a qualifying diary, retrieve the actual attachment content through the Wunderbuild document-content operation using:
   - action: `get_attachment_content`
   - sourceType: `SITE_DIARY_ATTACHMENT`
   - the resolved Site Diary id; and
   - the attachment id from that diary.
8. For every Site Diary image attachment, call `get_attachment_content` with `mode: images` and explicitly set `imageFormat: jpeg`. Do this on the first retrieval for visual assessment — do not use the tool's default WebP render and do not rely on converting a WebP later. If original uploaded-file bytes become directly available in a future connector response, prefer those originals; otherwise the JPEG render is the canonical working copy for review, selection, ZIP packaging and Gmail attachment. Do not treat `uploadUrl: null`, filename, MIME type, size or other attachment metadata as evidence that the photo is unavailable.
9. The built-in browser is not part of the normal photo-retrieval path. Do not use browser/computer access for Site Diary photos unless `get_attachment_content` itself fails or returns no usable content, and record that exact failure.
10. Reuse retrieved records and photo bytes instead of repeatedly fetching them.
11. Record each failed retrieval without inventing a substitute.

## Control the evidence

- Read all qualifying diary responses before drafting.
- Link every material client-facing fact to its diary, local date, diary name, field and response.
- Consolidate identical or overlapping entries without multiplying progress, labour, incidents, delays or milestones.
- Preserve all contributing sources in the audit.
- If material facts conflict and reliable evidence does not resolve them, omit the client-facing claim and flag the conflict.

Prioritise meaningful visible progress, important work completed or underway, supported milestones and information the homeowner reasonably needs.

Normally exclude workforce counts, attendance, sign-ins, routine safety administration, minor incidents without project impact, minor plant interruptions, routine deliveries, internal trade coordination, housekeeping administration, internal commercial information and minor rectification administration. Record material exclusions in the audit.

## Draft the client update

- Write as an experienced Australian residential builder speaking naturally to the client.
- Sound like a real builder or project manager writing a weekly update, not a report generator.
- Avoid artificial project-name phrasing such as `work at your King Street home`, `at the King Street residence`, or repeatedly naming the project inside the body when the client already knows which job the email is about.
- Prefer natural openings such as `This week, work on the project...`, `This week, work at your home...`, `This week we completed...`, or lead directly with the progress made.
- Use the project/job name in the subject or heading where useful, but keep the body conversational and natural.
- Be professional, friendly, positive, factual and concise.
- Use two to four coherent paragraphs, normally 150–250 words when the evidence supports that length.
- Consolidate the reporting period rather than listing individual days or diaries.
- Do not mention Site Diaries, source records, evidence mechanisms or AI in client-facing text.
- Use Australian construction terminology, including `air conditioning` rather than `HVAC`.
- State `on schedule`, `ahead`, `delayed` or similar only when the reporting-period evidence directly supports it.
- Include `Coming Up` only when future work is explicitly recorded. Never infer the next construction stage.

### Tone examples

Prefer:
- `This week, work on the project progressed through the final services fit-off and external works.`
- `This week we completed the front path, landscaping and final services fit-off.`
- `Work at your home progressed well this week, with the front path, landscaping and final fit-off completed.`

Avoid:
- `This week, work at your King Street home progressed...`
- `Works at the King Street residence advanced...`
- repeatedly restating the street/project name in the body.

## Assess and select photos

1. Visually assess every successfully retrieved image.
2. Deduplicate before building the builder review set, using reliable underlying-content identity or exact digest where possible, not filename alone.
3. Preserve full provenance for duplicate groups in the audit, but never show duplicate copies as separate builder-review choices.
4. Build one **unique-photo review set** from the qualifying period.
5. Number every unique photo in that review set sequentially: `Photo 1`, `Photo 2`, and so on.
6. Mark each unique photo as either:
   - **Recommended** — clear, client-suitable and representative of meaningful reported progress; or
   - **Available** — usable and relevant enough to keep as an option, but not part of the recommended set.
7. Exclude from the review set entirely:
   - exact duplicates;
   - blurred or unusable images;
   - safety/privacy-sensitive images;
   - irrelevant images; and
   - images that materially pre-date or contradict the reported stage.
8. Never recommend or retain an image solely from its filename or metadata.
9. Prefer a representative recommended set, usually three to six photos, without forcing a target.
10. Retain the usable returned JPEG image content locally for review and packaging.

### Builder photo review

Create a local **Builder Review HTML** file as the canonical visual photo-review experience. Do not depend on OpenMaus chat itself to render the final review gallery correctly.

The Builder Review HTML must contain:
- the project/job and reporting period;
- the final draft client update;
- one visual card for every photo in the **unique-photo review set**, and no duplicate copies;
- each card's review number (`Photo 1`, `Photo 2`, etc.);
- the actual JPEG preview;
- a short plain-language description;
- a clear **Recommended** or **Available** label; and
- the current recommended selection summarised by review number.

Arrange the photo cards in a clean responsive grid that is easy for a builder to scan. Recommended photos must be visually obvious without hiding the Available photos.

After creating the Builder Review HTML:
1. validate that it opens;
2. verify every expected unique-photo card is present exactly once;
3. verify the displayed JPEGs correspond to the numbered review set;
4. expose the HTML file to the builder as **Open photo previews and full review**.

In the OpenMaus chat response, do not try to recreate the entire visual gallery. Instead:
- provide the **Open photo previews and full review** file/link first;
- state the recommended selection by number;
- provide the selected JPEG downloads and selected-photo ZIP;
- remind the builder they can reply naturally, for example:
  - `Remove Photo 3.`
  - `Add Photo 5.`
  - `Use Photos 1, 4 and 7.`
  - `Keep the recommended photos.`

Do not require the builder to make a change. If they accept the recommended set, that becomes the approved client-photo set.

OpenMaus may automatically display raw MCP image results earlier in the transcript while images are being inspected. Those platform-generated tool-result previews are not the Builder Review and may include duplicates. Never describe that raw gallery as the review set, and never use its order as the builder-facing photo numbering.

### Selected-photo files and ZIP

Create individual local `.jpg` or `.jpeg` files for every photo in the current approved client-photo set from the JPEG content returned by Wunderbuild, preserving a clear source-based filename where practical. Do not save or attach selected client photos as `.webp`.

Attach or expose the approved selected JPEG files as individually downloadable builder-review files when the runtime supports file attachments.

Create a ZIP containing only the approved selected unique photos and validate that it opens and contains exactly those selected files.

If Wunderbuild's attachment-content operation returns rendered images rather than original uploaded-file bytes, use those rendered JPEGs for review and packaging, label the limitation once, and never claim they are originals.

## Create Sources & Audit

Create one downloadable internal Sources & Audit report containing:

- Job, reporting period and Job timezone;
- every qualifying diary;
- source mapping for material claims;
- exclusions, conflicts, unsupported or omitted claims and data-quality warnings;
- timezone/date handling and title/timestamp inconsistencies;
- every unique photo, description, source diary/local date, selection status and reason;
- duplicate groups and complete provenance;
- retrieval, preview and file limitations; and
- any builder-added fact clearly labelled as builder-supplied.

Never expose the audit to the client or attach it to client communication.

## Return the builder-review result

Return the result in this order:

1. Project.
2. Inclusive reporting period and Job timezone.
3. Draft client update.
4. Builder Review HTML download/link (`Open photo previews and full review`) containing the visual unique-photo review set, numbered and marked Recommended or Available.
5. Current recommended/approved selection by photo number.
6. Individually downloadable approved selected-photo JPEG files after the Builder Review link, where the runtime supports file attachments.
7. Validated selected-photo ZIP with exact photo count.
8. Sources & Audit download.
9. Explicit statement that nothing was sent automatically.
10. Measured runtime, or state that runtime was not exposed.
11. Platform limitations, or `None recorded`.
12. Post-review delivery choice.

If required data, image content, ZIP creation or audit creation fails, preserve any valid written draft but label the overall result incomplete and state the exact limitation. Never claim that a file exists unless it was created and validated.

## OpenMaus inspection-display note

OpenMaus may automatically render image blocks returned by MCP tool calls while the workflow inspects them. Those tool-result images are evidence inspected during the run; they are not automatically part of the selected client photo set. Do not present or describe the full tool-result gallery as the final review package. The final review package must identify only the selected photos and provide the selected-photo files/ZIP separately.

## Builder review

- Accept ordinary-language wording revisions and photo-selection changes by review number.
- When the builder adds/removes/replaces photos, update Recommended/Available status as needed, rebuild the approved selection, regenerate/validate the Builder Review HTML, and rebuild/validate the ZIP using retained JPEG files.
- Never silently overwrite builder edits.
- Distinguish builder-supplied facts from Wunderbuild-supported wording.
- Do not move into delivery until the review package exists.

## Post-review delivery choice

After presenting the complete builder-review package, ask exactly:

> **Your Weekly Client Update is ready for review. What would you like to do next?**
>
> 1. Create Gmail draft
> 2. Prepare for Wunderbuild
> 3. No delivery yet
>
> Nothing will be sent automatically.

Do not choose an option for the user.

### Option 1 — Create Gmail draft

1. Require a separate explicit request to create the draft.
2. Confirm the connected sender account, recipient and subject. Never infer an ambiguous recipient.
3. Use the final client-ready update as the email body.
4. Attach only builder-approved photos as individual JPEG (`.jpg`/`.jpeg`) image files. Do not attach WebP versions.
5. Do not attach the ZIP, Sources & Audit report, provenance or internal notes.
6. Create an unsent draft only. Never send, schedule, reply, forward, publish or press Send.
7. Report the sender, recipient, subject, individual-photo attachment count and that the draft remains unsent.

### Option 2 — Prepare for Wunderbuild

Provide a manual Wunderbuild handoff containing:

- final copy-ready client update text;
- builder-approved photos as accessible individual files; and
- a clear note that the builder must choose the correct client conversation in Wunderbuild, attach the photos, review the message and send it manually.

Do not create, paste, publish or send a Wunderbuild message. Do not claim that Wunderbuild delivery has occurred.

### Option 3 — No delivery yet

Take no external action. Confirm that the result remains available for further builder review and that nothing was created or sent externally.

## Absolute prohibitions

Never:

- send a client communication;
- write to Wunderbuild;
- select an unconfirmed sender or recipient;
- attach internal audit material to client communication;
- expose credentials;
- fabricate supporting evidence; or
- imply that builder review or delivery occurred when it did not.
