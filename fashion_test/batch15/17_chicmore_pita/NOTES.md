# Product 17 — CHICMORE kemeja wanita feminime variasi pita (Batch 15, batch 4)
- Product ID: 1734262430542431973
- Link: https://vt.tokopedia.com/t/ZS9fQj6W7yAbD-b2CcD/
- Reference: `tok_02.jpg` (800x800, from Jendral's Tokopedia link via curl-cffi). tok_00/tok_01 are NOT product photos (size chart "PILIH UKURAN", duplicated) — not used.
- Base: `~/workspace/fashion_test/bases/base_pita_v3_tumbler.jpg` (Pita v3 frame-0, black tumbler prop, 1536x2752)
- Movement: Set E adapted (lap → sentuh pita renda leher → dada → usap hem renda → pangkuan → muter samping → peace sign)

## Reference details (from tok_02.jpg)
White blouse on a hanger: lace ribbon tie at the neck (small bow + two long lace tails), small white buttons down the center front, wide ruffled eyelet-lace hem band with small round eyelet holes + scalloped edge, long sleeves attached at the shoulders with wide flared cuffs, slightly puffed shoulders. No bottom shown → bottom = base's white drawstring pants.

## Frame-0 v1
- File: `media-generation-frame0-pita-v1-0-36e9115d-bd91-4fe7-8ad0-94829da2265f.webp` (1168x2112, sharpness 130.3); also saved as `frame0_pita.jpg`
- One fresh LILO edit from the tumbler base, with the framing clause.

## GATE 1 — PASSED (first try)
Checked detail by detail vs the reference (with zoom crops `gate1_cuff.jpg`, `gate1_hem.jpg`, `gate1_neck.jpg`):
- White color ✓
- Lace ribbon tie at neck: bow + two long lace tails, lace-trimmed round collar ✓ (tails slightly longer than reference — same design, logged as defect)
- Front buttons: small white buttons down the center ✓
- Ruffled eyelet-lace hem: eyelet band with floral embroidery + holes + scalloped edge ✓ (frame-0 has an extra plain ruffle tier above the eyelet band; reference reads as a single eyelet ruffle band — logged as defect, not a fail: the eyelet hem itself matches)
- Long sleeves, attached, slightly puffed shoulders ✓
- Wide cuffs: visible right cuff is a wide gathered cuff with button ✓
- Fit: slightly loose, hip-length ✓
- Framing: mouth-cut, eyes NOT visible; chin/mouth peek at top (tolerated) ✓
- Hair: loose high bun with face-framing strands ✓
- Base kept: maroon wall, white drawstring pants, black tumbler bottom right, sitting pose, hand on hip ✓
- Pink bows + pearl buttons of the old cardigan: completely gone ✓

## Video v1 (raw)
- File: `media-generation-pita-duduk-lilo-v1-0-cf3450c2-5782-4650-ab9f-a9561105b313.mp4` (640x1168, 24fps, 10.0s, h264 + AAC audio, mean volume -51.7 dB — audio stripped in finishing)

## GATE 3 — PASSED
- Background 0 vs 0.6s identical ✓
- No eyes/full face in any frame: top of 9.5s frame enlarged (`g3_f9.5s_top.jpg`) — only lips/chin/cheek in side profile, nose tip at the very top edge, NO eye visible ✓ (same precedent as Hitam v1 / Kiyana)
- Product identical in all frames (0/2/3.5/6.5/9.5s), no invented details ✓
- Beats captured: hands crossed on lap (2s), both hands at the lace ribbon (3.5s), both hands tracing the lace hem (6.5s), peace sign + side turn (9.5s) ✓
- Calm motion, hands only ✓
- Sharpness: video frames 92.4–148.7 vs frame-0 58.9 (video SHARPER, no unsharp needed) ✓

## Final video
- File: `pita_duduk_lilo_v1_upscale720.mp4` — 720x1280, 24fps, 10.0s, h264, 3,482,919 bytes (~3.5 MB), video-only (audio stripped, ffprobe shows 1 video stream only)
- Finishing: top cropped 60px (~5%) as drift guard, then upscale lanczos crf 18
- Final 3.5s frame: `g3_final_3.5s.jpg` (sharpness 92.1 vs raw 140.1 — known upscale softening, accepted)

## Honest defects
1. Lace ribbon tails slightly longer than the reference (same design, just longer drape).
2. Hem has an extra plain ruffle tier above the eyelet band; reference reads as a single eyelet ruffle band. The eyelet band itself (floral embroidery + holes + scalloped edge) matches.
3. Thin gold chain from the base visible at the neck (base artifact, same as other videos).
4. Chin/mouth peek at the top edge of the raw video (tolerated); after the 60px crop the final frame cuts at the chin/neck — mouth no longer visible.
5. Upscale softening at 3.5s (140.1 → 92.1, known and accepted).

No generator refusal, no retry. 1 image call + 1 video call used. Not uploaded to Cloudinary / not logged in sheet — awaiting Jendral's approval.
