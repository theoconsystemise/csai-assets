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

## Runtime portability

This Skill defines the canonical workflow logic and required outcome. Keep runtime-specific tool names, browser mechanics, image/file rendering methods, navigation instructions and bot-to-bot handoff mechanics outside the canonical Skill where practical.

Use the runtime's supported authorised capabilities to complete the required workflow without changing the business rules, evidence standard, approval boundaries or builder-facing outcome. If a required capability is unavailable, report the limitation accurately rather than inventing a substitute action or weakening the workflow.

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

## Retrieve Site Diaries and review photos

1. Query a widened timestamp window so UTC boundaries cannot omit a qualifying diary: local start minus one day through local end plus two days, using an exclusive upper boundary where required.
2. Paginate until retrieval is complete.
3. Convert each reliable `entryDateTime` into the Job timezone and retain only diaries whose local dates fall inside the inclusive period.
4. Retrieve diary details before filtering when a list row lacks a reliable timestamp.
5. Flag title, timestamp or diary-date inconsistencies in the audit.
6. Retrieve every qualifying diary's full questions and answers for the written client update.
7. Apply the installed **ConsystemAI Photo Review** Skill to the qualifying Site Diary photos. By default, perform this photo-review method within the Weekly Client Update Specialist itself.
8. Retrieve the actual image content needed to visually inspect every qualifying image attachment. Never select photos from filenames or metadata alone.
9. Deduplicate, number and classify the unique usable photos according to the Photo Review Skill, preserving source provenance and stable review numbers for the run.
10. Build a representative Recommended set and retain the remaining usable photos as Available alternatives.
11. A runtime may delegate the Photo Review Skill to a separate worker only when delegation materially improves execution, permissions, context management or builder experience. A separate Photo Review bot is not required by this Skill.
12. Before writing the final builder-review response, ensure the actual image content for every Recommended photo has been retrieved and is available for visual presentation where the runtime supports it.
13. Show only the Recommended photos in the normal builder-review result. Do not intentionally dump the full qualifying photo set into the final response.
14. If the runtime automatically exposes raw image/tool previews during retrieval, continue the workflow and keep the final builder-facing result limited to the Recommended set.
15. If any Recommended photo cannot be visually retrieved or rendered in the builder-review response, label that preview as unavailable and do not pretend it was shown.
16. If the builder later asks to replace/add/remove a photo, use the retained Photo Review state to revise the selection and retrieve only any newly selected photo content that is not already available.

If the Photo Review Skill cannot be applied or the runtime cannot visually inspect the actual photo content, report that limitation rather than selecting from metadata alone.
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

## Use the Photo Review selection

Treat the current Photo Review state as the source of truth for review numbering, the Recommended set, Available alternatives and duplicate decisions.

In the Weekly Client Update conversation:

1. Show only the current Recommended photos.
2. Number them using the Photo Review Skill's stable review numbers, not a new numbering scheme.
3. Show each Recommended JPEG preview using the runtime's supported visual-preview capability. If a preview cannot be rendered, mark it unavailable and do not imply that it was shown.
4. Provide a short description under each Recommended photo.
5. Keep the full unique-photo review available internally for revisions or on explicit builder request; do not expose it by default.
6. Tell the builder they can simply say:
   - `Keep these.`
   - `Replace Photo 2.`
   - `Show me alternatives for Photo 2.`
   - `Use Photos 1, 4 and 7.`
7. For a change request, revise the current Photo Review selection and update the Recommended set while keeping the same review numbering where possible.
8. Create individual `.jpg` / `.jpeg` files only for the approved selected photos using the runtime's supported file-handling capability.
9. Create and validate a ZIP containing only the approved selected photos where the runtime supports file creation. If it does not, report that limitation without affecting the approved photo selection.

Do not display the entire qualifying photo set in the normal Weekly Client Update result. The detailed all-photo review is an internal review state unless the builder explicitly asks to inspect it.
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

Keep the builder-facing result simple. Do not expose internal workflow mechanics unless the builder asks.

Return only:

1. A clear heading: **Weekly Client Update — ready for review**
2. Project and inclusive reporting period.
3. The draft client update.
4. A **Recommended photos** section showing only the current Recommended photos, using the Photo Review Skill's review numbers.
5. A clear final action block at the very bottom:

> **What would you like to do?**
>
> - **Keep these photos**
> - **Show me alternatives**
> - **Replace a photo** — for example, `Replace Photo 2`

Nothing should appear after this action block.

Do not include Sources & Audit links, ZIP status, individual download links, runtime, platform limitations, duplicate explanations, internal photo-review notes, delivery options or technical commentary in this initial builder-review response.

Keep those internal artefacts available for verification or on request, but do not clutter the normal builder experience with them.

If the builder says **Keep these photos**, treat the current recommended photo set as approved and move to the post-review delivery choice.

If the builder says **Show me alternatives**, use the current Photo Review state to show a small set of useful alternatives in this conversation.

If the builder asks to replace a photo, revise the current Photo Review selection, present the replacement, and return the same simple action block again.

## Builder review

- Accept ordinary-language wording revisions.
- Accept `Keep these photos`, `Show me alternatives`, and natural replacement requests such as `Replace Photo 2`.
- Keep the detailed Photo Review state behind the scenes during the normal workflow. Do not require the builder to open another bot to change the selection.
- When alternatives are requested, return only a small useful set, not the entire photo library.
- When the builder changes the selection, revise the current Photo Review state and keep the same review numbering where possible.
- Do not create the final ZIP or client-delivery attachments until the builder has approved the photo set.
- Never silently overwrite builder wording edits.
- Distinguish builder-supplied facts from Wunderbuild-supported wording internally.

## Post-review delivery choice

Only after the builder has approved the wording and photo selection, ask:

> **Ready to deliver. What would you like to do?**
>
> - **Create Gmail draft**
> - **Prepare for Wunderbuild**
> - **No delivery yet**
>
> Nothing will be sent automatically.

Do not choose an option for the user.

### Option 1 — Create Gmail draft

1. Require a separate explicit request to create the draft.
2. Confirm the connected sender account, recipient and subject. Never infer an ambiguous recipient.
3. Resolve the client's preferred first name from the confirmed Wunderbuild client/contact record associated with the approved recipient. If the first name is missing or genuinely ambiguous, ask before creating the draft rather than guessing.
4. Resolve the builder's preferred sign-off name from builder configuration where available. If no configured sign-off exists, use a clearly verified sender/display name only when unambiguous; otherwise ask before creating the draft.
5. Build the email body in this form:

   `Hi [Client first name],`

   [final approved client-ready update]

   `Regards,`  
   `[Builder sign-off name]`

   Preserve any builder-approved wording edits in the update itself.
6. Attach only builder-approved photos as individual JPEG (`.jpg`/`.jpeg`) image files. Do not attach WebP versions.
7. Do not attach the ZIP, Sources & Audit report, provenance or internal notes.
8. Create an unsent draft only. Never send, schedule, reply, forward, publish or press Send.
9. Report the sender, recipient, subject, client greeting name, builder sign-off name, individual-photo attachment count and that the draft remains unsent.

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
