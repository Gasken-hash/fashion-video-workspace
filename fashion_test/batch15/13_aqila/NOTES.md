# Product 13_aqila — AQILA JAKET LUZY RENDA WANITA (Batch 15, batch 3)
- Product ID: 1737687385556682236
- Link: https://vt.tokopedia.com/t/ZS9fQi7S9yUzV-g8PpT/
- Reference: `tok_02.jpg` (800x800, from Jendral's Tokopedia link via curl-cffi)
- Base: `~/workspace/fashion_test/bases/base_pita_v3_tas.jpg` (Pita v3 frame-0, black bag prop, 1536x2752)
- Movement planned: Set B adapted (hair → trace closed zipper → touch navy pocket → stroke lace hem → lap → peace sign)

## Reference details (from tok_02.jpg)
Blue + white gingham check jacket, small white daisy flower embroidery scattered all over, NAVY pointed collar with white scalloped trim, TWO navy patch pockets on the chest with white scalloped trim, WHITE zipper down the center front (closed), WHITE lace ruffle hem, long PUFF sleeves with elastic gathered cuffs, cropped hip-length fit. Worn with a white skirt. NOTE: tok_00/tok_01 are text cards (DISCLAIMER WARNA / KETENTUAN KOMPLAIN), NOT product photos — never use them.

## Frame-0 v1
- File: `media-generation-frame0-aqila-v1-0-23de1dde-3422-4f12-89fb-c51b73f408ff.webp` (1168x2112, sharpness 327.8)
- One fresh LILO edit from the base, with BOTH zipper clauses (standard FULLY-CLOSED + stronger collar-meets) + framing clause.

## GATE 1 — FAILED (zipper open at the top). NO VIDEO generated.
Passed:
- Blue gingham check: colour + scale match
- White daisy embroidery: scattered white flowers with dark centres, match
- Navy collar with white scalloped trim: match
- 2 navy patch pockets with white scalloped trim: match
- White zipper, bottom closed: teeth joined down to the lace hem, no gap
- White lace ruffle hem: match
- Puff sleeves with elastic gathered cuffs: match, attached at shoulders
- White pleated mini skirt: match (replaces base white pants)
- Framing: mouth-cut, no eyes visible; chin/mouth peek at top (tolerated)
- Hair: loose high bun with face-framing strands
- Base kept: maroon wall, black bag on floor bottom right, hand on hip

FAILED — zipper top (evidence: `gate1_zipper_top.jpg`):
- The white zipper slider IS at the top just below the collar and the teeth are joined from the slider down — but the two navy collar flaps spread wide apart in a V, and a large triangle of bare neck/upper-chest skin + the gold necklace with flower pendant is fully visible between them.
- The collar flaps do NOT meet and touch at the center front; there IS a V-opening with a skin gap between the collar and the zipper.
- This is the same failure pattern as Zipper Leather Abu v1 / Beige v1 and Fuzzy v1. The stronger collar-meets clause did NOT hold this time (it did hold for Candy v2).
- Note: the reference itself wears the collar open in a V — but Jendral's hard zipper rule overrides the reference styling (open zipper/V-gap = suggestive = TikTok ban risk). A small natural neck opening (Krem/Candy v2 precedent) is tolerated; this wide V with full necklace visible is not.

Per the hard rule (open at top OR bottom = FAIL), no video was generated. Work stopped here per the task instruction.

## Prescription for a v2 fresh edit (NOT attempted — awaiting parent order)
Fresh LILO edit from the base with an even stronger zipper clause, e.g.:
"the white zipper is zipped ALL the way up so the navy collar stands closed around the neck, the two navy collar flaps MEET and OVERLAP slightly at the center front, the white zipper forms ONE continuous vertical line from the collar to the hem with NO break and NO V-gap, the neck and chest are completely covered by the navy collar and the gingham fabric, the gold necklace is NOT visible"
Plus the standard FULLY-CLOSED clause and the collar-meets clause. Never surgically fix this LILO frame-0.

## Frame-0 v2
- File: `media-generation-frame0-aqila-v2-0-b533d61a-1579-438f-a55c-3199bd3bbeb6.webp` (1168x2112, sharpness 284.3)
- One fresh LILO edit from the base, with ALL THREE zipper clauses (standard FULLY-CLOSED + collar-meets + strongest turtleneck/trim-one-line) + framing clause.

## GATE 1 — FAILED (zipper open at the top — collar V-gap remains). NO VIDEO generated.
Passed:
- Blue gingham check: colour + scale match
- White daisy embroidery: scattered white flowers with dark centres, match
- Navy collar with white scalloped trim: match
- 2 navy patch pockets with white scalloped trim: match
- White zipper, bottom closed: one continuous white line from collar to lace hem, teeth joined, no gap
- White lace ruffle hem: match
- Puff sleeves with elastic gathered cuffs: match, attached at shoulders
- White pleated mini skirt: match (replaces base white pants)
- Framing: mouth-cut, no eyes visible; chin/mouth peek at top (tolerated)
- Hair: loose high bun with face-framing strands
- Base kept: maroon wall, black bag on floor bottom right, hand on hip
- IMPROVEMENT over v1: the gold necklace is NOT visible in v2 (hidden by the closed zipper/collar area)

FAILED — zipper top (evidence: `gate1_v2_zipper_top.jpg`):
- The white zipper slider IS at the top just below the collar and the teeth are joined from the slider down — but the two navy collar flaps spread wide apart in a V, and a triangle of bare neck/upper-chest skin is visible between them down to the slider.
- The collar flaps do NOT meet and touch at the center front; there IS a V-opening with a skin gap between the collar and the zipper.
- This is the same failure pattern as v1 (minus the necklace) and as Zipper Leather Abu v1 / Beige v1 and Fuzzy v1. The three-clause prompt (including the strongest turtleneck clause) did NOT hold this time — it did hold for Fuzzy v2, whose collar is a soft stand-up collar; the AQILA pointed shirt collar keeps defaulting to the reference's own open-V styling.
- A small natural neck opening (Krem/Candy v2 precedent) is tolerated; this wide V with the upper chest exposed is not.

Per the hard rule (open at top OR bottom = FAIL), no video was generated. Work stopped here per the task instruction.

## Prescription for a v3 fresh edit (NOT attempted — awaiting parent order)
Fresh LILO edit from the base. The pointed shirt collar is the problem — it keeps splaying open in a V. Try describing the collar as a CLOSED stand-up/band collar instead of a pointed shirt collar, e.g.:
"the navy collar is a CLOSED stand-up collar that wraps snugly around the base of the neck like a band, the two collar ends MEET and OVERLAP at the center front so there is NO V-opening at all, only the neck column rises out of the collar, the white zipper runs in ONE continuous vertical line from the top of the closed collar to the lace hem with NO break, NO skin is visible anywhere on the chest, the gold necklace is NOT visible"
Plus the standard FULLY-CLOSED clause. Never surgically fix this LILO frame-0.

## Files in this folder
- `tok_00.jpg` … `tok_07.jpg` — Tokopedia gallery (8 images; tok_00/tok_01 are text cards)
- `media-generation-frame0-aqila-v1-0-23de1dde-3422-4f12-89fb-c51b73f408ff.webp` — frame-0 v1 (Gate 1 FAILED)
- `gate1_zipper_top.jpg` / `gate1_zipper_bottom.jpg` — v1 zipper evidence crops
- `ref_collar_zoom.jpg` — reference collar zoom (shows the reference also wears the collar open)
- `media-generation-frame0-aqila-v2-0-b533d61a-1579-438f-a55c-3199bd3bbeb6.webp` — frame-0 v2 (Gate 1 FAILED)
- `frame0_aqila_v2.jpg` — frame-0 v2 as JPG
- `gate1_v2_zipper_top.jpg` / `gate1_v2_zipper_bottom.jpg` — v2 zipper evidence crops
- `NOTES.md` — this file
