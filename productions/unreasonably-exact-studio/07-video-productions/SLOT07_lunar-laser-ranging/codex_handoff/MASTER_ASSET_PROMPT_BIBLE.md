# Master asset prompt bible

Prompts are *starting points*. Every prompt below is paired with the saved reference images (paths) that must be attached or inspected first. Codex must verify the references, may improve the prompt, and must record the exact prompt used and rejected ones in `IMAGE_GENERATION_PROMPTS.md`.

## Prompt structure (use for every asset)
1. **Reference attachment line**: list the reference file paths and what to take from each (silhouette, proportions, colour, material).
2. **Subject and view**: the exact object, camera angle, canvas, and that it is ONE isolated asset.
3. **Geometry and counts**: proportions, numbers (cubes, fingers, struts).
4. **Style**: painterly-clean cinematic illustration, no outlines, no photographic noise.
5. **Light**: sun from the left, about 30 degrees up, hard shadows only where the brief says.
6. **Layering and background**: isolated on transparent or flat neutral background; separate layers requested explicitly.
7. **Negative list**: no text, numbers, arrows, rays, beams, lens flare, motion blur, logos, people's faces, cast shadow that is not requested, extra objects.

## Global negative prompt (append to every prompt)
"text, letters, numerals, arrows, diagrams, laser beams, light rays, lens flare, glow standing for light, motion blur, depth of field blur, logos, watermarks, signage, faces, extra limbs, extra fingers, fused geometry, floating parts, photographic noise, outlines, cartoon outlines"

## Earth
Must not change: Sun from the left about 30 degrees up (lit side left, night side right); cloud layer separate from surface; no light, shadow or atmosphere baked into the surface texture; same texture registration (wrap seam at the antimeridian, clean poles).

Failure modes: baked clouds or lighting in the surface map; seam or pole pinching; oversaturated land; atmosphere drawn as a thick halo; clouds with hard cut-out edges.

### EARTH_001_SURFACE
- attach / inspect first: `references/earth/earth_fullglobe_translunar_nasa_as17-148-22727.jpg`, `references/earth/earth_fullglobe_composite_nasa_bluemarble2012_e001788.jpg`, `references/earth/earth_moon_transit_dscovr_epic_nasa_e000670.png`, `references/earth/earth_crescent_deepspace_nasa_art002e014225.jpg`, `references/earth/earth_surface_nocloud_equirect_svs_nasa_3615.jpg`
- prompt skeleton: "Cloud-free Earth surface map: ocean, continents, polar ice. No light, shadow, atmosphere or clouds baked in. The only public cloud-free map (SVS 3615, 2048x1024) has a grey filler band at the north: the poles must be repainted clean. Canvas 4096x2048 equirectangular. Views: globe; limb at bottom of frame; top-down orbit view (north pole up, pole regions must be clean). Isolated asset, opaque RGB. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/EARTH_001_SURFACE.md`

### EARTH_002_CLOUDS
- attach / inspect first: `references/earth/earth_fullglobe_translunar_nasa_as17-148-22727.jpg`, `references/earth/earth_fullglobe_composite_nasa_bluemarble2012_e001788.jpg`, `references/earth/earth_moon_transit_dscovr_epic_nasa_e000670.png`, `references/earth/earth_clouds_equirect_svs_nasa_3615.jpg`, `references/earth/earth_layers_cloud_atmos_nightlight_svs_nasa_5570.jpg`
- prompt skeleton: "Independent cloud layer: white cloud formations with soft alpha, no shadow, drifts slower than the surface. No transparent public cloud layer exists: it is authored from the cloud references. Canvas 4096x2048 equirectangular. Views: globe; limb. Isolated asset, RGBA PNG, alpha = cloud density. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/EARTH_002_CLOUDS.md`

### EARTH_004_NIGHT_LIGHTS
- attach / inspect first: `references/earth/earth_nightlights_globalmap_nasa_blackmarble2012_e001593.jpg`, `references/earth/earth_layers_cloud_atmos_nightlight_svs_nasa_5570.jpg`, `references/earth/earth_lighting_equinox_diagram_wikimedia_blueshade.png`, `references/earth/earth_limb_night_airglow_cloud_deck_city_lights_iss_nasa_iss040e062704.jpg`, `references/earth/earth_nightlights_nadir_urban_road_network_iss_nasa_iss035e017286.jpg`
- prompt skeleton: "City-lights layer visible only on the night side (masked by the terminator). Used in the final pull-back. Canvas 4096x2048 equirectangular. Views: wide space view (B37). Isolated asset, RGBA PNG, emissive points on black alpha. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/EARTH_004_NIGHT_LIGHTS.md`

### EARTH_006_ATMOS_SLICE
- attach / inspect first: `references/earth/earth_limb_glow_iss_nasa_iss074e0089803.jpg`, `references/earth/earth_limb_edge_on_sunset_layers_iss_nasa_iss023e057948.jpg`, `references/earth/earth_limb_twilight_noctilucent_layer_iss_nasa_iss024e006136.jpg`, `references/earth/earth_limb_edge_on_sunrise_cloud_silhouette_shuttle_nasa_sts047-54-018.jpg`, `references/earth/diagrams_time_of_flight_range_diagram_wikimedia_20200501-time-of-flight.svg`
- prompt skeleton: "Side cross-section of the air over a ground limb, in layers with one turbulent band, for the atmosphere beat. Thickness is exaggerated and labelled magnified. Canvas 2160x1200. Views: side view, beam passes through. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/EARTH_006_ATMOS_SLICE.md`

## Moon
Must not change: Near side only; same maria/highlands layout in every Moon asset; sun from the left; black sky, hard shadows, sharp horizon, no atmosphere haze; no flag or hardware unless the brief names it.

Failure modes: Earth-like colours; craters repeating visibly; atmosphere haze; shadows pointing the wrong way; horizon too close or too curved for the camera height.

### MOON_001_GLOBE
- attach / inspect first: `references/earth/earth_moon_transit_dscovr_epic_nasa_e000670.png`, `references/earth/earth_crescent_withmoon_nasa_art002e014211.jpg`, `references/earth/earth_moon_scale_galileo_nasa_pia00342.jpg`, `references/moon/moon_limb_large_clean_edge_earth_behind_artemis2_nasa_art002e009287.jpg`, `references/moon/moon_limb_low_oblique_earth_peeking_over_horizon_artemis2_nasa_art002e021283.jpg`
- prompt skeleton: "Near-side-first Moon map: maria (incl. Tranquillitatis), highlands, major craters. The Apollo 11 site region must be locatable on it. Canvas 4096x2048 equirectangular. Views: globe (ground sky, schematic, top-down orbit view, closing pull-back). Isolated asset, opaque RGB. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/MOON_001_GLOBE.md`

### MOON_002_TERRAIN_SURFACE
- attach / inspect first: `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg`, `references/earth/earth_rising_moonhorizon_apollo11_nasa_as11-44-6552.jpg`, `references/astronaut/astronaut_apollo15_rear34_stoop_reach_boulder_long_shadow_nasa_as15-85-11437.jpg`, `references/moon/moon_surface_hard_shadow_slopes_ridge_horizon_apollo15_nasa_as15-85-11451.jpg`, `references/moon/moon_terminator_craters_artemis2_nasa_art002e014055.jpg`
- prompt skeleton: "Grey fine regolith ground plane in perspective; low albedo (dark grey) but HARD-LIT: crisp black shadows from the single sun direction, no fill light, no atmosphere haze, sharp horizon (reference: Apollo 11/12 surface photographs). Canvas 2160x3840 px (2x of 1080x1920). Views: low lunar-surface 3/4 view, slow parallax. Isolated asset, RGBA PNG, soft alpha at far edge to meet the horizon. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/MOON_002_TERRAIN_SURFACE.md`

### MOON_003_HORIZON
- attach / inspect first: `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg`, `references/earth/earth_rising_moonhorizon_apollo11_nasa_as11-44-6552.jpg`, `references/moon/moon_limb_low_oblique_earth_peeking_over_horizon_artemis2_nasa_art002e021283.jpg`, `references/moon/moon_surface_hard_shadow_slopes_ridge_horizon_apollo15_nasa_as15-85-11451.jpg`, `references/moon/moon_surface_longshadow_apollo12_nasa_as12-46-6813.jpg`
- prompt skeleton: "Low lunar horizon, subdued hills, black sky (no stars required in the daylight surface view), no haze. Canvas 4320x2160 (2x width for parallax pan). Views: surface view background. Isolated asset, opaque RGB (sky black). Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/MOON_003_HORIZON.md`

### MOON_005_PROPS
- attach / inspect first: `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg`, `references/moon/moon_copernicus_crater_lroc_nasa_pia13524.jpg`, `references/moon/moon_regolith_bootprint_apollo11_nasa_as11-40-5878.jpg`, `references/moon/moon_surface_longshadow_apollo12_nasa_as12-46-6813.jpg`, `references/moon/moon_tranquility_base_lroc_nasa_pia12925.jpg`
- prompt skeleton: "Sprite sheet: rocks (3 sizes), small craters (oblique), boot prints (4), regolith clumps. Footprints give scale next to the reflector. Canvas 4096x4096 sheet, individual sprites <= 1024 px. Views: surface view. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/MOON_005_PROPS.md`

### MOON_006_SITE_DRESSING
- attach / inspect first: `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg`, `references/moon/moon_limb_large_clean_edge_earth_behind_artemis2_nasa_art002e009287.jpg`, `references/moon/moon_limb_low_oblique_earth_peeking_over_horizon_artemis2_nasa_art002e021283.jpg`, `references/moon/moon_through_atmosphere_flattened_refraction_airglow_iss_nasa_iss039e001440.jpg`, `references/moon/moon_surface_hard_shadow_slopes_ridge_horizon_apollo15_nasa_as15-85-11451.jpg`
- prompt skeleton: "OPTIONAL distant Apollo 11 site details seen in AS11-40-5948: flag, TV camera, seismometer silhouettes. Flag does NOT flutter (vacuum). Canvas 2048x1024. Views: surface view, far midground. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/MOON_006_SITE_DRESSING.md`

## Lunar retroreflector
Must not change: Exactly 100 round cube faces in a 10x10 grid on a 46 cm panel (Apollo 11 style); cube diameter 3.8 cm = 1/12 of the panel width; same panel colour, frame and tilt toward Earth in every view; sun from the left.

Failure modes: wrong cube count; cubes fused into a texture; panel too large relative to the astronaut; perspective that differs between array and cutaway so the match cut cannot line up; baked glow standing for light.

### RETRO_001_ASSEMBLY
- attach / inspect first: `references/astronaut/astronaut_apollo11_rear_walking_carrying_lrrr_psep_nasa_as11-40-5942.jpg`, `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg`, `references/astronaut/astronaut_apollo11_surface_front34_stoop_leveling_handle_nasa_as11-40-5951.jpg`, `references/retroreflector/reflector_apollo11_lrrr_threequarter_deployed_nasa_as11-40-5952.jpg`, `references/retroreflector/reflector_apollo11_lrrr_elevated_from_lm_window_nasa_as11-37-5551_crop.jpg`
- prompt skeleton: "Hero composite on regolith, 3/4 view, tilted toward Earth: frame, support, 10x10 face grid and shadow. Assembled from RETRO_004, RETRO_002 and RETRO_006. Canvas 3000x2000. Views: 3/4 hero; low surface. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/RETRO_001_ASSEMBLY.md`

### RETRO_002_CUBE_ARRAY
- attach / inspect first: `references/retroreflector/reflector_apollo11_lrrr_threequarter_deployed_nasa_as11-40-5952.jpg`, `references/retroreflector/reflector_apollo11_lrrr_preflight_hardware_nasa_sp214_fig7-6.png`, `references/retroreflector/reflector_apollo11_cube_mount_section_figure_nasa_sp214_fig7-1.png`, `references/retroreflector/reflector_apollo14_lrr_closeup_high_threequarter_tilt_support_nasa_as14-67-9385.jpg`, `references/retroreflector/reflector_apollo14_lrr_medium_threequarter_sunlit_horizon_nasa_as14-67-9386.jpg`
- prompt skeleton: "Front and close-up view of the 10x10 grid of round glassy cube faces, dark glossy glass in a silver-aluminium frame (exactly 100 faces visible). Canvas 4096x4096. Views: front; close-up macro for the push-in. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/RETRO_002_CUBE_ARRAY.md`

### RETRO_004_FRAME_MOUNT
- attach / inspect first: `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg`, `references/retroreflector/reflector_nglr1_modern_retroreflector_housing_red_cap_pivot_bracket_side34_nasa_nglr-payload.jpg`, `references/retroreflector/reflector_apollo11_lrrr_threequarter_deployed_nasa_as11-40-5952.jpg`, `references/retroreflector/reflector_apollo11_lrrr_preflight_hardware_nasa_sp214_fig7-6.png`, `references/retroreflector/reflector_apollo14_lrr_closeup_high_threequarter_tilt_support_nasa_as14-67-9385.jpg`
- prompt skeleton: "Silver aluminium box frame with a white-bright base, mounting structure and tilt support as seen in the Apollo 11/14 photographs (AS11-40-5952, AS14-67-9385); faces left out (fit RETRO_002 by registration). Canvas 3000x2000. Views: 3/4; top; side. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/RETRO_004_FRAME_MOUNT.md`

### RETRO_005_CUBE_3FACE
- attach / inspect first: `references/retroreflector/optical_corner_cube_photo_gold_wikimedia_corner-cube.jpg`, `references/retroreflector/reflector_apollo11_cube_mount_section_figure_nasa_sp214_fig7-1.png`, `references/retroreflector/reflector_corner_cube_ray_path_3d_diagram_wikimedia_corner-reflector.png`, `references/retroreflector/optical_diffuse_scatter_reflection_wikimedia_diffuse-reflection1_render.png`, `references/retroreflector/reflector_nglr1_modern_retroreflector_housing_red_cap_pivot_bracket_side34_nasa_nglr-payload.jpg`
- prompt skeleton: "One cube seen looking into its corner: three mutually perpendicular faces meeting at the apex; same glass look as RETRO_002. Canvas 2160x2160. Views: perspective into the corner. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/RETRO_005_CUBE_3FACE.md`

## Observatory environment
Must not change: Generic illustrated station, never a named real site; no signage or logos; the dome receives no sunlight; one consistent dome radius and slit width across all OBS and TEL assets; night palette.

Failure modes: fused dome and slit (cannot open); telescope floating; real-site signage; mountains as one flat layer; a sunlit dome at night.

### OBS_001_EXTERIOR
- attach / inspect first: `references/observatory/observatory_vlt-enclosures_closed-on-hilltop_full-moon-behind_wikimedia_eso-moonset.jpg`, `references/observatory/observatory_laser-ranging-night_beams_nasa_gsfc-e001958.jpg`, `references/observatory/observatory_apo-3p5m-apollo-ranging_night-exterior_wikimedia_d70050914-15.jpg`, `references/observatory/observatory_wiyn-3p5m-enclosure_dusk-exterior_noirlab_wiynsunset.jpg`, `references/observatory/observatory_paranal-ut-laser-guide-star_beam-night_eso_ann15034h.jpg`
- prompt skeleton: "Observatory building body (no dome), doors, vents, a few lit windows; cool dim night light. Canvas 2160x3840 px (2x of 1080x1920). Views: ground-level wide, vertical frame. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/OBS_001_EXTERIOR.md`

### OBS_002_DOME
- attach / inspect first: `references/observatory/observatory_vlt-ut-enclosure_bi-parting-leaves-open-day-exterior_wikimedia_paranal-opendome.jpg`, `references/observatory/observatory_ntt-box-enclosure_night-slit-open-front-low-angle_wikimedia_eso-phot-07b-07.jpg`, `references/observatory/observatory_laser-ranging-night_beams_nasa_gsfc-e001958.jpg`, `references/observatory/observatory_apo-3p5m-apollo-ranging_night-exterior_wikimedia_d70050914-15.jpg`, `references/observatory/observatory_kitt-peak-wiyn_aerial-day-mountain_noirlab_kittpeakaerial5.jpg`
- prompt skeleton: "Dome shell, closed state, with the slit region left as a clean cut-out; hidden overlap under the ring. DECIDED: generic hemispherical dome with two bi-parting leaves (the real 3.5 m enclosure form is unresolved; do not copy any specific building). Canvas 2160x3840 px (2x of 1080x1920). Views: ground wide. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow (slit region transparent). Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/OBS_002_DOME.md`

### OBS_003_INTERIOR
- attach / inspect first: `references/telescope/telescope_vlt-ut-82m_interior-altitude-ring-nasmyth-pointing-up-open-slit_wikimedia_eso-paranal-16.jpg`, `references/observatory/observatory_vlt-ut-enclosure_slit-opening-tilted_eso_img7670-cc.jpg`, `references/observatory/observatory_vlt-ut-enclosure_interior-fisheye_eso_vlt1-brunier.jpg`, `references/observatory/observatory_paranal-ut-laser-guide-star_beam-night-vertical_eso_ann15034b.jpg`, `references/observatory/observatory_mayall-4m-dome_interior-floor-and-slit_noirlab_mayallinterior-5000.jpg`
- prompt skeleton: "Dome interior: ribs, floor, catwalk, shutter rails; separate foreground occlusion layer (structure that passes in front of the telescope). Canvas 2160x3840 px (2x of 1080x1920). Views: cutaway interior, 3/4 view. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/OBS_003_INTERIOR.md`

### OBS_004_MOUNTAINS
- attach / inspect first: `references/observatory/observatory_vlt-enclosures_closed-on-hilltop_full-moon-behind_wikimedia_eso-moonset.jpg`, `references/observatory/observatory_wiyn-3p5m-enclosure_dusk-exterior_noirlab_wiynsunset.jpg`, `references/observatory/observatory_kitt-peak-wiyn_aerial-day-mountain_noirlab_kittpeakaerial5.jpg`, `references/observatory/observatory_la-silla-ntt-36m_twilight-exterior_eso_img5380.jpg`, `references/observatory/observatory_vlt-ut-enclosure_bi-parting-leaves-open-day-exterior_wikimedia_paranal-opendome.jpg`
- prompt skeleton: "Three parallax ridge layers (far, mid, near) of a dry mountain-top site; distant landscape merges into the far layer. Canvas 4320x1400 per layer (x3). Views: ground wide. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/OBS_004_MOUNTAINS.md`

### OBS_006_DOME_SLIT
- attach / inspect first: `references/observatory/observatory_vlt-ut-enclosure_bi-parting-leaves-open-day-exterior_wikimedia_paranal-opendome.jpg`, `references/observatory/observatory_ntt-box-enclosure_night-slit-open-front-low-angle_wikimedia_eso-phot-07b-07.jpg`, `references/observatory/observatory_laser-ranging-night_beams_nasa_gsfc-e001958.jpg`, `references/observatory/observatory_ntt-box-enclosure_slit-open-twilight-exterior_eso_eso9704a.jpg`, `references/observatory/observatory_vlt-ut1-enclosure_open-doors-day_eso_ut1-at1-open-2007.jpg`
- prompt skeleton: "Shutter doors (two halves) and the opened slit, delivered as a slide-open pair with hidden overlap. Canvas 2160x3840 px (2x of 1080x1920). Views: ground wide; telescope visible through the slit. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/OBS_006_DOME_SLIT.md`

### OBS_007_PROPS
- attach / inspect first: `references/observatory/observatory_kitt-peak-wiyn_aerial-day-mountain_noirlab_kittpeakaerial5.jpg`, `references/observatory/observatory_vlt-ut-enclosure_bi-parting-leaves-open-day-exterior_wikimedia_paranal-opendome.jpg`, `references/observatory/observatory_ntt-box-enclosure_night-slit-open-front-low-angle_wikimedia_eso-phot-07b-07.jpg`, `references/observatory/observatory_vlt-enclosures_closed-on-hilltop_full-moon-behind_wikimedia_eso-moonset.jpg`, `references/observatory/observatory_laser-ranging-night_beams_nasa_gsfc-e001958.jpg`
- prompt skeleton: "Foreground props: rocks, antenna mast, fence posts, utility box; sprite sheet. Canvas 4096x4096 sheet. Views: ground wide foreground. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/OBS_007_PROPS.md`

## Telescope
Must not change: One telescope design across exterior, aperture and cutaway; same proportions, same mount type; not any specific real telescope; no text or logos.

Failure modes: invented hardware; mount that cannot rotate; aperture not a true circle; different design in cutaway vs exterior; text on the housing.

### TEL_001_HOUSING
- attach / inspect first: `references/observatory/observatory_ntt-box-enclosure_night-slit-open-front-low-angle_wikimedia_eso-phot-07b-07.jpg`, `references/telescope/telescope_vlt-ut-82m_interior-altitude-ring-nasmyth-pointing-up-open-slit_wikimedia_eso-paranal-16.jpg`, `references/observatory/observatory_vlt-ut-enclosure_slit-opening-tilted_eso_img7670-cc.jpg`, `references/observatory/observatory_mayall-4m-dome_slit-view-from-inside-sunset-silhouette_noirlab_noirlab-05025.jpg`, `references/telescope/telescope_ntt-358m_frontlow-ring-spider-secondary_eso_jfs-ls-2011-8239.jpg`
- prompt skeleton: "Tube/truss, secondary-mirror cage and exterior instrument housings, side and 3/4 views, no mount. Canvas 3000x3000. Views: side; 3/4; interior 3/4. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/TEL_001_HOUSING.md`

### TEL_002_MOUNT
- attach / inspect first: `references/telescope/telescope_vlt-ut-82m_interior-altitude-ring-nasmyth-pointing-up-open-slit_wikimedia_eso-paranal-16.jpg`, `references/telescope/telescope_ntt-358m_threequarter-drawing-altaz-structure_eso_eso8602a.jpg`, `references/telescope/telescope_vlt-ut1-82m_altitude-bearing-threequarter_eso_eso9804c.jpg`, `references/telescope/telescope_vlt-ut2-82m_centrepiece-and-bearing-threequarter_eso_eso9902g.jpg`, `references/telescope/telescope_ntt-358m_frontlow-ring-spider-secondary_eso_jfs-ls-2011-8239.jpg`
- prompt skeleton: "Azimuth base and two pylons (yoke) carrying the altitude bearings, 3/4 view; hidden overlap where the tube sits between them. Not a classic fork: follow the NTT/VLT-class references. Canvas 3000x3000. Views: side; 3/4. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/TEL_002_MOUNT.md`

### TEL_003_APERTURE
- attach / inspect first: `references/observatory/observatory_ntt-box-enclosure_night-slit-open-front-low-angle_wikimedia_eso-phot-07b-07.jpg`, `references/telescope/telescope_ntt-358m_frontlow-ring-spider-secondary_eso_jfs-ls-2011-8239.jpg`, `references/telescope/telescope_vlt-ut-82m_secondary-mirror-unit-lifted-on-floor_eso_eso9812a.jpg`, `references/telescope/telescope_vlt-ut-82m_interior-altitude-ring-nasmyth-pointing-up-open-slit_wikimedia_eso-paranal-16.jpg`, `references/telescope/telescope_ntt-358m_threequarter-drawing-altaz-structure_eso_eso8602a.jpg`
- prompt skeleton: "Head-on view of the open aperture: rim, secondary-mirror spider, primary mirror visible; clean area for the laser flash. NOTE: no photograph shows this exact view (the only front views hide the primary behind the centre box): a simplified illustration from the geometry. Canvas 2160x2160. Views: front-on (B04), slow push-in (B24). Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/TEL_003_APERTURE.md`

### TEL_004_PRIMARY_CUTAWAY
- attach / inspect first: `references/telescope/telescope_vlt-ut4-82m_mirror-cell-on-transporter-side_eso_max-313677s.jpg`, `references/telescope/telescope_wiyn-3p5m_new-mirror-cell-carried_noirlab_01073-cc.jpg`, `references/telescope/telescope_wiyn-3p5m_primary-mirror-lowered-onto-cell_noirlab_01074-cc.jpg`, `references/telescope/telescope_vlt-ut-82m_interior-altitude-ring-nasmyth-pointing-up-open-slit_wikimedia_eso-paranal-16.jpg`, `references/telescope/telescope_ntt-358m_frontlow-ring-spider-secondary_eso_jfs-ls-2011-8239.jpg`
- prompt skeleton: "Simplified educational cutaway: tube sliced, concave primary, return light path from sky to detector. Marked simplified; no fictional specs. The real return path folds sideways via a third mirror to a receiver at the axis, not through a hole behind the primary: label it simplified. Canvas 2160x3000. Views: cutaway side view. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/TEL_004_PRIMARY_CUTAWAY.md`

### TEL_005_DETECTOR_BOX
- attach / inspect first: `references/telescope/telescope_ntt-358m_nasmyth-rotator-and-instrument-box_eso_agil1766-cc.jpg`, `references/telescope/telescope_vlt-ut-82m_interior-altitude-ring-nasmyth-pointing-up-open-slit_wikimedia_eso-paranal-16.jpg`, `references/telescope/telescope_ntt-358m_frontlow-ring-spider-secondary_eso_jfs-ls-2011-8239.jpg`, `references/telescope/telescope_ntt-358m_threequarter-drawing-altaz-structure_eso_eso8602a.jpg`, `references/telescope/telescope_vlt-ut1-82m_altitude-bearing-threequarter_eso_eso9804c.jpg`
- prompt skeleton: "Plain instrument housing on the telescope that receives the return; generic, no brand, no invented dials. Canvas 1500x1500. Views: interior 3/4; cutaway. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/TEL_005_DETECTOR_BOX.md`

## Apollo astronaut
Must not change: Costume, helmet, gold visor, PLSS, gloved hands and boots identical in every pose; no face visible; no named patch; sun from the left; height ratio to the 46 cm reflector panel fixed.

Failure modes: face visible in the visor; bare hands; extra or fused fingers; detached equipment; cloth billowing; joint caps that are round discs; different boots left/right; proportions drifting between poses.

### ASTRO_001_HELMET
- attach / inspect first: `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg`, `references/astronaut/astronaut_apollo11_front34_standing_visor_reflection_nasa_as11-40-5873.jpg`, `references/astronaut/astronaut_apollo11_training_front34_and_rear34_reach_equipment_nasa_s69-32243.jpg`, `references/astronaut/astronaut_apollo11_training_pure_side_profile_helmet_visor_pole_nasa_s69-32247.jpg`, `references/astronaut/astronaut_apollo11_training_side34_helmet_visor_tool_lm_leg_nasa_s69-32248.jpg`
- prompt skeleton: "Polycarbonate helmet shell, neck ring, communication cap. Canvas delivered per pose, 3000x3000 each, same scale and registration across poses. Views: 3/4 view (all poses); side view (step-back). Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/ASTRO_001_HELMET.md`

### ASTRO_002_VISOR
- attach / inspect first: `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg`, `references/astronaut/astronaut_apollo11_front34_standing_visor_reflection_nasa_as11-40-5873.jpg`, `references/astronaut/astronaut_apollo17_front34_stooping_dusty_a7lb_nasa_as17-145-22157.jpg`, `references/astronaut/astronaut_apollo11_training_front34_and_rear34_reach_equipment_nasa_s69-32243.jpg`, `references/astronaut/astronaut_apollo11_training_pure_side_profile_helmet_visor_pole_nasa_s69-32247.jpg`
- prompt skeleton: "Gold-coated outer visor and sun shade, separate from the shell. Canvas delivered per pose, 3000x3000 each, same scale and registration across poses. Views: 3/4 view (all poses); side view (step-back). Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/ASTRO_002_VISOR.md`

### ASTRO_003_VISOR_REFLECTION
- attach / inspect first: `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg`, `references/astronaut/astronaut_apollo11_surface_front34_stoop_leveling_handle_nasa_as11-40-5951.jpg`, `references/astronaut/astronaut_apollo11_helmet_visor_closeup_crop_nasa_as11-40-5903.jpg`, `references/astronaut/astronaut_apollo11_front34_standing_visor_reflection_nasa_as11-40-5873.jpg`, `references/astronaut/astronaut_apollo11_side_profile_standing_nasa_as11-40-5874.jpg`
- prompt skeleton: "Replaceable reflection plate for the visor (surface, sun glint, reflector). Canvas delivered per pose, 3000x3000 each, same scale and registration across poses. Views: 3/4 view (all poses); side view (step-back). Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/ASTRO_003_VISOR_REFLECTION.md`

### ASTRO_004_TORSO
- attach / inspect first: `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg`, `references/astronaut/astronaut_apollo11_side_profile_standing_nasa_as11-40-5874.jpg`, `references/astronaut/astronaut_apollo12_side_bending_lean_core_tube_nasa_as12-49-7286.jpg`, `references/astronaut/astronaut_apollo16_front_crouch_dusty_a7lb_nasa_as16-114-18423.jpg`, `references/astronaut/astronaut_apollo17_front34_stooping_dusty_a7lb_nasa_as17-145-22157.jpg`
- prompt skeleton: "Suit torso with chest remote-control unit and hose connectors. Canvas delivered per pose, 3000x3000 each, same scale and registration across poses. Views: 3/4 view (all poses); side view (step-back). Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/ASTRO_004_TORSO.md`

### ASTRO_005_PLSS
- attach / inspect first: `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg`, `references/astronaut/astronaut_apollo11_front34_standing_visor_reflection_nasa_as11-40-5873.jpg`, `references/astronaut/astronaut_apollo11_side_profile_standing_nasa_as11-40-5874.jpg`, `references/astronaut/astronaut_apollo11_rear_walking_carrying_lrrr_psep_nasa_as11-40-5942.jpg`, `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg`
- prompt skeleton: "Backpack life-support system, rigid. Canvas delivered per pose, 3000x3000 each, same scale and registration across poses. Views: 3/4 view (all poses); side view (step-back). Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/ASTRO_005_PLSS.md`

### ASTRO_006_ARMS
- attach / inspect first: `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg`, `references/astronaut/astronaut_apollo11_rear34_striding_tool_nasa_as11-40-5964.jpg`, `references/astronaut/astronaut_apollo12_front34_striding_tool_visor_nasa_as12-47-6919.jpg`, `references/astronaut/astronaut_apollo12_side_bending_lean_core_tube_nasa_as12-49-7286.jpg`, `references/astronaut/astronaut_apollo11_training_side34_bend_tool_to_ground_nasa_s69-32233.jpg`
- prompt skeleton: "Upper arm and forearm, left and right, with hidden overlap at shoulder and elbow. Canvas delivered per pose, 3000x3000 each, same scale and registration across poses. Views: 3/4 view (all poses); side view (step-back). Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/ASTRO_006_ARMS.md`

### ASTRO_007_GLOVES
- attach / inspect first: `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg`, `references/astronaut/astronaut_apollo12_lowerbody_glove_boot_dust_closeup_nasa_as12-48-7149.jpg`, `references/astronaut/astronaut_apollo12_front34_striding_tool_visor_nasa_as12-47-6919.jpg`, `references/astronaut/astronaut_apollo11_training_side34_bend_tool_to_ground_nasa_s69-32233.jpg`, `references/astronaut/astronaut_apollo11_training_front34_and_rear34_reach_equipment_nasa_s69-32243.jpg`
- prompt skeleton: "Gloves with wrist rings, left and right. Canvas delivered per pose, 3000x3000 each, same scale and registration across poses. Views: 3/4 view (all poses); side view (step-back). Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/ASTRO_007_GLOVES.md`

### ASTRO_008_LEGS
- attach / inspect first: `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg`, `references/astronaut/astronaut_apollo11_side_profile_standing_nasa_as11-40-5874.jpg`, `references/astronaut/astronaut_apollo11_rear_walking_carrying_lrrr_psep_nasa_as11-40-5942.jpg`, `references/astronaut/astronaut_apollo11_rear34_striding_tool_nasa_as11-40-5964.jpg`, `references/astronaut/astronaut_apollo11_rear_lowangle_ladder_boot_sole_nasa_as11-40-5866.jpg`
- prompt skeleton: "Upper and lower legs, left and right, with hidden overlap at hip and knee. Canvas delivered per pose, 3000x3000 each, same scale and registration across poses. Views: 3/4 view (all poses); side view (step-back). Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/ASTRO_008_LEGS.md`

### ASTRO_009_BOOTS
- attach / inspect first: `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg`, `references/astronaut/astronaut_apollo11_side_profile_standing_nasa_as11-40-5874.jpg`, `references/astronaut/astronaut_apollo11_rear_walking_carrying_lrrr_psep_nasa_as11-40-5942.jpg`, `references/astronaut/astronaut_apollo11_rear34_striding_tool_nasa_as11-40-5964.jpg`, `references/astronaut/astronaut_apollo11_rear_lowangle_ladder_boot_sole_nasa_as11-40-5866.jpg`
- prompt skeleton: "Lunar boots with tread, left and right. Canvas delivered per pose, 3000x3000 each, same scale and registration across poses. Views: 3/4 view (all poses); side view (step-back). Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/ASTRO_009_BOOTS.md`

### ASTRO_010_POSE_SET
- attach / inspect first: `references/astronaut/astronaut_apollo11_front_standing_visor_reflection_nasa_as11-40-5903.jpg`, `references/astronaut/astronaut_apollo11_front34_standing_visor_reflection_nasa_as11-40-5873.jpg`, `references/astronaut/astronaut_apollo11_side_profile_standing_nasa_as11-40-5874.jpg`, `references/astronaut/astronaut_apollo11_rear_walking_carrying_lrrr_psep_nasa_as11-40-5942.jpg`, `references/astronaut/astronaut_apollo11_rear34_walking_plss_nasa_as11-40-5948.jpg`
- prompt skeleton: "Registered complete poses: 3/4 standing rest, 3/4 kneel with equipment interaction (aligning the array; STYLISED: no photograph shows kneeling, name no astronaut), side step-back. Rear view, walking and top view are NOT PLANNED (no beat shows them). Canvas 3000x3000 per pose, registered. Views: 3/4 stand; 3/4 kneel; side step. Isolated asset, RGBA PNG, straight alpha, no matte fringe, no baked cast shadow. Sun from the left, about 30 degrees up. Painterly-clean illustration, no outlines." + global negative prompt
- full brief: `individual_asset_briefs/ASTRO_010_POSE_SET.md`
