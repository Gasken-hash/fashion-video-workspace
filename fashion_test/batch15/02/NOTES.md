# Product 02 — MAMAMARA Cardigan Zipper Candy Rainbow (Batch 15, Batch 1)
- Product ID: 1737095077250500180
- Link: https://vt.tokopedia.com/t/ZS9fQg8G63srt-fzieY/
- Reference: `tok_00.jpg` (800x800, from Jendral's Tokopedia link via curl-cffi)
- Base: `~/workspace/fashion_test/bases/base_pita_v3_kacamata.jpg` (Pita v3 frame-0, glasses prop, 1536x2752)
- Movement planned: Set A adapted (hip/hair → trace closed zipper → chest → hem → lap → slight torso turn → peace sign)

## Reference details (from tok_00.jpg)
Pastel rainbow horizontal stripes (light blue / pink / yellow / white bands), light blue flat polo collar, FULL front silver zipper, small yellow rectangular chest patch on left chest, long sleeves with light blue ribbed cuffs, light blue ribbed hem band, hip-length slightly loose fit. Flat-lay, no bottom shown → bottom = base's white drawstring pants.

## Frame-0 v1
- File: `media-generation-frame0-candy-duduk-lilo-v1-0-85e9a247-236c-4bdd-96b2-2978105b2a15.jpg` (1168x2112, sharpness 40.8)
- One fresh LILO edit from the base, with the FULLY-CLOSED zipper clause + framing clause.

## GATE 1 — FAILED (zipper open at the top). NO VIDEO generated.
Passed:
- Rainbow stripes: colours + order match (blue/pink/yellow/white bands across chest, body, sleeves)
- Polo collar: light blue, same shape
- Yellow chest patch: present, left chest, yellow, rectangular (text garbled "EONUSTINGI" — reference text also illegible at this size)
- Long sleeves + light blue ribbed cuffs: match
- Light blue ribbed hem band: match
- Fit: hip-length, slightly loose: match
- Framing: mouth-cut, no eyes visible; chin/mouth peek at top (tolerated)
- Hair: loose high bun with face-framing strands
- Base kept: maroon wall, white drawstring pants, glasses on floor bottom right, hand on hip

FAILED — zipper (evidence: `gate1_zipper_top.jpg`, `gate1_zipper_bottom.jpg`):
- TOP: zipper OPEN. The two collar flaps spread wide apart in a V; the slider sits at MID-CHEST (below the yellow patch, at the pink stripe), NOT at the top below the collar; above the slider the zipper teeth are separated and a triangle of bare neck/upper-chest skin + the gold necklace/pendant is visible in the V.
- BOTTOM: closed OK — panels meet, bottom slider at the hem, no gap.
- This is the same failure pattern as Zipper Leather Abu v1 / Beige v1 (slider mid-chest, V of skin + necklace).

Per the hard rule (open at top OR bottom = FAIL), no video was generated. Work stopped here per the task instruction.

## Prescription for a v2 fresh edit (NOT attempted — awaiting parent order)
Fresh LILO edit from the base with the stronger clause (from the Abu v2 notes):
"the two light blue polo collar flaps MEET and TOUCH at the center front, the zipper teeth are joined all the way to the very top edge of the collar, the neckline is a closed collar with NO V-opening, NO skin gap anywhere between the collar and the zipper, the slider sits at the very top just below the collar". Plus the standard FULLY-CLOSED clause. Never surgically fix this LILO frame-0.

## Files in this folder
- `tok_00.jpg` … `tok_07.jpg` — Tokopedia gallery (8 images)
- `media-generation-frame0-candy-duduk-lilo-v1-0-85e9a247-236c-4bdd-96b2-2978105b2a15.jpg` — frame-0 v1 (Gate 1 FAILED)
- `gate1_zipper_top.jpg` / `gate1_zipper_bottom.jpg` — zipper evidence crops v1
- `NOTES.md` — this file

## Frame-0 v2 — GATE 1 PASSED (13 Nov 2026, ~18:33 WITA)
- File: `media-generation-frame0-candy-duduk-lilo-v2-0-eb9a1737-a9a6-4d9a-b1c8-5afcf8291525.webp` (1168x2112, sharpness 46.3); JPG copy `frame0_candy_v2.jpg`
- Fresh LILO edit from the base with BOTH zipper clauses (standard FULLY-CLOSED + stronger collar-meets clause).
- ZIPPER FIXED: slider at the TOP just below the collar, teeth joined all the way down, both panels meet, NO chest skin, NO cleavage, NO necklace visible (evidence: `gate1_v2_zipper_top.jpg`, `gate1_v2_zipper_bottom.jpg`). Only a small natural neck opening where the neck emerges from the polo collar — same as the Krem Zipper Leather precedent (deemed safest). Bottom closed OK, bottom slider at hem (two-way zipper, matches reference).
- Everything else passed again: rainbow stripes (colours + order), light blue polo collar, yellow patch left chest ("SOMISTING", garbled like the reference's illegible text), long sleeves + light blue ribbed cuffs, light blue ribbed hem, hip-length slightly loose fit, mouth-cut framing (no eyes; chin/mouth peek tolerated), bun, base kept (maroon wall, white pants, glasses bottom right, hand on hip). No invented details.

## Video v2 — GATE 3 PASSED (13 Nov 2026, ~18:34 WITA)
- Raw: `media-generation-candy-duduk-lilo-v2-0-7f288824-efb8-4413-b17b-918f520cb7cb.mp4` (640x1168, 24fps, 10.0s, h264 + AAC audio from generator, stripped in finish)
- Movement: Set A adapted (hip/hair → trace closed zipper → chest spread → hem → lap → slight torso turn → peace sign). Calm, torso still, hands only.
- Background 0 vs 0.6s: identical (wall/floor/glasses frozen). ✓
- Eyes/face: NO eyes or full face in any frame. Enlarged top of 9.5s (`g3_v2_top95.jpg`) shows only mouth/chin/nose — eyes cut. 6.5s side-turn is a profile (nose/lips/chin, eye not visible) — same tolerance as Hitam v1. ✓
- Zipper: FULLY CLOSED in ALL frames checked (0 / 2 / 3.5 / 6.5 / 9.5s; crops `g3_v2_zip2.jpg`, `g3_v2_zip6.5.jpg`, `g3_v2_zip9.5.jpg`), slider at top throughout. ✓
- Product identical in all frames; no invented details. ✓
- Sharpness: video frames 112.5–135.6 vs frame-0 46.3 — video much sharper, no unsharp needed. ✓
- Finish: top cropped 58px (~5%) as drift guard, audio stripped, upscale lanczos crf 18 to 720x1280.
- FINAL: `candy_duduk_lilo_v2_upscale720.mp4` — 720x1280, 24fps, 10.0s, h264, video-only (ffprobe-verified, no audio stream), 3.84 MB. Final 3.5s frame `g3_final_3.5s.jpg` (sharpness 98.8 — known upscale softening, accepted).

## Cacat jujur (v2 final)
1. Dagu/mulut ngintip di tepi atas frame mentah (ditoleransi); setelah crop 58px, frame final motong di hidung/dagu — tidak ada mulut kelihatan.
2. Patch kuning tulisannya "SOMISTING" (garbled) — sama seperti referensi yang tulisannya juga tidak terbaca di ukuran ini.
3. Di 3.5 dtk kedua tangan menutupi sebagian patch kuning (gerakan chest-spread) — patch utuh di frame lain.
4. Pelembutan upscale (diketahui, diterima): ketajaman 3.5 dtk final 98.8 vs video mentah 135.6.
5. Kalung emas base tidak kelihatan (tertutup resleting yang tertutup penuh) — bagus, bukan cacat.
6. Frame-0 sendiri agak lembut (46.3) tapi videonya jauh lebih tajam, jadi final tidak kelihatan lembut.

## Media calls used this task: 1 image (frame-0 v2) + 1 video. No refusal, no retry.
