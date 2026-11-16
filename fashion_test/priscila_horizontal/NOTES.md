# Priscila Horizontal — model lama (Adelia)

Keputusan Jendral 12 Nov 2026, 22:38 WITA: "kita kembali kesana aja"
— balik ke video HORIZONTAL (resep lama yang dapat "Oke sekarang bagus").
Pilihan lewat widget: "Priscila horizontal, model lama".

## Produk
- NEWARRIVAL Priscila Coquette V Neck Fitted Top, maroon (SOLID maroon,
  tanpa polkadot), shop shopatbear.official (Bandung, 4.9), Rp147.911.
- Canonical: https://shopee.co.id/product/92254947/41461882745
- Referensi: ref_priscila_maroon.jpg (gal_18, maroon on-shoulder).
- Spesifikasi: solid dark maroon; V-neck + white scalloped lace;
  lengan puff pendek + shirring elastis, on-shoulder; ruched bust;
  lace band putih di bawah dada + pita hitam kecil + 2 ekor; hem lace
  putih; fitted, flare dikit di hem.

## Frame-0 (Gate 1 LOLOS percobaan pertama)
- Base: Adelia landscape tanpa tas
  (bedah_maroon_1111/media-generation-adelia-model-landscape-no-bag-0-...webp,
  2096x1184), swap HANYA atasan ke Priscila maroon.
- File: media-generation-frame0-priscila-horizontal-0-a18f042f-....webp
  (2096x1184). Detail semua cocok: warna, V lace, lengan puff
  on-shoulder, ruched bust, lace band + pita hitam, hem lace.
  Model faceless, kamar pink + kasur boneka kiri + pintu kayu kanan,
  tanpa tas.

## Video (Gate 3 LOLOS)
- File kirim: priscila_horizontal_v1_silent.mp4 (1280x720, 10,0 dtk,
  video-only, audio generator -53,6 dB di-strip).
- Ketajaman BAGUS: frame-0 399,2 -> frame video 2 dtk 653,6 —
  TIDAK perlu unsharp (video malah lebih tajam dari frame-0).
- Background 0 vs 0,6 dtk IDENTIK (freeze jalan, tidak ada kedip).
- Beat: pita di ~2 dtk, bahu 3,5 dtk, muter samping JELAS di 6,5 dtk,
  peace sign 9,5 dtk. Baju konsisten di semua frame.
  Cacat jujur: nyaris tidak ada — dagu ngintip dikit di 9,5 dtk
  (dalam toleransi).
- QC: h_qc_0/0,6/2/3,5/6,5/9,5.jpg, h_qc_contact.jpg,
  h_flick_check.jpg, h_before_after.jpg.
- Belum di-upload / dicatat di sheet — menunggu putusan Jendral.
- Anggaran: image 1/4, video 1/6.

## Video v2 — tes maju ke depan (Jendral, 12 Nov 2026, 22:42 WITA)
Keputusan: "Coba maju ke depan di Priscila" (pilihan widget).
Frame-0 yang SAMA dengan v1 (tidak di-generate ulang).
- File kirim: priscila_horizontal_v2_maju_silent.mp4 (1280x720,
  10,0 dtk, video-only, audio -49,1 dB di-strip).
- Gerakan BERHASIL (Gate 3 LOLOS): 0 dtk jarak awal, 1-4 dtk MAJU
  (di 3-3,5 dtk PALING DEKAT — dada memenuhi frame, pita + lace
  band + kain kelihatan close-up), 4-7 dtk MUNDUR, 6,5 dtk sudah
  jarak medium, 8 dtk kembali ke jarak awal (tangan di pinggang),
  9,5 dtk muter samping. Background BEKU di semua frame (0 vs 0,6
  dtk identik; pintu/kasur/boneka tidak melengkung). Baju konsisten.
  Wajah tidak pernah masuk frame (bahkan di titik terdekat).
- Cacat jujur: frame 2-3 dtk agak lembut (motion blur saat melangkah
  + close-up kain maroon polos; skor 168,8/123,8 vs frame-0 399,2)
  — tapi detail lace + pita tetap terbaca di close-up.
- QC: v2_qc_0/0,6/2/3/3,5/6,5/8/9,5.jpg, v2_qc_contact.jpg,
  v2_flick_check.jpg, v2_before_after.jpg (frame 3 dtk vs ref).
- Anggaran: image 0, video 1/6 (total tes ini).
- Status: menunggu putusan Jendral — jadikan resep baru atau tetap v1.

## Video v3 — start lebih dekat + 1 langkah + menunduk (Jendral, 12 Nov 2026, 22:47 WITA)
Koreksi Jendral: "karakter kita ini terlalu jauh, buat agak dekat
biar majunya cuma 1 langkah aja terus menuntuk sedikit kekamera
untuk memperlihatkan bajunya seperti video referensi".
- Frame-0 baru: frame0_priscila_horizontal_closer.jpg (1612x906,
  crop=1612:907:369:130 dari frame-0 v1 — ~1,3x lebih dekat; dagu
  terpotong di atas, hem lace + rok masih kelihatan).
- File kirim: priscila_horizontal_v3_closer_silent.mp4 (1280x720,
  10,0 dtk, video-only, audio -45,0 dB di-strip).
- Gerakan BERHASIL (Gate 3 LOLOS): 0 dtk start LEBIH DEKAT (badan
  memenuhi frame), 1-2 dtk 1 LANGKAH KECIL maju, 2-4 dtk MENUNDUK
  sedikit ke kamera (badan atas condong ke depan, tangan membuka
  di atas pita/lace — close-up detail), 4-6 dtk mundur ke jarak
  awal, 6,5-8 dtk tangan di pinggang, 9,5 dtk muter samping.
  Background BEKU (0 vs 0,6 dtk identik). Baju konsisten.
  Wajah tidak pernah masuk frame.
- Ketajaman: frame-0 491,2; frame video 0 dtk 552,6 (tajam);
  2,5 dtk 215,9; 3,5 dtk 122,9 — agak lembut saat menunduk
  (motion blur + close-up kain maroon polos), detail tetap terbaca.
- QC: v3_qc_0/0,6/1,5/2,5/3,5/5/6,5/8/9,5.jpg, v3_qc_contact.jpg,
  v3_flick_check.jpg, v3_before_after.jpg (frame 2,5 dtk vs ref).
- Anggaran: image 0 (crop ffmpeg), video 1/6.
- Status: menunggu putusan Jendral.
