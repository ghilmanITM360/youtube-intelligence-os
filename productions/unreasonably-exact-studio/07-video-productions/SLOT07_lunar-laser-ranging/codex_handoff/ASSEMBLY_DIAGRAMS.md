# Assembly diagrams for compound assets

How the individual layers fit together. Draw order: lower number = further back. Arrows `->` mean "child of" (inherits parent's transform). All layers of one pose share one canvas and pixel registration.

## ASTRO_000_SYSTEM: Apollo astronaut (per pose: stand34, kneel34, side_step; canvas 3000x3000; ground contact (1500,2700))

```
astro_master_<pose>  (flat reference composite; also the REST TEST target)
└─ torso (ASTRO_004)  d46   pivot: hip line centre
   ├─ plss (ASTRO_005)  d43  rigid, behind torso/helmet
   ├─ helmet (ASTRO_001) d42 pivot: neck ring
   │   └─ visor (ASTRO_002) d44 pivot: helmet frame hinge
   │       └─ visor_reflection (ASTRO_003) d45  replaceable plate
   ├─ upper_arm_far (d40) -> forearm_far (d41) -> glove_far (d42)      [behind torso]
   ├─ upper_arm_near (d48) -> forearm_near (d49) -> glove_near (d50)   [in front]
   ├─ thigh_far (d39) -> shin_far (d40) -> boot_far (d41)              [behind]
   └─ thigh_near (d47) -> shin_near (d48) -> boot_near (d49)           [in front]
contact_shadow (ASTRO_011, code) child of ground contact point
```
Back-to-front: thigh_far, upper_arm_far, shin_far, forearm_far, boot_far, glove_far, plss, helmet, visor, reflection, torso, thigh_near, upper_arm_near, shin_near, forearm_near, boot_near, glove_near. Each child carries hidden overlap under its parent (see each brief, section 9).

Construction rule (UE 7.2 + HC 4.1): large pose change = pose replacement (cross-dissolve on matched ground point); small limb offsets (<= +-8 degrees) = rigid FK about the listed pivots with drawn suit joint rings; no mesh deformation (hard suit); contact shadow by code.

## RETRO_000_SYSTEM: Apollo 11 retroreflector array

```
retro_assembly_master (3000x2000, hero composite, ground contact bottom-centre)
├─ retro_assembly_frame  (RETRO_004 frame_34 + legs)  d45
│   └─ retro_assembly_faces (RETRO_002 faces mapped onto the tilted panel plane) d55
└─ shadow (RETRO_006, code) d44
Match-cut chain:  array front (RETRO_002 front)  ->  macro 3x3 (RETRO_002 macro)  ->  3-face cube (RETRO_005, apex = canvas centre)  ->  cutaway (RETRO_003, code)
Registration: face (5,5) centre in the front view, the macro crop and the cube apex are the same optical point (test B9).
```

## OBS_000_SYSTEM + TEL_000_SYSTEM: observatory scene (canvas 2160x3840 per plate)

```
back to front:
 d5   sky (OBS_005, code)
 d15  ridge far -> d17 ridge mid                                 (OBS_004)
 d30  building body (OBS_001) + window light (d31)
 d34  pylon_far (TEL_002)
 d35  azimuth base (TEL_002) -> pylon_near (d36)
 d36  telescope tube (TEL_001) -> cell box (d37) -> instrument housing (d38)   [seen THROUGH the slit]
 d40  dome shell with slit cut-out (OBS_002)
 d41  slit leaf_L, leaf_R (OBS_006)  children of the dome, slide outward
 d19  ridge near (OBS_004): behind the building, so the building base overlaps it (the building stands on the near ridge)
 d50  props sheet sprites (OBS_007)
 d92  dome rim front occluder (OBS_002), d90 interior occluder (OBS_003, interior shots only)
Telescope interior shot: interior back (OBS_003 d10) -> tel_* -> interior occluder (d90)
Axes: dome rotation = vertical axis through the ring centre; telescope tilt = altitude axis (bearing centre); azimuth = base centre.
Telescope draw order 34-38 is BEHIND the dome shell (40): the telescope shows only through the transparent slit; a dome rim front occluder (92) hides the telescope's lower end.
```

## EARTH_000_SYSTEM / MOON_000_SYSTEM: globes (runtime sphere mapping)

```
Earth (back to front): surface (d10) -> night lights (d15, masked by terminator) -> clouds (d20, drifts) -> terminator shade (d25, code) -> atmosphere rim (d30, code)
Moon:  globe texture (d10) -> terminator + limb darkening (d20, code)
Both use ONE sun direction function (light from the left, ~30 deg up; see PRODUCTION_ART_DIRECTION section 3).
Moon surface scene (back to front): black sky (d5) -> far hills (d10) -> terrain far (d40) -> terrain mid (d41) -> terrain near (d42) -> props (d50) -> astronaut + reflector (d45-55) -> dust (code, d60)
```
