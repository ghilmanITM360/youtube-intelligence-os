---
title: Falling From 100 km vs 1 km: Which One Hits the Ground Faster?
channel: UNREGISTERED (Unreasonably Exact; CH-id pending)
images: none (no images or media were created or stored)
---

# Slot 01 · LONG · Falling From 100 km vs 1 km: Which One Hits the Ground Faster?

- **Recommended title:** Falling From 100 km vs 1 km: Which One Hits the Ground Faster?
- **Calendar slot / day / format:** slot 01 · day 1 · Long (calendar band 3–5 min)
- **Version:** V2 (2026-11-24). Replaces nothing silently: the v1 text is preserved in `../../v1_baseline/`.
- **Word count (spoken text only, counted by script):** 706
- **Estimated runtime:** 4:41–5:06 (planning rate 2.5–2.75 words/second plus 1.5 s per paragraph break). **An estimate only: it must be confirmed by recording and listening.** The range 4:41–5:06 sits at the top edge of the owner's 3–5 minute band and is slightly over it at the calmer rate; v1 gave two different runtimes (4:45 and 3.5–4 min). Trimming the posture sentence in paragraph 14 or the recap in paragraph 12 would bring it inside the band.
- **Status:** DRAFT_WITH_OPEN_SCIENCE. Claude self-review only: no expert, human-listener or independent review has happened.
- **Required science checks before any release:** Drag coefficient and its change from subsonic to Mach ~3 (aerodynamicist); Air density above 86 km (recalled table, not re-read from the standard); Heating omitted: confirm it does not change arrival speed; Head-down posture treated only as a rough bound; Compare with owner-approved Day 1 v3 before any release choice

## Voice-over

Two people step off the edge of the sky at the same moment. One starts one kilometre up. The other starts a hundred kilometres up, at the Kármán line, one common convention for where space begins.

Neither has a parachute. Both start at rest and fall straight down. This is a thought experiment about speed, not advice, and it says nothing about whether a person would survive.

So, which one hits the ground faster? That question hides two others. Who arrives first? And who is moving faster at the moment of arrival?

Arrival time is the easy one. From one kilometre, the fall takes roughly twenty seconds. From a hundred kilometres, our model says between five and a half and six minutes. More height costs more time.

Arrival speed is the interesting one, so here are the rules of the model. Each person wears a pressure suit, falls belly down and holds that shape all the way. No wind, no spin. And the air pushes back with a force that grows with the square of your speed.

Start with the short fall. You gain almost ten metres per second, every second. As you speed up, the air pushes back harder. At around two hundred kilometres an hour, that push equals your weight, and you stop speeding up. That is called terminal speed, and one kilometre is almost long enough to reach it.

In our model, the person from one kilometre lands at about one hundred and ninety kilometres an hour. That number moves with posture and suit. Across the drag values we tried, it ranged from about one hundred and sixty to two hundred and five.

Now the tall fall. At a hundred kilometres the air is more than a million times thinner than at the ground. For the first minute or so, it hardly matters. The faller simply speeds up, almost ten metres per second, every second.

Around forty kilometres up, the model puts this person at their peak speed: roughly thirty-six hundred kilometres an hour, about three times the speed of sound at that height. That is the top of the speedometer. It is not the arrival speed.

Below that, the air thickens fast, and its push becomes stronger than gravity's pull. So the faller slows down while still falling. The speedometer climbs, peaks, and drops.

By the ground, the tall faller has been slowed to almost exactly the speed of the person who fell one kilometre. In the model, the two arrival speeds differ by far less than one percent.

So there are three different numbers. Time in the air: about twenty seconds against about six minutes. Peak speed: about one hundred and ninety against about thirty-six hundred. Arrival speed: about the same for both. Height changes the time and the peak. It hardly changes the arrival speed. The air sets that.

Only part of this has been measured. In 2012, Felix Baumgartner stepped out at about thirty-nine kilometres and reached about thirteen hundred and fifty-eight kilometres an hour. In 2014, Alan Eustace jumped from about forty-one. The highest jump on record is therefore about forty-one kilometres. Everything above that here is calculation.

And the calculation has limits. It assumes the air pushes back in a fixed way even near three times the speed of sound. Real drag changes with speed and with how thin the air is, and the model leaves out heating. Posture matters too. A head-down shape, which we treat only as a rough bound, lands both people near two hundred and eighty to two hundred and ninety kilometres an hour, still within about three percent of each other.

So trust the shape of the result, not the decimals. Once a fall is long enough to reach terminal speed, a longer one does not change the arrival speed.

This is not how spacecraft come home. They return from orbit moving sideways at roughly twenty-eight thousand kilometres an hour, so they meet the air much faster and much hotter. Our two people start from rest.

So, which one hits the ground faster? In this model, neither. The fall from space takes longer and has a far faster middle, but the air hands both people back to about the same arrival speed.

## Sources
Claim-level sources, calculations and access dates: `FACT_CHECK_V2.md` and `../../MASTER_SCIENCE_CLAIM_LEDGER_V2.csv`. Model: `work/models/fall_model.py` (copied from the v1 package; 1-D vertical fall, quadratic drag, constant drag area over mass, RK4). Baumgartner/Eustace figures: see ledger.
