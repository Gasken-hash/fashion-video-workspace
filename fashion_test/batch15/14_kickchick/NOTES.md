# Product 14_kickchick — Kickchick Doublesleeve Stitch Stripe Cat Love (Batch 15, batch 3)
- Product ID: 1734475100271183768
- Link: https://vt.tokopedia.com/t/ZS9fQj0T1zVwX-h9QqU/
- Reference: `tok_01.jpg` (800x800, from Jendral's Tokopedia link via curl-cffi) — flat-lay BLACK version. tok_00 is a 3-color display, NOT used as main ref.
- Base: `~/workspace/fashion_test/bases/base_pita_v3_kacamata.jpg` (Pita v3 frame-0, glasses prop, 1536x2752)
- Movement: Set D adapted (one-hand anchor: right hand on hip; left hand: heart logo → lift striped sleeve → hem → lap → peace sign)

## Reference details (from tok_01.jpg)
Black short-sleeve outer tee, round crew neck, thin white contrast stitching around collar/sleeve hems/hem, layered over long WHITE inner sleeves with thin BLACK horizontal stripes (striped sleeve extends below the black short sleeve, visible on both arms). Small red-and-white heart patch on left chest (white square, red heart). Straight hem. Relaxed fit, hip-length. No bottom shown → bottom = black pants (matched to top).

## Frame-0 v1
- File: `media-generation-frame0-kickchick-0-a568ca7e-fe8d-4d5f-890a-b502029580f2.webp` (1168x2112, sharpness 193.3 scipy / 138.8 manual); copy `frame0_kickchick.jpg`
- One fresh LILO edit from the kacamata base.

## GATE 1 — PASSED (first try)
- Black color ✓, doublesleeve construction both arms ✓ (black short outer over white/black striped long inner, stripes match), heart patch left chest ✓ (white square, red heart), white contrast stitching collar/sleeve hems/hem ✓, round crew neck ✓, straight hem ✓, relaxed hip-length fit ✓
- Bottom: solid black straight-leg pants ✓ (not the base's white pants)
- Framing: mouth-cut, eyes NOT visible ✓ (mouth/chin peek at top, tolerated); hair loose high bun ✓
- Base kept: maroon wall, speckled floor, glasses bottom right, hand on hip ✓
- No bows, no pearl buttons, no ruffle cuffs, no pink cardigan ✓

## Video v1 (raw)
- File: `media-generation-kickchick-duduk-lilo-v1-0-62ee6712-615d-45eb-89dc-97423d0c32ab.mp4` (640x1168, 24fps, 10.0s, h264 + aac audio — stripped in final)

## GATE 3 — PASSED
- Background 0 vs 0.6s identical ✓ (wall/floor/glasses frozen)
- Eyes/full face: never visible in any frame. Enlarged top of raw 9.5s: nose tip + mouth at the top edge, eyes cut. After the 60px top crop, final 9.5s top shows ONLY mouth/chin ✓ (verified on `g3_final_top95.jpg`)
- Product identical in all frames 0/2/3.5/6.5/9.5 ✓ — black doublesleeve, striped inner sleeves, heart patch, white stitching, black pants; no invented details
- Beats captured: touch heart logo (2s), hem/lap (3.5s), lift striped inner sleeve at wrist (6.5s), peace sign clear (9.5s) ✓
- Sharpness (manual Laplacian): video frames 397.8–551.4 vs frame-0 138.8 — video much sharper, no unsharp needed ✓
- Calm motion, hands only, torso/shoulders/chest still ✓

## Final video (ffprobe-verified)
- File: `kickchick_duduk_lilo_v1_upscale720.mp4` — 720x1280, 24fps, 10.0s, h264, video-only (no audio stream), 3.52 MB
- Top cropped 60px (~5%) as drift guard, then upscale lanczos crf 18. Final 3.5s sharpness 260.6 vs raw 403.3 (known upscale softening, accepted).

## Honest defects
1. Gold necklace from the base visible at the collar (base artifact, same as Krem/Beige/Hitam and most batch-15 videos).
2. Minor choreography drift: at 6.5s the RIGHT hand leaves the hip to rest on the lap while the left hand lifts the striped sleeve (Set D anchor broken briefly). Same class as the Denim v1 defect. Product/background/face all pass; not a Gate 3 failure.
3. Mouth/chin peek at the top edge in the raw video (tolerated); after the 60px crop the final frame cuts at the mouth/chin, nose tip removed.
4. Upscale softening (known, accepted): final 3.5s sharpness 260.6 vs raw video 403.3.

## Files in this folder
- `tok_00.jpg` … `tok_05.jpg` — Tokopedia gallery (6 images)
- `media-generation-frame0-kickchick-0-....webp` — frame-0 v1 (Gate 1 PASSED); `frame0_kickchick.jpg` — copy
- `media-generation-kickchick-duduk-lilo-v1-0-....mp4` — raw video (with generator audio)
- `kickchick_duduk_lilo_v1_upscale720.mp4` — FINAL (720x1280, 10.0s, silent)
- `g3_f0s.jpg` / `g3_f0.6s.jpg` / `g3_f2s.jpg` / `g3_f3.5s.jpg` / `g3_f6.5s.jpg` / `g3_f9.5s.jpg` — Gate 3 frames (raw)
- `g3_top95.jpg` / `g3_top65.jpg` — enlarged tops (raw); `g3_final_3.5s.jpg` / `g3_final_9.5s.jpg` / `g3_final_top95.jpg` — final-file frames
- `NOTES.md` — this file

No generator refusal, no retry. 1 image call + 1 video call used. Not uploaded to Cloudinary / not logged in sheet — awaiting Jendral's approval.
