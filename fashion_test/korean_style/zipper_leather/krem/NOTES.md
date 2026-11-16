# Zipper Leather — KREM (duduk LILO v1)

Produk: MAMAMARA Cardigan Rajut Wol Zipper Leather Elegant Knit Jaket (krem)
Referensi: DARI LINK TOKOPEDIA Jendral — tokopedia/tok_06_6fe7a7242f96.jpg
Base: cable_knit/base_pita_v3_frame0.jpg (dinding maroon, celana putih, tas hitam di lantai)

## File
- Frame-0: media-generation-frame0-krem-duduk-lilo-v1-0-8be2e66e-066c-4978-b43c-8992ae0c6b71.webp
- Video mentah: media-generation-krem-duduk-lilo-v1-0-9697ad7d-8f68-46cd-bd3f-15e3f2f91eb6.mp4 (640x1168, 10,0 dtk, ada audio AAC)
- FINAL: krem_duduk_lilo_v1_silent.mp4 — 640x1110, 10,0 dtk, video-only (tanpa audio)

## Post-process
- ffmpeg crop=640:1110:0:58 (crop 58 px dari atas, ~5%, drift insurance), -an, crf 18.
- Verifikasi: hanya 1 stream video (ffprobe csv: stream,video); durasi 10,000000 dtk.

## Gate 1 — LOLOS (sekali jalan)
- Warna krem ✓, kerah kulit coklat pointed 2 flap ✓, resleting silver penuh tengah ✓,
  lengan panjang ✓, hem lurus ✓, fit ✓, framing mouth-cut tanpa mata ✓,
  celana putih ✓, dinding maroon + lantai speckled + tas hitam ✓, pose tangan di pinggang ✓,
  cepol ✓. Kalung emas tipis ada di frame-0 — WARISAN dari base (bukan hasil invent generator).

## Gate 3 — LOLOS
- Ketajaman (Laplacian variance, numpy/PIL): frame-0 49,3; video 0s 144,4 / 0,6s 168,2 /
  2s 174,5 / 3,5s 220,5 / 6,5s 178,6 / 9,5s 238,7 — video LEBIH TAJAM dari frame-0,
  TIDAK perlu unsharp.
- Background 0 vs 0,6 dtk: wall TL mean abs diff 7,72; floor L 4,54 (skala 0-255) — beku,
  hanya noise kompresi. Full-frame diff 11,66 (termasuk gerakan tangan).
- Produk identik di semua frame: krem ribbed, kerah kulit coklat, resleting silver, lengan panjang.
- Mata: TIDAK ADA di frame manapun; top crop 9,5 dtk diperbesar 2x hanya mulut + dagu.
- Badan tenang (torso/bahu/dada diam, hanya tangan bergerak). Beats terkonfirmasi di frame
  sampel: pinggang (0s) → rambut/kerah (2s) → dada (3,5s) → pangkuan (6,5s) → peace sign (9,5s).
- Peace sign di 9,5 dtk: 2 jari rapi, kuku nail art sama seperti base.

## Cacat jujur
1. Mulut + dagu kelihatan di tepi atas semua frame — ini framing mouth-cut yang DITOLERANSI
   Jendral, bukan cacat; crop 58 px sudah diterapkan.
2. Beat "telusuri resleting" (antara 3,5–6,5 dtk) tidak tertangkap di frame sampel — tidak bisa
   dikonfirmasi langsung dari 6 frame yang diekstrak; alur gerakan selebihnya lengkap.
3. Di frame 2 dtk kedua tangan naik ke rambut sempat menutupi sebagian kerah — sesaat saja,
   produk tidak berubah.
4. Frame-0 (webp) lebih lembut dari frame video — tidak berpengaruh ke video final yang tajam.
5. Resolusi final 640x1110 (bukan 668x1188 seperti video LILO sebelumnya) — variasi output
   generator; ketajaman terukur bagus.
