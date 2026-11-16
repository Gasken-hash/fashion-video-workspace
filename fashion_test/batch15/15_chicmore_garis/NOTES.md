# Product 15 — CHICMORE Atasan modis garis-garis (Batch 15, Batch 4)
- Product ID: 1734336768351045349
- Link: https://vt.tokopedia.com/t/ZS9fQj3V4xYzA-a1BbC/
- Reference: `tok_00.jpg` (800x800, from Jendral's Tokopedia link via curl-cffi)
- Base: `~/workspace/fashion_test/bases/base_pita_v3_kacamata.jpg` (Pita v3 frame-0, glasses prop, 1536x2752)
- Movement: Set A adapted (hip/hair → touch drawstring at hem → chest spread → hem → lap → slight torso turn → peace sign)

## Reference details (from tok_00.jpg)
Light blue/white fine vertical pinstripes, pointed shirt collar, front white buttons down center placket, CROPPED body ending above waist, elastic ruched hem with thin striped drawstring tie at front center, long sleeves slightly puffed at shoulder, wide solid WHITE cuffs, plain white shirt layered underneath (peeks below hem + at cuffs), one flat chest pocket on left chest. On a hanger, no bottom shown → bottom = base's white drawstring pants.

## Frame-0 v1
- File: `media-generation-frame0-garis-v1-0-0e68fd72-38dc-48c8-a474-d805c571234c.webp` (1168x2112, sharpness 710.0) — also saved as `frame0_garis.jpg`
- One fresh LILO edit from the kacamata base, with framing clause.

## GATE 1 — PASSED (first try)
Checked detail by detail vs reference:
- Stripes: thin even vertical pinstripes light blue on white ✓
- Collar: pointed shirt collar, striped fabric ✓
- Buttons: small white buttons down center placket ✓
- Cropped fit: short body ends above waistband, elastic ruched hem ✓
- Drawstring: thin striped tie in a bow at front center of hem ✓
- Cuffs: wide solid white cuffs both wrists ✓
- White layer: plain white shirt peeking below hem ✓
- Pocket: flat chest pocket on left chest ✓
- Sleeves: long, attached at shoulders, slightly puffed ✓
- Framing: mouth-cut, eyes NOT visible, mouth/chin peek at top (tolerated) ✓
- Hair: loose high bun with face-framing strands ✓
- Base kept: maroon wall, white drawstring pants, glasses on floor bottom right, hand on hip ✓
- No invented details: the base's 6 pink bows + pearl buttons + ruffle cuffs are all gone ✓

## Video v1
- Raw: `media-generation-garis-duduk-lilo-v1-0-f7d0fcf6-097b-4068-9a74-1f03c8f0e116.mp4` (640x1168, 24fps, 10.0s, h264 + AAC audio mean -56.2 dB — stripped in finishing)

## GATE 3 — PASSED
- Background 0 vs 0.6s: identical (wall/floor/glasses frozen) ✓
- Eyes/full face: never in any frame — enlarged top of 9.5s frame shows only mouth/chin ✓
- Product identical in all frames (0/2/3.5/6.5/9.5s): stripes, collar, buttons, pocket, drawstring, white cuffs, white layer — no invented details ✓
- Sharpness: video frames 691.8–1224.6 vs frame-0 710.0 (different scales; video sharp, no unsharp needed) ✓
- Beats captured: hair (0.6s), chest spread (3.5s), lap (6.5s), peace sign clear (9.5s) ✓
- Motion: calm, hands only, torso/shoulders/chest still ✓

## Final video
- `garis_duduk_lilo_v1_upscale720.mp4` — 720x1280, 24fps, 10.0s, h264, 6.35 MB, video-only (no audio stream, ffprobe-verified). Top cropped 60px (~5%) as drift guard, then upscale lanczos crf 18.
- Final 3.5s frame sharpness: 602.8 (vs raw video 841.1 — upscale softening, known and accepted).

## Honest defects
1. Small gold necklace from the base visible at the collar (base artifact, same as Krem/Beige/Hitam and other batch-15 videos).
2. Chin/mouth peek at the top edge of the raw video (tolerated); after the 60px crop, the final cuts at the nose/chin — mouth no longer visible.
3. At 6.5s the head turns to a side profile (nose/lips/chin visible, eyes still cut) — same tolerated profile case as Hitam v1.
4. Upscale softening at 3.5s (841.1 → 602.8, known and accepted; still sharp).
5. The drawstring bow sits slightly higher on the waist in the video than in the flat-lay reference (sitting pose), same design otherwise.

## Files in this folder
- `tok_00.jpg` … `tok_06.jpg` — Tokopedia gallery (7 images)
- `media-generation-frame0-garis-v1-0-0e68fd72-38dc-48c8-a474-d805c571234c.webp` / `frame0_garis.webp` / `frame0_garis.jpg` — frame-0 v1 (Gate 1 PASSED)
- `media-generation-garis-duduk-lilo-v1-0-f7d0fcf6-097b-4068-9a74-1f03c8f0e116.mp4` — raw video (with generator audio)
- `garis_duduk_lilo_v1_upscale720.mp4` — FINAL (720x1280, silent)
- `g3_f0s.jpg`, `g3_f0.6s.jpg`, `g3_f2s.jpg`, `g3_f3.5s.jpg`, `g3_f6.5s.jpg`, `g3_f9.5s.jpg` — Gate 3 frames
- `g3_top95.jpg`, `g3_top65.jpg` — enlarged top crops (eyes check)
- `g3_final_3.5s.jpg` — 3.5s frame from the FINAL video
- `NOTES.md` — this file

Media calls: 1 image + 1 video. No generator refusal, no retry.
