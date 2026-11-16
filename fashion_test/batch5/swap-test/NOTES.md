# Swap-test: ganti baju saja, background tetap (12 Nov 2026)

Keluhan Jendral (00:12 WITA): background batch 5 tidak konsisten antar
produk, padahal dia cuma mau bajunya yang diganti.

## Metode
- Base: foto model Adelia landscape (media-generation-adelia-model-
  landscape-0-1936c196....webp) — kamar pink, kasur kiri, pintu kanan.
- Edit via media.generate_image: ganti HANYA blouse burgundy jadi
  Lunelly pink polkadot halter (referensi foto seller Lunelly), dengan
  instruksi eksplisit jangan redraw background/pose/rok/tas.
- Tes 1x produk Lunelly (paling beda struktur dari Adelia).

## Hasil foto edit
- File: media-generation-batch5-swap-test-lunelly-0-9e71ae3b....webp
- Background TERBUKTI identik dengan foto Adelia: kasur, boneka, bantal,
  tanaman, pintu kayu, dinding, lighting, pose, rok putih, tas rantai —
  semua sama.
- Baju: pink polkadot + 2 pita kecil + hem lancip = benar. CACAT:
  lengan jadi off-shoulder/detached (lengan panjang terlepas dari bahu),
  padahal Lunelly asli lengannya nempel di bahu. Perlu edit ulang dengan
  penekanan "sleeves attached at the shoulders, NOT off-shoulder".

## Hasil video (dari foto hasil edit)
- File: media-generation-batch5-swap-test-lunelly-video-0-586acb7d....mp4
  1248x704, 10,0 dtk, 24 fps, SILENT (mean -47,8 dB).
- QC (qc/w_*.jpg): langkah maju JELAS (2 dtk framing ketat, tangan di
  pita), kamera diam, background tetap sama di semua frame, beat 1-3
  jalan.
- CACAT: mulut/dagu ngintip di 3,5 dtk (w_08) dan 9,5 dtk (w_20) —
  lebih parah dari Adelia v3 (yang cuma di 1 dtk terakhir). Penyebab
  kemungkinan: crop atas frame ini lebih ketat sehingga kepala gampang
  masuk frame saat model bergerak.

## Kesimpulan
- Pertanyaan Jendral terjawab: YA, BISA — background bisa dipertahankan
  identik, hanya bajunya yang diganti.
- Yang belum beres: (1) lengan off-shoulder di hasil edit, (2) mulut
  ngintip di video.
- Tawaran ke Jendral: perbaiki lengan via 1x edit ulang, atau langsung
  terapkan swap ke 4 produk lain (LILO, HYLE, Luluna, Kamila) dengan
  base yang sama.
- Catatan kuota: edit gambar max 4/pesan; 1 sudah terpakai di pesan ini
  (swap Lunelly). Video 1/6 terpakai di pesan ini.

## Perbaikan v2 — aturan cek-gambar-dulu (12 Nov 2026, 00:19 WITA)

Aturan baru dari Jendral: sebelum generate video, generate gambar dulu
dan cek samakan dengan foto asli seller; kalau belum sama, perbaiki
gambarnya dulu; baru generate video kalau sudah sama.

- Edit ulang dari foto dasar Adelia (BUKAN dari edit v1 yang cacat):
  media-generation-batch5-swap-test-lunelly-v2-0-76cc45e7....webp
- Cek lawan foto asli seller Lunelly: LOLOS.
  - Pink polkadot: sama.
  - Halter + 2 pita kecil di tali bahu: sama.
  - Lengan panjang NEMPEL di bahu, bahu tertutup: SAMA (cacat v1
    off-shoulder sudah hilang).
  - Fit body: sama.
  - Hem: v2 bentuk V tajam, aslinya lekuk U lembut — beda derajat,
    bukan beda produk. Dicatat sebagai minor, bukan gagal.
  - Background: identik dengan foto dasar Adelia. Faceless.
- Video v2: media-generation-batch5-swap-test-lunelly-v2-vi-0-2be3fb96....mp4
  1248x704, 10,0 dtk, 24 fps, SILENT (mean -44,1 dB).
- QC (qc2/x_*.jpg): produk BENAR sepanjang video (lengan nempel,
  pita, polkadot); langkah maju jelas di 2 dtk; kamera diam; background
  konsisten; beat 1-3 jalan.
- Cacat tersisa: mulut/dagu ngintip di ~1 dtk terakhir (x_20) — pola
  berulang dari Adelia v3 dan batch Lunelly. Di 3,5 dtk sudah aman
  (v1 ngintip di 3,5 dtk juga, v2 tidak).
- Keputusan Jendral soal lanjut ke 4 produk lain (LILO, HYLE, Luluna,
  Kamila) dengan cara swap yang sama masih pending.

## Perbaikan v3 — bedah hem (12 Nov 2026, 00:25 WITA)

Pertanyaan Jendral: bajunya tidak sama bentuknya, bagaimana caranya
supaya bentuknya sama? Ide yang ditawarkan:
1. Bedah detail: edit bedah, ubah HANYA bagian yang tidak sama dengan
   kata bentuk yang eksplisit. (Terbukti di bawah.)
2. Kalau bedah gagal 2x: pakai foto asli seller langsung, di-crop
   faceless (cara LILO) — bentuk 100% asli karena memang foto aslinya,
   tapi background jadi background seller, bukan kamar pink.
3. Komposit: potong baju asli, tempel ke foto dasar — paling eksak di
   teori, tapi pose dan lighting beda, rawan kelihatan tempelan.
   Opsi terakhir.

- Edit bedah dari foto v2 (BUKAN dari dasar):
  media-generation-batch5-swap-test-lunelly-v3-he-0-199ba15c....webp
  Ubah HANYA hem (jadi lekuk U lembut, tanpa titik tajam/lipatan
  diagonal) + neckline (jadi scoop bulat).
- Cek lawan foto asli seller Lunelly: LOLOS. Hem kini lekuk U lembut
  seperti aslinya, neckline scoop bulat, lengan tetap nempel di bahu,
  pita, polkadot, fit, background identik. Bentuk baju SAMA.
- Video v3: media-generation-batch5-swap-test-lunelly-v3-vi-0-bf08e258....mp4
  1248x704, 10,0 dtk, 24 fps, SILENT (mean -41,4 dB).
- QC (qc3/y_*.jpg): bentuk baju BENAR sepanjang video (hem bulat,
  lengan nempel); langkah maju jelas di 2 dtk; kamera diam; background
  konsisten; beat 1-3 jalan.
- Cacat tersisa: mulut/dagu ngintip di ~1 dtk terakhir (y_20) — pola
  berulang dari v2/Adelia v3; pita membesar di 3,5 dtk (y_08).
- Keputusan Jendral soal lanjut ke 4 produk lain masih pending.
