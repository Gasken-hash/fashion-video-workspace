# Product 11_kiyana — Kiyana Cirebon Cloth Fiora Ribbon Collar Top (Batch 15, batch 3)
- Product ID: 1734970180507830128
- Link: https://vt.tokopedia.com/t/ZS9fQi1Q6wSxP-e6NnR/
- Reference: `tok_00.jpg` (800x800, from Jendral's Tokopedia link via curl-cffi)
- Base: `~/workspace/fashion_test/bases/base_pita_v3_tas.jpg` (Pita v3 frame-0, black bag prop, 1536x2752)
- Movement: Set E adapted (lap → touch ribbon tie at collar → chest → trace lace ruffle hem → lap → slow side turn → peace sign)

## Reference details (from tok_00.jpg)
Cream pale-yellow fine-ribbed knit top, fitted, long sleeves; blue-and-white gingham pointed shirt collar; LONG blue gingham ribbon tie at the neck, tied in a small bow with two long tails hanging down the center chest; flared white lace ruffle peplum hem over a blue gingham ruffle layer, scalloped lace edge; blue gingham cuffs; worn with LIGHT BLUE jeans. "cirebon cloth" watermark on the chest (ignore, do NOT reproduce). No buttons down the front.

## Frame-0 v1
- File: `media-generation-frame0-kiyana-0-9eb258e1-d356-400d-b075-84eee5150650.webp` (1168x2112, sharpness 51.9); JPG copy `frame0_kiyana.jpg`
- One fresh LILO edit from the tas base.

## GATE 1 — PASSED (first try)
Checked detail by detail vs reference:
- Cream color + fine ribbed texture ✓
- Blue gingham pointed collar ✓
- Ribbon tie: bow + two long tails down the center chest ✓ (tails hang longer than in the reference because she is sitting and they drape down — same design, noted as minor)
- White lace ruffle hem over blue gingham, scalloped edge ✓
- Blue gingham cuffs on both wrists ✓
- Light blue jeans (not the base's white pants) ✓
- No buttons down the front, no pink bows, no pearl buttons, no ruffle cuffs — all base details removed ✓
- No watermark text ✓
- Framing: mouth-cut, eyes NOT visible; mouth/chin peek at top (tolerated) ✓
- Hair in a bun with face-framing strands ✓
- Base kept: maroon wall, speckled floor, black bag bottom right, hand on hip, sitting pose ✓

## Video v1 (raw)
- File: `media-generation-kiyana-duduk-lilo-v1-0-a7862d98-3c5d-4d28-9da0-26d247c44806.mp4` (640x1168, 24fps, 10.0s, h264 + AAC audio)

## GATE 3 — PASSED (on the final cropped/upscaled video)
- Background 0 vs 0.6s: identical ✓
- Sharpness: video frames 93–128 vs frame-0 51.9 — video SHARPER, no unsharp needed ✓
- Beats captured: ribbon-tie touch (2s + 3.5s, both hands on the tie), hem trace (6.5s, both hands on the lace ruffle), peace sign (9.5s) ✓
- Product identical in all frames (0/2/3.5/6.5/9.5) — no invented details ✓
- Calm motion, torso/shoulders/chest still, hands only ✓
- EYES: the RAW video at 9.5s had an eye drifting in at the very top edge (head turns to the side at the peace sign). The 60px top crop REMOVED it — the final video's enlarged 9.5s top shows only lips/chin, no eye. Profile (nose/lips/chin, eyes cut) matches the Hitam v1 precedent. Disclosed honestly here.

## Final video
- File: `kiyana_duduk_lilo_v1_upscale720.mp4` — 720x1280, 24fps, 10.0s, h264, video-only (no audio stream; generator audio stripped), 6.16 MB
- Finishing: top cropped 60px (~5%) as drift guard, then upscale lanczos crf 18
- Final frame sharpness: 2s 99.1, 3.5s 111.1, 9.5s 90.5 (upscale softening vs raw, as known/accepted)

## Honest defects
1. Ribbon tails hang longer than in the reference (they drape to the jeans because she is sitting); same bow + two-tail design, just longer drape.
2. Raw video at 9.5s had an eye at the very top edge (head turn at the peace sign) — removed by the 60px crop; final video shows only lips/chin in profile, eyes cut.
3. Mouth/chin peek at the top edge in most frames (tolerated).
4. The gold necklace from the base is NOT visible (covered by the collar) — a plus vs other videos.
5. Upscale softening (known, accepted): 3.5s sharpness 111.1 final vs 127.5 raw.

## Files in this folder
- `tok_00.jpg` … `tok_09.jpg` — Tokopedia gallery (10 images)
- `media-generation-frame0-kiyana-0-….webp` + `frame0_kiyana.jpg` — frame-0 v1 (Gate 1 PASSED)
- `media-generation-kiyana-duduk-lilo-v1-0-….mp4` — raw video (with audio, before finishing)
- `kiyana_duduk_lilo_v1_upscale720.mp4` — FINAL (720p, silent)
- `g3_f*.jpg` — Gate 3 frames (raw); `g3_final_*.jpg` — final frames; `g3_top95.jpg` / `g3_final_top95.jpg` — enlarged 9.5s tops
- `NOTES.md` — this file

Media calls: 1 image + 1 video. No generator refusal, no retry.
