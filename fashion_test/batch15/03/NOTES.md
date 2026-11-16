# Product 03 — Ribbon Cable Knit (Batch 15) — NOTES

## Product
- **Name:** MAMAMARA Cardigan Rajut Wol 2 Layer Ribbon Cable Knit Coquette Korean Style
- **Product ID:** 1737346068617463380
- **Link:** https://vt.tokopedia.com/t/ZS9fQg61vwAf6-ggOaF/
- **Reference photo:** `batch15/03/tok_00.jpg` (800x800, from Tokopedia gallery via curl-cffi, verified)
- **Base photo:** `bases/base_pita_v3_tumbler.jpg` (1536x2752, Pita v3 frame-0, black tumbler floor prop)
- **Movement:** Set B adapted (detail showcase)

## Reference details (tok_00.jpg + gallery tok_01/tok_02 cross-check)
- Color: very pale pink / cream, almost off-white with a pink tint
- Round ribbed neckline, center front placket with small round buttons (~7)
- Two vertical braided cable columns down the front, one each side of the placket
- **Bows: 6 small bows total — 3 per side, arranged along the two cable columns only. NO bows in the center of the chest.** (Confirmed in tok_00 zoom, tok_01 cream colorway, tok_02 yellow colorway — all show 6 bows, 3 per side.)
- Scalloped/wavy hem, long sleeves with ribbed cuffs, slightly loose fit
- No bottom shown (hanger shot)

## Frame-0
- File: `media-generation-frame0-ribbon-0-f5c3fa53-c205-43d4-9326-67e9615fec81.webp` (1168x2112)
- Generated: LILO edit from base_pita_v3_tumbler.jpg + tok_00.jpg reference, one fresh edit

## GATE 1 — FAILED (do NOT generate video)
Checked frame-0 vs reference, detail by detail:
- Color light pink/cream: PASS
- Round neck: PASS
- Buttons count/position: PASS (~6-7 small round buttons down the center)
- Cable braids (two vertical columns): PASS
- **Bows count/position: FAIL — frame-0 has 10 bows, reference has 6.**
  - Frame-0: 3 pale yellow bows on the left cable column + 3 on the right cable column (these 6 match) + **4 extra PINK bows in the center of the chest (upper-left, upper-right, lower-left, lower-right) that do NOT exist in the reference.**
  - The 4 pink center bows are prominent and clearly visible; the generator invented them.
- Scalloped hem: PASS
- Fit (slightly loose): PASS
- Bottom (white drawstring pants kept): PASS
- Tumbler (black, bottom right kept): PASS
- Framing (mouth-cut, eyes NOT visible): PASS
- Pose (sitting, right hand on hip): PASS
- Wall (warm maroon): PASS

**Verdict: GATE 1 FAIL — one deviation (bow count 10 vs 6, 4 invented pink center bows). No video generated, per the locked rule (one deviation = FAIL).**

## Next step (for parent agent)
- A LILO frame-0 must never be surgically fixed (it reverts). The fix is a FRESH LILO edit from the base with the bow count spelled out explicitly, e.g. "exactly SIX small bows in total, THREE on each cable column, and NO bows anywhere else on the chest, NO pink bows in the center".
- This subagent stopped at Gate 1 per its task instructions ("report it and stop") — no retry was attempted.

## Frame-0 v2 — GATE 1 FAILED (buttons)
- File: `media-generation-frame0-ribbon-v2-0-d9636c5b-2f39-4517-9516-fb2bea937fff.webp` (1168x2112, sharpness 48.2)
- Generated: fresh LILO edit from base_pita_v3_tumbler.jpg + tok_00.jpg reference, with the explicit bow clause.
- **BOWS — FIXED, PASS:** exactly SIX small pale bows, 3 per cable column, center of chest plain with NO bows. The 4 invented pink center bows from v1 are gone. Verified in `f0v2_chest_zoom.jpg`.
- **BUTTONS — FAIL:** v2 has only **5 buttons**, and they are **large pearl domes with gold rims** in a single column. Reference has ~7 small FLAT round buttons (white/pink alternating) in a single column down the ruffled placket; v1 had ~6-7 small flat buttons and PASSED. v2 regressed on buttons: count 5 vs ~7, larger size, pearl/gold style vs small flat white/pink. Verified in `f0v2_placket_zoom.jpg` vs `ref_placket_zoom.jpg` and `f0v1_placket_zoom.jpg`.
- Everything else PASSES: color light pink/cream, round ribbed neck, two cable braids, scalloped hem, slightly loose fit, white drawstring pants, black tumbler, mouth-cut framing (eyes NOT visible), bun, sitting pose, maroon wall.
- **Verdict: GATE 1 FAIL — one deviation (buttons). No video generated, per the locked rule.**
- **Prescription for v3 (not attempted):** fresh LILO edit from the base, KEEP the exact bow clause from v2 AND add the button clause: "SEVEN small flat round buttons, white and pink alternating, in a single column down the center placket, small and flat, NOT large pearl domes, NO gold rims". The v3 edit must preserve the 6-bow fix — re-verify both bows and buttons at Gate 1.

## Frame-0 v3 — GATE 1 PASSED, video made, GATE 3 PASSED
- File: `media-generation-frame0-ribbon-v3-0-54b590a5-0588-464c-a076-cfca182d686f.webp` (1168x2112, sharpness 45.7); JPG copy `frame0_ribbon_v3.jpg`
- Generated: fresh LILO edit from base_pita_v3_tumbler.jpg + tok_00.jpg reference, with BOTH clauses (exact 6 bows + 7 small flat alternating buttons).
- **BOWS — PASS:** exactly SIX small pale bows, 3 per cable column, center of chest plain, NO center bows. The v2 fix is preserved. Verified in `f0v3_chest_zoom.jpg`.
- **BUTTONS — PASS:** small FLAT round buttons, white/pink alternating, single column down the center ruffled placket, NO pearl domes, NO gold rims. The v2 regression is fixed. Count is 6 (white, pink, white, pink, pink, white) vs the 7 prescribed — disclosed honestly: the reference count is "~7" (approximate; the flat-lay's overlapping placket makes an exact count ambiguous) and v1 passed with "~6-7", so 6 is within the range previously accepted as passing. Style, size, color alternation, and position all match the reference.
- Everything else PASSES: light pink/cream color, round ribbed neck, two cable braids, scalloped hem, slightly loose fit, long sleeves + ribbed cuffs, white drawstring pants, black tumbler, mouth-cut framing (eyes NOT visible), bun, sitting pose, maroon wall.
- **Verdict: GATE 1 PASS — both v1 and v2 failure modes fixed in one fresh edit.**
- Video: `media-generation-ribbon-duduk-lilo-v3-0-5d19bdf4-7284-45ba-abe0-ac2aee492f25.mp4` (raw 640x1168, 24fps, 10.0s, h264 + AAC generator audio) — Set B adapted (hair → lift cuff → touch top bow → pinch hem → stroke cable → lap → peace sign), calm, torso still, hands only, background-freeze clause.
- **GATE 3 — PASS:** background 0 vs 0.6s identical; no eyes/full face in any frame (enlarged top of 9.5s shows only mouth/chin/nose tip, eyes never visible); product identical in all frames (6 bows + small flat buttons at 0/2/3.5/6.5/9.5s, no invented details); beats captured (cuff-lift + top-bow touch at 3.5s, cable stroke at 6.5s, clear peace sign at 9.5s); sharpness video 142–179 vs frame-0 45.7 (video much sharper, no unsharp needed).
- **Final:** `ribbon_duduk_lilo_v3_upscale720.mp4` — 720x1280, 24fps, 10.0s, h264, 3.77 MB, video-only (audio stripped, ffprobe shows 1 video stream). Top cropped 58px (~5%) as drift guard, upscale lanczos crf 18. Final 3.5s sharpness 104.9 vs raw 145.6 (known upscale softening, accepted).
- **Honest defects:** (1) Button count 6 vs 7 prescribed (see above — within the ~6-7 range that passed v1; style is exactly right). (2) Thin gold chain from the base visible at the neck (no pendant; base artifact, same family as Krem/Beige/Hitam). (3) Chin/mouth peek at the top edge of the raw frames (tolerated); after the 58px top crop the final cuts at chin/nose, mouth no longer visible. (4) At 3.5s the raised hand briefly covers the right top bow and part of the placket (beat in progress; bow + buttons fully visible in the other frames). (5) Upscale softening at 3.5s (145.6 → 104.9, known and accepted).
- Media calls: 1 image + 1 video. No generator refusal, no retry.
