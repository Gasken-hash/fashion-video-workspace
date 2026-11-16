# Priscila Duduk (sitting) — vertikal 9:16

Keputusan Jendral 13 Nov 2026, 00:14 WITA: "Coba pakai video aku
yang ini, mungkin ini bisa lebih baik, soalnya sederhana banget dia
duduk aja" — format DUDUK (referensi: video dress abu-abu, duduk,
1080x1920, 9,96 dtk, bermusik; bedah di ref_duduk/BREAKDOWN.md).

## Referensi duduk (bedah)
- Model DUDUK sepanjang video (tidak berdiri/jalan/maju), kamera
  diam, framing medium close-up vertikal (dagu-lutut), faceless.
- Tangan bercerita: pinggang/rambut → leher → dada (membuka) →
  hem → pangkuan → muter badan dikit → peace sign di akhir.
- Tas hitam ditaruh di lantai di samping (bukan dipakai).
- Dress abu-abu ribbed U-neck (BUKAN Priscila) — perlu link kalau
  mau dibuat.

## Base duduk baru
- Base: media-generation-base-sitting-adelia-0-864f0110-....webp
  (model Adelia duduk di tepi kasur, kamar pink, atasan putih polos
  + rok putih, vertikal 9:16, faceless). Diturunkan dari base
  Adelia landscape (referensi identitas).
- Frame-0: media-generation-frame0-priscila-duduk-0-15a1b8aa-....webp
  (2096x1184) — swap HANYA atasan ke Priscila maroon.
  LOLOS Gate 1 percobaan pertama: maroon solid, V lace, lengan
  puff on-shoulder, ruched bust, lace band + pita hitam, hem lace;
  pose duduk + rok + kamar utuh.

## Video (Gate 3 LOLOS)
- File kirim: priscila_duduk_v1_silent.mp4 (704x1248, 10,0 dtk,
  video-only, audio -50,1 dB di-strip).
- Ketajaman BAGUS: frame-0 438,9 -> frame video 2 dtk 409,8;
  3,5 dtk 542,0 — TIDAK perlu unsharp.
- Background 0 vs 0,6 dtk IDENTIK (freeze jalan).
- Beat: pinggang 0 dtk, leher 2 dtk, dada 3,5 dtk, pangkuan 6,5 dtk,
  peace sign 9,5 dtk. Duduk terus (tidak berdiri/jalan/maju).
  Baju konsisten di semua frame.
  Cacat jujur: mulut/dagu ngintip dikit di 9,5 dtk (dalam toleransi,
  sama kayak referensi).
- QC: d_qc_0/0,6/2/3,5/6,5/9,5.jpg, d_qc_contact.jpg,
  d_flick_check.jpg, d_before_after.jpg.
- Belum di-upload / dicatat di sheet — menunggu putusan Jendral.
- Anggaran: image 2/4 (base duduk + swap), video 1/6.

## Video LILO v2 — frame asli referensi + Priscila + rambut diikat (Jendral, 13 Nov 2026, 00:26 WITA)
Permintaan: "Pakai ini aja cukup ganti baju aja sama ubah gaya
rambutnya jadi di ikat seperti foto yang lama itu bisa?"
"Foto yang lama" = foto karakter kita (22:14 WITA) — rambut diikat
cep Polos (bun longgar di atas + helaian keriting di pipi).
- Frame asli: ref_duduk/frame0_ref_duduk.png (1080x1920, frame 0
  video duduk, model asli, dress abu-abu, dinding maroon).
- LILO v1 (edit pertama): atasan Priscila BENAR + rambut diikat
  BENAR, tapi rok ikut jadi MAROON (set maroon) dan framing
  menampilkan wajah penuh. Gate 1 GAGAL (2 penyimpangan).
- PELAJARAN PENTING (terbukti 2x): perbaikan bedah (surgical fix)
  pada frame LILO TIDAK BEKERJA — generator kembali ke frame asli
  (dress abu-abu + rambut terurai) dan hanya menerapkan instruksi
  terbaru (rok putih). Fix 1 (path gambar) dan fix 2 (resume
  snapshot) hasilnya SAMA: atasan abu-abu + rambut terurai + rok
  putih. Jadi: JANGAN perbaiki frame LILO dengan edit lanjutan;
  ulangi edit segar dari frame asli dengan semua perubahan sekaligus.
- LILO v2 (edit segar, instruksi rok putih dipertegas: "SOLID
  WHITE, bukan maroon, bukan bagian dari set yang matching"):
  SEMUA BENAR — atasan Priscila, rok putih, rambut diikat cepol,
  wajah terpotong di mulut/dagu (faceless). LOLOS Gate 1.
  File: media-generation-frame0-priscila-duduk-lilo-v2-0-fa4d417e-....webp
  (2096x1184).
- Video: priscila_duduk_lilo_v2_silent.mp4 (704x1248, 10,0 dtk,
  video-only, audio -50,1 dB di-strip) — LOLOS Gate 3.
  Ketajaman TERBAIK SEJAUH INI: frame-0 789,9 -> frame video
  2 dtk 679,5; 3,5 dtk 667,3 (base foto asli jauh lebih tajam
  dari base generate). Background 0 vs 0,6 dtk IDENTIK.
  Beat: pinggang 0 dtk, leher 2 dtk, dada 3,5 dtk, pangkuan 6,5 dtk,
  peace sign 9,5 dtk. Duduk terus. Cepol tetap terikat di semua
  frame. Baju konsisten.
  Cacat jujur: mulut/dagu ngintip dikit di 0-9,5 dtk (dalam toleransi,
  sama kayak referensi).
- QC: lilo_qc_0/0,6/2/3,5/6,5/9,5.jpg, lilo_qc_contact.jpg,
  lilo_flick_check.jpg, lilo_before_after.jpg.
- Belum di-upload / dicatat di sheet — menunggu putusan Jendral.
- Anggaran tes ini: image 4/4 (LILO v1, fix1, fix2, LILO v2),
  video 1/6.

## Perbaikan wajah (Jendral, 13 Nov 2026, 00:30 WITA)
Jendral: "Kepalanya keliatan 🤣" — di video LILO v2, wajahnya
masuk frame penuh di 9,5 dtk (mata + senyum kelihatan jelas)
saat peace sign + menunduk. Igris sempat menilai "mulut/dagu
ngintip dikit" — itu SALAH, di 9,5 dtk wajahnya kelihatan
penuh. Penyebab: frame-0 terpotong di mulut (wajah tepat di tepi
atas), jadi drift kecil saat video berjalan membawa wajah masuk.
- Perbaikan (TANPA generate ulang frame-0 — crop ffmpeg saja):
  frame0_lilo_v2_tight.jpg (crop=982:1746:101:350 dari frame-0
  LILO v2) — framing jadi leher ke bawah, wajah sama sekali
  tidak ada di frame, atasan + rok putih tetap terlihat penuh.
- Video regenerasi dari crop ketat + klausul wajah dipertegas
  (kepala/wajah TIDAK BOLEH masuk frame di detik manapun,
  termasuk saat senyum/menunduk/peace sign).
- File kirim: priscila_duduk_lilo_v2_tight_silent.mp4
  (672x1216, 10,0 dtk, video-only — audio generator -34,4 dB
  di-strip). LOLOS Gate 3: wajah TIDAK ADA di semua frame
  (0/0,6/2/3,5/6,5/9,5 — dicek langsung frame 9,5 dtk ukuran
  penuh: hanya leher + sedikit cepol di tepi atas, tanpa mata/
  hidung/mulut), background 0 vs 0,6 dtk identik, ketajaman
  bagus (frame-0 660,9 -> 761,1/617,9), duduk terus, beat
  lengkap, cepol utuh, baju konsisten.
- PELAJARAN (aturan baru): frame-0 yang terpotong di mulut
  TIDAK CUKUP — drift video bisa membawa wajah penuh masuk.
  Untuk video duduk/close-up, potong frame-0 sampai leher/
  tulang selangka (tight crop) supaya ada margin drift.
  QC Gate 3 WAJIB cek frame 9,5 dtk ukuran penuh untuk wajah.
- QC: tight_qc_0/0,6/2/3,5/6,5/9,5.jpg, tight_qc_contact.jpg,
  tight_flick_check.jpg, tight_before_after.jpg.
- Belum di-upload / dicatat di sheet — menunggu putusan Jendral.
  Anggaran tes ini: image 0 (crop ffmpeg saja), video 1/6.

## Video "ketawa" (Jendral, 13 Nov 2026, 00:33 WITA)
Jendral (tentang video tight): "Kok videonya karakternya ketawa?"
Penyelidikan: frame rapat tiap 0,5 dtk (dense_*.jpg, 20 frame)
membuktikan wajah TIDAK ADA di frame manapun — jadi bukan
wajahnya yang senyum di kamera. Penyebabnya gerak BADAN: generator
memberi gerakan bahu/dada yang memantul dan gelisah (terutama
saat tangan di dada 2-4,5 dtk + muter badan 5-7 dtk yang
condongnya berlebihan), dibaca mata sebagai ketawa/cekikikan.
Referensi aslinya gerakannya lambat, halus, dan tenang.
Catatan jujur: metrik garis bahu (top_y maroon) TIDAK bisa
dipakai sebagai bukti — detektornya menangkap lengan/bahu
saat tangan terangkat, jadi angkanya tidak stabil.
- Perbaikan: video diregenerasi dari frame-0 tight yang sama
  dengan klausul gerak TENANG dipertegas (bergerak lambat,
  halus, tenang; torso/bahu/dada diam total, tidak memantul/
  gemetar/cekikikan; hanya tangan yang bergerak pelan).
- File kirim: priscila_duduk_lilo_v2_tight_calm_silent.mp4
  (672x1216, 10,0 dtk, video-only, audio -46,1 dB di-strip).
  LOLOS Gate 3: wajah TIDAK ADA di semua frame, beat lengkap
  dan tepat, background 0 vs 0,6 dtk identik, ketajaman BAGUS
  SEKALI (frame-0 660,9 -> 1009,7/1054,0), badan di frame QC
  terlihat tegak dan tenang (bahu rata, torso stabil).
  Penilaian gerak "ketawa sudah hilang atau belum" ada di
  Jendral — gerak hanya bisa dipastikan dengan menonton.
- QC: calm_qc_0/0,6/2/3,5/6,5/9,5.jpg, calm_qc_contact.jpg,
  calm_flick_check.jpg, calm_before_after.jpg, calm_dense_*.jpg.
- Belum di-upload / dicatat di sheet — menunggu putusan Jendral.
  Anggaran tes ini: image 0, video 1/6.

## Framing pilihan Jendral (13 Nov 2026, 01:13 WITA)
Jendral (tentang frame-0 LILO v2): "Yang seperti ini bagus, yang
kepotong cuma matanya aja" — framing yang dia mau: terpotong di
mulut, HANYA mata yang kepotong (bukan sampai leher). Crop ketat
sampai leher tadi kelewat sempit.
- Video mouth-cut + tenang diregenerasi dari frame-0 LILO v2
  (klausul kepala diam + gerak tenang). LOLOS Gate 3 sebagian:
  beat lengkap, background identik, ketajaman bagus (789,9 ->
  595,5/714,4), badan tenang. TAPI di 9,5 dtk matanya masuk
  SEDIKIT di tepi atas (dicek perbesar: mata bawah kelihatan,
  hidung + mulut senyum kelihatan) — drift naik saat peace sign
  masih membawa mata masuk walau kepala sudah diarahkan diam.
  Jadi framing terpotong-di-mulut TIDAK AMAN sendiri: drift
  video selalu menarik mata ke tepi atas di momen peace sign.
- Perbaikan FINAL (deterministik, tanpa generate ulang): crop
  atas video jadi 60 px (ffmpeg crop=668:1188:18:60, re-encode
  crf 18) — mata terbuang, mulut/hidung tetap kelihatan.
  File kirim: priscila_duduk_lilo_v2_mc_calm_crop_silent.mp4
  (668x1188, 10,0 dtk, video-only). LOLOS Gate 3: mata TIDAK
  ADA di semua frame (dicek perbesar frame 9,5 dtk: hanya hidung
  ujung + mulut senyum + dagu, tanpa mata), beat lengkap,
  background 0 vs 0,6 dtk identik, ketajaman TIDAK BERUBAH
  (575,1/719,0), badan tegak dan tenang.
- PELAJARAN (aturan baru): untuk framing terpotong-di-mulut,
  SELALU crop atas video jadi ~5% sebagai pengaman drift —
  mata dijamin tidak masuk walau video naik di momen akhir.
  QC Gate 3 WAJIB cek perbesar tepi atas frame 9,5 dtk.
- QC: mcc_qc_0/0,6/2/3,5/6,5/9,5.jpg, mcc_qc_contact.jpg,
  mcc_95_top.jpg, mcc_flick_check.jpg.
- Belum di-upload / dicatat di sheet — menunggu putusan Jendral.
  Anggaran tes ini: image 0, video 1/6.

## DISETUJUI Jendral (13 Nov 2026, 01:18 WITA)
Jendral: "Udah pas dan perfect" — video final
priscila_duduk_lilo_v2_mc_calm_crop_silent.mp4 DISETUJUI.
- Format duduk LILO (frame asli video referensi + Priscila +
  rambut diikat cepol + framing terpotong-di-mulut + gerak
  tenang) RESMI JADI RESEP — bukan lagi tes.
- Upload Cloudinary: https://res.cloudinary.com/dpllb7idh/video/upload/v1794503896/Priscila-Duduk-LILO-V2.mp4
  (public_id Priscila-Duduk-LILO-V2, 3.303.901 bytes, 10,0 dtk,
  668x1188).
- Dicatat di sheet tab "Video Fashion" baris 5, Status
  "Siap tayang" (terverifikasi baca ulang).
- Video Priscila lain (horizontal v1/v2/v3, vertikal, medium,
  karakter, duduk v1, LILO v2, tight, tight-calm) TETAP di
  disk, belum di-upload/dicatat — hanya yang disetujui ini
  yang dicatat.
