# FLORA Vest Top One Set — MODE FULL BODY TEST (pertama)
Produk: b17_61, ID 1736227362728019067, FLORA Vest Top One Set (vest + celana cutbray highwaist, kancing gold).
Link: https://vt.tokopedia.com/t/ZS9fsPKSp8Hyu-b5Bgy/
Ref: tok_00.jpg (hitam, flat-lay, set lengkap) — vest tanpa lengan, kerah bulat, 5 kancing gold tengah + 2 saku flap (1 kancing gold tiap saku), hem peplum + slit tengah; celana hitam high-waist, cutbray lebar, lipatan tengah.

## Mode baru: Berdiri Full Body Vertikal (mode ke-4) — DITOLAK JENDRAL 15 Nov ~14:47 WITA
- Base baru: ~/workspace/fashion_test/bases/lala_berdiri_vertikal_fullbody_base.webp (1184x2096) — dibuat dari base berdiri vertikal Flow di-extend ke bawah (mulut sampai kaki, kaki telanjang di lantai kayu).
- Verdict Jendral: "jelek kalau gini, lebih bagus yang horizontal kalau setelan gini". Mode full body vertikal JANGAN dipakai untuk setelan; mode setelan = horizontal (sedang diklarifikasi: medium shot biasa atau full-body 16:9).
- FLORA vertikal sudah lolos Gate 1+3 tapi BUKAN patokan setelan.

## Frame-0
- v1 GAGAL Gate 1: kancing tengah cuma 3 (harus 5), celana kurang lebar flare-nya.
- v2 (surgical fix 1x) LOLOS Gate 1 (~97%): 5 kancing tengah + 2 saku = 7 gold total, flare cutbray jelas, lipatan tengah ada. File: media-generation-frame0-flora-fullbody-v2-0-1d398f4e-94da-4dd9-a9bb-a12f5feca59f.webp

## Video v1 — Gate 3 LOLOS (tapi Jendral bilang jelek)
- Final: flora_berdiri_fullbody_v1_upscale720.mp4 (720x1280, 10.0s, silent, 2.5 MB, ffprobe-verified)
- Beat jalan: tangan ke kancing (ujung jari) 2s → trace kolom kancing + cubit hem 3.5s → usap sisi celana 6.5s + putar badan ~45-60 derajat (kepala tetap depan) → peace sign 9.5s.
- Background 0 vs 0.6s IDENTIK (freeze lolos). Produk ~96-97% di semua frame (7 kancing lengkap di 3.5s). Bentuk dada bersih di semua frame. Faceless aman (9.5s top enlarged = mulut + dagu saja, tanpa mata/hidung).
- CACAT: (1) framing mengencang setelah 0.6s — kaki telanjang kepotong dari ~2s; (2) dekor dinding kanan drift — foto-foto kecil tambahan muncul di dinding dari 2s; (3) peace sign mendarat TINGGI di dada atas, ujung jari dekat dagu; (4) kalung emas base di kerah; (5) tangan sempat menutupi 1-2 kancing di 2s; (6) putaran badan overshoot ~45-60 derajat.
- Cloudinary: Flora-FullBody-V1 (v1794721843). Sheet Video Fashion No 43 "Siap tayang" (Harga kosong, link Tokopedia).

## Video v2 — MAJU-MUNDUR (Jendral, 15 Nov ~14:51 WITA: "pakai yang ini aja... maju dulu buat kasih liat bajunya terus mundur lagi, seperti video Flow")
- Gerakan: tangan di pinggang → MAJU (push-in, close-up vest di 3.5s, 7 kancing kelihatan tajam) → MUNDUR (full body lagi di 5s) → tangan di pinggang 6.5s → peace PIPI 9.5s. Maju-mundur JALAN (bentuknya push-in/pull-out kamera, efeknya sama seperti melangkah).
- Gate 3 LOLOS: produk ~96-97% semua frame, background 0 vs 0.6s beku, dada bersih (ujung jari saja, tanpa tekan telapak), maju-mundur jalan, final 720x1280 10.0s silent.
- PERINGATAN FACELESS: di video MENTAH, ending pipi narik wajah masuk — di 9.5s mentah mata kelihatan jelas (satu mata menatap kamera) + hidung + senyum. Top-crop 62px (drift guard standar) MENGHAPUS matanya — di video FINAL 9.5s cuma mulut + dagu (sudah dicek enlarged). Ini alasan top-crop WAJIB, jangan pernah di-skip di mode ini.
- CACAT LAIN: (1) kaki kepotong di pergelangan dari ~5s (set tetap utuh); (2) dekor dinding kanan drift — foto-foto kecil tambahan dari 2s; (3) peace pipi (rotasi — v1 dada tinggi, v2 pipi); (4) kalung emas base; (5) tangan sempat nutupi 1 kancing di 2s.
- Final: flora_berdiri_fullbody_v2_upscale720.mp4; Cloudinary Flora-FullBody-V2 (v1794725570); sheet No 44 "Siap tayang".

## V2 CACAT — PEACE 2x (Jendral, 15 Nov ~14:59 WITA)
- Jendral benar: peace ada 2x di v2 — peace ke-1 di ~7s (tangan kanan bentuk V di dada, saat tangan kiri di pinggang), peace ke-2 di ~8-9.5s (pipi, ending). Gate 3 Igris KELEWATAN karena cuma sample 6.5s (tangan blur, peace mulai terbentuk) dan 9.5s.
- Pelajaran: di mode full-body, Gate 3 WAJIB sample 7s + 8s juga (cek peace ganda), jangan cuma 0/2/3.5/6.5/9.5.
- Status sheet No 44 diubah dari "Siap tayang" jadi "Cacat - peace 2x, jangan tayang". Menunggu perintah Jendral apakah dibuat v3.

## Video v3 — MENUNDUK — GAGAL Gate 3 (Jendral, 15 Nov ~15:26 WITA: "suruh karakternya menunduk gitu ke kamera buat kasih liat bajunya")
- Gerakan: maju → menunduk (kepala nunduk ke kamera, tangan sentuh kancing) → mundur → peace pipi 1x.
- GAGAL: menunduk narik WAJAH PENUH masuk frame — di 5s dan 7s kedua mata kelihatan jelas + hidung + mulut, menunduk terus ~2 detik. Top-crop 62px TIDAK BISA menyelamatkan (wajah menempati 25% atas frame). Penyebab: klausul prompt "chin tilting slightly down" — kepala nunduk = mata masuk frame.
- Yang BERHASIL di v3: peace cuma 1x di pipi (klausul "peace hanya sekali, jari tidak boleh bentuk V sebelum ending" jalan — di 7s tidak ada V). Produk tetap ~96-97% (close-up 3.5s bagus).
- TIDAK di-upload, TIDAK dicatat sheet. Perbaikan yang diusulkan: v4 = badan condong ke depan, KEPALA TETAP TEGAK (dagu sedikit terangkat, bukan nunduk) — menunggu perintah Jendral.

## Video v4 — MAJU ALA REFERENSI MAROON — LOLOS Gate 3 (Jendral, 15 Nov ~15:27 WITA, kirim video referensi)
- Referensi: ref_maju_maroon.mp4 (1920x1080, 10.05s, atasan maroon polkadot + rok putih + tas hitam bahu kiri). Gerakan referensi: mulai medium shot → MAJU ke kamera sambil tangan naik ke dada (sentuh pita/kain, jari tersebar) → tangan turun usap hem → MUNDUR ke posisi awal, tangan di pinggang → full outfit. Wajah TIDAK PERNAH kelihatan (framing potong di dagu/leher, kepala tetap tegak).
- Gerakan v4 (ikut referensi): tangan di pinggang → maju, tangan naik ke dada (jari tersebar ringan di kancing/kain, tanpa tekan) → usap turun ke hem → mundur, tangan di pinggang → peace PIPI 1x (naik ~7s, ditahan sampai akhir).
- Gate 3 LOLOS: produk ~96-97% semua frame (7 kancing lengkap, close-up 3.5s tajam), background 0 vs 0.6s beku, dada bersih (tangan ringan, tidak ada tekan telapak, tidak melorot), faceless AMAN di semua frame (tanpa mata; ujung hidung sekilas di 7-9.5s mentah, dihapus top-crop — final 9.5s cuma mulut + dagu, dicek enlarged). Peace 1x SAJA (satu gerakan ditahan 7s→9.5s, bukan 2x).
- CACAT: (1) kaki kepotong di pergelangan dari ~5s (set tetap utuh); (2) dekor dinding kanan drift — foto-foto kecil tambahan dari 2s; (3) peace mulai agak awal (~7s, ditahan lama); (4) kalung emas base; (5) tangan sempat menutupi 1 kancing di 2s.
- Final: flora_berdiri_fullbody_v4_upscale720.mp4 (720x1280, 10.0s, silent, 2.6 MB); Cloudinary Flora-FullBody-V4 (v1794727777); sheet No 45 "Siap tayang" (URL sempat salah tulis versi v2, sudah diperbaiki + read-back).

## Video v5 — PUTAR KIRI+KANAN (percobaan 1) — GAGAL (sisi kanan hilang) (Jendral, 15 Nov ~15:33 WITA: "perlihatkan juga baju bagian kanan dan kirinya")
- Gerakan: maju → usap hem → putar kiri → balik depan → putar kanan → balik depan → mundur → peace pipi 1x.
- HASIL: putar KIRI jalan (5s, side view ~90 derajat, kepala menghadap kamera, tanpa wajah profil — sisi baju kelihatan bagus). Putar KANAN HILANG — generator langsung balik depan (6-6.5s) lalu peace; tidak ada frame sisi kanan di mana pun. Yang lain lolos: produk ~96-97%, dada bersih, background 0 vs 0.6s beku, peace 1x pipi (8s→9.5s), tanpa mata (9.5s cuma hidung + mulut — top-crop bisa hapus).
- TIDAK di-upload, TIDAK dicatat sheet.

## Video v6 — PUTAR KIRI+KANAN (percobaan 2, pakai HOLD + "kedua putaran WAJIB") — GAGAL (sisi kanan tetap hilang + wajah penuh di ending) (15 Nov ~15:40 WITA)
- Gerakan: maju → putar kiri + TAHAN → putar kanan + TAHAN → balik depan → mundur → peace pipi 1x.
- HASIL: putar kiri jalan lagi (5s, side view, kepala ikut menoleh profil tapi wajah terpotong di mulut — tanpa mata/hidung). Putar KANAN TETAP HILANG — generator cuma bikin SATU putaran lalu balik depan (6-7s) dan peace. PLUS: wajah PENUH masuk di ending — 8s dan 9.5s kedua mata + hidung + mulut tersenyum kelihatan jelas (kepala menoleh ke kamera saat peace). Top-crop 62px TIDAK BISA menyelamatkan (wajah makan ~20% atas frame).
- KESIMPULAN: generator meruntuhkan "putar kiri lalu putar kanan" jadi SATU putaran — 2 percobaan dengan 2 wording berbeda hasilnya sama. Opsi ke depan: (a) SATU putaran sapuan kontinu kiri → depan → kanan (satu instruksi putar, bukan dua); (b) satu sisi per video (v5 = sisi kiri, video lain = sisi kanan); (c) terima satu sisi saja. Menunggu keputusan Jendral.
- TIDAK di-upload, TIDAK dicatat sheet.

## Video v7 — SAPUAN KONTINU kiri → depan → kanan — GAGAL (tetap satu sisi) (Jendral, 15 Nov ~15:38 WITA: "mau")
- Gerakan: maju → SATU putaran sapuan mulus (sisi kiri → depan → sisi kanan) → balik depan → mundur → peace pipi 1x (kepala tegak, ala v4).
- HASIL: sapuan tetap cuma nunjukin SATU sisi — 5s tiga-perempat, 5.5-6s side view (sisi kiri, kepala ikut profil tapi wajah terpotong di mulut, tanpa mata), 6.5s sudah balik depan. Sisi kanan TIDAK PERNAH muncul. Tiga percobaan (v5, v6, v7) dengan tiga wording berbeda, hasilnya sama: generator cuma bikin SATU putaran ke satu sisi lalu balik.
- Ending v7: peace 1x pipi ✓ (mulai ~8.5s, ditahan sampai akhir), tapi mata kiri ngintip di tepi atas 9.5s mentah — top-crop 62px kemungkinan menghapusnya (seperti v2/v4), tapi belum dicek final karena video sudah gagal di putaran.
- KESIMPULAN: dua sisi dalam SATU video 10 detik TIDAK BISA dicapai generator ini (3x gagal). Opsi: (a) SATU SISI PER VIDEO — v5 sudah jadi video sisi kiri yang bersih (tinggal upload + catat), lalu buat v8 khusus sisi kanan (satu putaran saja, yang generator BISA); (b) terima satu sisi saja (v5). Menunggu keputusan Jendral.
- TIDAK di-upload, TIDAK dicatat sheet.

## Video v5 — SISI KIRI — LOLOS Gate 3, di-upload (Jendral, 15 Nov ~15:44 WITA: "oke gitu aja yang penting produknya identik")
- Gerakan: maju → putar kiri → balik depan → mundur → peace pipi 1x.
- Gate 3 LOLOS: produk ~96-97% semua frame (7 kancing lengkap), sisi KIRI kelihatan jelas di 5s (side view ~90 derajat, kepala menghadap kamera, tanpa wajah profil), background 0 vs 0.6s beku, dada bersih, peace 1x pipi (8s→9.5s), faceless AMAN di final (9.5s setelah top-crop cuma mulut + dagu, dicek enlarged — hidung di mentah terhapus crop).
- CACAT: kaki kepotong di pergelangan dari ~5s; dekor dinding kanan drift (foto-foto kecil tambahan dari 2s); kalung emas base.
- Final: flora_berdiri_fullbody_v5_upscale720.mp4 (720x1280, 10.0s, silent, 2.9 MB); Cloudinary Flora-FullBody-V5 (v1794728685); sheet No 46 "Siap tayang" (sisi kiri).

## Video v8 — SISI KANAN — LOLOS Gate 3 SETELAH TRIM, di-upload (15 Nov ~15:48 WITA)
- Gerakan: maju → putar kanan → balik depan → mundur → peace pipi 1x. Putaran kanan JALAN (5-5.5s, side view sisi kanan, kepala menghadap kamera, tanpa wajah profil) — satu-satunya video yang dapat sisi kanan (v9/v10 malah balik ke kiri lagi; kiri/kanan di prompt itu lotre, v8 1 dari 3).
- MASALAH: ending peace narik wajah PENUH masuk — 8s dan 9.5s mentah kedua mata + hidung + mulut tersenyum kelihatan jelas (kepala menoleh ke kamera saat peace, seperti v6). Top-crop TIDAK BISA menyelamatkan. Mata sudah ngintip di 7.4s; frame 7.0s masih bersih (mulut + dagu + hidung, tanpa mata).
- PERBAIKAN: video DIPOTONG di 7.0 detik (buang ending peace) — final 7.0s: maju → sisi kanan → balik depan → tangan di pinggang, tanpa peace. Final 6.9s dicek: mulut + dagu saja, tanpa mata/hidung. Produk tetap identik ~96-97%.
- Final: flora_berdiri_fullbody_v8_upscale720.mp4 (720x1280, 7.0s, silent, 2.2 MB); Cloudinary Flora-FullBody-V8 (v1794728911); sheet No 47 "Siap tayang" (sisi kanan, durasi 7).

## Video v11 — MIRROR SELFIE (base baru Jendral) — TES LOLOS Gate 1+3 (16 Nov ~02:00 WITA)
- Base baru Jendral 16 Nov 01:54 WITA: ~/workspace/fashion_test/bases/lala_berdiri_fullbody_mirror_base.jpg (1536x2752, vertikal) — model full-body DI DALAM cermin tinggi, pegang HP menutupi wajah (faceless built-in), kamar yang sama. Menggantikan base fullbody lama (webp) untuk setelan ke depan.
- Gerakan TES (Jendral: "gerakan sederhana aja"): HP tetap diangkat menutupi wajah sepanjang video → tangan kanan keluar saku, sentuh kancing vest (ujung jari) → usap turun ke hem peplum → putar badan ~30° ke samping (HP/kepala tetap menghadap cermin) → kembali depan. TANPA peace, TANPA maju-mundur.
- Frame-0: v1/v2/v3 GAGAL Gate 1 — semuanya cuma 4 kancing tengah (harus 5), walau posisi kancing sudah dieja eksplisit di prompt (v3). v4 LOLOS Gate 1 ~97% — trik yang jalan: pakai frame-0 FLORA LAMA v2 (yang sudah benar 7 kancing) sebagai referensi baju, bukan flat-lay tok_00. PELAJARAN: kalau flat-lay terus kehilangan detail hitungan, pakai frame-0 lama yang sudah benar sebagai referensi. (v3 juga ada cacat tambahan: selip kulit/perut kelihatan di slit — v4 bersih, vest menutup pinggang penuh.)
- Video v1: Gate 3 LOLOS ~97% — sentuh kancing 2s ✓ → usap hem 3.5s ✓ (tangan sempat menutupi kancing ke-5 sebentar = oklusi sementara, bukan cacat) → putar 30° 6.5s ✓ (sisi kelihatan, HP tetap menutupi wajah, kepala tidak ikut berputar) → kembali depan 9.5s ✓. Background 0 vs 0.6s beku, framing tidak berubah, kaki/sepatu putih utuh di semua frame, tanpa kulit/perut, tanpa wajah di semua frame (HP selalu menutupi wajah — faceless paling aman dari semua mode). Final: flora_mirror_v1_upscale720.mp4 (720x1280, 10.0s, silent, 3.2 MB; crop atas 60px + lanczos, final 9.5s dicek bersih).
- KESIMPULAN: base mirror JALAN untuk setelan dengan gerakan sederhana. HP di tangan = faceless terjamin, putar 30° jalan, framing stabil. Jendral 16 Nov 02:01 WITA: "cukup bagus" — tes DISETUJUI. Belum di-upload/dicatat; siap di-upload + dicatat sebagai versi FLORA mirror kapan saja Jendral mau.

## Video v12 — PROMPT JENDRAL (mirror selfie, step + putar kiri/kanan) — TES, Gate 3 LOLOS ~96% (16 Nov ~02:07 WITA)
- Prompt Jendral (verbatim, Inggris): mirror selfie realistis — (1) berdiri natural, HP menutupi wajah → (2) SATU langkah kecil maju ke cermin → (3) putar badan atas sedikit ke KIRI → (4) putar sedikit ke KANAN → (5) kembali depan, tahan pose. Tangan satunya tetap di saku celana. Kamera statis, tanpa zoom/cut, kamar + cermin dipertahankan, pencahayaan konsisten.
- Hasil: semua beat MENDARAT — langkah maju (framing mengencang di 2s) ✓ → putar kiri 3.5s ✓ (5s jadi side profile penuh, siluet samping kelihatan) → kembali depan 6.5s ✓ → tahan pose depan 8-9.5s ✓. HP SELALU menutupi wajah di semua frame (faceless aman). Produk ~96-97% (7 kancing lengkap di semua frame depan). Background konsisten (tanpa drift poster).
- CATATAN JUJUR: (1) Framing BERUBAH — mengencang setelah langkah maju (2-6.5s, kaki sedikit kepotong di tepi bawah), lalu melebar lagi di 8-9.5s. Ini bawaan dari beat "langkah maju" di prompt Jendral (sama seperti pelajaran horizontal v1: langkah maju = framing gerak). (2) Putar KIRI + KANAN runtuh jadi SATU sisi — ada sisi kiri jelas (5s), tapi TIDAK ADA sisi kanan yang jelas; dari kiri langsung balik depan. Sama seperti pelajaran mode-4 lama (2 putaran = 1 putaran). (3) Kaki sedikit kepotong di tengah video (framing dekat).
- Final: flora_mirror_jendral_prompt_v1_upscale720.mp4 (720x1280, 10.0s, silent, 3.5 MB; crop atas 60px + lanczos, final 9.5s dicek bersih). TES SAJA — belum di-upload/dicatat. Jendral 16 Nov 02:18 WITA: "bagus kok ini lumayan natural juga sesuai keinginan aku" — DISETUJUI. Framing yang berubah karena langkah maju DITERIMA Jendral sebagai natural (bukan cacat). Prompt Jendral ini sekarang RESEP BAKU mode mirror untuk setelan (ganti resep maju-mundur/peace mode-4 lama).

## Video v9 + v10 — SISI KIRI LAGI (tidak dipakai)
- v9 (prompt kepala diperkuat): ending membaik (cuma ujung mata ngintip di tepi atas 8-9.5s, top-crop bisa hapus) TAPI putaran malah ke KIRI lagi (5s, depan menghadap kiri). v10 (retry prompt sama): putaran KIRI lagi (5-5.5s), ending ujung mata ngintip di tepi atas 9.5s. Keduanya duplikat v5 — tidak di-upload, tidak dicatat.
- Pelajaran: arah putar kiri/kanan di prompt TIDAK deterministik — generator milih sisi sendiri (kiri 2 dari 3, kanan 1 dari 3). Kalau butuh sisi tertentu, generate dan cek arahnya, jangan andalkan kata "kiri/kanan" di prompt.
