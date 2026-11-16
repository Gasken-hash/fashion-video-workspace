# 04 Mirella — Lunelly Mirella Tweed Vest (batch-16 #04)

## Produk
- **Nama:** Lunelly Mirella Tweed Vest Wanita Premium | Atasan Vest Korea Chic Elegan Knitwear | Sleeveless Top Blouse Wanita Fashion Kekinian
- **ID Tokopedia:** 1737590191794849168 | showcase: SUDAH ADA (konfirmasi Jendral 14 Nov 23:29 WITA)
- **Ref:** `04_lunelly/tok_00.jpg` — vest tweed TANPA LENGAN motif kotak-kotak krem/putih garis hitam + kuning muda, leher bulat, EXACTLY 4 kancing besar emas di depan tengah, hem depan meruncing (V kecil di tengah bawah). Varian krem (peach). Bawahan: rok mini putih.
- **Resleting:** tidak ada.
- **Base:** `bases/base_pita_v3_tas.jpg` (1536x2752, Pita v3 frame-0, tas hitam di lantai kanan bawah)
- **Format:** duduk, vertikal 9:16, dinding maroon, resep LILO.

## Gate 1 — LOLOS (frame-0 v1, tanpa perbaikan)
- Frame-0: `media-generation-frame0-mirella-v1-0-89e48897-4dba-4704-bcfa-145faeb105ef.webp`
- Cocok detail per detail vs tok_00.jpg: tweed kotak krem/putih garis hitam + kuning muda ✓, leher bulat ✓, EXACTLY 4 kancing besar emas di depan tengah ✓, hem meruncing V kecil ✓, tanpa lengan ✓, rok mini putih polos ✓, framing potong mulut/dagu (mata tidak kelihatan) ✓, rambut cepol tinggi longgar ✓, dinding maroon + lantai + tas di lantai dipertahankan ✓.
- Ketajaman frame-0 (Laplacian): 166,1.

## Gate 3 — LOLOS (video v1, tanpa regen)
- Video raw: `media-generation-mirella-duduk-lilo-v1-0-659c3a54-b0f7-490b-9200-1449f1fc7973.mp4` (640x1168, 10,0 dtk, 24fps)
- Background 0 vs 0,6 dtk identik (beku) ✓
- Produk identik di semua frame 0/2/3,5/6,5/9,5 dtk — jumlah kancing tetap 4 di semua frame, tidak ada detail diciptakan/dihilangkan ✓
- Mata/wajah penuh tidak ada di frame mana pun; cek bagian atas frame 9,5 dtk yang diperbesar (g3_top95.jpg) = ujung hidung + mulut + dagu saja, tanpa mata (dalam toleransi kalibrasi Jendral 14 Nov 13:31 — hidung boleh, full face tidak) ✓
- Ketajaman (Laplacian): frame-0 166,1; video 0 dtk 560,8; 2 dtk 671,7; 3,5 dtk 582,5; 6,5 dtk 667,3; 9,5 dtk 599,1 — video LEBIH tajam dari frame-0, tanpa unsharp ✓
- Gerakan tenang, bahu/dada diam, sesuai adaptasi fitur (rambut → leher bulat → kancing emas satu-satu → telusuri motif kotak di dada → hem meruncing → rok → pangkuan → peace sign di level dada di 9,5 dtk) ✓

## Post-proses
- Crop atas 58px (~5%) → buang audio → upscale lanczos 720x1280, libx264, crf 18, preset slow, -an.
- Final: `mirella_duduk_lilo_v1_upscale720.mp4` — 720x1280, 10,0 dtk, 24fps, h264, video-only (silent, tidak ada audio stream).
- Ketajaman final 3,5 dtk: 393,7.
- Frame 3,5 dtk final: `mirella_3.5s.jpg`.

## Daftar cacat jujur
1. Kalung emas tipis dari base kelihatan di kerah di semua frame (artefak base; model di foto referensi juga memakai kalung tipis, jadi bukan ketidakcocokan produk).
2. Mulut/dagu ngintip di tepi atas sepanjang video (dalam toleransi); ujung hidung tampak sekilas di 9,5 dtk (dalam toleransi kalibrasi, dan terpotong oleh crop atas 58px di final).
3. Kancing emas ke-1 tertutup sebagian oleh jari saat tangan menyentuh leher di 3,5 dtk — keempat kancing tetap terbaca jelas di frame lain.
4. Tangan kanan bertumpu di pinggang di frame-0/0 dtk (pose bawaan base).
5. Grid tweed di frame-0 menampilkan garis biru muda yang sedikit lebih terlihat dibanding foto referensi (di ref, garis kuning muda lebih dominan) — motif kotak + garis hitam tetap sama.

## Status
- Belum diupload ke Cloudinary, belum dicatat ke sheet — menunggu persetujuan Jendral.
