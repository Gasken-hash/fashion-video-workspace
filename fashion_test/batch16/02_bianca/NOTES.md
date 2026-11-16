# BIANCA Inner Floral Vest — batch-16 #02 — NOTES

- **Produk:** BIANCA INNER KARDIGAN FLORAL VEST ATASAN WANITA TANPA LENGAN
- **Tokopedia ID:** 1736485039649555762 | shortlink: ZS9fq5YS9gamP-kJu0G
- **Showcase:** SUDAH ADA (Rp57.800)
- **Ref:** `02_bianca/tok_01.jpg` (flat-lay, 800x800) — vest tanpa lengan, dasar putih,
  motif bunga matahari kuning + bunga pink + daun hijau/biru, leher bulat,
  kerut di pinggang, hem peplum/ruffle melebar. Produk = vest saja (di video
  dipakai sebagai atasan LUAR, tanpa kardigan). Bawahan: celana putih lebar.
- **Base:** `bases/base_pita_v3_kacamata.jpg` (1536x2752, dinding maroon, kacamata di lantai kanan bawah)
- **Format:** duduk LILO vertikal 9:16, gerakan Set B adaptasi (rambut → tali bahu →
  leher bulat → telusuri motif bunga di dada → hem peplum → celana → pangkuan →
  peace sign di level dada)
- **Tidak ada resleting.**

## Gate 1 — LOLOS (frame-0 v1, tanpa perbaikan)
- Frame-0: `media-generation-frame0-bianca-v1-0-6c34c717-f555-485e-a1cb-aa9df1fa3dbc.webp`
- Cocok detail per detail lawan tok_01.jpg: dasar putih ✓, motif bunga matahari
  kuning + pink + hijau/biru ✓, tanpa lengan ✓, leher bulat ✓, kerut pinggang +
  hem peplum melebar (kain datar, flare lembut) ✓, dipakai sebagai atasan luar
  tanpa kardigan ✓, celana putih lebar ✓, framing potong mulut/dagu (mata tidak
  kelihatan) ✓, cepol tinggi longgar + helai depan ✓, dinding maroon + lantai +
  kacamata dipertahankan ✓.

## Gate 3 — LOLOS (video v1, tanpa regen)
- Video raw: `media-generation-bianca-duduk-lilo-v1-0-1d423e9f-845b-4909-b5ba-0e121404b13b.mp4`
  (640x1168, 24fps, 10.0 dtk, ada audio AAC -57.5 dB — dibuang di post-proses)
- Background 0 vs 0.6 dtk identik (beku); produk identik di semua frame
  0/2/3.5/6.5/9.5 dtk — tidak ada detail diciptakan/dihilangkan.
- Mata/wajah penuh tidak ada di frame mana pun; cek bagian atas frame 9.5 dtk
  yang diperbesar (2x) = mulut + dagu saja, tanpa mata, tanpa hidung.
- Ketajaman (Laplacian): frame-0 269.3; video 0 dtk 1039.8, 0.6 dtk 1087.7,
  2 dtk 938.4, 3.5 dtk 829.0, 6.5 dtk 770.7, 9.5 dtk 846.8 — video TIDAK lebih
  lembut dari frame-0, tanpa unsharp.
- Gerakan tenang, bahu/dada diam, tangan saja bergerak; peace sign jelas
  terbentuk di 9.5 dtk di level dada, tidak dekat wajah.
- Peplum tetap flare kain datar — tidak ada ruffle kaku menonjol yang diciptakan video.
- Post-proses: crop atas 58px (~5%) → buang audio → upscale lanczos 720x1280, crf 18.
- Final: `bianca_duduk_lilo_v1_upscale720.mp4` — 720x1280, 10.0 dtk, h264, 24fps,
  video-only (silent, terverifikasi ffprobe: hanya 1 stream video).

## Daftar cacat jujur
1. Kalung emas tipis dari base kelihatan di kerah di semua frame (artefak base,
   bukan bagian produk).
2. Mulut/dagu ngintip di tepi atas sepanjang video (dalam toleransi).
3. Tali serut di celana putih adalah bawaan base (di foto model ref, celana
   putih lebar — detail serut tidak terverifikasi di ref; minor, bukan produk).
4. Tangan kanan motion-blur saat menyentuh leher di 3.5 dtk; tangan menutupi
   motif dada sebagian di 6.5 dtk (motif tetap terlihat penuh di frame lain).
5. Framing sedikit mengetat di 3.5 dtk (kepala menengadah) — tetap hanya
   mulut/dagu yang kelihatan.
6. Peplum di frame-0/video ada garis lipatan sehingga terbaca sedikit lebih
   bertingkat dari flat-lay (satu tier) — siluet sama (kerut pinggang + flare
   melebar), bukan tier terpisah.

## Status
- Belum diupload ke Cloudinary, belum dicatat ke sheet (menunggu persetujuan Jendral).
- Frame video 3.5 dtk: `bianca_3.5s.jpg` (dari video final).
