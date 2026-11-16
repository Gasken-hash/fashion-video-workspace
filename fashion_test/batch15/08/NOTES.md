# Product 08 — Sweater Rajut Wol Stripe Ribbon Collar — NOTES

**Produk:** MAMAMARA Sweater Rajut Wol Stripe Ribbon Collar Coquette Soft Knit
**ID:** 1737394484556629588 — Link: https://vt.tokopedia.com/t/ZS9fQh2M5qRwT-b8ZzX/
**Referensi:** `batch15/08/tok_00.jpg` (dari link Tokopedia Jendral, via curl-cffi)
**Base:** `bases/base_pita_v3_kacamata.jpg` (Pita v3 frame-0, kacamata di lantai kanan bawah)
**Gerakan:** Set A adaptasi — pinggang/rambut → sentuh pita biru di kerah → dada (garis) → hem → pangkuan → muter samping → peace sign
**Tanggal:** 13 Nov 2026

## Gate 1 — LULUS (frame-0 pertama, tanpa perbaikan)
Frame-0: `media-generation-frame0-stripe-duduk-lilo-v1-0-a737531f-99b6-4a89-b73a-2caa1b218eea.webp` (1168x2112, ketajaman 34,1; salinan `frame0_stripe.jpg`)
- Putih + garis biru muda horizontal merata di badan dan lengan ✓
- Kerah polo putih, 2 garis biru tipis di tiap sisi kerah ✓
- Pita biru muda di leher, simpul rapi ✓
- Tepat 2 kancing putih di bawah pita ✓
- Lengan panjang menempel di bahu ✓
- Hem ribbed putih lebar, lurus ✓
- Celana putih drawstring dipertahankan (referensi tidak menunjukkan bawahan) ✓
- Framing potong mulut, mata tidak kelihatan ✓, rambut cepol ✓
- Base utuh: dinding maroon, lantai speckled, kacamata kanan bawah, tangan di pinggang ✓
- Tidak ada pita pink / cardigan pink tersisa ✓

## Gate 3 — LULUS
Video mentah: `media-generation-stripe-duduk-lilo-v1-0-3f896b2c-2b8a-47ec-b98a-7f4038cab6ce.mp4` (640x1168, 10,0 dtk, 24fps, h264 + AAC bawaan generator)
- Background 0 vs 0,6 dtk identik (dinding/lantai/kacamata tidak bergerak) ✓
- Mata/wajah penuh tidak muncul di frame manapun — top 9,5 dtk dan 6,5 dtk diperbesar, cuma mulut + dagu ✓
- Produk identik di semua frame (garis, kerah, pita, 2 kancing, hem ribbed utuh; tanpa detail inventaris) ✓
- Ketajaman video 53–78 vs frame-0 34,1 (video lebih tajam, tanpa unsharp) ✓
- Gerakan tenang, tangan saja; beat kena: rambut (2 dtk), sentuh pita (3,5 dtk), cubit hem (6,5 dtk), peace sign jelas (9,5 dtk) ✓

## Final
`stripe_duduk_lilo_v1_upscale720.mp4` — 720x1280, 24fps, 10,0 dtk, 3,9 MB, video-only (audio bawaan generator di-strip, ffprobe hanya 1 stream video). Potong atas 60px + upscale lanczos crf 18.
Frame 3,5 dtk final: `g3_final_3.5s.jpg` (720x1280, ketajaman 55,5 vs video mentah 64,9 — pelembutan upscale yang diketahui dan diterima).

## Cacat jujur
1. Kalung emas kecil dari base kelihatan di kerah (artefak base, sama seperti Krem/Beige/Hitam).
2. Frame-0 sendiri agak lembut (34,1), tapi videonya lebih tajam, jadi final tidak kelihatan lembut.
3. Dagu/mulut ngintip di tepi atas (ditoleransi); mata tidak pernah kelihatan.
4. Di 6,5 dtk kepala muter ke profil samping (hidung/bibir/dagu kelihatan, mata tetap kepotong).
5. Pita di video sedikit lebih besar dari referensi, tapi bentuk, warna, dan posisi tepat.
6. Pelembutan upscale (diketahui, diterima): ketajaman 3,5 dtk final 55,5 vs video mentah 64,9.

Tidak ada penolakan generator, tidak ada retry. 1 image call + 1 video call dipakai.
