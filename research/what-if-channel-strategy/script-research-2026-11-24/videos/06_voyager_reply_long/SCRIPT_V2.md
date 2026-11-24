---
title: How Do You Fix a Spacecraft When Every Reply Takes Two Days?
channel: UNREGISTERED (Unreasonably Exact; CH-id pending)
images: none (no images or media were created or stored)
---

# Slot 06 · LONG · How Do You Fix a Spacecraft When Every Reply Takes Two Days?

- **Recommended title:** How Do You Fix a Spacecraft When Every Reply Takes Two Days?
- **Calendar slot / day / format:** slot 06 · day 16 · Long (calendar band 3–5 min)
- **Version:** V2 (2026-11-24). Replaces nothing silently: the v1 text is preserved in `../../v1_baseline/`.
- **Word count (spoken text only, counted by script):** 610
- **Estimated runtime:** 3:58–4:20 (planning rate 2.5–2.75 words/second plus 1.5 s per paragraph break). **An estimate only: it must be confirmed by recording and listening.** Paragraph 10 (2026 status) must be rewritten if NASA's status changes; without it the video is about 40 seconds shorter.
- **Status:** DRAFT_WITH_OPEN_SCIENCE. Claude self-review only: no expert, human-listener or independent review has happened.
- **Required science checks before any release:** Recheck every NASA status sentence on production day (paragraph 10); Read the 2024-04-04 NASA/JPL post for the diagnosis wording; Confirm that the command-and-reply cycle (~45 h in April 2024) is the thing called 'two days'

## Voice-over

On the eighteenth of April, 2024, engineers sent a message to a spacecraft more than twenty-four billion kilometres away. Then they waited. Two days later, they learned it had worked.

The spacecraft was Voyager 1, launched in 1977. A radio signal needed about twenty-two and a half hours to reach it, NASA wrote at the time, and the answer needed as long to come back. One command and its reply took about forty-five hours.

Now imagine repairing something that way. On the fourteenth of November, 2023, Voyager 1 stopped sending science and engineering data that anyone could use. It still received commands and still followed them. It just was not reporting in a form engineers could read. For about five months, they had no readable view of its health.

That is a strange kind of broken, like a patient who can hear you while every monitor shows noise.

So how do you debug a machine that answers every forty-five hours? If each step waits for its reply, five months holds fewer than ninety turns. You cannot poke at it. You work out where the fault must be, and you plan each command carefully.

By March 2024, the team had found it. The trouble was in one of Voyager's three onboard computers, the flight data subsystem, which gathers data and packages it for the trip home. One memory chip in that computer had failed, and it had held part of the computer's software. Without that code, the science and engineering data came out unusable.

No technician can be sent to swap a chip, and this one could not be repaired. So the team moved the software instead. No single free area was big enough, so they split the code into sections and stored the sections in different places. Then they adjusted the sections so they still worked together, and updated every reference to where the code used to live.

Then came the part where the delay matters. They began with the section that packages engineering data and sent it on the eighteenth of April. On the twentieth, the spacecraft's reply showed the change had worked. For the first time in about five months, engineers could see how Voyager was doing.

It was not finished. NASA said the team would spend the following weeks moving the other affected software, including the code needed to return science data.

The story continues, and this part can change. On November nineteenth, 2026, NASA reported that Voyager 1 had reached one light-day from Earth, about twenty-six billion kilometres, so each message now takes about twenty-four hours one way. NASA also reported that on the fourteenth of November, 2026, the team found that Voyager 1 had stopped sending science and engineering data again. A carrier signal is still arriving, which NASA reads as a sign that the spacecraft is still pointing at Earth and its radio is working. The missing data points to the computer that collects and formats the spacecraft's data. NASA said finding the cause may take weeks or longer, and that it is checking whether this is connected to an outage of about two days in October, from which the spacecraft recovered on its own.

NASA has not said that this problem shares a cause with the one in 2023. Both were discovered on the fourteenth of November, which may only be a coincidence.

So why would a reply take about two days? Because every question has to cross a light-day each way. Fixing a distant spacecraft is less about speed than about making each command count and being willing to wait. Whether Voyager 1 answers this time is something nobody can say yet.

## Sources
Claim-level sources, calculations and access dates: `FACT_CHECK_V2.md` and `../../MASTER_SCIENCE_CLAIM_LEDGER_V2.csv`. NASA Voyager blog 2024-04-22; NASA release 2026-11-19; NASA Voyager blog 2026-11-18 (updated 2026-11-20).
