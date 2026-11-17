# Skill: Video Fashion di Google Flow (Frames-to-Video)

Buat video fashion TikTok (karakter Lala, @lala.coquette) dengan Google Flow.
Pola kerja: **frame-0 digenerate dulu oleh AI sendiri (generator gambar), lalu frame-0 itu dilempar ke Flow sebagai gambar awal (Frames-to-Video) untuk dianimasikan jadi video 10 detik.**
Flow TIDAK bikin gambar dari nol — dia nerusin gerakan dari frame-0 yang sudah benar.
Alasan: frame-0 adalah KONTROL yang mengunci produk agar identik dengan foto seller (minimal 95%). Tanpa frame-0, generator video membuat keputusannya sendiri dan produk bisa meleset (sudah terbukti gagal di tes tanpa frame-0, b17_50).

Skill ini melengkapi (bukan menggantikan) skill `fashion_video_tutorial` — semua aturan produk, Gate 1, Gate 3, dan rotasi di sana TETAP berlaku. Yang baru di sini hanya: cara memakai Flow sebagai generator video.

---

## 1. Foto jangkar (base) — pakai ini, jangan bikin base baru

Ada 7 foto jangkar. Unduh dari link Cloudinary di bawah (sudah terverifikasi bisa dibuka), atau pakai file lokal kalau ada di mesin. **Versi yang berlaku: file `*_cahaya.jpg` (17 Nov 2026)** — komposisi sama dengan base lama, ditambah sinar matahari sore hangat dari jendela kiri, dinding semua base cream hangat (keputusan Jendral 17 Nov 2026).

| Mode | File lokal | Link Cloudinary |
|---|---|---|
| Duduk — prop TAS | `bases/base_pita_v3_tas_cahaya.jpg` (1168x2112) | https://res.cloudinary.com/dpllb7idh/image/upload/v1794890098/base_pita_v3_tas_cahaya.jpg |
| Duduk — prop KACAMATA | `bases/base_pita_v3_kacamata_cahaya.jpg` (1168x2112) | https://res.cloudinary.com/dpllb7idh/image/upload/v1794890101/base_pita_v3_kacamata_cahaya.jpg |
| Duduk — prop TUMBLER | `bases/base_pita_v3_tumbler_cahaya.jpg` (1168x2112) | https://res.cloudinary.com/dpllb7idh/image/upload/v1794890102/base_pita_v3_tumbler_cahaya.jpg |
| Berdiri vertikal | `bases/lala_berdiri_vertikal_flow_base_cahaya.jpg` (1184x2096) | https://res.cloudinary.com/dpllb7idh/image/upload/v1794890103/lala_berdiri_vertikal_flow_base_cahaya.jpg |
| Berdiri horizontal v2 | `bases/lala_berdiri_horizontal_base_v2_cahaya.jpg` (2112x1168) | https://res.cloudinary.com/dpllb7idh/image/upload/v1794890104/lala_berdiri_horizontal_base_v2_cahaya.jpg |
| Mirror selfie (setelan + dress) — tangan di SAKU | `bases/lala_berdiri_fullbody_mirror_base_cahaya.jpg` (1168x2112) | https://res.cloudinary.com/dpllb7idh/image/upload/v1794890105/lala_berdiri_fullbody_mirror_base_cahaya.jpg |
| Mirror selfie (setelan + dress) — tangan SANTAI | `bases/lala_berdiri_fullbody_mirror_base_tangan_santai_cahaya.jpg` (1168x2112) | https://res.cloudinary.com/dpllb7idh/image/upload/v1794890106/lala_berdiri_fullbody_mirror_base_tangan_santai_cahaya.jpg |

Catatan base:
- Duduk: model duduk, dinding cream hangat, kasur di samping, sinar matahari sore hangat dari jendela kiri. Prop lantai dirotasi: tas → kacamata → tumbler → tas (lihat bagian 8).
- Berdiri vertikal: model berdiri, medium shot, kamar krem.
- Horizontal v2: model berdiri, kamar + CERMIN TINGGI di dinding kiri. Cermin memantulkan PINTU, model TIDAK terpantul. JANGAN pakai base horizontal v1 (tanpa cermin).
- Mirror selfie: model full-body DI DALAM cermin lengkung tinggi, HP menutupi wajah (faceless built-in). Untuk SETELAN dan DRESS. Ada DUA base mirror: **tangan di saku** (pakai kalau setelan ADA saku) dan **tangan santai** (pakai kalau setelan TANPA saku — celana pendek elastis, rok, piyama, dress). Pilih base SESUAI foto seller SEBELUM generate frame-0 (lihat ATURAN SAKU di bagian 6).

---

## 2. Google Flow — akun, kredit, harga

- Proyek: buka flow.google.com dengan akun sendiri (proyek Flow itu per akun, bukan proyek bersama).
- Akun: login pakai akun email Google MASING-MASING (akun sendiri). JANGAN login pakai akun/email orang lain — tidak akan bisa. Sheet pencatatan TETAP SAMA untuk semua orang (spreadsheet "Stok Video Reels Pure By Nature", tab "Video Fashion" + "Antrian Link").
- Saldo: **50 kredit**, refresh tiap hari jam **20:14 WITA**.
- Harga per 1 video (1x generate = 1 video; output x2/x3/x4 = bayar kelipatan):
  - **Omni 1.1 Flash**: 360p/8dtk = 6 | 720p/8dtk = 12 | **720p/10dtk = 15**
  - Omni 1.2 Flash: 360p/8dtk = 8 | 720p/8dtk = 24
  - Veo 3.1 Lite: 720p/8dtk = 10
- **Pakai Omni 1.1 Flash, 720p, 10 detik, output x1 = 15 kredit/video.** Dengan 50 kredit/hari = **3 video/hari** (45 kredit, sisa 5).
- **Omni 1.1 TUTUP 5 Des 2026** (label "Akan dihentikan pada 5 Des" di Flow). Setelah itu yang tinggal Omni 1.2 + Veo Lite.
- Peringatan "Poin tidak cukup": muncul kalau saldo tersisa di bawah 15 kredit. Kalau generasi sudah jalan (progress terlihat), biarkan selesai — videonya tetap jadi dan bisa diunduh. Jangan beli kredit, jangan ubah pengaturan.
- Flow TIDAK menampilkan sisa saldo yang persis di semua layar. Hitung manual: saldo awal 50 dikurangi 15 per video.
- **JANGAN PERNAH generate video langsung dari foto seller tanpa frame-0.** Sudah terbukti gagal (b17_50).

---

## 3. Alur produksi (8 langkah)

**ATURAN BATCH — WAJIB, JANGAN DILANGGAR: generate frame-0 untuk SEMUA 3 produk dulu (sekaligus, dalam satu batch gambar), Gate 1 satu per satu, BARU buka Flow sekali dan generate 3 videonya berurutan. JANGAN pola 1 gambar → 1 video → 1 gambar → 1 video. Alasannya: sesi Flow gampang logout dan kredit terbatas (3 video/hari) — kalau gambar produk sudah siap semua, begitu Flow dibuka langsung gas 3 video tanpa jeda, tanpa bolak-balik.**

0. **Identifikasi produk.** Sebutkan balik nama produk + linknya ke pengguna (konfirmasi match). Foto produk HARUS dari link persis yang pengguna kirim — jangan substitusi dari marketplace lain.
1. **Ambil galeri foto seller.** Utamakan cara non-browser dulu (curl + og_info / curl-cffi untuk Tokopedia). Foto referensi = foto produk bersih PERTAMA yang benar-benar menggambarkan produk sesuai nama (bukan sekadar foto bersih pertama; untuk listing multi-desain, cocokkan motifnya; kalau tidak ada yang jelas cocok, tandai RAGU — jangan nebak). Lewati infografik/size chart.
2. **Generate frame-0 untuk SEMUA produk hari itu (3 produk = 3 frame-0, sekaligus dalam satu batch gambar)** (generator gambar AI sendiri, BUKAN Flow). Canvas = foto jangkar (base) sesuai mode. Referensi = foto seller. Ganti HANYA bajunya — sisanya jangan di-redraw. Tulis bentuk dengan kata geometri + larangan eksplisit (lihat bagian 4).
3. **Gate 1 — untuk SETIAP frame-0** — bandingkan frame-0 dengan foto seller, detail per detail. Produk harus **identik minimal 95%**: warna, motif (jumlah/posisi), kerah, lengan, kancing (jumlah/ukuran/posisi), resleting, hem, fit. Kalau ragu sudah 95% atau belum, video TIDAK dibuat. Kalau frame-0 gagal, perbaiki dengan **fresh re-edit** (bukan edit bedah pada frame-0 yang gagal — sudah terbukti edit bedah bisa mengembalikan foto seller itu sendiri). Kalau 2x fresh re-edit gagal, fallback = crop faceless foto asli seller.
4. **Generate video di Flow — SEKALI buka, 3 video berurutan** (bagian 5). Frame-0 sebagai gambar awal (Frames-to-Video). Model Omni 1.1 Flash, 720p, 10 detik, x1. Prompt gerakan sesuai mode (bagian 6). **JANGAN buka Flow sebelum SEMUA frame-0 batch hari itu selesai + lolos Gate 1.**
5. **Gate 3** — cek frame video di 0 / 0,6 / 2 / 3,5 / 6,5 / 9,5 detik + background freeze (0 vs 0,6) + ketajaman vs frame-0 + bentuk dada + faceless (bagian 7). Video yang mengubah detail produk di tengah jalan = GAGAL walau frame-0 lolos.
6. **Post-process** (bagian 8): crop atas sebagai drift guard, buang audio, verifikasi final 9,5 detik faceless.
7. **Upload + catat OTOMATIS** (bagian 9): upload ke Cloudinary + catat ke sheet "Video Fashion" ("Siap tayang") + update "Antrian Link" jadi "Selesai". Langsung, tanpa tanya persetujuan dulu.

---

## 4. Frame-0 — cara generate + aturan prompt

Frame-0 digenerate dengan generator gambar AI sendiri (bukan Flow). Kirim 2 gambar: (1) foto jangkar sebagai canvas, (2) foto seller sebagai referensi, plus teks prompt.

Rumus prompt frame-0:
- "Edit this photo: keep the woman, her pose, the bedroom/background, the framing and everything exactly the same, only change her top to the [DESKRIPSI PRODUK] from the reference photo."
- Deskripsi produk pakai kata GEOMETRI + LARANGAN EKSPLISIT, contoh: "EXACTLY 5 small white buttons down the center front", "the silver zipper is FULLY CLOSED and zipped all the way up to the collar, the slider sits at the very top just below the collar, both front panels meet completely, NO bare skin is visible, NO cleavage".
- Selalu sebutkan bawahan yang dipakai (ikuti foto seller; kalau foto cuma atasan, pakai rotasi rok — bagian 8).
- Selalu sebutkan: "Do NOT add the [tas/topi/dll] from the reference photo, it is only styling" kalau ada properti styling di foto seller.
- Selalu sebutkan framing faceless: "The framing is a medium shot cut at the mouth, her face is not shown, only mouth and chin at the top edge."
- Untuk horizontal: "The tall arched mirror on the left wall reflects only the door, never the model."
- Untuk mirror: HP menutupi wajah sepanjang waktu.

Aturan hitungan:
- Kalau jumlah detail (kancing, pita, motif) diragukan, CROP + PERBESAR foto seller dulu sebelum menilai frame-0.
- Kalau frame-0 kehilangan detail hitungan berulang kali, pakai frame-0 LAMA yang sudah benar sebagai referensi garmen (bukan flat-lay seller).

---

## 5. Generate video di Flow — langkah demi langkah

1. Buka flow.google.com. Pastikan login dengan akun email Google kamu sendiri. JANGAN login pakai akun/email orang lain.
2. Pilih mode **Frames to Video** (bukan Text to Video). Unggah frame-0 sebagai gambar awal.
3. Atur: model **Omni 1.1 Flash** | resolusi **720p** | durasi **10 detik** | output **x1** | aspect ratio sesuai mode:
   - Duduk = **9:16 vertikal**
   - Berdiri vertikal = **9:16 vertikal**
   - Horizontal = **16:9**
   - Mirror selfie = **9:16 vertikal**
4. Masukkan prompt gerakan sesuai mode (bagian 6). Prompt ditulis dalam bahasa Inggris, natural, dan SELALU mengandung: kamera completely static (no zoom, no cuts), wajah tidak pernah terlihat (framing cut at the mouth), background beku.
5. Generate. Tunggu sampai selesai. JANGAN generate ulang kalau hasilnya sudah jadi — 1 video per produk per mode.
6. Unduh videonya. Flow memberi video 720p native (1280x720 atau 720x1280) **dengan audio AAC** — audionya dibuang di post-process.
7. Catat: 15 kredit terpakai per video. Sisa saldo = 50 − (15 × jumlah video hari ini).

Catatan:
- Kalau muncul "Gagal memuat adegan" di halaman edit tapi preview dan timeline video tetap jalan + unduhan berhasil, itu BUKAN kegagalan — lanjutkan.
- Kalau muncul "Poin tidak cukup" saat submit tapi generasi sudah mulai (progress terlihat), tunggu sampai selesai — videonya tetap jadi.

---

## 6. Prompt gerakan per mode (untuk Flow)

Tulis prompt dalam bahasa Inggris. Sesuaikan nama produk dan detailnya. Klausul yang dicetak tebal WAJIB ada di setiap prompt.

### Duduk (Set A–E — pilih/adaptasi sesuai ciri produk)
Pilih set gerakan dari ciri produk (bukan urutan tetap):
- Pita/kancing depan → sentuh pita/kancing. Manset flare → angkat manset. Hem scalloped/renda → cubit/telusuri hem. Leher V/renda → sentuh leher. Rajut tebal → usap dada/lengan (ujung jari). Fit ketat/pinggang → tangan di pinggang. Tali pita → sentuh tali.
- Set A: hip/hair → neckline → chest (spread, fingertips only) → hem/skirt → lap → slight torso turn → peace sign.
- Set B: hair → lift one cuff → touch top bow/button → pinch hem → skirt → lap → peace sign.
- Set C: shoulders → chest → waist/hem → skirt → slow side turn → peace sign + small wave.
- Set D: one hand stays on hip the whole time; other hand: neckline → bow → hem → cuff → lap → peace sign.
- Set E: hands crossed on lap → rise to neckline → spread over chest (fingertips on buttons/features, never flat palms) → trace hem → hands on skirt → slow side turn → peace sign.
- Template prompt (Set B, contoh Lunelly): "A woman sitting in her bedroom, calm, only her hands move. She touches her hair, then lifts one short sleeve cuff, then touches the white ribbon bow at her neck with her fingertips, then pinches the lace hem of her maroon top, then rests her hands on her lap, then raises one hand and makes a single peace sign at chest level, well below her chin, and holds it until the end. **The camera is completely static, no zoom, no cuts. She stays sitting the whole time, her head stays upright and never bows down. Her face is never shown, the framing stays cut at her mouth. The background is frozen.**"
- Tambahkan klausul kepala tegak di SEMUA prompt duduk: "head stays upright the whole time, chin slightly raised, NEVER bows her head down and NEVER looks down at her hands, gaze stays forward, framing stays cut at the mouth in every frame".
- Ending: SATU peace sign di level dada, jauh di bawah dagu. (Set C boleh peace di ~8 detik + wave di 9,5 detik.)

### Berdiri vertikal (Set F)
Urutan: tangan kanan di pinggang → kedua tangan ke kerah/pita → tangan terbuka lebar di dada atas (ujung jari saja) → kedua tangan ke hem peplum → usap sisi rok → putar badan pelan ~30-45 derajat (kepala TETAP menghadap kamera) → balik depan, kedua tangan di pinggang → tangan santai → ending peace sign di level dada.
- Template prompt: "A woman standing in her bedroom. She starts with her hands on her hips, then touches the collar and ribbon ties of her [produk] with her fingertips, then spreads her fingertips lightly over her chest, then traces the peplum hem, then rests her hands on the sides of her skirt, then slowly turns her body about 30 degrees to the side while keeping her head facing the camera, then returns to face the camera, relaxes her arms, and raises one hand to make a single peace sign at chest level, well below her chin, holding it until the end. **The camera is completely static, no zoom, no cuts. Her face is never shown, the framing stays cut at her mouth. The background is frozen. Bust stays naturally high and lifted, no sagging/drooping/flattening. Never press flat, never spread palms over chest.**"
- Peace sign dirotasi antar video: pipi ↔ dada. Satu video = SATU peace sign saja.
- PERINGATAN (temuan 16 Nov 2026): Flow cenderung membuat putaran jadi ~90 derajat profil (kepala ikut mutar) padahal prompt minta 30 derajat. Kalau hasil putarannya profil penuh tapi wajah HANYA profil (bukan full face, mata tidak jelas) dan kepala tidak menunduk, masih diterima borderline. Kalau wajah penuh kelihatan = GAGAL.

### Berdiri horizontal (resep "review outfit")
Resep: TETAP berdiri di tempat (TANPA melangkah maju), condongkan badan sedikit ke depan, GOSOK LEMBUT dan perlahan dengan kedua tangan di dada (ujung jari menyentuh kain, tidak menekan keras, tidak cepat), kembali ke posisi awal, putar badan perlahan ~30 derajat ke samping + tarik baju di perut, kepala TETAP menghadap kamera dan tidak pernah menunduk, tanpa voice. Kamera COMPLETELY STATIC. Putar penuh 90 derajat DILARANG. Poster dinding yang drift/nambah sendiri DITERIMA — yang penting gerakan karakternya benar. **Resep ini TANPA peace sign** — endingnya putar + tarik baju.
- Template prompt: "A woman standing in her bedroom, reviewing the [produk] she is wearing. She leans in place toward the camera slightly, then gently strokes the jacket fabric on her chest with her fingertips, slow and soft. She touches the top button, then returns to her starting position, turns her body about 30 degrees to the side while keeping her head facing the camera, and gently pulls the jacket at the waist. **The camera is completely static, no zoom, no cuts, no voice. She stays in place the whole time. Her face is never shown, the framing stays cut at her mouth.**"
- VARIASI (wajib): setelah pembuka "condong + gosok lembut", lanjutannya HARUS bervariasi tiap video (putar kiri/kanan, sentuh kerah/syal, rapikan hem, tangan di pinggang, dll) supaya tidak repetitif.

### Mirror selfie (setelan + dress)
Resep baku: HP menutupi wajah sepanjang video, SATU langkah kecil maju ke cermin, putar badan atas sedikit ke KIRI lalu ke KANAN, kembali depan, tahan pose; tangan satunya di saku (atau rileks di sisi badan kalau setelan tanpa saku). **DIAKHIRI peace sign 1x di level dada** (tangan bebas, jauh di bawah dagu, jauh dari HP/wajah, tahan sampai habis). Framing yang berubah setelah langkah maju DITERIMA sebagai natural. Putaran kiri+kanan sering menyatu jadi satu sisi — itu perilaku yang diketahui, diterima. **ATURAN SAKU (Jendral, 17 Nov 2026): kalimat saku HANYA dipakai kalau foto seller JELAS ada saku; kalau tidak ada saku, ganti jadi "Her other hand rests relaxed at her side, never pressed against her hip or thigh." Tangan "masuk saku" tanpa saku bisa dirender menempel ke pinggul-paha = sugestif, bahaya buat TikTok. Gate 3 wajib cek posisi tangan bebas di semua frame. AKAR MASALAH: foto jangkar mirror lama tangannya masuk saku jeans — jadi ada DUA base mirror: `lala_berdiri_fullbody_mirror_base_cahaya.jpg` (tangan di saku, untuk setelan ADA saku) dan `lala_berdiri_fullbody_mirror_base_tangan_santai_cahaya.jpg` (tangan rileks di sisi, untuk setelan TANPA saku; Cloudinary: https://res.cloudinary.com/dpllb7idh/image/upload/v1794890106/lala_berdiri_fullbody_mirror_base_tangan_santai_cahaya.jpg). Pilih base SESUAI foto seller sebelum generate frame-0.**
- Template prompt: "A realistic mirror selfie video. A woman stands in front of a tall arched mirror, holding her phone up so it covers her entire face the whole video. She takes one small step forward toward the mirror, pauses, turns her upper body slightly to the left, then rotates slightly to the right, then returns to face the mirror and holds the pose. Her other hand stays in her jeans pocket the whole time (or relaxed at her side if the outfit has no pockets). At the very end, she raises her free hand and makes ONE peace sign at chest level, well below her chin, far from the phone and her face, and holds it until the video ends. **The phone covers her entire face throughout, her face is never shown. The camera is completely static, no zoom, no cuts, no voice.**"
- Rotasi setelan: variasinya di DALAM mode mirror — arah putar (kiri/kanan, satu sisi per video), tangan bebas (di saku / rileks / sentuh kancing-hem), posisi peace (dada/pipi, dirotasi). Jangan dua setelan berurutan dengan variasi yang persis sama.

## 7. Gate 3 — QC video (wajib sebelum upload)

Ekstrak frame di 0 / 0,6 / 2 / 3,5 / 6,5 / 9,5 detik dan periksa satu per satu:
- **Produk identik ≥95% di SEMUA frame** (warna, motif, kerah, lengan, kancing, resleting, hem, fit). Video yang mengubah detail produk di tengah jalan = GAGAL walau frame-0 lolos.
- **Faceless**: hidung/mulut ngintip di tepi atas BOLEH. Wajah penuh + mata jelas yang menetap = GAGAL. Profil sekilas (tanpa mata jelas) dalam gerakan = bisa diterima borderline. Wajah penuh HANYA untuk foto profil, bukan video.
- **Background freeze**: frame 0 vs 0,6 detik harus identik (tidak ada yang berubah/pindah). Poster dinding yang drift di mode horizontal DITERIMA (aturan khusus mode itu).
- **Bentuk dada**: tangan TIDAK BOLEH menekan rata di dada — sentuh hanya ujung jari, lalu ke hem. Bentuk dada harus tetap sama seperti frame-0 di semua frame. (Pengecualian borderline: tangan menyebar di dada dalam SATU frame tapi bentuk dada utuh = diterima, catat cacatnya.)
- **Resleting**: HARUS tertutup penuh kerah sampai hem di semua frame, slider di ATAS tepat di bawah kerah, kedua panel bertemu rapat, TIDAK ADA kulit/dada kelihatan. Resleting terbuka = GAGAL, video tidak dibuat.
- **Tas**: kalau di foto referensi ADA tas, PAKAI tas yang sesuai fotonya (tas sama, bahu sama) — berlaku umum semua mode. Tas harus menggantung di bahu yang SAMA dengan talinya + kena gravitasi di semua frame. Tas tidak boleh muncul/hilang/terbang/pindah bahu. Kalau tidak bisa dirender bersih, fallback TANPA tas. Tas jinjing (tote) BELUM teruji — jangan dicoba dulu.
- **Aksesoris**: gelang/jam/kalung harus tetap menempel di semua frame (melayang/hilang = gagal).
- **Gerakan**: beat sesuai mode (bagian 6). Peace sign tepat 1x di akhir (kecuali horizontal: tanpa peace). Kepala tidak pernah menunduk (mode duduk + horizontal).
- **Ketajaman**: bandingkan ketajaman frame 2 detik dengan frame-0. Flow memberi 720p native jadi biasanya tajam — kalau melembut, catat saja (tidak ada LUT/sharpening, lihat aturan keras).
- Kalau Gate 3 GAGAL: video TIDAK di-upload. Regenerasi video hanya dengan perbaikan spesifik; kalau gagal dengan cara yang sama 2x, BERHENTI dan laporkan + tawarkan opsi. Generation yang ditolak (integrity check) TIDAK PERNAH di-retry.

## 8. Post-process

Flow memberi video 720p native **dengan audio AAC**. Video fashion harus SILENT. Langkahnya:
- **Horizontal (1280x720)**: `ffmpeg -i <raw.mp4> -vf "crop=1280:688:0:32,scale=1280:720:flags=lanczos" -c:v libx264 -crf 18 -an -movflags +faststart <final>.mp4`
- **Duduk / Mirror (720x1280)**: `ffmpeg -i <raw.mp4> -vf "crop=720:1220:0:60,scale=720:1280:flags=lanczos" -c:v libx264 -crf 18 -an -movflags +faststart <final>.mp4`
- **Berdiri vertikal (720x1280)**: `ffmpeg -i <raw.mp4> -vf "crop=720:1218:0:62,scale=720:1280:flags=lanczos" -c:v libx264 -crf 18 -an -movflags +faststart <final>.mp4`
- Crop atas = drift guard (memotong area wajah yang mungkin masuk). Setelah itu verifikasi dengan ffprobe: ukuran benar (720x1280 atau 1280x720), durasi 10,0 detik, HANYA ada stream video (tanpa audio).
- **Verifikasi frame 9,5 detik final**: harus faceless (mulut/dagu saja). Kalau masih ada hidung/mata, crop lebih dalam atau video tidak dipakai.
- **DILARANG**: LUT / efek warna / sharpening / AI upscale. Alasannya: LUT mengubah warna produk (risiko pelanggaran TikTok, kasus Fuzzy). Pipeline tetap polos (crop + lanczos saja).

## 9. Upload + catat (otomatis, tanpa tanya dulu)

**ATURAN KLAIM (Jendral, 17 Nov 2026 — dua AI kerja di sheet yang sama): SEBELUM mulai mengerjakan satu baris Antrian Link, tulis NAMAMU di kolom J (AI) baris itu. Baris yang kolom J-nya sudah ada nama AI lain = sedang dikerjakan AI lain, LEWATI. Ambil hanya baris Status "Pending" DAN kolom J masih kosong.**

Setelah Gate 3 lolos + post-process selesai:
1. **Upload ke Cloudinary** (video): `curl -F file=@<final.mp4> -F upload_preset=ml_default -F public_id=<KodeVideo> https://api.cloudinary.com/v1_1/dpllb7idh/video/upload` (cloud `dpllb7idh`, preset `ml_default`, upload-only). Catat `secure_url` + `version` yang dikembalikan. Verifikasi linknya dengan `curl -I` (harus 200 OK, Content-Type video/mp4).
2. **Catat ke sheet "Video Fashion"** (spreadsheet "Stok Video Reels Pure By Nature", ID `1g-QJp_HVaU7aB0MEtRvwswrcbxdvqFPqWXNGsJ2TR-I`): baris kosong berikutnya — BACA sheet fresh tepat sebelum menulis (jangan pakai hitungan baris kosong dari bacaan awal kerja, itu menimpa baris orang lain); kolom: No | Kode Video | Produk | Harga (KOSONG — barang bukan milik kita) | Link Produk | Durasi (10) | Link Cloudinary | Status ("Siap tayang") | AI (namamu) | Mode (mode yang dipakai). **Selalu read-back setelah menulis.**
3. **Update tab "Antrian Link"**: baris produk itu → Status "Selesai" + Kode Video (kolom F) + Link Video (kolom G) + mode yang dipakai ke kolom D. Kolom J (AI) sudah terisi namamu sejak klaim (lihat aturan klaim di atas). **Read-back juga.**
4. **Kode Video**: `<NamaProduk>-<Mode>-Flow-V1` (contoh: `DevinaTop-Horizontal-Flow-V1`, `LunellyStella-Duduk-Flow-V1`, `PoppyVest-Berdiri-Flow-V1`). Tambahkan "-Flow-" supaya jelas ini video Flow, bukan generator sendiri.
5. **Tulis NOTES.md** di folder produk: nama, link, referensi, desain (dengan jumlah detail yang terverifikasi), mode, hasil Gate 1 + Gate 3 (dengan persen + cacat), nama file final, link Cloudinary, nomor baris sheet.
6. **Laporan ke pengguna**: kirim sebagai GAMBAR saja — foto asli seller + frame-0 per video, plus nama produk, link Cloudinary, nomor baris sheet. **JANGAN kirim file video ke chat** (aturan produksi). PENGECUALIAN: kalau ini PERCOBAAN/tes (bukan produksi massal), video WAJIB dikirim ke chat sebagai file video. Dan kalau pengguna bilang link Cloudinary tidak bisa diputar di UI web, kirim file videonya langsung sebagai lampiran.

## 10. Rotasi

- **Rotasi mode ANTAR PRODUK** (bukan 1 produk langsung semua gaya): produk A duduk, B berdiri vertikal, C horizontal, lalu balik duduk. Tiap produk 1 mode per pass. File counter: `rotasi_mode.txt` (isi = mode BERIKUTNYA yang dipakai). Urutan: Duduk → Berdiri Vertikal → Horizontal → Duduk. Setelan/dress TIDAK ikut counter (tetap mirror). **MODE DUDUK DI-PAUSE SEMENTARA (Jendral, 17 Nov 2026): atasan rotasi HANYA Berdiri Vertikal ↔ Horizontal sampai Jendral bilang lanjut.**
- **Rotasi setelan (dalam mode mirror)**: arah putar, tangan bebas, posisi peace — dirotasi tiap video, jangan dua berurutan sama.
- **Rotasi prop lantai (duduk)**: tas → kacamata → tumbler → tas.
- **Rotasi rok** (kalau foto seller cuma atasan): ruffle putih → plisket putih → A-line putih polos → denim → midi krem → kembali ke ruffle putih. Warna disesuaikan dengan atasan.
- **Rotasi set gerakan duduk (A–E)**: pilih sesuai ciri produk; fallback urutan A→B→C→D→E→A. Jangan set yang sama di dua video berurutan.
- **Rotasi peace (berdiri vertikal + mirror)**: pipi ↔ dada antar video. Satu video = SATU peace saja.
- **Bawahan mengikuti foto seller dulu**: ada celana → pakai celana itu; ada rok → pakai rok itu; cuma atasan → baru rotasi rok.

## 11. Aturan keras (jangan dilanggar)

1. Frame-0 WAJIB sebelum video. Jangan pernah generate video langsung dari foto seller/base tanpa frame-0.
2. Produk di frame-0 DAN di semua frame video HARUS identik minimal 95% dengan foto seller. Kalau ragu, video TIDAK dibuat/di-upload.
3. Resleting HARUS tertutup penuh di semua frame (slider di atas, panel bertemu, tanpa kulit/dada kelihatan).
4. Wajah penuh + mata jelas = GAGAL. Video tetap faceless; wajah penuh hanya untuk foto profil.
5. Tangan TIDAK BOLEH menekan rata di dada. Ujung jari saja.
6. Tas: kalau di foto referensi ADA tas, PAKAI tas yang sesuai fotonya (tas sama, bahu sama, gaya yang sama) — berlaku umum semua mode, "kalau bisa". Tas TIDAK BOLEH muncul/hilang/terbang/pindah bahu; kalau tidak bisa dirender bersih, fallback TANPA tas. Tas jinjing (tote) BELUM teruji.
7. Hijab TIDAK dipakai. Produk hijab + mom&kids TIDAK diproduksi.
8. Foto produk HARUS dari link persis yang pengguna kirim. Jangan substitusi dari marketplace lain.
9. Generation yang DITOLAK (integrity check) TIDAK PERNAH di-retry, walau dirombak kata-katanya.
10. TIDAK ADA LUT / efek warna / sharpening. Pipeline polos.
11. Harga di sheet SELALU kosong (barang bukan milik kita).
12. Produk baru HARUS masuk Showcase TikTok dulu lewat aplikasi (sebelum bisa dijadwalkan). Produk di video HARUS sama persis dengan produk yang dipasang di TikTok Studio; kalau tidak ada yang persis, JANGAN pasang mirip — laporkan gagal.
13. Saat upload/jadwalkan di TikTok Studio, label "AI-generated content" JANGAN dicentang — TikTok memberi labelnya sendiri setelah upload.
14. Video "Cacat" JANGAN PERNAH dijadwalkan.
15. Jangan pakai jumlah view di profil web TikTok sebagai bukti tayang — cek langsung di TikTok Studio (Posts).
16. Jangan dorong spend kredit Flow kalau pengguna tidak minta. Flow = backup produk andalan; generator sendiri = utama.
17. Dinding mode duduk TETAP maroon hangat. Jangan usulkan ganti background kecuali pengguna yang mulai.
18. Satu produk = 1 frame-0 + 1 video per mode. Jangan generate video dari frame-0 yang belum lolos Gate 1.

## 12. Batas kerja

- **Per pesan/request: max 4 gambar + 6 video** (termasuk yang dibuat subagent). 1 produk = 1 frame-0 + 1 video.
- **Kredit Flow adalah batas keras**: 3 video/hari di 720p/10dtk (45 kredit). Kalau saldo habis, berhenti — tunggu refresh 20:14 WITA. Jangan beli kredit.
- **Retry**: tidak ada auto-retry. Berhenti, diagnosa KENAPA, retry hanya dengan perbaikan spesifik. Gagal dengan cara yang sama 2x = BERHENTI + laporkan + tawarkan opsi. Frame-0 max 3 total, video max 2 total per produk per mode.
- **Waktu**: 1 produk Flow ≈ 10-15 menit (frame-0 + generate Flow + QC + post-process + upload + catat).

## 13. Contoh nyata — 3 video Flow pertama (16 Nov 2026)

Produksi 3 mode rotasi, antrean No 14-16. Semua lolos Gate 1 + Gate 3 sekali jalan, "Siap tayang".

| Produk | Mode | Frame-0 | Video (Flow) | Gate 3 | Sheet |
|---|---|---|---|---|---|
| Devina Top (jaket putih, 8 kancing perak, resleting) | Horizontal | v1 ~97% | Omni 1.1, 720p/10dtk, 15 kredit | ~96%; putaran 6,5s ~90° profil (borderline) | No 111, `DevinaTop-Horizontal-Flow-V1` |
| Lunelly Stella (maroon, pita, 5 kancing, renda) | Duduk (Set B) | v1 ~97% | Omni 1.1, 720p/10dtk, 15 kredit | ~97% — paling bersih, peace dada mendarat | No 112, `LunellyStella-Duduk-Flow-V1` |
| Vest Poppy (polkadot krem, pita, peplum) | Berdiri Vertikal (Set F) | v1 ~96% | Omni 1.1, 720p/10dtk, 15 kredit | ~96%; putaran 6,5s ~90° profil (borderline) | No 113, `PoppyVest-Berdiri-Flow-V1` |

Pelajaran dari batch ini:
- Flow menganimasikan frame-0 dengan sangat setia (produk, background, framing hampir tidak berubah).
- Kelemahan Flow: putaran badan cenderung jadi ~90 derajat (kepala ikut mutar) walau prompt minta 30 derajat. Diterima borderline kalau wajah cuma profil.
- Flow memberi audio AAC — wajib dibuang.
- Lunelly membuktikan resep duduk Set B bekerja sempurna di Flow (semua beat mendarat, peace di dada).

## Contoh kedua — 3 setelan mirror via Flow (16 Nov 2026, 20:26)

Setelan pakai mode **mirror selfie** di Flow (resep bagian 6). Ketiga frame-0 digenerate dulu sekaligus (aturan batch), baru Flow dibuka sekali dan 3 video digenerate berurutan. Semua lolos Gate 1 + Gate 3 sekali jalan, "Siap tayang".

| Produk | Variasi mirror | Frame-0 | Gate 3 | Sheet |
|---|---|---|---|---|
| Arwen Set (outer putih motif, rok plisket putih) | tangan rileks di sisi, peace DADA | v1 ~97% | ~97%; putaran = satu sisi di 6,5s (diterima) | No 123, `ArwenSet-Mirror-Flow-V1` |
| GLADIA One Set (denim navy, 5 kancing, celana pendek) | tangan di saku, peace PIPI | v1 ~97% | ~97% | No 124, `GladiaSet-Mirror-Flow-V1` |
| Monica One Set Jeans (peplum denim, mutiara di lengan) | tangan sentuh hem peplum, peace DADA | v1 ~97% | ~97% | No 125, `MonicaSet-Mirror-Flow-V1` |

Pelajaran dari batch ini:
- Resep mirror (langkah maju + putar kiri/kanan + peace di dada) BEKERJA di Flow, sama seperti di generator sendiri.
- Variasi rotasi setelan (tangan bebas + posisi peace) diterapkan di ketiganya — jangan dua setelan berurutan dengan variasi yang persis sama.
- Catatan: di batch ini tas di foto seller TIDAK dipakai (tasnya cuma styling, bukan bagian produk). Aturan tas terbaru (16 Nov 21:30): kalau di foto referensi ADA tas, pakai tas yang sesuai fotonya — lihat aturan keras No 6.

## 14. Kegagalan yang sudah diketahui (jangan ulangi)

- **Tanpa frame-0 (b17_50)**: video langsung dari base + foto seller = perut terbuka di semua frame, wajah masuk di 9,5 detik, framing berubah, pose berubah. Frame-0 tetap WAJIB.
- **Edit bedah pada frame-0 yang gagal (b17_56)**: editor mengembalikan FOTO SELLER itu sendiri. Selalu fresh re-edit.
- **Putar 90 derajat (b18_01 v2, horizontal)**: kepala menunduk + mutar → wajah penuh masuk. Pakai ~30 derajat + kepala menghadap kamera.
- **Langkah maju di horizontal (b18_01 v1)**: framing mengencang seperti kamera zoom. Ganti dengan "condong di tempat".
- **Gosok kencang (b18_01 v3)**: gosok harus LEMBUT dan perlahan, ujung jari.
- **Dua sisi dalam 1 video (FLORA v5-v7)**: tidak bisa — generator menyatukan dua putaran jadi satu sisi. Satu sisi per video.
- **Peace 2x (FLORA v2)**: satu video = SATU peace saja.
- **LUT (b18_01)**: warna produk berubah (rompi abu jadi lebih muda) — DITOLAK pengguna, jangan pakai.
- **Dinding terracotta (b17_57)**: frame-0 merender dinding oranye bukan maroon — cacat yang dicatat, produk tetap jalan.
- **"Poin tidak cukup" (16 Nov)**: bukan kegagalan — generasi yang sudah jalan tetap selesai dan bisa diunduh.
