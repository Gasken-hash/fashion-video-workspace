# Product 05 — MAMAMARA Atasan Rajut Wanita Cable Knit Kerah Denim Layer Style Kekinian

- Product ID: 1735676465724491348
- Link (Tokopedia, from Jendral): https://vt.tokopedia.com/t/ZS9fQgBHhqK3x-f3y31/
- Reference: `tok_00.jpg` (800x800, from Tokopedia gallery via curl-cffi, verified) — gray cable-knit cardigan, denim collar + denim cuffs, 5 cream buttons, V-neck denim layer, long sleeves, on a chair. No bottom shown. Watermark "OFFICIAL STORE MAMAMARA" ignored, NOT reproduced.
- Base: `~/workspace/fashion_test/bases/base_pita_v3_kacamata.jpg` (Pita v3 frame-0, GLASSES prop on floor bottom right, 1536x2752, white pants in base, maroon wall, mouth-cut framing, hand on hip).
- Movement: Set D adapted (one-hand anchor) — right hand on hip; left hand: denim collar → buttons → stroke cable texture → lift denim cuff → hem → lap → peace sign. Calm, shoulders/chest still, hands only.
- Bottom: reference shows no bottom → matched to top: DARK denim jeans (dark indigo, straight-leg, plain), NOT the base's white pants. Written explicitly in the edit prompt.

## Frame-0
- File: `media-generation-frame0-denim-0-10ae0033-3ea6-4364-b374-a2528d1ef336.webp` (1168x2112) + `frame0_denim.jpg` (converted copy)
- Sharpness (Laplacian var): 195.2

## GATE 1 — PASSED (first try)
Checked frame-0 vs reference, detail by detail:
- Color: light heather-gray knit — MATCH
- Cable pattern: vertical braided columns down front + sleeves — MATCH
- Denim collar: blue denim, pointed, folded down — MATCH
- Denim V layer at chest: dark blue denim peeking in a V, 1 button on it — MATCH
- Buttons: exactly 5 round cream/pearl (1 on denim V + 4 down knit placket) — MATCH
- Denim cuffs: wide folded-up blue denim at both wrists — MATCH
- Sleeves: long, attached at shoulders, NOT off-shoulder — MATCH
- Hem: straight knit hem, small center front slit — MATCH
- Fit: fitted, as reference — MATCH
- Bottom: dark indigo denim jeans, plain, straight-leg — MATCH (task rule)
- Framing: mouth-cut, chin/mouth visible, eyes NOT visible — MATCH
- Hair: loose high bun + face-framing strands — MATCH
- Base kept: maroon wall, speckled floor, glasses bottom right, sitting pose, right hand on hip, gold necklace — MATCH
- No watermark reproduced; no bows/ruffles invented — GOOD

## Video (Gate 2)
- Raw: `media-generation-denim-duduk-lilo-v1-0-0a2010a7-9035-4c3d-a263-698464e6916a.mp4` (640x1168, 24fps, 10.0s, 5.8 MB, h264 + aac audio — audio stripped in finishing)
- Beats captured: collar touch at 2s, buttons/texture stroke at 3.5s, denim cuff shown/lifted at 2s, hem pinch at 6.5s, peace sign at 9.5s.

## GATE 3 — PASSED
- Background 0 vs 0.6s: visually identical (maroon wall, speckled floor, glasses same position); mean abs diff 9.83 is arm motion + resampling, not a background jump — PASS
- No eyes/full face at any frame (0 / 0.6 / 2 / 3.5 / 6.5 / 9.5s all mouth-cut); enlarged top of 9.5s frame (`g3_f9.5s_top_enlarged.jpg`) shows mouth + chin only, NO eyes — PASS
- Product identical in all frames: gray cable knit, denim collar, denim V, 5 buttons, denim cuffs, dark jeans — no invented details (no bows, no ruffles, no extra buttons) — PASS
- Sharpness: video frames 336.2–403.8 vs frame-0 195.2 — video SHARPER than frame-0, no unsharp needed — PASS
- Motion: calm, torso/shoulders/chest still, hands only — PASS

## Finishing
- Top crop 60px (~5%) as drift guard + audio stripped + upscale lanczos to 720x1280, crf 18.
- Final: `denim_duduk_lilo_v1_upscale720.mp4` — 720x1280, 24fps, 10.0s, 5.8 MB, video-only (volumedetect: no audio stream). ffprobe-verified.
- Final 3.5s frame: `g3_final_3.5s.jpg` (720x1280, sharpness 239.1).

## Honest defect list
1. Choreography drift (minor): at ~6.5s the RIGHT hand leaves the hip to pinch the hem, while Set D asked the left hand to do the hem beat and the right hand to stay anchored. The motion stays calm and hands-only; product/background/face all pass. Not a Gate 3 failure.
2. Buttons read slightly gold-toned in the video (warm light) vs cream/pearl in the reference; shape, count (5), and placement are exact.
3. Mouth/chin peek at the top edge in all frames (tolerated per face rule, 12 Nov 2026); eyes never visible.
4. Upscale softening (known, accepted): final 3.5s sharpness 239.1 vs raw video 367.5 — interpolation only, looks better to the eye per Jendral's 720p rule.
