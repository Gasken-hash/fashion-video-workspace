# Fashion Video Fidelity

Build fashion try-on videos where the garment in the video is the
same garment as the seller's original photo. The rule that governs
this skill was set by Jendral 12 Nov 2026: generate the frame-0
image first, check it against the original seller photo, and only
generate the video once it matches.

## The locked standard

Follow these steps in order. A failed step stops the work; never
skip ahead to the video.

- **0. Product identity.** State the product back (name, price,
  canonical Shopee link `shopee.co.id/product/{shop_id}/{product_id}`)
  and use the original seller photo from that link. Without the
  original photo, there is no production.

- **1. One fixed base photo.** Use the same base model photo for
  every product. **FORMAT: HORIZONTAL 16:9 (1280x720) — Jendral's
  decision 12 Nov 2026, 22:38 WITA ("kita kembali kesana aja",
  widget choice "Priscila horizontal, model lama"), returning to the
  old recipe that earned "Oke sekarang bagus". The vertical era
  (18:46–22:38 WITA 12 Nov) is OVER; vertical videos already made
  stay as-is.** The production base photo is the Adelia LANDSCAPE
  no-bag base:
  `~/workspace/fashion_test/bedah_maroon_1111/media-generation-adelia-model-landscape-no-bag-0-a8511160-681b-4d4b-8960-388184ae1405.webp`
  (2096x1184, same model and pink bedroom, no bag, full body). The
  bag was removed on 12 Nov 2026 under Jendral's bag-physics rule,
  see "Known failure modes"). The character photo
  (`vertical_test_priscila/character_base.jpg`, Jendral's own
  character, 22:14 WITA) is PARKED — it was used for one vertical
  Priscila video only; it is NOT the production base. Swap ONLY the
  garment; background, pose, and skirt are never touched. There is no
  bag in the base photo anymore. Pass the seller's original photo as
  an image reference in every edit call. The generator must SEE the
  shape, not just read a description.

- **2. Generate the frame-0 image first.** Never the video. Write
  the shape in geometry words plus explicit prohibitions, for
  example "hem is a soft rounded U-curve, longer at the center,
  no sharp point, no diagonal overlap" and "sleeves attached at the
  shoulders, NOT off-shoulder, NOT detached". Vague words get filled
  in by the generator with its own fashion defaults.

- **3. Gate 1: check the frame-0 against the original.** Check
  detail by detail, not "looks similar": color, pattern, neckline
  shape, sleeves (attached or detached, length), bows and details
  (count, size, position), hem shape, fit (fitted or loose). One
  deviation means NOT PASSED and no video is made.

- **4. Surgical fix.** If Gate 1 fails, edit the already-good
  photo and change ONLY the wrong part, at most 2 attempts. Never
  regenerate from scratch; a full regeneration re-rolls every
  detail. Proven: sleeves fixed in one edit (v1 to v2), hem and
  neckline fixed in one edit (v2 to v3).

- **5. Fallback.** If 2 surgical fixes fail, crop the real seller
  photo faceless (the LILO method). The shape is 100% real because
  it IS the photo; the background becomes the seller's. Note: this
  fallback is weaker for HYLE, whose seller photo carries a large
  "HYLE" watermark across the torso.

- **6. Gate 2: generate the video.** Only when Gate 1 passes.
  Recipe (the old horizontal recipe, back in force 12 Nov 2026,
  22:38 WITA): LANDSCAPE 16:9 (1280x720), 10 seconds, framing exactly
  as the frame-0 (full body, chin to skirt/feet, the garment fills the
  frame), camera completely locked off (no pan, tilt, zoom, or shake),
  the model STAYS in place with no step forward; the HANDS do the
  storytelling: sides → chest/bow → shoulders → hem → side turn →
  hips → playful ending (optional), silent (music is added in
  editing). The vertical/medium-shot recipe (18:46–22:38 WITA 12 Nov)
  is retired. Finished landscape videos are left as-is, not remade;
  vertical videos already made stay as-is too.
- **Forward step (TESTED and WORKING, 12 Nov 2026, Priscila
  horizontal v2 + refined in v3):** start CLOSER than the full
  frame-0 (crop the frame-0 ~1.3x tighter, chin cut at the top, hem
  lace still visible). The model takes just ONE small step forward
  (1-2s), then leans her upper body slightly toward the camera
  (2-4s), tilting her chest forward with both hands spread over
  the bow and lace to present the garment in close-up; then she
  straightens and steps back to the exact starting distance
  (4-6s), hands on hips, side turn at the end. Camera stays locked
  off and the background stays frozen; the face must never enter
  frame even at the closest point or during the lean. Motion blur
  at 2-3.5s is expected (close-up of a solid-color garment reads
  softer) — the details must still be readable. Adoption as the
  default recipe awaits Jendral's verdict.
- **Sitting format (TESTED and WORKING, 13 Nov 2026, Priscila
  duduk v1):** the model sits on the edge of the bed for the WHOLE
  video — she never stands, walks, or steps anywhere. Only her
  hands and upper body move. VERTICAL 9:16, medium close-up
  (chin to knees), camera locked off, background frozen, faceless.
  Hands: hip/hair → neckline → chest (spread, presenting the top)
  → hem → lap → slight torso turn → peace sign. The sitting base
  is a separate base photo (`priscila_duduk/`); the standing base
  stays the production base for standing videos.
- **Sitting LILO format (APPROVED by Jendral 13 Nov 2026,
  "Udah pas dan perfect"):** use the real first frame of a sitting
  reference video as the base, swap ONLY the garment to the
  product + tie the hair in a bun (one fresh edit with all changes
  at once; never surgical-fix a LILO frame — it reverts). Framing:
  mouth-cut, ONLY the eyes are cut off (Jendral's preferred
  framing). Motion: calm, slow, composed — torso/shoulders/chest
  completely still, no bouncing/shaking/giggling, only the hands
  move gently. SAFETY: after the video is generated, crop the top
  ~5% of the finished video (ffmpeg) as drift insurance, so the
  eyes can never enter at the end (the generator drifts up at the
  peace sign even with a still head). QC Gate 3 must check the
  enlarged top edge of the 9.5s frame for eyes. Approved video:
  `priscila_duduk_lilo_v2_mc_calm_crop_silent.mp4` (668x1188,
  10.0s, silent), uploaded to Cloudinary + logged in the sheet
  tab "Video Fashion" (row 5, "Siap tayang").
  LESSON (Mutiara, 13 Nov 2026): a LILO edit can reframe to show
  the full face (Mutiara v1 failed Gate 1 on the face while the
  garment was perfect). ALWAYS include an explicit framing clause
  in the LILO edit prompt ("the top of the frame cuts at her mouth
  and chin, so her eyes are NOT visible — do NOT show her full
  face, do NOT zoom out, do NOT reframe to include her eyes");
  never rely on the generator keeping the framing. A fresh edit
  with the clause (Mutiara v2) passed Gate 1 first try.
- **Rotasi rok (Jendral, 13 Nov 2026, 09:47 WITA): "udah bagus
  tapi roknya itu itu aja njir kek gk pernah dicuci kwkw"** — the
  same white ruffle mini skirt was used in 5 videos (Katie,
  Mutiara, Inara, Ruffle, Ribbon). NEW RULE: the skirt must NOT
  stay the same across videos — vary it per video, matched to the
  top when it fits. Rotation: ruffle putih (used 5x) → plisket
  putih (Pita Timbul, baris 8) → A-line putih polos → denim →
  midi krem, and so on. Write the skirt EXPLICITLY in every LILO
  edit prompt (e.g. "a plain white PLEATED mini skirt: neat
  vertical pleats, a smooth waistband, a simple A-line pleated
  shape, solid white with NO ruffles and NO frills"), never just
  "a white skirt". Old videos are NOT remade.
- **Bottom follows the reference photo (Jendral, 13 Nov 2026,
  09:59 WITA): "kalau gambar referensinya ada celana gini bisa
  gk kamu pakai juga celananya biar maching sama bajunya tapi
  kalau gk ada pakai yang ada aja"** — NEW RULE: the bottom in
  the video MUST follow the seller's original photo. If the photo
  shows pants → use those pants (Pita Timbul: loose white
  straight-leg pants with a drawstring waist). If it shows a
  skirt → use that skirt. If it shows only the top (no bottom) →
  only then use the skirt rotation above. Other styling in the
  photo (hat/beret, crossbody bag) is NOT used — only the bottom
  follows the reference. The Pita Timbul v1 (pleated skirt) was
  replaced by v3 (white pants) under this rule.
- **Rotasi gerakan duduk (Jendral, 13 Nov 2026, 08:46 WITA):
  "gerakannya diubah bisa gk, biar gk identik gitu gitu semua"** —
  sitting videos must NOT all use the same hand choreography.
  The sets below are TEMPLATES, not a fixed order: for each
  product, CHOOSE/ADAPT the beats to showcase THAT product's
  distinctive features (Jendral, 08:53 WITA: "bisa di sesuaikan
  sama produknya gk ini gaya?"). Feature → beat mapping:
  bow/buttons down the front → hands touch the bow/buttons;
  flare/wide cuff → lift one cuff to show the sleeve; scalloped
  or lace hem → pinch/trace the hem; V-neck or lace neckline →
  hands touch the neckline; thick/visible knit texture → hands
  stroke the chest/sleeve; fitted waist → hands on the waist;
  ribbon tie → hands touch the tie. The rotation A → B → C → D
  → E → A is only the FALLBACK when a product has no
  distinctive feature to showcase. Every set keeps the locked
  rules (sitting the whole time, calm, torso/shoulders/chest
  still, only the hands move, mouth-cut framing, background
  frozen, product identical).
  - Set A (baseline, APPROVED): hip/hair → neckline → chest
    (spread) → hem/skirt → lap → slight torso turn → peace sign.
  - Set B (detail showcase): hair → lift one cuff to show the
    sleeve → touch the top bow/button → pinch the hem → skirt →
    lap → peace sign.
  - Set C (fit/waist): shoulders → chest → waist/hem (hands on
    the waist) → skirt → slow side turn → peace sign + small wave.
  - Set D (one-hand anchor): one hand stays on the hip the whole
    time; the other hand: neckline → bow → hem → cuff → lap →
    peace sign.
  - Set E (slow reveal): hands start crossed on the lap → rise to
    the neckline → spread over the chest → one hand traces the hem
    → both hands on the skirt → slow side turn → peace sign.
  Used so far: A = Priscila LILO v2 + Katie LILO v1 (Katie's
  features — 5 black bows, flare cuffs, scalloped hem — would
  have fit Set B best; noted, not remade).

- **Face rule (Jendral, 12 Nov 2026, 19:14 WITA):** PRIORITY is
  faceless (face cropped out of frame) — BUT a slight chin/mouth peek
  at the top edge is TOLERATED (just report it). NOT allowed: eyes or
  a full face clearly visible. The chin peek that used to be logged as
  a framing defect is now within tolerance, not a failure.

- **Background freeze (Jendral, 12 Nov 2026, 20:35 WITA):** the
  generator re-settles the scene in the first ~0.5 seconds — the
  background jumps (window and curtains move) and then stays stable.
  The video prompt must carry an explicit freeze clause ("the
  background is completely frozen and identical to the photo in every
  single frame ... nothing moves, shifts, or changes, especially in
  the first second"). Gate 3 must compare frame 0 against frame 0.6s:
  any background jump there is a FAIL.

- **Sharpness (Jendral, 12 Nov 2026, 21:32 WITA):** video generation
  can soften a sharp frame-0 (measured: frame-0 Laplacian 691, video
  frame 384, ~45% loss). The format is not the cause — a vertical
  Adelia v1 video measured 812, as sharp as the horizontal ones. Gate 3
  must compare the video frame at 2s against the frame-0 for sharpness.
  Regenerating does not reliably fix softness (a regen measured 348).
  The reliable fix is an unsharp pass in editing (ffmpeg
  `unsharp=5:5:0.8:5:5:0.4`, crf 18), which measured 597 — use it as a
  finishing step when the video comes out soft.

- **Bed composition (Jendral, 12 Nov 2026, from his corrections):**
  the bed must sit right at the model's feet (not set back behind her
  with a strip of floor between — that looks wrong), AND the bed's long
  side must be visible (bed on the model's left, mattress side, bedding
  and pillows at the far left end visible, model standing on the floor
  at the bed's side edge). Never put the model standing ON the bed.

- **Lighting (Jendral, 12 Nov 2026, 20:06 WITA):** light must be
  directional warm window light, from the left: the model's body casts
  a soft shadow on the bed and floor to the opposite side, with a soft
  contact shadow under her feet, gentle shading on the side of her body
  away from the window, and shadows in the fabric folds. A picture with
  no cast shadow (character not grounded, even light everywhere) does
  NOT pass.

- **7. Gate 3: QC the video frames against the original.** Read
  frames at 0, 2, 3.5, 6.5, and 9.5 seconds. The product details
  must stay the same through the whole video. A video that invents
  details is a FAILED video and is not delivered as final. Proven:
  HYLE's video added bows on both wrists that were in neither the
  frame-0 nor the original.

- **8. Delivery.** Per product: the original seller photo, the
  frame-0, the video, the frame at 2 seconds, and an honest list of
  defects. Report framing defects (for example a chin peek) as they
  are; never hide them.

## Aturan 13 Nov 2026 — produksi duduk LILO (berlaku sekarang)

Added 13 Nov 2026, 14:45 WITA, because the working docs did not
yet record these locked rules. Everything here is a rule Jendral
already approved, except the bottom-colour mapping, which is
marked PROPOSED, not locked.

- **Current production format: sitting LILO, vertical 9:16.**
  All work since 13 Nov 2026, 00:44 WITA (Katie onward — 7 Korean
  Style videos + Zipper Leather) uses the sitting LILO recipe:
  base = base duduk cahaya (`base_pita_v3_*_cahaya.jpg`, 1168x2112),
  warm CREAM wall + golden afternoon sunlight from the left window,
  model sitting, mouth-cut framing, calm hands-only motion, top crop
  ~60px as drift guard. The horizontal 16:9 sections in steps 1
  and 6 above are history (Jendral's 12 Nov 22:38 decision); do
  NOT switch back to horizontal without Jendral ordering it.
  Wall stays warm CREAM as in the cahaya bases (Jendral, 17 Nov
  2026: all base walls unified to the horizontal base's warm cream)
  — Jendral cancelled the pale-pink wall change 13 Nov 11:03 WITA
  ("stop jelek kamu aneh bikinnya, stop ya").
  **MODE DUDUK DI-PAUSE SEMENTARA (Jendral, 17 Nov 2026)** sampai
  Jendral bilang lanjut. **ROTASI MODE GLOBAL (Jendral, 20 Nov
  2026):** produksi memilih produk dari sheet mengikuti giliran
  mode — siklus Berdiri Vertikal → Horizontal → Mirror (counter
  `rotasi_global.txt`); giliran Berdiri/Horizontal = atasan
  berikutnya, giliran Mirror = setelan/dress berikutnya; full-body
  tetap mirror saja.
- **Photo source — HARD RULE (Jendral, 13 Nov 2026, 13:03 WITA):**
  product photos MUST come from the exact link Jendral sent.
  NEVER substitute a photo from another marketplace, even for
  the "same" product — a wrong photo can get his TikTok account
  banned. Non-browser first: curl/og_info for Tokopedia,
  image-search with susercontent/cf.shopee filter for Shopee;
  browser only if non-browser fails. The earlier Shopee-sourced
  Zipper Leather set is quarantined at
  `~/workspace/fashion_test/korean_style/zipper_leather/QUARANTINE-bahaya-jangan-pakai`
  — never use it for TikTok.
- **Zipper FULLY CLOSED — HARD RULE (Jendral, 13 Nov 2026,
  13:19 WITA):** for zip products, the zipper is FULLY CLOSED
  from collar to hem in EVERY frame-0 and video frame — slider
  at the very top just below the collar, both front panels meet
  completely, NO bare skin visible, NO cleavage. Open zipper =
  suggestive content = TikTok ban risk. Prompt clause: "the
  silver zipper is FULLY CLOSED and zipped all the way up to the
  collar, the slider sits at the very top just below the collar,
  both front panels meet completely, NO bare skin is visible, NO
  cleavage". Gate 1 AND Gate 3 must check the zipper. Status
  13 Nov: Krem safe; Beige v2 + Hitam v1 passed; Abu v2 failed
  again (V-gap above slider, skin visible); Coklat failed Gate 1
  (open at the bottom); Merah system-rejected with no video —
  never retry a generator refusal.
- **Floor prop rotation (Jendral, 13 Nov 2026, 13:34 WITA):**
  the sitting base rotates its floor prop so videos do not all
  look identical: tas hitam → kacamata → tumbler hitam → tas...
  Three bases, all 1536x2752, in `~/workspace/fashion_test/bases/`:
  `base_pita_v3_tas.jpg`, `base_pita_v3_kacamata.jpg`,
  `base_pita_v3_tumbler.jpg`. Planned: Coklat on the glasses base,
  Abu v3 on the tumbler base. Props are STATIC floor props, never
  worn or carried — the bag-physics rule still applies.
- **Upscale 720p (Jendral, 13 Nov 2026, 13:59 WITA, "begini jadi
  bagus"):** every final video is upscaled to 720x1280 with
  ffmpeg lanczos, crf 18. The generator outputs ~640x1110; the
  upscale adds no real detail (measured sharpness at 3.5s on
  Krem fell 210 → 138 — interpolation only) but looks better to
  the eye. Verified 720x1280, 10.0s files:
  `korean_style/zipper_leather/krem/krem_duduk_lilo_v1_upscale720.mp4`,
  `.../beige/beige_duduk_lilo_v2_upscale720.mp4`,
  `.../hitam/hitam_duduk_lilo_v1_upscale720.mp4`. Applies to all
  future videos; Coklat + Abu v3 go straight to 720p.
- **Bottom matched to the top colour — PROPOSED, NOT LOCKED
  (13 Nov 2026, 13:38 WITA):** Jendral asked "yang masih kurang
  itu untuk bawahannya aja sih, kebanyakan rok yang itu itu aja,
  gk bisa di sesuaikan dengan atasan nya gk". Proposed mapping,
  only for products whose seller photo shows the top alone (if
  the photo shows a bottom, follow the photo): Coklat → celana
  krem/beige atau denim gelap; Abu → celana hitam; Hitam →
  celana hitam atau denim; Krem/Beige → tetap celana putih/krem.
  Do NOT apply until Jendral says yes — it was offered for
  Coklat + Abu v3 and he has not answered yet.
- **Full workflow, as given to Jendral 13 Nov 2026, 14:16 WITA:**
  0. Product + original seller photo from his exact link.
  1. Base (Pita v3, prop rotated; bottom follows the reference
  photo, or the skirt rotation when the photo shows top only).
  2. Frame-0 (LILO edit: garment only + bun; geometry words +
  explicit bans; zipper clause for zip products).
  3. Gate 1 vs the original, detail by detail (zipper closed top
  + bottom for zip products). Max 2 fixes; LILO frames are
  re-edited fresh, never surgically fixed.
  4. Video only if Gate 1 passes; movement adapted to the
  product's features, sets A–E only as fallback; calm, torso
  still, hands only; background frozen.
  5. Gate 3 at 0 / 2 / 3.5 / 6.5 / 9.5s; background 0 vs 0.6s
  identical; no eyes/full face in any frame; zipper closed in
  every frame; top crop ~60px.
  6. Upscale 720p (see above).
  7. Handover: original photo + frame-0 + 720p video + 3.5s frame
  + honest defect list. **Upload + catat OTOMATIS (Jendral, 15 Nov
  2026 03:56 WITA): setelah video selesai generate dan Gate 3
  lolos, LANGSUNG upload ke Cloudinary + LANGSUNG catat ke sheet
  tab "Video Fashion" sebagai "Siap tayang" — TANPA tanya
  persetujuan dulu. Berlaku untuk semua video ke depan. (Aturan
  lama "ONLY after his approval" DICABUT.) Pengecualian: video
  yang Jendral sendiri tandai cacat (mis. Set F v3, dada turun)
  TIDAK dicatat "Siap tayang" sampai ada versi perbaikannya.**
- **Per-colour rule:** 1 video per colour, different movement
  per colour. Max 4 image calls + 6 video generations per
  message. A generator refusal is never retried.

## Preserving details

- Change as little as possible in each edit. The more that is
  redrawn, the more that can drift.
- Describe shapes with geometry and name what is forbidden. "Pointed
  hem" alone produced a sharp V; "soft rounded U-curve" produced the
  original's hem.
- Fix one defect per edit. Each surgical fix so far has landed on
  the first try.
- Generating a fresh model photo from a description drifts details
  (HYLE gained wrist bows that do not exist). Editing from the real
  photo does not.
- NEVER pass a reference image whose garment differs from the target
  garment when the garment must be preserved: the generator copies the
  reference's garment into the result no matter how explicitly the
  prompt forbids it (proven 12 Nov 2026: every edit that included the
  room-v4 base as a reference produced its polka-dot top). For
  background-only or lighting-only edits, use text only, no reference
  image — that is how the side-bed and shadow fixes landed.
- **LILO edit rule (proven 13 Nov 2026):** a surgical fix on a
  real-photo LILO frame-0 does NOT work — the generator re-derives
  from the original frame and applies only the latest instruction,
  reverting the earlier changes (proven twice: both skirt fixes
  returned the gray top + hair down). So get ALL changes right in
  ONE fresh edit from the original frame (top + white skirt + bun),
  with the white skirt spelled out explicitly ("SOLID WHITE, not
  maroon, not part of a matching set") — that is how LILO v2 landed
  all three. Never attempt a surgical fix on a LILO frame-0; if a
  fresh edit fails, re-do the fresh edit.

## Known failure modes

- Off-shoulder or detached sleeves when the original has attached
  sleeves (swap-test v1). Fix with an explicit attachment clause.
- Sharp V hem where the original has a soft U dip (swap-test v2).
- Waist bow invented in the frame-0 (batch HYLE).
- Bows growing larger during the video (LILO from 3.5s, swap v3).
- Ruffle or frill invented at the waist seam during the video (Luluna v1):
  the gathered peplum seam became a protruding wavy ruffle at 6.5s and
  9.5s, absent from both the original and the frame-0. Gate 3 caught it;
  v1 was discarded, not delivered. Fixed in v2 by adding "waist seam is
  flat and smooth against the body, no ruffle trim, no frill" to the
  video prompt.
- Wrist bows invented during the video (batch HYLE).
- Chin or mouth peeking at the top edge, most often in the last
  second (Adelia v1 and v3, batch Lunelly, LILO, swap v1, v2, v3).
  TOLERATED since 12 Nov 2026, 19:14 WITA (Jendral: slight peek is
  fine, priority stays faceless) — report it, do not fail the video
  for it. Only eyes or a full face clearly visible fails Gate 3.
- The model steps back to medium distance around 6.5 seconds
  without being asked, so the close-up lasts only the first half.
  Beats run faster than the prompted timestamps.
- The bag: Jendral's physics rule (12 Nov 2026, 12:00 WITA) — a bag
  must obey physics: it hangs from one shoulder by its strap under
  gravity for the whole video, never appears out of nowhere,
  disappears, floats, or switches shoulders. Proven failures: bag
  flipped to the other shoulder (Adelia v2), bag hidden during the
  turn (HYLE 6.5s), strap dangling with no bag (Luluna v2 6.5s), bag
  suddenly appearing (MH). Default decision: NO BAG AT ALL — the
  base photo is now the bag-less variant (see step 1). If a bag is
  ever used again, Gate 1 and Gate 3 must check it in every frame:
  same shoulder, strap attached, hanging down, never floating.

## Caps and tools

- At most 4 image calls and 6 successful video generations per user
  message, subagents included. Plan batches within those caps.
- Image-to-video output follows the input image's aspect ratio, so
  a vertical video needs a vertical frame-0 (and a vertical base
  photo — see step 1).
- All videos are silent; verify with volumedetect and report the
  measured level.
- Always report duration and specs measured from the final file,
  never from the prompt.

## Reference files

- The full standard: `~/workspace/fashion_test/STANDAR_VIDEO_FASHION.md`
- Audit of 11 videos against the standard (9 passed, 2 failed):
  `~/workspace/fashion_test/audit_aturan_baru_12nov.md`
- Base photo (Adelia landscape, pink bedroom, NO BAG — bag removed
  12 Nov 2026 under the bag-physics rule):
  `~/workspace/fashion_test/bedah_maroon_1111/media-generation-adelia-model-landscape-no-bag-0-a8511160-681b-4d4b-8960-388184ae1405.webp`
  (original with-bag version kept at
  `~/workspace/fashion_test/bedah_maroon_1111/media-generation-adelia-model-landscape-0-1936c196-9190-4231-bac5-f08611c4c057.webp`)
- VERTICAL base photo (current, for all videos since 12 Nov 2026, 18:46 WITA):
  `~/workspace/fashion_test/vertical_test_priscila/media-generation-base-vertical-no-bag-0-b5a9403c-a835-4074-a827-40d4753fd196.webp`
  (1152x2048, same model/room, no bag; full-body including feet and white flats).
  First vertical video with it: Priscila maroon test, Gates 1+3 passed first try —
  notes at `~/workspace/fashion_test/vertical_test_priscila/NOTES.md`.
- Worked fix spec (HYLE): `~/workspace/fashion_test/batch5/hyle_fix_spec.md`
- Swap-test log (v1, v2, v3): `~/workspace/fashion_test/batch5/swap-test/NOTES.md`

## Alternatives for better results

- If the base-photo swap keeps failing after 2 surgical fixes,
  use the cropped real seller photo (LILO method). Exact shape,
  seller's background.
- Compositing (cutting the real garment out and pasting it onto
  the base photo) is the last resort. Pose and lighting differ
  between the two photos, so it risks looking pasted on.

## Aturan 14 Nov 2026 — identitas produk ≥95% (Jendral, 23:43 WITA) — FOKUS UTAMA
- Produk di frame-0 dan di semua frame video HARUS IDENTIK minimal 95% dengan foto asli seller. Ini fokus utama supaya tidak kena pelanggaran TikTok (pelajaran dari pelanggaran Fuzzy 14 Nov).
- Yang dinilai: produknya (baju) — warna, motif (jumlah/posisi), kerah, lengan, kancing (jumlah/ukuran/posisi), resleting, hem, fit. Detail kecil yang menyimpang dari foto asli = pengurang persen; kalau ragu apakah sudah 95%, video TIDAK dibuat/di-upload.
- Artefak base (kalung emas, mulut/dagu ngintip) bukan produk — tidak dihitung ke persen produk, tapi tetap dicatat sebagai cacat.
- Berlaku di Gate 1 (frame-0 vs foto asli) DAN Gate 3 (frame video vs foto asli). Video yang mengubah detail produk di tengah jalan = GAGAL walau frame-0 lolos.

## Aturan 14 Nov 2026 — aksesoris untuk lengan pendek (Jendral, 23:49 WITA)
- Produk LENGAN PENDEK boleh ditambah AKSESORIS (gelang, jam tangan wanita, atau yang lain) di frame-0 — supaya tangan tidak kelihatan sepi/kosong.
- Syarat: aksesoris TIPIS/halus, tidak mengubah produk (garmen tetap ≥95% identik), tidak menutupi detail produk (kancing/pita/motif), dan Gate 3 wajib cek aksesorisnya tetap menempel/konsisten di semua frame (kalau melayang/hilang = gagal, sama seperti aturan fisika tas).
- Catatan: ini pertama kali diusulkan 13 Nov 12:11 ("coba pakai tangan pendek dulu") tapi belum pernah dites karena tidak ada foto produk lengan pendek yang bisa diambil. Kandidat pertama kalau nanti disetujui: YOLA (lengan pendek, tapi masih di-hold karena off-shoulder).

## Gaya gerak berdiri Flow Gingham — Set Berdiri F (Jendral, 15 Nov 2026 02:05 WITA)
- Sumber: video referensi Flow gingham (576x1024, 10s, model berdiri, medium shot mulut ke paha tengah, kamar pink). Detail beat ada di `~/workspace/fashion_test/gerak_flow_gingham.md`.
- Urutan: tangan kanan di pinggang → kedua tangan ke kerah/pita → tangan terbuka lebar di dada atas → kedua tangan ke hem peplum (cubit/usap) → usap sisi rok → putar badan pelan ~30-45 derajat (kepala TETAP menghadap kamera) → balik depan, kedua tangan di pinggang → tangan santai di sisi → ending peace sign ✌️ di level dada.
- Yang TIDAK ikut dari referensi: wajah penuh + senyum + julur lidah di ending — Lala tetap faceless, peace sign di dada, tidak dekat wajah, kepala tidak nunduk/miring jauh. Tidak ada langkah maju/mundur, tidak ada bungkuk — pemicu wajah masuk frame di Katie berdiri v3-v8.
- Kamera locked-off total, background beku. Gate 3 cek khusus: putaran 5s kepala tidak ikut mutar (profil = gagal); peace sign 9.5s di dada, bukan di pipi.
- **Rotasi 2 mode peace sign (Jendral, 15 Nov 2026 02:33 WITA, diklarifikasi 02:37 WITA): ending Set F dirotasi pipi ↔ dada — 1 video = SATU peace sign saja, pilih pipi ATAU dada, rotasi antar video, BUKAN dua peace dalam satu video.** Mode pipi = v1 (tangan kanan di pipi, wajah tetap aman — mulut saja, tanpa mata). Mode dada = v3 (tangan kiri di tengah dada, jari sampai tulang selangka, jauh di bawah dagu; klausul yang jalan: "forearm bent across her waist, hand staying below her collarbone with fingertips far below her chin" + Negative "never rises above the chest, never goes near cheek/chin/mouth/ear, no hand near her head"). v2 DIBUANG (peace di bahu + beat putar hilang — bukan mode). Syarat kedua mode: faceless tetap (tanpa mata/full face).
- **Bentuk dada — ATURAN BARU (Jendral, 15 Nov 2026 03:48 WITA):** di v3 frame 3.5s payudara kelihatan TURUN. Penyebab: beat "tangan terbuka lebar di dada" — telapak menekan rata dada bawah, generator me-render bentuk dada melorot. Tangan TIDAK BOLEH menekan rata di dada: sentuh dada hanya dengan UJUNG JARI (pita/kancing), lalu langsung ke hem. Prompt video wajib bawa: "bust stays naturally high and lifted, no sagging, no drooping, no flattening" + Negative "hands never press flat against her bust, never spread their palms over her chest". Gate 3 wajib cek bentuk dada di semua frame lawan frame-0. Perbaikan terbukti 2x (v4 + v5 bentuk dada bersih). Catatan: tinggi peace sign itu lotre — cuma v3 dari 4 percobaan yang mendarat di dada; v2/v4/v5 semua di bahu.
- Berlaku sebagai Set Berdiri F, pendamping koreografi review berdiri v9.

## Aturan 14 Nov 2026 — aksesoris BEBAS DIPADUKAN (Jendral, 23:57 WITA)
- Kalung BOLEH diganti model lain (tidak terkunci ke kalung emas tipis base).
- Gelang + jam tangan BOLEH digabung kanan-kiri beda (mis. gelang kanan + jam kiri, atau sebaliknya) supaya visual makin kaya.
- Syarat tetap: tidak mengubah produk (garmen ≥95% identik), tidak menutupi detail produk, Gate 3 wajib cek semua aksesoris tetap menempel di semua frame.

## Mode ke-4: Berdiri Full Body Vertikal (15 Nov 2026, tes FLORA lolos)
- REVISI BASE Jendral 16 Nov 2026 01:54 WITA: base setelan sekarang MIRROR SELFIE — ~/workspace/fashion_test/bases/lala_berdiri_fullbody_mirror_base_cahaya.jpg (1168x2112, vertikal): model full-body DI DALAM cermin tinggi (arched mirror), pegang HP menutupi wajah (faceless built-in), rambut cepol messy, kamar yang sama (kasur gingham + plush + poster pink). Base lama (lala_berdiri_vertikal_fullbody_base.webp, FLORA) DIGANTI untuk setelan ke depan — video FLORA yang sudah dicatat tetap sah.
- TES MIRROR 16 Nov ~02:00 WITA (Jendral: "gerakan sederhana aja") — FLORA, LOLOS Gate 1+3 ~97%: HP tetap diangkat menutupi wajah sepanjang video → tangan kanan keluar saku, sentuh kancing (ujung jari) → usap turun ke hem → putar badan ~30° ke samping (HP/kepala tetap menghadap cermin) → kembali depan. TANPA peace, TANPA maju-mundur. Putar 30° JALAN, framing stabil, background beku, tanpa wajah di semua frame (HP selalu menutupi wajah — faceless paling aman dari semua mode). Frame-0: v1/v2/v3 GAGAL Gate 1 (semuanya 4 kancing tengah, harus 5) — v4 LOLOS pakai frame-0 FLORA LAMA v2 (yang sudah benar 7 kancing) sebagai referensi baju, bukan flat-lay tok_00. PELAJARAN: kalau flat-lay terus kehilangan detail hitungan, pakai frame-0 lama yang sudah benar sebagai referensi. Post-process: crop atas ~60px, upscale lanczos 720x1280, crf 18, buang audio. Final: flora_mirror_v1_upscale720.mp4. (Tes saja, belum di-upload/dicatat.)
- PROMPT JENDRAL (16 Nov ~02:07 WITA, verbatim Inggris, dipakai apa adanya) — FLORA, LOLOS Gate 3 ~96%: mirror selfie realistis — berdiri natural HP menutupi wajah → SATU langkah kecil maju ke cermin → putar badan atas sedikit ke KIRI → putar sedikit ke KANAN → kembali depan, tahan pose. Tangan satunya tetap di saku. Semua beat mendarat (langkah maju, putar kiri jadi side profile penuh di 5s, kembali depan, tahan pose). HP selalu menutupi wajah; produk ~96-97%. CATATAN: (1) Framing BERUBAH — mengencang setelah langkah maju (2-6.5s, kaki sedikit kepotong), lalu melebar lagi (8-9.5s). Bawaan beat "langkah maju" (pelajaran horizontal v1: langkah maju = framing gerak). (2) Putar kiri+kanan runtuh jadi SATU sisi (sisi kiri jelas, sisi kanan tidak ada) — pelajaran mode-4 lama. Final: flora_mirror_jendral_prompt_v1_upscale720.mp4. (Tes saja, belum di-upload/dicatat.) Jendral 16 Nov 02:18 WITA: "bagus kok ini lumayan natural juga sesuai keinginan aku" — DISETUJUI, framing yang berubah DITERIMA sebagai natural. **Prompt Jendral ini sekarang RESEP BAKU mode mirror untuk setelan (ganti resep maju-mundur/peace mode-4 lama). Cron produksi set (antrean No 93+) harus di-update ke resep ini sebelum jalan.** **REVISI (Jendral, 16 Nov 2026 ~14:25 WITA): video mirror WAJIB diakhiri peace sign 1x — setelah kembali depan, tangan bebas (bukan tangan HP) angkat peace di level dada, jauh di bawah dagu, jauh dari HP/wajah, tahan sampai video habis; HP TETAP menutupi wajah. Kalau setelan pakai rok/celana tanpa saku, tangan lain rileks di sisi badan — JANGAN pakai kalimat saku (aturan saku Jendral 17 Nov 2026: kalimat saku HANYA kalau foto seller jelas ada saku; tangan "masuk saku" tanpa saku bisa dirender menempel ke pinggul-paha = sugestif, bahaya buat TikTok; kalau tidak ada saku ganti jadi "Her other hand rests relaxed at her side, never pressed against her hip or thigh."). AKAR MASALAH: foto jangkar mirror lama tangannya masuk saku jeans — jadi ada DUA base mirror: lala_berdiri_fullbody_mirror_base_cahaya.jpg (tangan di saku, untuk setelan ADA saku) dan lala_berdiri_fullbody_mirror_base_tangan_santai_cahaya.jpg (tangan rileks di sisi, untuk setelan TANPA saku; Cloudinary: https://res.cloudinary.com/dpllb7idh/image/upload/v1794890106/lala_berdiri_fullbody_mirror_base_tangan_santai_cahaya.jpg). Pilih base SESUAI foto seller sebelum generate frame-0. Terbukti di OneSet3in1-Mirror-V2 (b18_10, No 106), Gate 3 ~96%.** **ROTASI SETELAN (Jendral, 16 Nov 2026 ~15:41 WITA, "yap bener"): setelan JUGA dirotasi — variasinya di dalam mode mirror: arah putar (kiri/kanan, satu sisi per video), tangan bebas (di saku / rileks di sisi badan / sentuh kancing-hem), posisi peace (dada/pipi, dirotasi). Jangan dua setelan berurutan pakai variasi yang sama persis.** **DRESS = MIRROR juga (Jendral, 16 Nov 2026 ~15:46 WITA): dress full-length kayak setelan, butuh full-body biar kelihatan utuh dari atas sampai bawah — kalau pakai mode atasan (medium shot), roknya kepotong. Jadi dress masuk MIRROR SELFIE, ikut rotasi variasi mirror.**
- Pakai khusus SETELAN (atasan + bawahan panjang: celana panjang / rok panjang). Set rok pendek tetap bisa mode medium shot biasa. **TAS (ATURAN BARU Jendral, 16 Nov 2026 ~21:30 WITA, menggantikan larangan tas styling 15 Nov): kalau di foto referensi seller ADA TAS, PAKAI tas yang sesuai dengan fotonya (tas yang sama, bahu yang sama, gaya yang sama) — berlaku umum untuk semua mode (atasan + setelan), bukan cuma tas yang bagian dari produk.** Syarat: tas HARUS lolos Gate 1 + Gate 3 (fisika tas penuh: bahu yang sama dengan talinya, kena gravitasi, tidak hilang/terbang/pindah bahu, tidak melayang); kalau tas tidak bisa dirender bersih, fallback TANPA tas — jangan dipaksa. Yang TERBUKTI: tas bahu (shoulder bag, contoh GLADIA rantai, Gate 1 ~97% + Gate 3 ~96% lolos 16 Nov 21:06 WITA, file GladiaSet-Mirror-Bag-V1, sheet No 128; tas sempat ketutup badan ~1 dtk pas putaran maksimal lalu balik di bahu yang sama = oklusi, diterima). Tas jinjing (tote dipegang tangan) BELUM teruji — jangan dicoba dulu. Mode DUDUK paling rawan buat tas — cek Gate ekstra ketat di sana.
- Base: ~/workspace/fashion_test/bases/lala_berdiri_vertikal_fullbody_base.webp (1184x2096) — base berdiri vertikal Flow di-extend ke bawah. Framing MULUT SAMPAI KAKI (potong di mulut, mata tidak kelihatan, wajah tetap aman), kaki telanjang di lantai kayu.
- Gerakan WAJIB (Jendral, 15 Nov 2026; resep baku dari video referensi maroon, file ref_maju_maroon.mp4 di folder FLORA): MAJU-MUNDUR — tangan di pinggang → MAJU ke arah kamera sambil tangan naik ke dada, jari tersebar ringan di kancing/kain buat nunjukin baju (TANPA tekan, dada tidak boleh melorot) → tangan usap turun ke hem → MUNDUR ke posisi awal, tangan di pinggang → peace sign. Larangan "tidak boleh maju/mundur" (mode berdiri biasa) TIDAK berlaku di sini. Putar badan OPSIONAL, bukan inti gerakan ini.
- PUTAR KIRI+KANAN (Jendral, 15 Nov 2026, "perlihatkan juga baju bagian kanan dan kirinya"): generator HANYA BISA satu putaran ke satu sisi per video — v5, v6, v7 (dua putaran / sapuan) gagal semua. Solusi yang JALAN: SATU SISI PER VIDEO — v5 = sisi kiri (No 46, bersih), v8 = sisi kanan (No 47, dipotong 7 detik). TAPI arah putar kiri/kanan di prompt TIDAK deterministik: v8 dapat kanan, v9/v10 (prompt sama) malah kiri lagi — generator milih sisi sendiri. Kalau butuh sisi tertentu, generate lalu CEK arahnya di frame 5s, jangan andalkan kata "kiri/kanan" di prompt. Ending peace pipi itu lotre wajah (v6 + v8 gagal wajah penuh di 8-9.5s; v4/v5/v9/v10 bersih) — kalau ending gagal, POTONG video sebelum peace (v8 dipotong di 7.0 detik, ending tangan di pinggang tetap bersih).
- KEPALA (pelajaran v3): kepala TETAP TEGAK, dagu sedikit terangkat, TIDAK BOLEH nunduk — v3 gagal karena "chin tilting slightly down" narik mata masuk frame (5-7s wajah penuh). Di video referensi, wajah tidak pernah kelihatan karena kepala tetap tegak dan framing potong di dagu.
- PEACE (Jendral, 15 Nov 2026 ~14:59 WITA): 1x SAJA per video, DI SAMPING PIPI saja — rotasi pipi ↔ dada DIBATALKAN di mode ini. 2x peace = aneh = GAGAL. Prompt video WAJIB bawa larangan: peace hanya sekali, hanya di akhir, hanya di samping pipi; sebelum ending, jari TIDAK BOLEH membentuk V. FLORA v2 jadi contoh gagal: peace di ~7s (dada) + peace di ~9.5s (pipi).
- Gate 3 mode full-body: WAJIB sample frame 7s + 8s juga (cek peace ganda) — sampling 0/2/3.5/6.5/9.5 saja pernah kelewatan peace ke-2.
- PERINGATAN FACELESS: ending peace (terutama pipi) bisa narik wajah masuk — di FLORA v2, 9.5s mentah ada mata jelas. Top-crop ~62px WAJIB dan harus dicek ulang di frame 9.5s video FINAL (bukan cuma mentah); kalau mata masih kelihatan setelah crop = GAGAL.
- Aturan bust + background-freeze + top-crop ~5% + Gate 3 (termasuk cek dada lawan frame-0) berlaku penuh seperti mode berdiri lain.
- Cacat yang sudah diketahui (terima sebagai cacat, bukan gagal): framing mengencang setelah 0.6s (kaki kepotong dari ~2s, set tetap utuh); dekor dinding kanan bisa drift (foto kecil tambahan). Peace dada bisa mendarat tinggi (ujung jari dekat dagu) — tetap dihitung dada selama telapak di dada dan bukan di pipi.
- Frame-0 FLORA: v1 gagal (kancing tengah 3, harus 5) → v2 surgical fix lolos. Selalu hitung kancing/saku di Gate 1 untuk setelan (jumlah kancing = detail yang dinilai).

## Mode Berdiri Horizontal — resep "review outfit" (Jendral, 15 Nov 2026 22:51 WITA, tes b18_01 v4 LOLOS Gate 3 ~96%)
- Base: ~/workspace/fashion_test/bases/lala_berdiri_horizontal_base_v2_cahaya.jpg (2112x1168, 16:9, kamar, low bun). REVISI Jendral 16 Nov 2026 01:54 WITA: base v2 = base lama + CERMIN TINGGI (arched mirror) di dinding kiri, memantulkan pintu — biar vibesnya tetap 1 kamar. v1 (tanpa cermin) disimpan sebagai ~/workspace/fashion_test/bases/lala_berdiri_horizontal_base_v1.jpg. Cermin memantulkan PINTU saja, model TIDAK terpantul di cermin — Gate 3 wajib cek cermin tetap konsisten dan tidak memunculkan wajah/model. Framing medium shot (mulut sampai paha tengah). Post-process: crop atas ~32px (~5%), upscale lanczos 1280x720, crf 18, buang audio, cek ulang frame 9.5s final.
- Resep gerakan (prompt review Jendral): gerakan realistis/natural seperti mereview outfit. TETAP berdiri di tempat TANPA melangkah maju (langkah maju = framing mengecil, kelihatan kayak kamera gerak — v1 gagal rasa ini), condongkan badan sedikit ke depan untuk perlihatkan detail jahitan kerah, GOSOK LEMBUT dan perlahan dengan kedua tangan di dada (ujung jari menyentuh kain, tidak menekan keras, tidak cepat — gosok kencang + telapak datar = v3 ditolak), kembali ke posisi awal, putar badan perlahan ~30° ke samping + tarik baju di perut, kepala TETAP menghadap kamera dan tidak pernah menunduk, tanpa voice.
- Kamera COMPLETELY STATIC (framing tidak berubah sama sekali dari frame pertama sampai terakhir, hanya karakter yang gerak — klausul diperkuat: "no zoom, no push-in, no pan, no tilt, no drift, the shot scale stays exactly the same").
- Putar penuh 90° DILARANG: kepala ikut berputar + menunduk, wajah masuk frame (v2 gagal di 6.5s: mata + hidung + mulut kelihatan). Putar yang jalan = ~30° + kepala tetap menghadap kamera (aturan putar Set F).
- Poster dinding kanan yang drift/nambah sendiri DITERIMA, tidak masalah — yang penting gerakan karakternya benar (Jendral, 22:51 WITA).
- ATURAN VARIASI (Jendral, 22:51 WITA): setelah pembuka "condong + gosok lembut", LANJUTANNYA HARUS BERVARIASI tiap video supaya tidak repetitif dan tidak kelihatan spam. Rotasi lanjutan (pilih/adaptasi per produk, seperti Set A–E di mode duduk): putar 30° kiri / putar 30° kanan, sentuh kerah/syal, rapikan hem, tangan di pinggang, usap turun ke hem, tarik baju di perut. Pembuka tetap sama, lanjutan dirotasi.
