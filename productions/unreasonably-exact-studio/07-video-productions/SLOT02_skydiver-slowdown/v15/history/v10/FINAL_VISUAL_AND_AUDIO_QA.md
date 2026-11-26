# V10 final visual and audio QA

**Verdict: V10 is a much better review cut, but it is not publication-ready.**

Blockers:
1. The Codex V10 instrument, forearm, glance head and both painted landscapes are **candidate** artwork, which Codex itself has not approved.
2. Joint caps remain visible in the generated character art.
3. The library SFX licences are not cleared.
4. **No human has listened to the mix.**
5. The narration version is unconfirmed by the owner.

## Evidence base (what was actually done)

- **Two full renders, with fixes between them.** The second render first crashed on a frame-buffer lifetime bug, which was fixed before a clean third run. The picture was built from `tools/v10.py` + `tools/v10_shots.py`.
- **File check of the final MP4:**
  - 1877 video frames and 3666 audio frames, both 78.2 s.
  - Full decode with no errors.
  - Freezedetect (noise 0.0008, ≥0.75 s): one hit at 50.63–52.04 s, the end of the equal-time diagram. It is a deliberate read hold; frame differencing confirms motion continues in it (marching velocity dashes, figure flutter, 2.7k changed pixels).
- **Full-film contact sheet** every 1.5 s (`qa/V10_contact_1p5s.jpg`), viewed.
- **Motion strips:** `qa/seq_wrist.jpg` (8.2–11.4 s at 6 fps) and `qa/seq_cross.jpg` (41–47 s at 3 fps), viewed.
- **Storyboard:** 82 full-size 1080×1920 panels, START/DEVELOPMENT/PAYOFF/TRANSITION for 15 motion-critical shots.
- **Browser playback** of `review.html` in the in-app browser:
  - Playing unmuted, the audio decoder was active (107 kB decoded after 4 s), with 0 dropped of 99 frames.
  - A screenshot was taken during playback at about 6 s.
- **Loudness:** EBU R128 −16.4 LUFS, LRA 4.4 LU, peak −1.2 dBFS.

## Review passes

| Pass | Finding | Action / status |
|---|---|---|
| Image asset provenance | 65 of 73 Codex V9 assets used, plus 10 V10 candidate files. Every file is hashed in `CODEX_ASSET_INTEGRATION_MANIFEST.csv`. No procedural character art remains. | Done |
| Joint seams | No gaps in film or at 60% of the limits. Round joint caps are visible. | Art repair requested |
| Character identity | Consistent costume. The three-quarter head differs (smiling). | Art repair requested |
| Character animation | Glance with head replacement and arm lift; close-up eyes, brows, blink replacement and mouth swap; flutter calming with speed; fixed posture in the model section | Done |
| Wrist attachment | The device sits on the right wrist in side, forearm and close-up shots. Straps are masked to the sleeve. | Done (candidate art) |
| Instrument perspective | Face-on art only; the side view is approximated by a squash | **Open:** needs true side and oblique device art |
| Needle continuity | Zero at the reset, peak at STATE 2, monotonic fall after 47.7 s (asserted) | Done |
| Physical direction | v ≥ 0, altitude never rises, no upward motion of the character or world (asserted and viewed) | Done |
| Force accuracy | One scale (118 units = weight). The lens zooms the tips 10×. No mis-scaled side arrow. | Done |
| Equal-time demo | Model positions every 15 s; gaps shrink ~31%; every mark lower | Done. The shrink is modest because the physics is modest. |
| Graph | Readable axes and a tracking dot. Alternative curves only at the end, labelled. | Done. The label "smaller drag area" touches its curve. |
| Airflow | Streamlines move upward (relative flow); faint short specks; distinct from all force arrows | Done |
| Environment | Painted horizon (A1) and painted top-down terrain (O1, zooming in) from Codex V10 candidates; procedural perspective farmland elsewhere; Codex cumulus and wisps everywhere | **Open:** painted A1/O1 are more detailed than the flat character style; the 18% and 12% haze overlays only partly reconcile them |
| Camera continuity | Motivated push-ins (A1, B2, B3), insert cuts on the glance, pull-back on the model caveat | Done |
| Text readability | Captions 15 units (45 px); diagram labels 9–13 units; footnotes 7.5–8.5 units (22–25 px) | Footnotes remain small on a phone |
| Overload (V9 defect) | V9's ruler, net inset, velocity lane and density boxes no longer share one frame. Density, comparison, positions and graph each get their own full-frame card. | Done |
| Sound design | V9 design kept and retimed: 11 library cues (added a softer paper cue at 47.66 s; instrument tick moved to 10.18 s); wind drops under the four diagram cards | Measured only |
| Narration sync | Owner's 78.2 s recording, unaltered. Shot boundaries sit on phrase boundaries, but phrase times are ±0.3 s ASR estimates. | Manual word alignment is still open |
| Mobile viewing | Viewed at 180×320 thumbnails and in the browser pane (≈320 px wide) | Main beats read; footnotes do not |
| Muted viewing | Contact sheet without audio: plane → you → closed pack → gravity → glance → wrist → dial → reaction → questions → airflow → model at rest → thin air → speeding up → three densities → same-air comparison → states 1–3 with lens → moving down / net up → slowing → dial → ground closer → still closed → graph → recap → model caveat → other inputs | Reads in order |
| Overall storytelling | Each beat now has one primary visual idea | Improved. B3 and B4 are short (0.9 s each). |

## Audio statement

**No listening verification was performed.** The assistant cannot hear audio. Levels come from measurement; cue placement comes from the V9 spectrogram work and the V10 retiming. A person needs to listen on headphones before publication.

`audio/V10_mix_rights_clear.wav` contains the VO plus generated wind and aircraft only, as the alternative while library licences remain uncleared.
