# Batik Naira — batch-16 #03 — NOTES

- **Produk:** BATIK KANTORAN ID Atasan Batik Wanita Couple Motif Naira Series PEKALONGAN (varian MAROON)
- **Tokopedia ID:** 1736321032961558507 | shortlink: ZS9fbwVs5Ct7o-ktzYB
- **Ref:** `tok_01.jpg` (800x800) — atasan batik putih motif maroon, kerah Shanghai tegak, kancing depan miring (silang) 2 kancing putih, zigzag maroon di sepanjang kancing, motif bunga bintang di dada, motif daun di hem bawah, lengan 3/4 bahu sedikit puff, celana putih.
- **Showcase:** SUDAH ADA (konfirmasi Jendral 14 Nov 23:29 WITA, semua 10 produk batch-16 ada di showcase).
- **Base:** `~/workspace/fashion_test/bases/base_pita_v3_tumbler.jpg` (1536x2752, Pita v3 frame-0, tumbler hitam di lantai kanan bawah).
- **Format:** duduk LILO vertikal 9:16, dinding maroon, gerakan tenang (Set adaptasi fitur: rambut → kerah Shanghai → usap motif bunga dada → telusuri garis kancing miring → hem motif daun → celana → pangkuan → peace sign).

## Gate 1 — LOLOS (frame-0 v1, tanpa perbaikan)
- File: `media-generation-frame0-batik-v1-0-ad7b78a7-3f46-40b1-b69f-3732dc81080a.webp` (1168x2112).
- Cocok detail per detail lawan tok_01.jpg: putih + motif maroon ✓, kerah Shanghai tegak tertutup di leher ✓, kancing miring diagonal 2 kancing putih di dada atas ✓, garis zigzag berlian maroon mengikuti kancing ✓, motif bunga bintang di dada ✓, titik-titik kecil di kain putih ✓, pita motif daun di hem bawah ✓, trim zigzag maroon di tepi bawah hem ✓, lengan 3/4 bahu sedikit puff ✓, celana putih polos ✓. Framing potong mulut/dagu, mata tidak kelihatan ✓. Dinding maroon + lantai speckled + tumbler dipertahankan ✓. Rambut cepol tinggi longgar + helai depan ✓. Tanpa pita, tanpa kancing mutiara, tanpa cardigan pink ✓.

## Gate 3 — LOLOS (video v1, tanpa regen)
- Raw: `media-generation-batik-duduk-lilo-v1-0-3f042e12-aed6-4039-a0ae-bca497ced52f.mp4` (640x1168, 24fps, 10.0s, h264, tanpa audio).
- Background 0 vs 0.6 dtk identik (beku); produk identik di semua frame 0/2/3.5/6.5/9.5 dtk — tidak ada detail diciptakan/dihilangkan.
- Mata/wajah penuh tidak ada di frame mana pun; cek bagian atas frame 9.5 dtk yang diperbesar (`g3_f9.5s_top.jpg`) = mulut + dagu saja, hidung dan mata tidak kelihatan.
- Gerakan tenang, bahu/dada diam, tangan saja bergerak; beat kerah + motif bunga + peace sign di level dada tertangkap jelas.
- Ketajaman (Laplacian variance): frame-0 359.5; video 2 dtk 1839.9; 3.5 dtk 2044.4; 9.5 dtk 2253.6. Angka didominasi pola batik yang rapat (kontras maroon-putih), bukan ukuran ketajaman antar produk — intinya video TIDAK lebih lembut dari frame-0, tanpa unsharp.
- Post-proses: crop atas 58px (~5%) → buang audio → upscale lanczos 720x1280, crf 18, preset slow.
- **Final:** `batik_duduk_lilo_v1_upscale720.mp4` — 720x1280, 24fps, 10.0 dtk, h264, 5.86 MB, video-only (silent, terverifikasi ffprobe + volumedetect "NO AUDIO STREAM").
- Frame 3.5 dtk: `batik_3.5s.jpg`.

## Daftar cacat jujur
1. Mulut/dagu ngintip di tepi atas sepanjang video (dalam toleransi).
2. Tangan kiri motion-blur saat naik ke rambut di 0.6 dtk; terbaca jelas di frame-frame berikutnya.
3. Beat "telusuri garis kancing miring" tidak tertangkap sebagai beat yang jelas terpisah — tangan lebih banyak di dada/kerah (3.5 dtk) lalu langsung ke hem/pangkuan (6.5 dtk); garis kancing tetap terlihat penuh di semua frame.
4. Jepit rambut metalik kecil muncul di cepol (terlihat di 2 dtk dan 3.5 dtk) — detail rambut yang diciptakan generator, bukan bagian produk.
5. Kalung emas dari base TIDAK kelihatan (kerah Shanghai menutup leher) — tidak seperti video-video sebelumnya.
6. Gerakan ke arah peace sign di akhir sedikit cepat (tangan sudah naik di 9.5 dtk, peace sign terbentuk jelas).

## Status
- Gate 1 + Gate 3 LOLOS pertama jalan. Belum diupload ke Cloudinary, belum dicatat ke sheet (menunggu persetujuan Jendral).
