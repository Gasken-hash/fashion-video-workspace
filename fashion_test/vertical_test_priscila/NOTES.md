# Tes vertikal pertama — Priscila Coquette V Neck Fitted Top (Maroon)
12 Nov 2026 ~18:47-18:49 WITA. Produk BARU (belum pernah dibuat videonya).
Keputusan format vertikal Jendral 18:46 WITA.

## Produk (Step 0)
- Nama: NEWARRIVAL Priscila Coquette V Neck Fitted Top Maroon Polkadot Black White Lace Blouse Ribbon Pink Yellow Atasan Wanita Korea Tali Pita Renda
- Harga: Rp147.911 (halaman produk 12 Nov 18:46 WITA)
- Toko: shopatbear.official, Bandung, rating 4.9
- Link kanonik: https://shopee.co.id/product/92254947/41461882745
- Varian dites: MAROON. Catatan penting: varian maroon itu POLOS (solid, tanpa polkadot) — yang berpolkadot cuma varian hitam/putih/pink. Judul listing "Maroon Polkadot" sedikit menyesatkan.
- Referensi: ref_priscila_maroon.jpg = gal_18.jpg (foto depan bersih, on-shoulder, tanpa tas)

## Detail produk asli (gal_18)
- Maroon solid gelap, TANPA polkadot
- Leher V dengan renda putih bergigi (scalloped) di tepi
- Lengan pendek puff cap, karet/shirring, nempel di bahu, dipakai on-shoulder (bisa juga off-shoulder = style ke-2, TIDAK dipakai)
- Dada tengah berkerut (ruched)
- Pita renda putih horizontal di bawah dada + pita hitam tipis kecil di tengah depan, 2 ekor tali menggantung
- Badan fitted, hem sedikit melebar, renda putih bergigi di hem bawah

## Foto dasar vertikal (Step 1) — BARU
- File: media-generation-base-vertical-no-bag-0-b5a9403c-a835-4074-a827-40d4753fd196.webp
- 1152x2048 (9:16), dari foto dasar landscape (reframe). Model + kamar pink sama,
  tanpa tas, faceless. Catatan: framing sekarang full-body sampai kaki (sepatu flat
  putih ikut kelihatan — baru, di base landscape kaki tidak kelihatan).

## Frame-0 (Step 2) — GATE 1 LOLOS percobaan pertama
- File: media-generation-frame0-priscila-maroon-vertica-0-d114da74-8839-46d3-b49b-81eaece5e3e0.webp
- Cek lawan gal_18: warna maroon cocok, tanpa polkadot, renda V cocok, lengan nempel
  di bahu, kerut dada ada, pita renda + pita hitam + ekor tali ada, hem + renda bawah
  cocok, fit fitted. Tidak ada bedah yang dibutuhkan (0x).

## Video (Step 6) — GATE 3 LOLOS
- File asli generate: media-generation-priscila-maroon-vertical-video-0-8cf7fc19-08b1-44ef-8246-12075683db92.mp4
- File diserahkan (audio di-strip): priscila_maroon_vertical_silent.mp4
- Spesifikasi terukur: 704x1248 (9:16 vertikal), 10,0 detik, video-only setelah strip.
  Audio bawaan generator: AAC mean -66,5 dB / max -34,4 dB (noise samar) — di-strip pakai ffmpeg -an.
- Frame QC 0 / 2 / 3,5 / 6,5 / 9,5 dtk (qc_*.jpg, qc_contact.jpg): detail produk
  KONSISTEN di semua frame — tidak ada polkadot yang muncul, tidak ada ruffle,
  tidak ada pita tambahan, lengan tetap di bahu, tidak ada tas. Beat: 2 dtk tangan
  ke pita, 3,5 dtk cubit pita, 6,5 dtk tangan kiri di pinggang + muter, 9,5 dtk
  kembali ke depan. Wajah ter-crop di semua frame, TIDAK ada dagu ngintip.
- Cacat jujur (minor): 6,5 dtk framing lebih dekat (medium shot) saat muter;
  9,5 dtk tangan kiri agak motion-blur saat kembali ke depan. Bukan cacat produk.

## Anggaran
- Image calls: 2/4 (base vertikal + frame-0, 0 bedah). Video: 1/6.

## Tes gaya referensi @eveyourmine_ — MEDIUM SHOT (12 Nov 2026, 19:15-19:17 WITA)
Produk sama: Priscila maroon. Keputusan Jendral: tampilan video kita ikut
video TikTok @eveyourmine_ "blouse fav akuu" (medium shot, kamera diam,
model diam di tempat, tangan bercerita) + aturan wajah baru (prioritas
faceless, dagu/mulut ngintip dikit BOLEH; mata/wajah penuh TIDAK BOLEH).
Frame-0 medium: frame0_priscila_medium.jpg — CROP murni dari frame-0 yang
sudah lolos Gate 1 (crop 704x1248 dari x=240,y=0, tanpa redraw). Gate 1
crop: LOLOS (semua detail baju utuh: maroon solid, lace V, lengan puff
di bahu, lace band + pita hitam, hem lace).
- v1 (media-generation-priscila-medium-shot-v1-0-83716986...mp4): GAGAL
  Gate 3 — DIBUANG, tidak dikirim. Wajah model keliatan PENUH (mata +
  senyum) di frame 2/3,5/6,5/9,5 dtk + model mundur dari kamera. Produknya
  sendiri benar, tapi aturan wajah dilanggar.
- v2 (media-generation-priscila-medium-shot-v2-0-cc563d6b...mp4,
  prompt ditegaskan: framing sama persis kayak foto, muka tidak pernah
  masuk frame, model tidak mundur): LOLOS Gate 1+3. Frame 0/2/3,5/6,5/
  9,5 dtk: detail baju konsisten, beat benar (pinggang → pita → bahu →
  hem → muter samping → pinggang → peace sign), framing medium shot
  stabil, dagu/mulut ngintip dikit di tepi atas (dalam toleransi baru).
  File kirim: priscila_medium_shot_v2_silent.mp4 (704x1248, 10,0 dtk,
  video-only, audio generator -48,8 dB di-strip). QC: ms2_qc_*.jpg,
  ms_before_after.jpg. Belum di-upload / dicatat di sheet — menunggu
  putusan Jendral.
- Anggaran tes ini: image 0 (crop ffmpeg saja), video 2/6 (v1 gagal + v2 lolos).

## Tes grade anti-"AI banget" (12 Nov 2026, 19:22 WITA)
Keluhan Jendral: background + pencahayaan referensi bagus, video kita
keliatan AI banget. Akar: foto dasar kita sendiri hasil generate AI —
dinding pink rata, kulit licin, cahaya merata tanpa bayangan; referensi
adalah video hp asli di kamar beneran. Tes: grade hangat + grain film
(eq contrast 1,06, saturation 1,08, colorbalance rs 0,06 / bs -0,05,
noise alls 9) pada v2 → priscila_medium_shot_v2_graded.mp4 (704x1248,
10,0 dtk) + grade_compare.jpg. Hasil: Jujur — cuma ngebantu DIKIT (lebih
hangat, kurang datar); dinding rata + kulit licinnya masih ketara. Grade
bukan obatnya; yang beneran ngaruh: (1) foto dasar gaya "foto hp candid"
atau (2) LILO (animasi foto asli seller). Menunggu putusan Jendral.

## Tes background kamar baru (12 Nov 2026, 19:40-19:45 WITA)
Jendral kirim gambar kamar (room_bg.jpg, 768x1365, dari Gemini — foto
gaya real: dinding pink, jendela + gorden hijau, kasur, boneka beruang):
"pakai background ini bagus sepertinya". Tes: base baru dari base vertikal
lama, ganti background doang → media-generation-base-vertical-room-v1-0-164e4725...webp.
Hasil base: kamar bener (gorden hijau, kasur, boneka, bantal, lantai kayu,
cahaya jendela + bayangan lembut), model sama, pose sama, rok + flats sama,
faceless. Catatan: atasan base ikut berubah jadi top maroon polkadot + pita
besar — tidak masalah karena swap mengganti atasannya, tapi swap harus
dipastikan bersih dari polkadot.
- Frame-0 swap Priscila maroon ke base baru: media-generation-frame0-priscila-room-v1-0-5fd64247...webp — LOLOS Gate 1 sekali jalan
  (maroon solid, tanpa polkadot, lace V, lengan puff di bahu, lace band +
  pita hitam, hem lace; kamar + model utuh).
- Frame-0 medium: frame0_priscila_room_medium.jpg (crop 704x1248 dari
  x=240,y=0, tanpa redraw).
- Video: media-generation-priscila-room-medium-v1-0-ae81283a...mp4 —
  LOLOS Gate 3. Frame 0/2/3,5/6,5/9,5: detail baju konsisten, beat benar
  (pinggang → pita → bahu → muter samping → pinggang → peace sign),
  framing medium shot stabil, gorden hijau + kasur keliatan di semua frame.
  Cacat jujur: 9,5 dtk mulut/senyum + dagu ngintip di tepi atas (mata TIDAK
  keliatan) — dalam toleransi aturan wajah baru, dilaporkan.
  File kirim: priscila_room_medium_silent.mp4 (704x1248, 10,0 dtk,
  video-only, audio generator -44,3 dB di-strip). QC: rm_qc_*.jpg,
  rm_before_after.jpg. Belum di-upload / dicatat di sheet — menunggu
  putusan Jendral apakah base kamar baru ini jadi base standar.
- Anggaran tes ini: image 2/4 (base baru + frame-0 swap, 0 bedah),
  video 1/6.

## Perbaikan komposisi kasur (12 Nov 2026, 19:46-19:55 WITA)
Koreksi Jendral: "kasurnya itu pas banget sama kaki orangnya, gk kayak
video kita ini aneh" — di referensi model berdiri nempel di kaki kasur,
kasur langsung di belakang betis; di video kita (base room v1) model
berdiri jauh di depan kasur dengan lantai kayu lebar di antaranya.
- Base room v2: GAGAL (kebablasan — model malah BERDIRI DI ATAS kasur,
  kaki tenggelam di selimut). Dibuang.
- Base room v3: media-generation-base-vertical-room-v2-... (nama file v2,
  isinya percobaan ke-3) — BENAR: model berdiri di lantai kayu, tumit
  hampir menyentuh tepi kasur, kasur langsung di belakang betis setinggi
  lutut. File: media-generation-base-vertical-room-v3-0-6741a0d2...webp.
- Frame-0 swap: media-generation-frame0-priscila-room-v3-0-546a7827...webp
  — LOLOS Gate 1 sekali jalan (maroon solid tanpa polkadot, semua detail
  baju benar, kasur nempel di belakang kaki).
- Frame-0 medium: frame0_priscila_room_v3_medium.jpg (crop 704x1248).
- Video: media-generation-priscila-room-v3-medium-0-d040d2f1...mp4 —
  LOLOS Gate 3. Kasur nempel di belakang pahanya di SEMUA frame, beat
  benar, framing stabil. Cacat jujur: dagu/mulut ngintip dikit di tepi
  atas (2-9,5 dtk, mata tidak keliatan) — dalam toleransi.
  File kirim: priscila_room_v3_medium_silent.mp4 (704x1248, 10,0 dtk,
  video-only, audio generator -47,6 dB di-strip). QC: rv3_qc_*.jpg,
  rv3_before_after.jpg. Belum di-upload / dicatat di sheet.
- Anggaran tes ini: image 3/4 (base v2 gagal + base v3 + frame-0 swap),
  video 1/6.

## Sisi kasur kelihatan (12 Nov 2026, 19:52-20:0x WITA)
Koreksi Jendral (balas foto base v3, kirim cover referensi): "bagian
samping kasurnya itu harus kelihatan seperti foto ini" — di referensi
kasur ada di samping kiri model dan keliatan sisi panjangnya (sisi kasur,
seprai, bantal di ujung); di base v3 kasur di tengah pas di belakang dia,
keliatan dari ujung kaki kasur.
- Base room v4: media-generation-base-vertical-room-v4-0-eafa9587...webp
  — BAGUS, komposisi yang diminta tercapai: kasur di kiri, sisi panjang
  keliatan (sisi kasur putih + seprai + boneka/bantal di ujung kiri),
  model nempel di sisi kasur, kaki di lantai kayu, gorden hijau + jendela
  + cahaya hangat utuh. Base v4 ini VALID sebagai foto dasar.
- Swap Priscila ke base v4: media-generation-frame0-priscila-room-v4-0-2f930676...webp
  — GAGAL Gate 1, DIBUANG: (1) komposisi kasur BALIK ke tengah (diambil
  dari ujung kaki, kayak v3), (2) ujung lengan ketambahan lace putih yang
  tidak ada di aslinya.
- Bedah 1 (frame-0 v4 + ref base v4 + ref seller): media-generation-frame0-priscila-room-v4-fix-0-235fa592...webp
  — GAGAL TOTAL: atasan balik jadi top polkadot base, kasur balik ke tengah.
- Bedah 2 (frame-0 v3 + ref base v4): media-generation-frame0-priscila-room-v4-fix2-0-5bcd4a22...webp
  — GAGAL: background sisi-kasur tercapai, TAPI atasan balik jadi top
  polkadot base lagi.
- POLA KEGAGALAN (pelajaran): kalau gambar base v4 (yang atasannya
  polkadot) ikut masuk ke prompt sebagai referensi, generator MENYALIN
  atasannya ke hasil, sekeras apa pun larangan "jangan copy atasannya".
  Swap atasan dan pindah komposisi kasur masing-masing JALAN sendiri,
  tapi digabung dalam satu generate gagal. Anggaran gambar pesan ini
  HABIS (4/4: base v4, swap v4, bedah 1, bedah 2) — video belum dibuat.
- RENCANA BERIKUTNYA (belum jalan): edit background SAJA pada frame-0 v3
  yang sudah benar (Priscila + kasur tengah), TANPA melewatkan gambar base
  v4 sebagai referensi (edit teks saja, seperti saat v3→v4 base yang
  berhasil) — supaya tidak ada atasan polkadot yang bisa disalin.
  Video v3 (kasur tengah, sudah lolos Gate 3) tetap jadi video terbaik
  yang sudah jadi.

## Bayangan hilang + sisi kasur (12 Nov 2026, 20:06-20:20 WITA)
Koreksi Jendral: "ada 1 detail yang hilang dari gambar kita itu,
bayangannya gk ada, coba kamu bandingkan karakter kita sama karakter
yang dari gambar referensi tiktok tadi". Perbandingan shadow_compare.jpg
(kiri referensi f_2, kanan video kita rv3_qc_2): di referensi cahaya
jendela dari kiri bersifat DIRECTIONAL — sisi badan yang jauh dari
jendela jatuh ke bayangan lembut, ada bayangan lembut badan di kasur,
bayangan di lipatan kain, dan bayangan kontak di bawah kaki; di gambar
kita cahayanya merata dari segala arah, tidak ada bayangan jatuh, tidak
ada gradasi gelap-terang di badan, karakter kelihatan nempel (tidak
membumi).
- Edit 1 (teks saja, frame-0 v3): media-generation-frame0-priscila-shadow-fix-0-77255ed1...webp
  — BERHASIL: cahaya hangat directional dari kiri (sinar jendela
  keliatan), bayangan lembut badan ke kanan di kasur + lantai, bayangan
  kontak di bawah kaki, shading di sisi kanan badan, lipatan baju ada
  bayangannya. Atasan + kamar utuh.
- Edit 2 (teks saja, pada hasil edit 1): media-generation-frame0-priscila-shadow-sidebed-0-54852232...webp
  — BERHASIL: kasur pindah ke kiri, sisi panjang keliatan (sisi kasur +
  seprai + boneka/bantal di ujung kiri), model nempel di sisi kasur,
  cahaya + bayangan dari edit 1 UTUH. Bukti: edit teks saja tanpa
  referensi bergambar TIDAK menularkan atasan (pelajaran dari kegagalan
  v4 kemarin).
- Frame-0 medium: frame0_priscila_shadow_sidebed_medium.jpg (crop
  704x1248 dari x=240,y=0).
- Video: media-generation-priscila-shadow-sidebed-v1-0-ac4f64dd...mp4 —
  LOLOS Gate 3. Cahaya hangat + bayangan lembut bertahan di semua frame
  (0/2/3,5/6,5/9,5), kasur sisi-kiri keliatan di semua frame, beat
  tangan ada (pinggang → bahu → pinggang → peace sign), framing medium
  shot stabil, dagu/mulut ngintip dikit (mata tidak keliatan, dalam
  toleransi). Cacat jujur: timing beat agak meleset (di 2 dtk tangan
  masih di sisi, belum menyentuh pita — beat jalan lebih cepat dari
  prompt, pola yang sudah dikenal). File kirim:
  priscila_shadow_sidebed_silent.mp4 (720x1280 — generator keluar di
  720p, tetap 9:16, 10,0 dtk, video-only, audio generator -40,5 dB
  di-strip). QC: ss_qc_*.jpg, ss_before_after.jpg, shadow_compare.jpg.
  Belum di-upload / dicatat di sheet.
- Anggaran tes ini: image 2/4 (edit bayangan + edit sisi kasur),
  video 1/6.

## Background kedip di detik awal (12 Nov 2026, 20:35-20:40 WITA)
Koreksi Jendral: "kedip gitu ya backgroundnya berubah di detik awal".
Bukti (flick_f_0/0,3/0,6/1,0/1,5/2,0 dari video v1): background LOMPAT
antara 0,3-0,6 dtk — di 0-0,3 dtk jendela di kiri jauh + gorden kiri,
di 0,6 dtk ke atas jendela pindah ke tengah di belakang kepala + gorden
pindah ke kanan. Setelah 0,6 dtk stabil sampai akhir. Ini "settle" scene
oleh generator, keluarga yang sama dengan frame-0 garble di pipeline PBN.
- Perbaikan: regenerate dengan klausul background-freeze eksplisit di
  prompt video ("background is completely frozen and identical to the
  photo in every single frame... nothing moves, shifts, or changes,
  especially in the first second").
- v2: media-generation-priscila-shadow-sidebed-v2-0-fe44c07c...mp4 —
  LOLOS Gate 3. Bukti (flick2_f_*): 0/0,3/0,6/1,0/1,5/2,0 dtk background
  IDENTIK (jendela kiri jauh, gorden kiri, kasur + boneka kiri bawah),
  tidak ada lompatan. Frame 3,5/6,5/9,5: baju konsisten, beat benar
  (sentuh pita di ~1 dtk — kali ini timing beat TEPAT), dagu/mulut
  ngintip dikit (mata tidak keliatan). File kirim:
  priscila_shadow_sidebed_v2_silent.mp4 (704x1248, 10,0 dtk, video-only,
  audio generator -48,6 dB di-strip). QC: flick2_*.jpg, ss2_qc_*.jpg,
  ss2_before_after.jpg. Belum di-upload / dicatat di sheet.
- Anggaran tes ini: image 0, video 1/6.
- Aturan baru di standar: Gate 3 wajib bandingkan frame 0 vs 0,6 dtk
  untuk lompatan background; prompt video wajib pakai klausul
  background-freeze.

## Kualitas menurun vs video horizontal lama (12 Nov 2026, 21:32-21:34 WITA)
Koreksi Jendral: "kok kualitasnya malah menurun ya, malah lebih bagus
video horizontal kita yang lama". Dicek dengan angka + frame, bukan tebak:
- Spesifikasi SAMA: horizontal lama 1248x704 @ 2,6-3,9 Mbps; vertikal
  baru 704x1248 @ 2,6-3,7 Mbps. Resolusi/bitrate bukan penyebabnya.
- Ketajaman (Laplacian variance, frame 2 dtk, makin besar makin tajam):
  HYLE horizontal 960; Adelia v1 VERTIKAL 812; Adelia v2 horizontal
  1086 — jadi format vertikal BUKAN penyebab: video vertikal Adelia v1
  juga tajam. Priscila vertikal full-body 187 (paling lembut), v2 medium
  384.
- Akar: frame-0 input TAJAM (691) tapi videonya keluar LEBIH LEMBUT
  (384, turun ~45%) — pelembutan terjadi di langkah generate video.
  Medium shot memperbesar efeknya karena model lebih besar di frame.
- Regen v3 dari frame-0 yang sama: 348 — TIDAK memperbaiki (bukan
  lotre per-generate). DIBUANG.
- Perbaikan yang JALAN: filter unsharp di editing (ffmpeg
  unsharp=5:5:0.8:5:5:0.4, crf 18) pada v2 → 597, dekat ke frame-0
  (691). File: priscila_shadow_sidebed_v2_sharp.mp4 (704x1248, 10,0 dtk,
  video-only). QC frame 0/6,5/9,5: tidak ada halo, tidak ada noise
  meledak di bayangan, lace + lipatan kain lebih tegas. Ini file kirim
  TERBARU. QC: quality_compare.jpg, quality_adelia_compare.jpg,
  quality_v2_v3_sharp.jpg, v2s_qc_*.jpg.
- Aturan baru: Gate 3 wajib bandingkan ketajaman frame video (2 dtk)
  lawan frame-0; kalau video keluar lembut, jangan regen membabi buta —
  pakai unsharp di editing sebagai langkah finishing.

## Karakter baru (Jendral, 12 Nov 2026, 22:14 WITA)
Jendral kirim foto: "pakai foto ini, ini foto karakter kita sendiri".
Foto karakter (Gemini, fotorealistis): cewek rambut hitam keriting,
kamar pink sendiri (poster, meja rias, kasur + boneka, rak baju),
baju gingham coklat + rok putih. Disimpan:
character_base.jpg (768x1376, dari
workspace/user/media_library/image/Gemini_Generated_Image_sap5qtsap5qtsap5.jpg).
- Swap Priscila maroon ke karakter ini: frame-0
  media-generation-frame0-priscila-character-0-a669f689-...webp
  (1168x2112) — LOLOS Gate 1 percobaan pertama: maroon solid,
  V-neck lace, lengan puff on-shoulder, ruched bust, lace band +
  pita hitam kecil + 2 ekor, hem lace; wajah/pose/rok/kamar utuh.
- Crop medium: frame0_priscila_character_medium.jpg (726x1292,
  crop=727:1292:245:502 — frame-0 keluar 1168x2112, koordinat crop
  harus diskala dari 768x1376).
- Video priscila_character_v1_silent.mp4 (720x1280, 10,0 dtk,
  video-only, audio -36,1 dB di-strip) — LOLOS Gate 3.
  Ketajaman BAGUS: frame-0 745,6 -> frame video 2 dtk 666,4
  (cuma turun ~11%, jauh lebih baik dari v2 lama 691->384) — TIDAK
  perlu unsharp. Background 0 vs 0,6 dtk IDENTIK (freeze jalan).
  Beat: pita di ~2 dtk, bahu 3,5 dtk, peace sign 9,5 dtk.
  Cacat jujur: (1) di 9,5 dtk mulut/senyum + dagu kelihatan agak
  banyak (mata tidak kelihatan, masih dalam toleransi);
  (2) muter sampingnya samar, di 6,5 dtk sudah balik depan.
  Belum di-upload / dicatat di sheet — menunggu putusan Jendral.
- Anggaran tes ini: image 1/4, video 1/6.
- Karakter ini MENGGANTIKAN base model Adelia untuk video-video
  berikutnya.
