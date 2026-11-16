# Product 10 — MAMAMARA Sweater Rajut Wol Kerah Kemeja Motif Puppy (Batch 15, batch 2)
- Product ID: 1735553127307052628
- Link: https://vt.tokopedia.com/t/ZS9fQh8P7vRzN-d2MmQ/
- Reference: `tok_00.jpg` (800x800, from Jendral's Tokopedia link via curl-cffi)
- Base: `~/workspace/fashion_test/bases/base_pita_v3_tumbler.jpg` (Pita v3 frame-0, tumbler prop, 1536x2752)
- Movement: Set C adapted (shoulders → touch dog motif → lift blue cuff → waist/hem → lap → slow side turn → peace sign)

## Reference details (from tok_00.jpg)
Gray knit sweater, round ribbed crew neck, long sleeves attached at shoulders, straight ribbed hem. Dachshund motif across the chest: long tan-brown dog lying horizontally, wearing a blue-white vertically striped shirt with THREE small red bows, red cap with green pompom, dark brown paws. Light blue shirt collar peeking at the neck, wide light blue shirt cuffs at both wrists. Close-up model shot, no bottom shown → bottom = dark denim jeans (matched to gray + light blue top).

## Frame-0 v1
- File: `frame0_puppy.webp` (1168x2112, sharpness 122.2); raw: `media-generation-frame0-puppy-0-3c18a126-c19f-4399-948a-38a24b485419.webp`
- One fresh LILO edit from the tumbler base, with framing clause.

## GATE 1 — PASSED (first try)
Checked detail by detail vs reference:
- Gray color, soft knit texture ✓
- Round ribbed crew neck ✓
- Dachshund motif: long tan-brown dog facing left, blue-white vertical striped shirt, exactly 3 small red bows, red cap + green pompom, dark brown paws ✓
- Light blue shirt collar, pointed, at neck ✓
- Wide light blue shirt cuffs at both wrists ✓
- Long sleeves attached at shoulders ✓, straight ribbed hem ✓, fitted fit ✓
- Bottom: dark indigo denim jeans, straight leg (NOT the base's white pants) ✓
- Framing: mouth-cut, mouth/chin peek at top, eyes NOT visible ✓
- Hair: loose high bun with face-framing strands ✓
- Base kept: maroon wall, speckled floor, black tumbler bottom right, hand on hip, gold necklace ✓
- Pink cardigan + 6 pink bows + pearl buttons completely gone ✓

## Video v1
- Raw: `media-generation-puppy-duduk-lilo-v1-0-1f170877-3a71-442d-8d55-9732bb74a35f.mp4` (640x1168, 24fps, 10.0s, h264 + AAC audio track, mean_volume -66.1 dB — generator noise, stripped in finishing)

## GATE 3 — PASSED
- Background 0 vs 0.6s identical (wall, floor, tumbler do not move) ✓
- No eyes/full face in any frame — top of 9.5s frame enlarged (`g3_f9.5s_top.jpg`): only mouth/chin/nose, eyes cut off ✓
- Product identical in all frames (0/2/3.5/6.5/9.5s): dog motif intact (3 red bows, hat, striped shirt), blue collar + cuffs intact, dark jeans intact, no invented details ✓
- Sharpness: video 2s 362.6, 3.5s 223.0, 6.5s 258.8, 9.5s 367.9 vs frame-0 122.2 — video SHARPER, no unsharp needed ✓
- Beats captured: shoulder (2s), cuff lift + motif touch (3.5s), waist/hem (6.5s), peace sign + slow side turn (9.5s) ✓
- Calm motion, torso/shoulders/chest still, hands only ✓

## Final video
- File: `puppy_duduk_lilo_v1_upscale720.mp4` — 720x1280, 24fps, 10.0s, h264, 5.9 MB, video-only (audio stripped, no audio stream). Top cropped 60px (~5%) as drift guard, then upscale lanczos crf 18.
- Final 3.5s sharpness: 158.8 (upscale softening vs raw 223.0 — known, accepted)

## Honest defects
1. Gold necklace from the base visible at the collar (base artifact, same as Krem/Beige/Hitam).
2. At 3.5s the left hand crosses the chest and covers most of the dog motif (only the head is visible) — choreography, not a product change; the motif is intact in all other frames.
3. Mouth/chin peek at the top edge in the raw frames (tolerated); after the 60px top crop the final video starts around the nose, mouth no longer visible.
4. Upscale softening (known, accepted): 3.5s sharpness 158.8 final vs 223.0 raw.
5. The dog motif in frame-0 sits slightly lower on the chest than in the reference close-up, but size, shape, colors, and all details match.

## Files in this folder
- `tok_00.jpg` … `tok_09.jpg` — Tokopedia gallery (10 images)
- `frame0_puppy.webp` — frame-0 (Gate 1 PASSED)
- `puppy_duduk_lilo_v1_upscale720.mp4` — final video
- `g3_f0s.jpg`, `g3_f0.6s.jpg`, `g3_f2s.jpg`, `g3_f3.5s.jpg`, `g3_f6.5s.jpg`, `g3_f9.5s.jpg` — Gate 3 frames
- `g3_f9.5s_top.jpg`, `g3_f6.5s_top.jpg` — enlarged tops (eyes check)
- `g3_final_3.5s.jpg` — 3.5s frame from the final video
- `NOTES.md` — this file
