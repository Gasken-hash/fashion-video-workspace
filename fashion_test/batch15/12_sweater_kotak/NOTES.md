# Product 12 — Sweater Wanita Korea Longgar Retro Kotak-kotak (Batch 15, Batch 3)
- Product ID: 1730009161227209050
- Link: https://vt.tokopedia.com/t/ZS9fQi4R8xTyU-f7OoS/
- Reference: `tok_00.jpg` (800x800, from Jendral's Tokopedia link via curl-cffi)
- Base: `~/workspace/fashion_test/bases/base_pita_v3_tumbler.jpg` (Pita v3 frame-0, tumbler prop, 1536x2752)
- Movement: Set A adapted (hip/hair → touch gold buttons → chest plaid → hem → lap → slight torso turn → peace sign)

## Reference details (from tok_00.jpg)
Deep green tweed with cream/white square plaid check grid, cream ribbed round neckline, cream ribbed center placket with small round GOLD buttons down the front (~5), two cream-trimmed patch pockets on the front each with a small gold button, long sleeves attached at shoulders with cream ribbed cuffs each with a small gold button, cream ribbed hem, loose/oversize fit. Mirror selfie; model carries a black crossbody bag with gold chain — NOT used (no-bag rule). Bottom not shown → white drawstring pants kept from base. Note: the reference hem is NOT visible (photo cropped at the bottom), so hem length could not be verified against the original.

## Frame-0 v1
- File: `media-generation-frame0-kotak-0-f259063d-705e-4ff9-afba-3bf892198067.webp` (1168x2112, sharpness 234.3); JPG copy `frame0_kotak.jpg`
- One fresh LILO edit from the tumbler base, with framing clause + explicit bans (no pink bows, no pearl buttons, no bag).

## GATE 1 — PASSED (first try)
- Green + cream plaid check: match (colour + grid scale)
- Cream ribbed round neckline: match
- Cream ribbed center placket + gold buttons (~5): match
- Two cream-trimmed patch pockets, each with a gold button: match (symmetric at chest level in frame-0; in the reference one sits lower due to the mirror-selfie angle)
- Long sleeves attached at shoulders + cream cuffs with gold buttons: match
- Cream ribbed hem: match
- Fit: loose, slightly boxy: match (reference hem unseen, so length not verifiable — noted, not a fail)
- Framing: mouth-cut, eyes NOT visible; hair in loose high bun with face-framing strands
- Base kept: maroon wall, white drawstring pants, black tumbler bottom right, hand on hip; NO bag, NO pink bows, NO pearl buttons
- Gold necklace from base visible at the collar (base artifact, same as Krem/Beige/Hitam)

## Video v1
- Raw: `media-generation-kotak-duduk-lilo-v1-0-98b3176f-dcbc-4970-9818-f58b4e3be040.mp4` (640x1168, 10.0s, 24fps, h264 + AAC audio — audio stripped in finishing)
- Set A adapted, calm, hands only.

## GATE 3 — PASSED
- Background 0 vs 0.6s: identical (wall/floor/tumbler frozen) ✓
- Product identical in all frames (0/2/3.5/6.5/9.5): green plaid, cream trim, gold buttons, 2 pockets, no invented details ✓
- Eyes/full face: never visible in any frame — enlarged top of 9.5s frame (`g3_top95.jpg`) shows only mouth/nose/chin ✓
- Sharpness: video frames 554–726 vs frame-0 234.3 — video MUCH sharper, no unsharp needed ✓
- Beats captured: hair (2s), chest/buttons (3.5s), hem/waist (6.5s), peace sign clear (9.5s) ✓
- Motion calm, torso/shoulders/chest still, hands only ✓

## Final video
- `kotak_duduk_lilo_v1_upscale720.mp4` — 720x1280, 24fps, 10.0s, h264, video-only (audio stripped), 5.84 MB
- Top cropped 58px (~5%) as drift guard, then upscale lanczos crf 18
- Final 3.5s frame sharpness 424.7 vs raw 612.7 (upscale softening, known + accepted; still well above frame-0's 234.3)
- Final 3.5s frame: `g3_final_3.5s.jpg` — crop cuts at the chin, mouth no longer visible in the final

## Honest defects
1. Gold necklace from the base visible at the collar (base artifact, same as Krem/Beige/Hitam).
2. Chin/mouth peek at the top edge of the RAW video (tolerated); after the 58px crop the final cuts at the chin — mouth no longer visible.
3. At 9.5s the raised peace-sign arm partly covers the left pocket's gold button (occlusion by pose, not a product change; pocket intact in all other frames).
4. The two pockets sit symmetric at chest level in frame-0, while in the reference one pocket sits lower (mirror-selfie angle); both pockets present with gold buttons.
5. Reference hem length not verifiable (hem unseen in tok_00); frame-0 hem sits at the waistband.
6. Upscale softening at 3.5s (612.7 → 424.7, known, accepted).

## Files in this folder
- `tok_00.jpg` … `tok_10.jpg` — Tokopedia gallery (11 images)
- `media-generation-frame0-kotak-0-....webp` + `frame0_kotak.jpg` — frame-0 v1 (Gate 1 PASSED)
- `media-generation-kotak-duduk-lilo-v1-0-....mp4` — raw video (with generator audio)
- `kotak_duduk_lilo_v1_upscale720.mp4` — FINAL (720x1280, silent)
- `g3_f0s.jpg`, `g3_f0.6s.jpg`, `g3_f2s.jpg`, `g3_f3.5s.jpg`, `g3_f6.5s.jpg`, `g3_f9.5s.jpg`, `g3_top95.jpg` — Gate 3 frames
- `g3_final_3.5s.jpg` — 3.5s frame from the final video
- `NOTES.md` — this file

Media calls used: 1 image + 1 video. No generator refusal, no retry.
