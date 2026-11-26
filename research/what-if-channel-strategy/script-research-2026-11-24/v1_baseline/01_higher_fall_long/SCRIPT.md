---
title: Falling From 100 km vs 1 km: Which One Hits the Ground Faster?
channel: UNREGISTERED (Unreasonably Exact; CH-id pending)
---

# Slot 01 · LONG · Falling From 100 km vs 1 km: Which One Hits the Ground Faster?

**Calendar title:** Would a Fall From Space Make You Hit the Ground Faster?
**Format:** Long (calendar band 3–5 min) · **Draft:** v1 · **Status:** DRAFT_WITH_OPEN_SCIENCE (see STATUS_AND_OPEN_ISSUES.md)
**Word count (voice-over only):** 696 · **Estimated narration:** 4:45 (2.7 words/s + 1.5 s per paragraph break × 18 breaks; planning assumption, not a recording)
**Length choice:** about 3.5–4 minutes: one comparison, one turn, one limits section. It follows the observed median of longer What If-style explainers without padding; the owner's 3–5 minute band is respected.

## Voice-over

Two people step off the edge of the sky at the same moment. One starts a kilometre up. The other starts a hundred kilometres up, a height called the Kármán line, a common convention for where space begins.

Neither has a parachute. Both begin standing still, and both fall straight down. This is a physics experiment, not a recommendation.

Here is the question. Which of them hits the ground faster?

"Faster" can mean two things. Who gets there first? And who is moving faster when they arrive?

The first one is easy. From one kilometre, the fall lasts about twenty seconds. From a hundred kilometres, our simple model says about six minutes. Height costs time.

The second meaning is the interesting one, so let's set the rules. Each person wears a pressure suit, falls belly-down, and keeps that shape the whole way. No wind. No spin. We are only asking about speed, so we are leaving out anything about whether a person could survive.

Start with the short fall. You speed up by almost ten metres per second, every second. But the faster you go, the harder the air pushes back, and that push grows with the square of your speed. At around two hundred kilometres an hour, the push would match your weight, and you would stop speeding up.

A kilometre is just long enough to get close. In our model, the person from one kilometre lands at around a hundred and ninety kilometres an hour. That number moves with body shape, suit and posture, from about one-sixty to two hundred in our versions.

Now the tall fall. At a hundred kilometres, the air is about two million times thinner than at the ground. For the first minute and a half, it hardly matters at all. You are simply falling, and you speed up by almost ten metres per second, every second.

By forty kilometres up, you are covering about a kilometre every second. In the model, that is somewhere around three and a half thousand kilometres an hour, about three times the speed of sound at that height.

Then the air thickens. Now it pushes back harder than gravity pulls, so you slow down while you are still falling. The speedometer climbs, peaks, and falls.

By the time the tall faller reaches the ground, the air has trimmed them back to the same speed as the person who fell a kilometre. In our model the two landing speeds differ by less than a fifth of one percent.

So, who hits faster? Neither. The air decides the landing speed, not the starting height. Drop from three kilometres, from ten, or from a hundred, and the model gives you about the same arrival speed.

The falls are not alike. The tall faller spends about six minutes in the air, goes through the speed of sound, and meets a lot of braking along the way. The model also leaves out heating, which at these speeds matters.

And here is where we need to be careful. Only part of this has ever been measured. In 2012, Felix Baumgartner stepped off from almost thirty-nine kilometres and reached about thirteen hundred and fifty-eight kilometres an hour. In 2014, Alan Eustace jumped from about forty-one. Nobody has jumped from anywhere near a hundred. Everything higher is a calculation, and it assumes the air pushes back in a fixed way even near three times the speed of sound. Real air does not behave quite that simply.

So, trust the shape of the result, not the decimals. The landing speed shifts with posture. Head-down, a rough bound puts both landings near two hundred and eighty to two hundred and ninety kilometres an hour, still within about three percent of each other. The air sets the speed, not the starting height.

This is not how spacecraft come home. They arrive at around twenty-eight thousand kilometres an hour, because they were already moving sideways at orbital speed. Our two people start from rest.

So here is the answer. The fall from space is not faster at the ground. It is longer, about six minutes of it, with the strange part in the middle.

## Sources
- Claim-level sources, calculations and uncertainty: FACT_CHECK.md and ../../08_MASTER_CLAIM_LEDGER.csv (claims V01-C01 to V01-C16).
- Baumgartner 2012 peak speed and exit height: Guerster & Walter 2017, PLoS ONE 12(12):e0187798 (https://pmc.ncbi.nlm.nih.gov/articles/PMC5720713/).
- Atmosphere: US Standard Atmosphere 1976 (own implementation; values above 86 km recalled, not re-read).
- Model: scripts/fall_model.py and scripts/finding_checks.py in this package (1-D vertical fall, quadratic drag, constant CdA/m).
