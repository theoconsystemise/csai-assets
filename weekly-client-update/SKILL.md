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

Treat every explicit Weekly Client Update request as a fresh evidence run unless the builder explicitly asks to continue or revise an earlier run. Retrieve the live Wunderbuild evidence for the requested period. Do not reference or reuse earlier review packages, cached drafts, prior photo numbering, prior photo selections or generated files unless the builder explicitly asks for that continuity.

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

## Retrieve Site Diaries and delegate photo review

1. Query a widened timestamp window so UTC boundaries cannot omit a qualifying diary: local start minus one day through local end plus two days, using an exclusive upper boundary where required.
2. Paginate until retrieval is complete.
3. Convert each reliable `entryDateTime` into the Job timezone and retain only diaries whose local dates fall inside the inclusive period.
4. Retrieve diary details before filtering when a list row lacks a reliable timestamp.
5. Flag title, timestamp or diary-date inconsistencies in the audit.
6. Retrieve every qualifying diary's full questions and answers for the written client update.
7. Do **not** retrieve every Site Diary photo in this bot. That would clutter the builder's main conversation with raw MCP image previews.
8. Delegate the photo review to the teammate named **Photo Review Specialist**, supplying:
   - resolved Job number/name;
   - resolved Job id if useful;
   - inclusive Job-local reporting period; and
   - Job timezone.
9. Ask the Photo Review Specialist to retrieve, visually inspect, deduplicate, number and recommend the qualifying Site Diary photos according to its installed skill.
10. Use the specialist's handoff to obtain the Recommended photos' Site Diary ids and attachment ids.
11. In this Weekly Client Update bot, retrieve **only the Recommended photos** via `get_attachment_content` with `sourceType: SITE_DIARY_ATTACHMENT`, `mode: images` and `imageFormat: jpeg`.
12. If the builder later asks to replace/add/remove a photo, coordinate with the Photo Review Specialist for the revised selection, then retrieve only any newly selected photos that this bot does not already hold.

If the Photo Review Specialist is unavailable or the delegation fails, report that limitation rather than reverting to retrieving every photo in the main conversation.

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

## Use the specialist photo selection

Treat the Photo Review Specialist as the source of truth for the current photo-review numbering, Recommended set, Available alternatives and duplicate decisions.

In this main Weekly Client Update conversation:

1. Show only the current Recommended photos.
2. Number them using the Photo Review Specialist's review numbers, not a new numbering scheme.
3. Show each Recommended JPEG preview where OpenMaus supports it.
4. Provide a short description under each Recommended photo.
5. State that the full unique-photo review and alternatives are available in the **Photo Review Specialist** bot.
6. Tell the builder they can simply say:
   - `Keep these.`
   - `Replace Photo 2.`
   - `Show me alternatives.`
   - `Use Photos 1, 4 and 7.`
7. For a change request, coordinate with the Photo Review Specialist and update the main-chat Recommended set.
8. Create individual local `.jpg` / `.jpeg` files only for the approved selected photos.
9. Create and validate a ZIP containing only the approved selected photos.

Do not retrieve or display all qualifying photos in this main bot. The detailed all-photo review belongs in the Photo Review Specialist conversation.

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
4. Recommended photos only, using the Photo Review Specialist's review numbers.
5. Note that the full unique-photo review and alternatives are available in the Photo Review Specialist bot.
6. Individually downloadable approved selected-photo JPEG files where supported.
7. Validated selected-photo ZIP with exact photo count.
8. Sources & Audit download.
9. Explicit statement that nothing was sent automatically.
10. Measured runtime, or state that runtime was not exposed.
11. Platform limitations, or `None recorded`.
12. Post-review delivery choice.

If required data, specialist photo review, image content, ZIP creation or audit creation fails, preserve any valid written draft but label the overall result incomplete and state the exact limitation. Never claim that a file exists unless it was created and validated.

## Builder review

- Accept ordinary-language wording revisions and photo-selection changes by review number.
- When the builder adds/removes/replaces photos, coordinate with the Photo Review Specialist, update the approved selection, retrieve only newly selected JPEGs as needed, and rebuild/validate the ZIP.
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
