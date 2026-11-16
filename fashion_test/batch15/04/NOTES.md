# Product 04 — Ruffle Cuff (Batch 15, TikTok batch)

**Product:** MAMAMARA — Atasan Rajut Ruffle Cuff Lengan Panjang Pita Coquette Sweet Style
**Product ID:** 1735428463595390548
**Link:** https://vt.tokopedia.com/t/ZS9fQgrHy3b16-u4DH0/
**Reference photo:** `batch15/04/tok_01.jpg` — NAVY version, LEFT model (ignore the white/cream version on the right model)
**Base:** `bases/base_pita_v3_tas.jpg` (Pita v3 frame-0, black bag on floor, 1536x2752)
**Movement:** Set C adapted (fit/waist) — shoulders → chest (bow) → waist/ruffle hem → lift ruffle cuff → lap → slow side turn → peace sign + small wave. Calm, shoulders/chest still, hands only.
**Date:** 13 Nov 2026

## Files
- Frame-0: `media-generation-frame0-ruffle-duduk-lilo-v1-0-986d4c6c-79e4-47ab-9766-39f935499864.webp` (1168x2112) + `frame0_ruffle.jpg`
- Raw video: `media-generation-ruffle-duduk-lilo-v1-0-7a599dfd-f1d5-4d12-a56d-ebe7aa3e3a5d.mp4` (640x1168, 10.0s, 24fps)
- **Final: `ruffle_duduk_lilo_v1_upscale720.mp4` (720x1280, 10.0s, 24fps, ~3.14 Mbps, video-only, ffprobe-verified)**
- 3.5s frame (final): `g3_final_3.5s.jpg` (720x1280)
- Gate 3 frames: `g3_f0s.jpg`, `g3_f0.6s.jpg`, `g3_f2s.jpg`, `g3_f3.5s.jpg`, `g3_f6.5s.jpg`, `g3_f9.5s.jpg` (+ enlarged tops `g3_f9.5s_top.jpg`, `g3_f6.5s_top.jpg`)
- Gate 1 crops: `g1_ref_collar.jpg`, `g1_f0_collar.jpg`, `g1_f0_hem.jpg`

## Gate 1 — PASSED (first try)
Frame-0 vs reference (navy, left model), detail by detail:
- NAVY color: deep navy ✓
- Checkered collar: pointed gingham collar with cream beaded trim along the edge — same kind as reference (zoomed comparison confirms reference also has a beaded trim) ✓
- Small bow: ONE small cream bow on upper chest, dark center ✓
- Black buttons: straight row down center front ✓
- Ruffle checkered hem: gingham ruffle band ✓
- Checkered ruffle cuffs: both wrists, flared ruffle ✓
- Fit: relaxed, matches ✓
- White pleated skirt: neat vertical pleats, smooth waistband ✓
- Framing: mouth/chin cut, eyes NOT visible ✓
- Hair: loose high bun with face-framing strands ✓
- Base elements kept: warm maroon wall, speckled floor, black bag bottom right, hand on hip ✓

## Gate 3 — PASSED
- Background 0 vs 0.6s: identical (wall, floor, bag unmoved) ✓
- No eyes/full face in any frame: enlarged tops of 9.5s and 6.5s frames show mouth/chin/nose only, eyes cut off ✓ (6.5s is a side-turn profile — nose/lips/chin visible, eyes NOT visible)
- Sharpness: frame-0 93.4; video 2s 395.8; video 3.5s 327.0 — video SHARPER than frame-0, no unsharp needed ✓
- Product details intact in all frames (0/2/3.5/6.5/9.5s): navy, collar, bow, buttons, hem ruffle, cuffs, pleated skirt ✓
- Movement beats visible: shoulders (2s) → bow touch (3.5s) → cuff lift + side turn (6.5s) → lap (9.5s) ✓

## Finishing
- Top crop 60px (~5%) as drift guard: crop=640:1108:0:60
- Audio stripped (generator added an AAC track; final is video-only, verified by ffprobe)
- Upscale to 720x1280 (ffmpeg lanczos, crf 18, preset slow)
- Final verified: 720x1280, 10.0s, 24fps, h264 video only, 3,932,748 bytes

## Honest defect list
1. Gold necklace/pendant from the base photo is visible at the collar (small, same base artifact as in Krem/Beige/Hitam — not part of the product).
2. Collar trim beads read slightly larger/more prominent than in the reference, though the same kind of trim.
3. Peace sign + small wave at the end is not crisp — at 9.5s the hands are on the lap with slight motion blur; the ending beat is implied rather than clearly shown.
4. Frame-0 itself is soft (sharpness 93.4), but the video came out sharper (395.8 at 2s), so no visible softness in the final.
5. Mouth/chin peek at the top edge throughout (tolerated per Jendral's face rule).
6. At 6.5s the head turns to a side profile (nose/lips/chin visible) — eyes stay cut off, within tolerance.
