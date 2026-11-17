# Cross-PC rebuild and review

Validated on a fresh checkout of PR #29 on a second macOS ARM64 machine, Node 24.14.0 / npm 11.9.0 / Python 3.9.6. Linux and Windows execution has not been tested. No proprietary fonts are distributed.

## Animation (from repository root)

```sh
cd productions/finance-short-01/animation
npm ci
npm test
npm run typecheck
python3 scripts/export_bundle.py
npx remotion still src/index.ts FinanceShort01 out/qa/check.png --frame=930
node scripts/qa_frames.mjs mobile S02B+40,S09B+40,S10B+40,S12+40 --scale=0.296296 --sheet=false
```

Node >=22.18 is needed for the native TypeScript tests. Remotion installs Chrome Headless Shell on first render; network access and the platform's Chrome system libraries are required. Rendering individual frames needs no ImageMagick. Contact sheets need ImageMagick (`magick` on PATH); pass `--font=<installed-font-name-or-path>` if its default font is unavailable. `--sheet=false` leaves labelled-by-frame PNG files in `out/qa/<name>/` and skips montage. All outputs there are ignored.

## Optional Phase 2 PNG rebuild

```sh
cd productions/finance-short-01/experiment/PHASE_2_ASSETS/build
npm ci
npm test
```

`render.mjs` now resolves locally installed Sharp 0.35.5 from its own lockfile; no Codex cache path is needed. The smoke test renders a scratch SVG from an unrelated working directory and verifies dimensions and repeated-output bytes. Do not rebuild the whole asset library for a dependency check. Full `build_assets.py` execution rewrites derived assets/manifests; only run it for an authorized asset or alignment change, then inspect hash differences.

## Fonts and identity

The approved stack is Avenir Next → Avenir → Nunito Sans → Arial → sans-serif. Avenir Next is proprietary and macOS-specific. On another OS, install a legally licensed Avenir Next locally if matching typography is required, or install the open-source Nunito Sans separately and explicitly review the fallback output. No silent typography substitution is claimed to be pixel-identical. Font weight availability, browser, OS rasterization, Sharp/librsvg and font versions affect pixels. Source-level rebuild compatibility does not establish cross-platform pixel identity.

The animation bundle rebuild is byte-identical on the second machine. Python-generated rig reference matrices differ by at most 4.55e-13 from the checkpoint because of floating-point math; the existing parity tolerance is 1e-6. Preserve the committed fixture unless the rig changes. Compare semantic numeric values when rebuilding fixtures across platforms, not only bytes.

## Integrity and gates

The asset manifest records SHA256 for all 244 SVGs and 196 PNGs. Verify those files before rebuilding. `IMPORT_MANIFEST.sha256` records the original imported package: it is historical provenance, not a manifest to rewrite after authorized generator-code changes. Keep original media intact.

No corrected MP3 was present in this checkout. `FAIL_MATERIAL_MISPRONUNCIATION` keeps final sync blocked. Previews remain muted and watermarked. Re-align a newly supplied, provenance-verified correction before any final audio/export work; owner approval is still required.
