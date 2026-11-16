# 05 Kaos Hati — NOTES

**Produk:** Kaos Wanita Bergaris Biru Bermotif Hati Lengan Panjang Bersulam Leher Kru
**ID Tokopedia:** 1731026900945634359 | **Showcase:** SUDAH ADA (konfirmasi Jendral 14 Nov 23:29 WITA)
**Ref:** `05_kaos_hati/tok_02.jpg` (800x800, flat-lay) — kaos lengan panjang garis horizontal biru muda di dasar krem/putih, kerah kru lis HITAM, EXACTLY 1 hati merah kecil di dada kiri, slim fit. Bawahan: jeans gelap.
**Base:** `bases/base_pita_v3_kacamata.jpg` (1536x2752, Pita v3 frame-0, kacamata di lantai kanan bawah)
**Format:** DUDUK, vertikal 9:16, dinding maroon, resep LILO. Gerakan disesuaikan fitur produk: rambut → kerah kru → hati merah → usap garis lengan → hem → jeans → pangkuan → peace sign.

## Gate 1 — LOLOS (frame-0 v1, tanpa perbaikan)
- Frame-0: `media-generation-frame0-kaoshati-v1-0-a17a777f-8d34-4f31-8b98-56e62f582267.webp` (copy: `frame0_kaoshati_v1.webp`, 1168x2112, ketajaman 79,0)
- Cek lawan tok_02.jpg: dasar krem/putih ✓, garis horizontal biru muda rata ✓, kerah kru lis HITAM ✓, EXACTLY 1 hati merah kecil di dada kiri ✓ (satu, polos, tanpa logo/teks lain), lengan panjang menempel di bahu ✓, slim fit ✓, hem lurus datar tanpa ruffle ✓, jeans gelap ✓, cepol tinggi longgar + helai depan ✓, framing potong mulut/dagu (mata tidak kelihatan) ✓, dinding maroon + lantai speckled + kacamata di lantai ✓.

## Gate 3 — LOLOS (video v1, tanpa regen)
- Video raw: `media-generation-kaoshati-duduk-lilo-v1-0-91be9b44-a8b7-43bb-a767-9bd39d5fd05e.mp4` (copy: `kaoshati_duduk_lilo_v1_raw.mp4`, 640x1168, 24fps, 10,0 dtk)
- Background 0 vs 0,6 dtk identik (beku) ✓; produk identik di semua frame 0/2/3,5/6,5/9,5 dtk — hati tetap 1, garis tetap biru muda, lis hitam utuh ✓
- Mata/wajah penuh tidak ada di frame mana pun; bagian atas frame 9,5 dtk yang diperbesar (g3_top95.jpg) = ujung hidung + mulut saja, tanpa mata — dalam toleransi (aturan terkalibrasi Jendral: hidung boleh, yang penting bukan full face) ✓
- Ketajaman video: 0s 138,3 / 0,6s 136,9 / 2s 116,1 / 3,5s 90,8 / 6,5s 143,8 / 9,5s 165,4 — video tidak lebih lembut dari frame-0, tanpa unsharp ✓
- Gerakan tenang, bahu/dada diam; beat terbaca: 3,5 dtk tangan di kerah/hati, 6,5 dtk usap garis lengan, 9,5 dtk peace sign di level dada ✓
- Post-proses: crop atas 58px (~5%) → buang audio → upscale lanczos 720x1280, crf 18, preset slow.
- Final: `kaoshati_duduk_lilo_v1_upscale720.mp4` — 720x1280, 24fps, 10,0 dtk, h264, video-only (silent, volumedetect tanpa stream audio). Intermediate: `kaoshati_duduk_lilo_v1_silent.mp4` (640x1110, 10,0 dtk).
- Frame 3,5 dtk final: `kaoshati_3.5s.jpg`

## Daftar cacat jujur
1. Kalung emas tipis dari base kelihatan di kerah di semua frame (artefak base, bukan produk).
2. Mulut/dagu ngintip di tepi atas sepanjang video (dalam toleransi); ujung hidung kelihatan di 9,5 dtk sebelum crop — setelah crop 58px terpotong.
3. Tangan agak motion-blur saat bergerak di 3,5 dtk; terbaca jelas di 6,5/9,5 dtk.
4. "Sentuh hati merah" di 3,5 dtk ter-cover sebagian oleh tangan yang menyentuh kerah — hati tetap terlihat penuh dan utuh di frame lain.
5. Tangan kanan bertumpu di pinggang di frame-0/0 dtk (pose bawaan base).

## Status
- TIDAK diupload ke Cloudinary, TIDAK dicatat ke sheet — menunggu persetujuan Jendral.
