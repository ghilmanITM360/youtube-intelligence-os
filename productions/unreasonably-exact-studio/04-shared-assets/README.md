# 04 · Shared asset library (v2026-11-26)

These assets were extracted from Slot 07 V3 by **APFS clone**: the files are independent and the original project is unchanged. Every file's sha256 was checked against its source.

- **Index:** [`../11-production-management/REUSABLE_ASSET_INDEX.csv`](../11-production-management/REUSABLE_ASSET_INDEX.csv), 41 rows.
- **Per-family detail:** one `ASSET_CARD.md` in each family folder. It covers the master artwork, component layers, rigging, source files, reference evidence, licensing, validation results, usage and known limitations.

**Status meanings**
- `APPROVED_IN_FILM`: used in a film the owner accepted, and passed Claude's measured tests.
- `CANDIDATE`: tested in part, not used in a final film.
- `REJECTED`: listed only so it is not reused.

**Nothing here is a blanket approval for any future shot.** Re-run the card's proof test in each new scene.

| Family | Folder | Future reuse |
|---|---|---|
| Earth | `celestial/earth/` | spaceflight, tides, orbital mechanics |
| Moon | `celestial/moon/` | lunar missions, tides, distance |
| Celestial environments (code) | `celestial/space-environments/` | any space video |
| Lunar terrain | `environments/lunar-terrain/` | Moon scenarios |
| Observatory + telescope rig | `environments/observatory/` | astronomy, experiments |
| Apollo astronaut | `characters/apollo-astronaut/` | space exploration |
| Apollo 11 retroreflector | `props/retroreflector/` | optics, lunar ranging |
| Stopwatch (code) | `graphics/stopwatch/` | time and measurement |
| Scientific motion graphics (code) | `graphics/scientific-motion/` | science explainers |
| Parallax components (code) | `rigs/parallax/` | general animation |
| Fonts | `fonts/` | captions and labels |

**Not extracted:**
- The Slot 02 skydiver character: its rig is bound to the V15 renderer. It is listed in the index with its location.
- The 4096×2048 textures are in the local library but are kept out of git (see the repo README for checksums).
