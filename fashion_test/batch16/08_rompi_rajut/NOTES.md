# 08 Rompi Rajut Garis — NOTES.md

Produk: Atasan rompi rajut bergaris dengan blok warna ala Korea yang dipadukan dengan kemeja.
Tokopedia ID: 1738462595784738573 | shortlink: ZS9fbE6bLQ7co-QJ3V5
Showcase: SUDAH ADA (Jendral 14 Nov 23:29 WITA: semua 10 produk batch-16 sudah di showcase).
Format: DUDUK (vertikal 9:16, dinding maroon, resep LILO). Base: `bases/base_pita_v3_tas.jpg`.

## Foto referensi
`tok_01.jpg` (800x800, di gantungan): rompi rajut TANPA LENGAN, garis horizontal navy + maroon + putih
(band navy lebar + band maroon + pinstripe putih, berulang rata), kerah polo PUTIH lebar dengan
flap runcing, placket krem-putih pendek dengan kancing putih kecil, lis MAROON ribbed di lubang
lengan dan di hem bawah, fit lurus pendek sampai pinggang. Bawahan: rok navy (dari foto manekin,
styling). JANGAN pakai tok_06 (kaos abu + jeans) — bukan produk ini.

## KOREKSI JUMLAH KANCING — PENTING
BATCH16_REFS.md dan brief awal menulis "EXACTLY 2 kancing putih". Setelah zoom ke area placket
di tok_01.jpg (crop 35-65% x 18-60%, diperbesar 4x), TERBUKTI ADA TIGA kancing putih kecil
(atas di bawah kerah, tengah, bawah). Produksi ini memakai TIGA kancing, sesuai foto asli.
Mohon BATCH16_REFS.md diperbaiki (2 → 3). Gate 1 di bawah dinilai terhadap foto asli (3 kancing).

## Gate 1 — LOLOS (frame-0 v1, tanpa perbaikan)
File: `media-generation-frame0-rompi-v1-0-798415a5-06b5-4a05-8b46-85cef1d65687.webp`
LILO edit dari base tas + tok_01.jpg. Perbandingan detail per detail vs foto asli:
- Warna: navy + maroon + putih ✓
- Motif/garis: horizontal, band navy lebar + maroon + pinstripe putih, ritme berulang sama ✓
- Kerah: polo putih lebar, flap runcing, rebah di dada ✓
- Kancing: EXACTLY 3 kecil putih di placket krem ✓ (sesuai foto asli)
- Lengan: tanpa lengan ✓ | Lis maroon di lubang lengan ✓ | Hem: band maroon ribbed ✓
- Fit: lurus, pendek sampai pinggang ✓ | Bawahan: rok navy polos ✓
- Framing: potong mulut/dagu, mata tidak kelihatan ✓ | Rambut: cepol tinggi longgar ✓
- Dinding maroon + lantai speckled + tas di lantai dipertahankan ✓
Penilaian identitas produk: ~97-98% (satu nit kecil: kerah di frame-0 sedikit lebih terbuka
dari ref sehingga kalung emas base terlihat — kerah bentuknya tetap benar). ≥95% → LOLOS.

## Video — v1 (tanpa regen)
File raw: `media-generation-rompi-duduk-lilo-v1-0-9adcfb56-0c6e-4692-8332-615f189b633b.mp4`
(640x1168, 24fps, 10.0s, ada audio AAC bawaan generator — dibuang di post-proses).
Gerakan (Set B adaptasi fitur): rambut → kerah polo → 3 kancing satu-satu → telusuri garis
di dada → hem lis maroon → rok → pangkuan → peace sign di level dada (9.5 dtk).

## Gate 3 — LOLOS (video v1)
Frame diekstrak 0 / 0.6 / 2 / 3.5 / 6.5 / 9.5 dtk (`g3_v1_f*.jpg`):
- Background 0 vs 0.6 dtk IDENTIK (beku); dinding, lantai, tas tidak bergeser.
- Produk identik ≥95% di SEMUA frame: garis tetap horizontal & rata, kerah polo sama,
  kancing tetap 3 di semua frame (di 3.5 dtk kancing atas tertutup sebagian oleh jari,
  kancing 2+3 tetap terlihat; ke-3 kancing terbaca penuh di 0/2/6.5/9.5 dtk),
  lis maroon lubang lengan + hem utuh, rok navy sama. Tidak ada detail diciptakan/dihilangkan.
- Mata/wajah penuh TIDAK ADA di frame mana pun. Cek bagian atas frame 9.5 dtk yang
  diperbesar 2x (`g3_v1_top95.jpg`): ujung hidung + mulut + dagu saja, tanpa mata —
  dalam toleransi kalibrasi Jendral (14 Nov 13:31: hidung boleh, full face tidak);
  ujung hidung itu terpotong oleh crop atas 58px di video final.
- Ketajaman (Laplacian): frame-0 115,4; video 0 dtk 426,0; 2 dtk 407,4; 3,5 dtk 339,3;
  6,5 dtk 433,9; 9,5 dtk 426,7 — video LEBIH tajam dari frame-0, tanpa unsharp.
- Gerakan tenang, bahu/dada diam; beat terbaca: 2 dtk tangan di rambut, 3.5 dtk sentuh
  kerah/kancing, 6.5 dtk tangan di pangkuan/hem, 9.5 dtk peace sign jelas di level dada,
  jauh dari wajah.
Penilaian identitas produk video: ~97% di semua frame → LOLOS.

## Post-proses
crop atas 58px (~5%) → buang audio → upscale lanczos 720x1280, crf 18, preset slow.
Final: `rompi_duduk_lilo_v1_upscale720.mp4` — terverifikasi ffprobe: 720x1280, h264,
24fps, 10.000000 dtk, 1 stream video saja (silent). Frame 3.5 dtk final: `rompi_3.5s.jpg`.

## Daftar cacat jujur
1. Kalung emas tipis dari base kelihatan di kerah di semua frame (artefak base, bukan
   bagian produk; model di foto referensi tidak pakai kalung — tapi ini artefak base,
   bukan ketidakcocokan produk).
2. Mulut/dagu ngintip di tepi atas sepanjang video (dalam toleransi); ujung hidung
   tampak sekilas di 9.5 dtk sebelum crop — terpotong di video final.
3. Kancing atas placket tertutup sebagian oleh jari saat tangan menyentuh kerah di
   3.5 dtk (kancing 2 dan 3 tetap terlihat; ke-3 kancing terbaca penuh di frame lain).
4. Tangan kanan bertumpu di pinggang di frame-0/0 dtk (pose bawaan base).
5. Kerah di frame-0/video sedikit lebih terbuka dari foto asli (V kecil di leher
   terlihat lebih lebar) — bentuk kerah tetap polo putih lebar yang benar.

Tidak ada upload Cloudinary, tidak ada pencatatan sheet (menunggu persetujuan Jendral).
Satu video ini saja — tidak ada produk lain yang dikerjakan.
