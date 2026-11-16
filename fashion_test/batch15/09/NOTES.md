# Product 09 — MAMAMARA Cardigan Bulu Fuzzy Jaket Zipper Resleting Coquette Girly (Batch 15, Batch 2)
- Product ID: 1734405195357521492
- Link: https://vt.tokopedia.com/t/ZS9fQh5K2mNwQ-c4RrT/
- Reference: `tok_00.jpg` (800x800, from Jendral's Tokopedia link via curl-cffi) — two models; RIGHT model used: white solid fuzzy zip-up cardigan, light pink trim along front zipper/collar/hem/pockets, small pink heart embroidery on left chest, long SOLID sleeves, white long tiered skirt. Left model wears a striped-sleeve variant — NOT used.
- Base: `~/workspace/fashion_test/bases/base_pita_v3_kacamata.jpg` (Pita v3 frame-0, glasses prop, 1536x2752)
- Movement planned: Set B adapted (hair → trace closed zipper → touch pink heart → pinch hem → lap → peace sign)

## Reference details (from tok_00.jpg, right model)
White soft fuzzy knit cardigan, light pink trim along the front zipper tape, collar edge, hem band and two front pocket openings, small pink heart embroidered on the left chest, long solid white sleeves (no stripes), full front zipper, hip-length slightly loose fit. Worn with a white long skirt. Bottom for video: white pleated mini skirt (per reference + skirt rotation).

## Frame-0 v1
- File: `media-generation-frame0-fuzzy-v1-0-d65d6bc1-4a71-4f5b-85be-0b025895d780.webp` (1168x2112, sharpness 108.3)
- One fresh LILO edit from the base, with BOTH zipper clauses (standard FULLY-CLOSED + stronger collar-meets) + framing clause + white pleated skirt.

## GATE 1 — FAILED (zipper open at the top). NO VIDEO generated.
Passed:
- White fuzzy texture: match
- Pink trim along zipper / collar / hem / pockets: match
- Small pink heart on left chest: match (pink heart, left chest)
- Long solid sleeves, no stripes: match (right-model version, not the striped variant)
- White pleated mini skirt: match (neat vertical pleats, smooth waistband)
- Fit: hip-length, slightly loose: match
- Framing: mouth-cut, no eyes visible; chin/mouth peek at top (tolerated)
- Hair: loose high bun with face-framing strands
- Base kept: maroon wall, speckled floor, glasses on floor bottom right, hand on hip
- Pita v3 details removed: pink bows, pearl buttons, ruffle cuffs all gone

FAILED — zipper (evidence: `gate1_zipper_top.jpg`, `gate1_zipper_bottom.jpg`):
- TOP: zipper OPEN. The slider sits at MID-CHEST (just below the heart embroidery), NOT at the top below the collar; above the slider the two collar flaps spread wide apart in a V, the zipper teeth are separated, and a large triangle of bare neck/upper-chest skin + the gold necklace with heart pendant is fully visible.
- BOTTOM: closed OK — panels meet at the hem, zipper runs to the bottom, no gap.
- Same failure pattern as Zipper Leather Abu v1 / Beige v1 and Candy v1 (slider mid-chest, V of skin + necklace). The stronger collar-meets clause did NOT hold this time (it did hold for Candy v2).

Per the hard rule (open at top OR bottom = FAIL), no video was generated. Work stopped here per the task instruction.

## Prescription for a v2 fresh edit (NOT attempted — awaiting parent order)
Fresh LILO edit from the base, same base (kacamata), with an even stronger zipper clause, e.g. add: "the zipper is zipped ALL the way up so the collar stands closed around the neck like a turtleneck collar, the slider is hidden at the very top of the collar, the two front panels overlap slightly at the center and the pink trim forms ONE continuous vertical line from the collar to the hem with NO break and NO V-gap, the neck and chest are completely covered by the white fuzzy fabric, the gold necklace is NOT visible". Keep the standard FULLY-CLOSED clause + collar-meets clause. Re-verify zipper top AND bottom at Gate 1 — the fresh edit re-rolls everything, so all other details must be re-checked too. Never surgically fix this LILO frame-0.

## Frame-0 v2 — GATE 1 PASSED (13 Nov 2026, ~18:44 WITA)
- File: `media-generation-frame0-fuzzy-v2-0-4d5373a9-fe51-4985-b746-ebad3692cdfb.webp` (1168x2112, sharpness 31.5) / `frame0_fuzzy_v2.jpg`
- One fresh LILO edit from the base with ALL THREE zipper clauses (standard FULLY-CLOSED + collar-meets + strongest turtleneck/continuous-trim) + framing clause + white pleated skirt.
- ZIPPER — FIXED, PASS: slider at the VERY TOP just below the collar; collar stands closed around the neck like a turtleneck; both collar flaps meet at center front; pink trim forms ONE continuous vertical line collar→hem, NO break, NO V-gap; NO bare skin, NO cleavage, NO necklace visible. Evidence: `gate1_v2_zipper_top.jpg` (slider top, collar closed) + `gate1_v2_zipper_bottom.jpg` (zipper runs to hem, panels meet, no gap). The three-clause combo held where the two-clause version failed in v1.
- Everything else PASSES: white fuzzy texture, pink trim along zipper/collar/hem/pockets, small pink heart on left chest (outline with tiny text inside — reference heart looks plain, minor), long solid sleeves (no stripes), white pleated mini skirt (neat vertical pleats), hip-length slightly loose fit, mouth-cut framing (no eyes; chin/mouth peek tolerated), loose high bun, base kept (maroon wall, speckled floor, glasses bottom right, hand on hip), old pink cardigan details gone (no bows, no pearl buttons, no ruffle cuffs).

## Video v2 — GATE 3 PASSED
- Raw: `media-generation-fuzzy-duduk-lilo-v2-0-fb2e907b-ce60-4b4a-bd03-2be9948917bd.mp4` (640x1168, 24fps, 10.0s, h264 + AAC — audio stripped in finishing).
- Movement Set B adapted: hair (2s) → trace closed zipper / touch pink heart (3.5s) → pinch hem (6.5s) → lap → peace sign (9.5s). Calm, shoulders/chest still, hands only.
- Background 0 vs 0.6s identical. Eyes/full face: NONE in any frame — enlarged top of 9.5s (`g3_v2_top95.jpg`) shows mouth/chin/nose tip only. Zipper FULLY CLOSED in ALL frames (0/2/3.5/6.5/9.5s), slider at top, collar closed. Product identical in all frames, no invented details.
- Sharpness: video frames 81.6–116.3 vs frame-0 29.3 — video SHARPER than frame-0, no unsharp needed.
- Finish: top cropped 60px (~5%) as drift guard, audio stripped, upscale lanczos crf 18 → **final: `fuzzy_duduk_lilo_v2_upscale720.mp4` — 720x1280, 24fps, 10.0s, h264, 3,138,577 bytes, video-only (ffprobe: 1 stream, volumedetect: NO AUDIO STREAM)**. Final 3.5s sharpness 61.0 vs raw 88.3 (known upscale softening, accepted). Delivery frame: `g3_final_3.5s.jpg`.

## Honest defects (v2 final)
1. Pink heart on left chest has tiny text inside the outline ("mp"-like); reference heart looks plain pink. Shape, color, size, position match.
2. Chin/mouth peek at top edge in raw frames (tolerated); after 60px crop the final cuts at nose/chin — mouth no longer visible.
3. Upscale softening at 3.5s (88.3 → 61.0, known and accepted).
4. Frame-0 itself is soft (31.5) but the video is sharper, so the final does not look soft.
5. Gold necklace from base NOT visible (covered by the fully closed zipper) — a plus vs other videos.

## Files in this folder
- `tok_00.jpg` … `tok_10.jpg` — Tokopedia gallery (11 images)
- `media-generation-frame0-fuzzy-v1-0-d65d6bc1-4a71-4f5b-85be-0b025895d780.webp` — frame-0 v1 (Gate 1 FAILED)
- `gate1_zipper_top.jpg` / `gate1_zipper_bottom.jpg` — zipper evidence crops
- `NOTES.md` — this file
