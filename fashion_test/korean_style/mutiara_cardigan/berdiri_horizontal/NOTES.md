# MAMAMARA Cardigan Lis Full Mutiara — tes berdiri (14 Nov 2026)
Produk (sheet "Affiliate Cue" tab Korean Style, baris 3):
- MAMAMARA - Cardigan Wol Rajut Korean Style Lis Full Mutiara
- ID 18979450611, https://shopee.co.id/product/689122241/18979450611
- Foto asli: `../ref_mutiara_original.jpg` (800x800, flat-lay, tanpa bawahan).
- Visual: cardigan HITAM, rajut wol halus, leher bulat crew rib, lengan panjang lurus manset rib, cropped (pinggang), hem rib lurus, lis mutiara putih di KEDUA sisi bukaan depan, LIMA kancing mutiara besar, DUA saku tempel depan masing-masing lis mutiara di tepi atas + 1 kancing mutiara. Watermark @mamamara.co (tidak boleh ikut).
- Harga: sheet Rp129.900 vs live Rp179.900 (tidak cocok — video tidak terpengaruh).

## Tujuan tes
Jendral (14 Nov ~12:59 WITA): "coba ke produk yang lain dulu, aku mau liat apakah udah bisa reusable atau gak" — uji resep review berdiri v9 (Katie) di produk lain. Produk uji: MUTIARA (hitam, mutiara — kontras total dari Katie pink pita).

## Frame-0 (base Lala berdiri + ref Mutiara)
- Base: `~/workspace/fashion_test/bases/lala_berdiri_horizontal_base.jpg`.
- v1 GAGAL Gate 1 (framing): produk BENAR semua (hitam, lis mutiara, 5 kancing, 2 saku, celana hitam) TAPI ujung hidung kelihatan di tepi atas.
- v2 (edit SEGAR + klausul "top of the frame cuts BELOW her nose, at her mouth and chin — nose NOT visible at all") LOLOS Gate 1: produk benar + framing mulut/dagu, tanpa hidung. File: `media-generation-frame0-mutiara-berdiri-v2-0-d7dbf942-79ed-4fb7-8b39-df10573cc9fe.webp` (2112x1168, ketajaman 161.0).
- Bawahan: foto asli hanya atasan → celana HITAM drawstring (warna ngikutin atasan hitam, per aturan bawah).

## Video v1 — resep v9 (review + negatif prompt + tag) — Gate 3 LOLOS (standar terkalibrasi)
- File: `mutiara_berdiri_v1_upscale720.mp4` (1280x720, 10.0 dtk, bisu). Pre-upscale: `mutiara_berdiri_v1_silent.mp4` (1168x640).
- Prompt: sama seperti v9 Katie, deskripsi produk diganti Mutiara + beat gosok dada disesuaikan (telusuri lis mutiara dengan ujung jari).
- Ketajaman: frame-0 161.0 → video 157.4–368.2 (≥ frame-0, tanpa unsharp).
- Background 0 vs 0.6 dtk IDENTIK ✓. Framing stabil, tidak ada mundur ✓. Kepala hadap depan saat muter ✓ (muter ~30°, pita depan tetap kelihatan).
- Wajah: TIDAK ADA wajah penuh + mata di semua frame. Satu-satunya momen wajah = hidung sekilas di ~2 dtk (sama seperti v9 Katie yang DISETUJUI Jendral) — DITOLERANSI per standar terkalibrasi.
- Gerakan review jalan: condong lihat kerah 2 dtk → gosok dada + telusuri lis mutiara 3.5 dtk → muter samping 6.5–8 dtk → sentuh hem 9.5 dtk.
- Cacat jujur: (1) hidung sekilas di ~2 dtk (transient, toleransi kalibrasi); (2) boneka kaktus hijau muncul di kasur dari ~3.5 dtk (drift background minor — struktur kamar identik); (3) kalung emas dari base kelihatan di kerah (artefak base, sama seperti video Katie); (4) 1 kancing mutiara ketutup tangan sesaat di 0.6 dtk + kancing bawah ketutup tangan di 9.5 dtk (transient).
- Status: MENUNGGU penilaian Jendral (apakah resep reusable). BELUM diupload ke Cloudinary, BELUM dicatat di sheet.

## Video v2 — pose akhir FINGER HEART 🫰 (14 Nov ~13:25 WITA)
- Jendral (13:18 WITA): "Pose akhirnya aku mau bikin gaya 🫰 atau gini ✌️, bisa gak?" — dicoba finger heart dulu (disebut pertama). Peace sign ✌️ jadi cadangan.
- Perubahan dari v1: hanya akhir video (2 dtk terakhir) — tangan kanan naik ke dada bikin finger heart kecil (jempol + telunjuk bersilang), tangan kiri di pinggang. Finger heart di level dada, JAUH di bawah dagu, tidak pernah dekat wajah (pelajaran dari v1 berdiri: peace sign dekat pipi bikin wajah masuk).
- File: `mutiara_berdiri_v2_upscale720.mp4` (1280x720, 10.0 dtk, bisu). Pre-upscale: `mutiara_berdiri_v2_silent.mp4` (1168x640). Frame-0 sama dengan v1 (v2, sudah lolos Gate 1).
- Ketajaman: frame-0 161.0 → video 229.1–379.6 (jauh lebih tajam, tanpa unsharp).
- Background 0 vs 0.6 dtk IDENTIK ✓. Framing stabil, tidak ada mundur ✓. Kepala hadap depan saat muter ✓.
- Finger heart: JALAN — gesturnya benar dan jelas (jempol + telunjuk bersilang) di 8 + 9.5 dtk, tangan kiri di pinggang. Tidak menarik wajah masuk seperti peace sign di pipi.
- Wajah (standar terkalibrasi): TIDAK ADA mata + TIDAK ADA wajah penuh di semua frame. Hidung kelihatan di 2, 8, 9.5 dtk (framing lebih dekat dari frame-0 sepanjang video) — tanpa mata. Dinilai LOLOS per standar terkalibrasi (seperti v9), TAPI hidung di akhir (8-9.5 dtk) lebih menetap dari v9 — diserahkan ke penilaian Jendral.
- Cacat jujur: (1) hidung kelihatan di 2/8/9.5 dtk, tanpa mata; (2) framing lebih dekat dari frame-0 sepanjang video; (3) boneka kaktus hijau muncul di kasur dari ~3.5 dtk (drift background kecil); (4) kalung emas dari base kelihatan di kerah.
- Status: MENUNGGU penilaian Jendral. v1 tetap jadi cadangan (akhir tangan di hem). BELUM diupload ke Cloudinary, BELUM dicatat di sheet.

## Video v3 — pose akhir PEACE SIGN ✌️ (14 Nov ~13:30 WITA)
- Jendral (13:25 WITA): "jujur ini bagus coba yang peace sign lagi" — v2 finger heart DISETUJUI ("bagus"), sekarang dicoba peace sign sebagai pembanding.
- Perubahan dari v2: hanya akhir video — tangan kanan naik ke dada bikin peace sign V, tangan kiri di pinggang. Peace sign di level dada, JAUH di bawah dagu (bukan dekat pipi seperti v1 yang gagal).
- File: `mutiara_berdiri_v3_upscale720.mp4` (1280x720, 10.0 dtk, bisu). Pre-upscale: `mutiara_berdiri_v3_silent.mp4` (1168x640). Frame-0 sama dengan v1/v2 (v2, sudah lolos Gate 1).
- Ketajaman: frame-0 161.0 → video 163.0–363.5 (≥ frame-0, tanpa unsharp).
- Background 0 vs 0.6 dtk IDENTIK ✓. Framing stabil, tidak ada mundur ✓. Kepala hadap depan saat muter ✓.
- Peace sign: JALAN — gestur V jelas di 9.5 dtk, tangan kiri di pinggang.
- Wajah: 0.6–8 dtk BERSIH (cuma mulut/dagu). TAPI di 9.5 dtk hidung + SENYUM kelihatan (kepala menunduk sedikit ke arah tangan, framing mengetat) — tanpa mata, tanpa wajah penuh. Ini masalah yang SAMA seperti v1 berdiri (peace sign narik wajah masuk di akhir), walau lebih ringan (v1: wajah penuh + mata; v3: hidung + senyum).
- Perbandingan: v2 finger heart lebih bersih di akhir (cuma hidung, mulut netral); v3 peace sign lebih ekspresif tapi hidung + senyum kelihatan di akhir.
- Cacat jujur: (1) hidung + senyum di 9.5 dtk; (2) boneka kaktus hijau muncul di kasur dari ~3.5 dtk; (3) kalung emas dari base kelihatan di kerah.
- Status: MENUNGGU pilihan Jendral — v2 (finger heart) vs v3 (peace sign). BELUM diupload ke Cloudinary, BELUM dicatat di sheet.

## Kalibrasi wajah (Jendral, 14 Nov 13:31 WITA)
- "Gakpapa hidung kelihatan yang penting gak fullface gitu" — hidung kelihatan (termasuk hidung + senyum di akhir) DITERIMA; yang tidak boleh = wajah penuh. Berlaku untuk semua video berdiri ke depan. v2 dan v3 sama-sama lolos di bawah aturan ini.
- Pilihan final Mutiara (v2 finger heart vs v3 peace sign) masih menunggu Jendral.

## Final — KEDUA video dipakai, dirotasi (Jendral, 14 Nov 13:32 WITA)
- "Pakai keduanya rotasi aja biar gak monoton" — v2 (finger heart) + v3 (peace sign) keduanya FINAL.
- Cloudinary: `Mutiara-Berdiri-V2` (https://res.cloudinary.com/dpllb7idh/video/upload/v1794634353/Mutiara-Berdiri-V2.mp4) + `Mutiara-Berdiri-V3` (https://res.cloudinary.com/dpllb7idh/video/upload/v1794634355/Mutiara-Berdiri-V3.mp4).
- Sheet "Video Fashion": No 26 (V2) + No 27 (V3), Harga 179900 (live, sama seperti baris duduk No 6), Status "Siap tayang" — sudah read-back terverifikasi.
- Aturan ke depan: pose akhir video berdiri dirotasi finger heart ↔ peace sign tiap video, biar gak monoton.
