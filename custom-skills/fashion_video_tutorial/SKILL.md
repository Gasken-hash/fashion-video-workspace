# Tutorial: Video Fashion Try-On (Fashion Video Fidelity) — v2

**Versi: 16 Nov 2026 (update besar).** Tutorial ini berisi SELURUH resep
produksi video fashion try-on yang dipakai Igris untuk Jendral
(@lala.coquette) sejak 12 Nov 2026, diperbarui sampai aturan terbaru
(rotasi mode, mode mirror, resep horizontal, sistem antrean + cron).
Tujuannya satu: **baju di video harus SAMA PERSIS (minimal 95%) dengan
foto asli seller**, supaya tidak kena pelanggaran TikTok dan produk yang
dipasang benar-benar produk yang ada di video.

File ini ditulis supaya AI lain bisa mengerjakan produksi yang sama
dari nol, tanpa perlu bertanya ulang. Ikuti langkahnya berurutan.
Satu langkah gagal = BERHENTI, jangan lanjut ke langkah berikutnya.

**Karakter: Lala.** Cewek coquette, cardigan pink pita, rambut hitam
cepol tinggi longgar (messy high bun) + helai depan membingkai wajah
di kedua sisi sampai bahu; BUKAN cepol rapi/ketat. Base duduk pakai
cepol tinggi longgar; base berdiri pakai cepol RENDAH. Video tetap
FACELESS (wajah penuh hanya untuk FOTO PROFIL, bukan video).
Akun TikTok: **@lala.coquette**, display name "Lalaa", bio
"Spal spil by Lala 💕".

---

## 1. Foto jangkar (anchor images) — SEMUA base yang dipakai

Foto jangkar = foto dasar (base) yang dipakai sebagai kanvas. SATU
base yang sama dipakai untuk semua produk dalam satu mode; yang diganti
HANYA bajunya. Foto-foto ini ada di mesin Igris DAN sudah di-upload ke
Cloudinary (16 Nov 2026) — AI lain bisa unduh langsung dari link di
bawah ini, tidak perlu minta file ke Jendral.

**VERSI YANG BERLAKU SEKARANG (17 Nov 2026): file `*_cahaya.jpg`.**
Komposisi/pose/prop SAMA PERSIS dengan base lama, ditambah sinar
matahari sore hangat dari jendela kiri + bayangan lembut, dan dinding
semua base DISAMAKAN ke **cream hangat** seperti dinding base
horizontal (keputusan Jendral 17 Nov 2026 ~12:00 WITA, "warnanya gini
semua samakan"). Pakai file `*_cahaya.jpg` + link Cloudinary di bawah.
Base lama (tanpa cahaya, dinding tan) masih tersimpan lokal sebagai
arsip — jangan dipakai lagi.

### 1a. Mode DUDUK (mode utama, atasan) — 3 base, prop lantai dirotasi
Semua 1168x2112 (versi cahaya, vertikal 9:16), dinding CREAM hangat,
model duduk di tepi kasur, framing potong di mulut (mata tidak
kelihatan), kamar krem + kasur + boneka plush, sinar matahari sore
hangat dari jendela kiri. Bedanya cuma PROP DI LANTAI
(kanan bawah), dirotasi tiap video supaya tidak monoton:
- `~/workspace/fashion_test/bases/base_pita_v3_tas_cahaya.jpg` — tas hitam di lantai
- `~/workspace/fashion_test/bases/base_pita_v3_kacamata_cahaya.jpg` — kacamata di lantai
- `~/workspace/fashion_test/bases/base_pita_v3_tumbler_cahaya.jpg` — tumbler hitam di lantai

Rotasi prop: tas → kacamata → tumbler → tas → ... (satu prop per
video). Prop STATIS di lantai — bukan dipakai/dibawa. Aturan tas-fisika
tetap berlaku (lihat bagian 6).

Link Cloudinary (unduh langsung, versi cahaya):
- Tas: https://res.cloudinary.com/dpllb7idh/image/upload/v1794890098/base_pita_v3_tas_cahaya.jpg
- Kacamata: https://res.cloudinary.com/dpllb7idh/image/upload/v1794890101/base_pita_v3_kacamata_cahaya.jpg
- Tumbler: https://res.cloudinary.com/dpllb7idh/image/upload/v1794890102/base_pita_v3_tumbler_cahaya.jpg

### 1b. Mode BERDIRI VERTIKAL (atasan, variasi hari lain)
- `~/workspace/fashion_test/bases/lala_berdiri_vertikal_flow_base_cahaya.jpg`
  (1184x2096, vertikal 9:16). Model BERDIRI, medium shot mulut–paha
  tengah, cardigan pink pita + celana putih, gelang emas kanan,
  kalung emas, cepol RENDAH, kamar krem + kasur + boneka plush,
  sinar matahari sore hangat dari jendela kiri.
  Gerakan: Set Berdiri F (lihat bagian 5).
  Link Cloudinary: https://res.cloudinary.com/dpllb7idh/image/upload/v1794890103/lala_berdiri_vertikal_flow_base_cahaya.jpg

### 1c. Mode BERDIRI HORIZONTAL (atasan, variasi hari lain)
- `~/workspace/fashion_test/bases/lala_berdiri_horizontal_base_v2_cahaya.jpg`
  (2112x1168, horizontal 16:9). **PAKAI v2 (yang terbaru).** v2 = base
  lama + CERMIN TINGGI (arched mirror) di dinding kiri, memantulkan
  PINTU — biar vibesnya tetap 1 kamar (revisi Jendral 16 Nov 2026).
  Model TIDAK terpantul di cermin (cermin memantulkan pintu saja).
  Gate 3 wajib cek cermin tetap konsisten dan tidak memunculkan
  wajah/model.
- v1 (tanpa cermin) disimpan sebagai
  `~/workspace/fashion_test/bases/lala_berdiri_horizontal_base_v1.jpg`
  — JANGAN dipakai lagi, pakai v2.
  Link Cloudinary (v2, versi cahaya): https://res.cloudinary.com/dpllb7idh/image/upload/v1794890104/lala_berdiri_horizontal_base_v2_cahaya.jpg
- Gerakan: resep "review outfit" (lihat bagian 5).

### 1d. Mode MIRROR SELFIE (SETELAN — atasan + bawahan panjang)
- `~/workspace/fashion_test/bases/lala_berdiri_fullbody_mirror_base_cahaya.jpg`
  (1168x2112, vertikal 9:16). Model full-body DI DALAM cermin tinggi
  (arched mirror), pegang HP menutupi wajah (faceless built-in),
  cepol messy, kamar yang sama (kasur gingham + plush + poster pink).
  **Ini base setelan yang berlaku sekarang (revisi Jendral 16 Nov 2026).**
- Base lama `lala_berdiri_vertikal_fullbody_base.webp` (FLORA, framing
  mulut–kaki, kaki telanjang) SUDAH DIGANTI — jangan dipakai untuk
  setelan baru. Video FLORA lama yang sudah dicatat tetap sah.
- Gerakan: PROMPT JENDRAL verbatim (lihat bagian 5) + peace sign 1x di akhir (revisi Jendral 16 Nov 2026 ~14:25 WITA: "peace sign nya jangan lupa ya" — mirror WAJIB diakhiri peace, tangan bebas, level dada, HP tetap menutupi wajah).
  Link Cloudinary: https://res.cloudinary.com/dpllb7idh/image/upload/v1794890105/lala_berdiri_fullbody_mirror_base_cahaya.jpg

### 1e. Yang TIDAK dipakai lagi (jangan pakai)
- Base Adelia landscape (bedah_maroon_1111, 2096x1184) — base lama
  12 Nov, sudah tidak dipakai.
- Base vertikal Priscila (vertical_test_priscila) — base lama, parkir.
- Foto karakter (character_base.jpg) — parkir, cuma dipakai 1 video.

---

## 2. Prasyarat (siapkan dulu sebelum produksi)

AI yang mengerjakan harus punya:

1. **Tool generate gambar** (image editing/generation) yang bisa edit
   foto dengan gambar referensi, dan **tool generate video**
   (image-to-video, 10 detik). Tanpa keduanya, produksi tidak jalan.
2. **ffmpeg** terinstall (untuk potong frame, crop, upscale, hapus audio).
3. **Akun Cloudinary** untuk hosting video: cloud name + unsigned
   upload preset. (Yang dipakai Igris: cloud `dpllb7idh`,
   preset `ml_default`. AI lain pakai akun Cloudinary sendiri/Jendral.)
4. **Akses Google Sheets** untuk pencatatan (spreadsheet "Stok Video
   Reels Pure By Nature", tab "Video Fashion" + tab "Antrian Link").
   Kalau tidak ada akses sheet, catat di file lokal dulu dan beri tahu
   Jendral.
5. **Foto dasar (base)** — lihat bagian 1. Minta ke Jendral kalau
   tidak ada di mesin kamu.
6. **Foto produk ASLI dari link persis yang Jendral kirim.** Ini aturan
   keras (lihat bagian 6). Jangan pernah ambil foto dari marketplace
   lain walau produknya "sama".

---

## 3. Alur produksi (8 langkah, berurutan)

```
0. Identitas produk (sebut balik + foto asli seller)
1. Ambil galeri foto produk dari link Jendral
2. Generate gambar frame-0 (EDIT foto dasar, ganti HANYA bajunya)
3. GATE 1 — cek frame-0 lawan foto asli, detail per detail (≥95%)
4. Kalau gagal: edit bedah / fresh re-edit / fallback foto asli
5. GATE 2 — generate video dari frame-0 yang lolos
6. GATE 3 — QC frame video (0 / 0.6 / 2 / 3.5 / 6.5 / 9.5 detik)
7. Post-processing: crop atas + upscale 720p + hapus audio
8. Upload Cloudinary + catat sheet + serahkan ke Jendral
```

### Langkah 0 — Identitas produk
Sebelum apa-apa, sebutkan balik ke Jendral (atau catat): nama produk,
link produk, dan foto asli seller yang dipakai. Kalau foto asli tidak
bisa didapat, TIDAK ADA produksi — laporkan gagal, jangan nebak pakai
foto lain.

### Langkah 1 — Ambil galeri foto produk
**Tokopedia (cara yang terbukti jalan):** curl polos DITOLAK (CAPTCHA).
Pakai Python `curl-cffi` impersonasi Chrome. Script siap pakai ada di
mesin Igris: `~/workspace/fashion_test/batch17/fetch_one.py <tag>`
(dijalankan dari folder batch dengan python venv yang ada curl-cffi-nya;
script ini membaca `products.json` untuk shortlink dan menyimpan
sampai 12 gambar galeri sebagai `tok_NN.bin` webp 800x800 di folder
produk). Kalau AI lain tidak punya script ini, intinya:
`requests.Session(impersonate="chrome")` GET ke link produk, ambil
URL `ibyteimg` (CDN Tokopedia) yang versi `resize-webp:800:800`,
unduh. Setelah itu convert: `ffmpeg -i tok_NN.bin tok_NN.jpg`.
**Shopee:** buka link kanonik `https://shopee.co.id/product/{id_toko}/{id_produk}`
(BUKAN shortlink `s.shopee.co.id`) dengan alat baca halaman, baca
sampai akhir, ambil URL galeri yang domainnya mengandung
`susercontent` (CDN asli, urut dari foto utama). JANGAN pakai API
Shopee (error 90309999), JANGAN HTML mentah, JANGAN screenshot.
**Pilih foto referensi:** foto produk bersih PERTAMA yang menggambarkan
produk sesuai nama (bukan infografik/size chart/promo; kalau foto
pertama infografik, ambil berikutnya yang bersih). Untuk listing
multi-varian/desain, foto HARUS menggambarkan varian yang sesuai nama
— kalau tidak ada yang jelas cocok, tandai RAGU/PENDING, jangan nebak.
**Nama Bersih selalu diturunkan dari nama produk, bukan dari foto.**

### Langkah 2 — Generate gambar frame-0 (EDIT, bukan generate baru)
**Frame-0 WAJIB. Tidak ada jalan pintas.** Tes 15 Nov 2026 membuktikan
video yang di-generate LANGSUNG dari base + foto seller (tanpa frame-0)
GAGAL total: perut terbuka di semua frame (generator MENGABAIKAN
instruksi "high-waist, NO midriff"), wajah masuk di 9.5s, framing
berubah, pose berubah. Frame-0 adalah KONTROL yang bikin aturan
dipatuhi — tanpa frame-0 tidak ada Gate 1, generator video membuat
keputusannya sendiri. **Jangan pernah coba cara langsung lagi.**

Edit foto dasar (base) dengan prompt seperti ini. Sertakan SELALU foto
asli seller sebagai gambar referensi di setiap edit — AI harus MELIHAT
bentuknya, generate dari kata-kata saja hasilnya ngaco.

Template prompt frame-0 (isi [...] sesuai produk):
```
Edit this photo: keep the same model, pose, background, framing and
camera angle exactly. Change ONLY the top/garment to the garment in
the reference photo.
The garment: [deskripsi bentuk dengan kata GEOMETRI + larangan eksplisit,
contoh: "a cream rib-knit cardigan, round ribbed crew neck, exactly 6
small white buttons down the center front, ribbed cuffs and hem; the
hem is a soft rounded U-curve, longer at the center, no sharp point;
sleeves are attached at the shoulders, NOT off-shoulder, NOT detached
sleeves"].
Bottom: [ikuti foto seller dulu; kalau foto cuma atasan, pakai rotasi
rok — lihat bagian 7].
The top of the frame cuts at her mouth and chin, so her eyes are NOT
visible — do NOT show her full face, do NOT zoom out, do NOT reframe
to include her eyes.
[Untuk produk resleting, tambahkan klausul resleting — lihat bagian 6.]
[Untuk produk lengan pendek, boleh tambah aksesoris tipis — lihat bagian 6.]
```
Catatan penting:
- Ubah sesedikit mungkin — ganti HANYA bajunya, sisanya jangan di-redraw.
- Tulis bentuk dengan kata geometri + larangan eksplisit. Kata kabur
  diisi AI dengan versi fashion standarnya (contoh: "pointed hem" saja
  menghasilkan V tajam, padahal aslinya lekuk U lembut).
- Kalau jumlah detail diragukan (mis. jumlah kancing/pita), CROP +
  PERBESAR foto asli seller dulu sebelum memutuskan — hitungan pertama
  sering salah (contoh nyata: "5 kancing" ternyata 4 setelah di-crop).
- Kalau flat-lay terus kehilangan detail hitungan (mis. kancing
  selalu salah jumlah walau sudah ditulis eksplisit), pakai FRAME-0
  LAMA yang sudah benar sebagai referensi baju, bukan flat-lay
  (terbukti di FLORA mirror: frame-0 lama v2 yang 7 kancing benar
  memperbaiki frame-0 baru yang selalu 4 kancing).

### Langkah 3 — GATE 1: cek frame-0 lawan foto asli (≥95%)
Bandingkan frame-0 dengan foto asli seller, DETAIL PER DETAIL —
bukan "kelihatan mirip". Checklist:
warna, pola/motif (jumlah + posisi), bentuk leher, lengan (nempel/
lepas, panjang), pita/detail (jumlah, ukuran, posisi), kancing
(jumlah, ukuran, posisi), resleting (tertutup penuh, slider di atas),
bentuk hem, fit (ketat/longgar). Satu menyimpang = BELUM LOLOS,
video TIDAK BOLEH dibuat. Kalau ragu apakah sudah ≥95%, anggap
BELUM LOLOS. Artefak base (kalung emas, mulut/dagu ngintip) bukan
produk — tidak dihitung ke persen, tapi tetap dicatat sebagai cacat.
Untuk setelan, hitung juga kancing/saku (jumlah kancing = detail yang
dinilai) dan cek HP menutupi wajah (mode mirror).

### Langkah 4 — Kalau Gate 1 gagal
- **Fresh re-edit (LEBIH DISUKAI):** edit ulang FRESH dari base +
  foto seller, dengan cacatnya disebut eksplisit. Terbukti: edit
  bedah pada frame-0 (pakai frame-0 sebagai kanvas + foto seller
  sebagai referensi) bisa GAGAL TOTAL — editor mengembalikan FOTO
  SELLER ASLINYA (b17_56). Fresh re-edit dengan cacat disebut
  eksplisit memperbaiki dalam 1x coba.
- **Edit bedah:** perbaiki HANYA bagian yang salah pada foto yang
  sudah bagus itu, maksimal 2x percobaan. Satu cacat per edit.
  Jangan generate ulang dari nol (itu mengacak semua detail lagi).
- **Frame-0 LILO (edit dari foto asli) TIDAK BOLEH dibedah:**
  edit bedah pada frame-0 LILO tidak jalan — generator mengembalikan
  frame ke bentuk awal dan cuma menerapkan instruksi terakhir.
  Kalau frame-0 LILO gagal, edit ulang FRESH dari frame aslinya
  dengan SEMUA perubahan sekaligus dalam satu edit.
- **Fallback (kalau 2x bedah gagal):** crop foto asli seller jadi
  faceless (cara LILO). Bentuk 100% asli karena itu memang fotonya;
  background jadi ikut foto seller. Jangan paksakan generate.
- **Penolakan generator (integrity check) TIDAK PERNAH di-retry,**
  walau dirombak kata-katanya, walau lewat tool/endpoint lain.
  Catat produknya sebagai SKIP dan laporkan ke Jendral (opsi:
  coba lagi nanti dengan penyesuaian, atau generator lain —
  keputusan Jendral). Catatan: tool call yang gagal karena error
  loading (bukan penolakan) BUKAN generation — boleh diulang.

### Langkah 5 — GATE 2: generate video (hanya kalau Gate 1 lolos)
Generate video dari frame-0 (image-to-video), 10 detik, silent (tanpa
audio). Pilih/adaptasi SET GERAKAN dari ciri produk (lihat bagian 5)
— jangan pakai satu koreografi yang sama untuk semua produk.
Mode duduk = vertikal 9:16. Mode berdiri vertikal = vertikal 9:16.
Mode horizontal = horizontal 16:9. Mode mirror = vertikal 9:16.

Template prompt video duduk (isi [...] sesuai produk + set):
```
Animate this photo into a 10-second vertical video. The model stays
sitting the whole time — she never stands, walks, or steps anywhere.
Calm, slow, composed; torso, shoulders and chest stay completely
still, only her hands move gently.
Camera is completely locked off — no pan, tilt, zoom, or shake. The
background is completely frozen and identical to the photo in every
single frame — nothing moves, shifts, or changes, especially in the
first second.
Head stays upright the whole time, chin slightly raised, NEVER bows
her head down and NEVER looks down at her hands, gaze stays forward,
framing stays cut at the mouth in every frame.
[BEAT GERAKAN sesuai set yang dipilih — contoh Set B: one hand lifts
a cuff to show the sleeve, fingertips touch the top bow, both hands
pinch the hem, hands rest on the skirt, hands on the lap, one peace
sign at the end at chest level, well below the chin.]
Bust stays naturally high and lifted, no sagging, no drooping, no
flattening. Hands never press flat against her bust, never spread
their palms over her chest — fingertips only on bows/buttons.
The garment stays exactly identical to the photo in every frame:
[detail kunci produk — warna, motif, jumlah kancing/pita, kerah, hem].
One peace sign only, at the very end, at chest level, well below the
chin. Silent, no audio.
Negative: no standing, no walking, no stepping, no camera movement,
no background movement, no face, no eyes, no looking down, no head
bowing, no flat palms on the chest, no bag appearing or disappearing.
```
Catatan: beat "cubit hem" bisa bikin kepala menunduk dan wajah masuk
frame — klausul kepala tegak WAJIB ada di semua prompt video duduk.

### Langkah 5b — Alternatif: generate video di Google Flow (bukan generator sendiri)
Selain generator sendiri, video juga bisa digenerate di **Google Flow** dari frame-0 yang sama (Frames-to-Video). Polanya IDENTIK: frame-0 digenerate dulu oleh AI sendiri (Langkah 2-4), lalu frame-0 itu dilempar ke Flow sebagai gambar awal untuk dianimasikan. Flow TIDAK bikin gambar dari nol.
- **ATURAN BATCH — WAJIB: generate frame-0 untuk SEMUA 3 produk dulu (sekaligus, dalam satu batch gambar), Gate 1 satu per satu, BARU buka Flow sekali dan generate 3 videonya berurutan. JANGAN pola 1 gambar → 1 video → 1 gambar → 1 video.** Sesi Flow gampang logout dan kredit terbatas (3 video/hari) — kalau gambar produk sudah siap semua, begitu Flow dibuka langsung gas 3 video tanpa jeda, tanpa bolak-balik.
- Akun Flow: login pakai akun email Google MASING-MASING (akun sendiri, BUKAN akun orang lain — jangan login pakai email orang lain, tidak akan bisa). Proyek Flow dan saldo kredit itu per akun: masing-masing buka flow.google.com dengan akun sendiri, saldo 50 kredit/hari, refresh tiap hari 20:14 WITA. Sheet pencatatan TETAP SAMA untuk semua orang (spreadsheet "Stok Video Reels Pure By Nature", tab "Video Fashion" + "Antrian Link").
- Pengaturan: model **Omni 1.1 Flash**, **720p**, **10 detik**, output **x1** = **15 kredit/video** → 3 video/hari (45 kredit, sisa 5). **Omni 1.1 TUTUP 5 Des 2026.**
- Aspect ratio: duduk/berdiri vertikal/mirror = 9:16; horizontal = 16:9.
- Flow memberi video 720p native **dengan audio AAC** — audionya WAJIB dibuang di post-process (Langkah 7).
- Peringatan "Poin tidak cukup" saat submit BUKAN kegagalan kalau generasi sudah jalan — videonya tetap jadi dan bisa diunduh.
- Temuan penting (16 Nov 2026): Flow menganimasikan frame-0 sangat setia (produk/background/framing hampir tidak berubah), TAPI putaran badan cenderung jadi ~90 derajat profil (kepala ikut mutar) walau prompt minta 30 derajat — diterima borderline kalau wajah cuma profil (bukan full face, mata tidak jelas).
- **Detail lengkap ada di skill terpisah: `~/workspace/custom-skills/flow_fashion_video/SKILL.md`** (foto jangkar + link Cloudinary, prompt gerakan per mode untuk Flow, harga, contoh nyata 3 video Flow pertama 16 Nov 2026). Baca skill itu sebelum generate video di Flow.
- JANGAN dorong spend kredit Flow kalau pengguna tidak minta. Generator sendiri = utama, Flow = backup produk andalan.

### Langkah 6 — GATE 3: QC frame video lawan foto asli
Ekstrak frame dari video mentah di detik 0 / 0.6 / 2 / 3.5 / 6.5 /
9.5 (mode mirror/full-body tambah 7 dan 8 kalau ada peace):
`ffmpeg -ss <detik> -i <video>.mp4 -frames:v 1 frame_<detik>.jpg`
Cek tiap frame:
- Produk tetap ≥95% identik dengan foto asli (warna, motif, jumlah
  kancing/pita, kerah, lengan, hem, fit). Video bisa mengarang detail
  sendiri dari frame-0 yang bersih (contoh nyata: pita pergelangan
  muncul di video padahal tidak ada di frame-0 maupun foto asli) —
  video yang mengarang detail = GAGAL.
- Background frame 0 vs 0.6 HARUS identik (generator suka me-reset
  scene di ~0.5 detik pertama; kalau background lompat = GAGAL).
- Faceless: dagu/mulut ngintip sedikit di tepi atas DITOLERANSI
  (laporkan saja); mata jelas atau wajah penuh = GAGAL. Mode mirror:
  HP harus menutupi wajah di SEMUA frame.
- Resleting (kalau ada) tertutup penuh di SEMUA frame.
- Bentuk dada vs frame-0 (tidak melorot/rata).
- Tas (ATURAN BARU Jendral 16 Nov 2026 ~21:30 WITA): kalau di foto referensi seller ADA TAS, PAKAI tas yang sesuai fotonya (tas sama, bahu sama) — berlaku umum semua mode, bukan cuma tas bagian produk. Tas harus lolos Gate 1 + Gate 3: di bahu yang sama, tali nyambung, menggantung kena gravitasi di semua frame; kalau tidak bisa dirender bersih, fallback TANPA tas. Terbukti: tas bahu GLADIA rantai (Gate 1 ~97% + Gate 3 ~96%, 16 Nov 21:06 WITA; sempat ketutup badan ~1 dtk pas putar maksimal lalu balik di bahu yang sama = oklusi, diterima). Tas jinjing (tote) BELUM teruji — jangan dicoba dulu. Mode duduk paling rawan buat tas.
- Aksesoris tetap menempel di semua frame.
- Ketajaman frame 2 detik vs frame-0 (video boleh lebih lembut, tapi
  detail produk harus tetap terbaca).
- Mode mirror: framing berubah sedikit setelah langkah maju DITERIMA
  sebagai natural (bukan cacat).
Kalau Gate 3 gagal: perbaiki frame-0 atau generate ulang videonya
(satu video gagal = generate ulang video itu saja, bukan semua produk).
Kalau ending peace menarik wajah masuk frame, POTONG video sebelum
peace (contoh nyata: video dipotong di 7 detik, ending tangan di
pinggang tetap bersih).

### Langkah 7 — Post-processing (ffmpeg)
Video mentah generator: 640x~1110, 10.0 detik, ada audio (harus dihapus).
Perintah final untuk video duduk/mirror (crop atas ~60px sebagai
pengaman drift + upscale 720x1280 + hapus audio):
```
ffmpeg -i <raw>.mp4 -vf "crop=640:1108:0:60,scale=720:1280:flags=lanczos" -c:v libx264 -crf 18 -an -movflags +faststart <final>.mp4
```
Mode horizontal: crop atas ~32px, upscale 1280x720:
```
ffmpeg -i <raw>.mp4 -vf "crop=1168:608:0:32,scale=1280:720:flags=lanczos" -c:v libx264 -crf 18 -an -movflags +faststart <final>.mp4
```
Setelah itu VERIFIKASI file final: `ffprobe` — harus 720x1280
(atau 1280x720 untuk horizontal), 10.0 detik, silent. Lalu cek ulang
frame 9.5 detik dari file FINAL (bukan mentah) — pastikan faceless
(mulut/dagu saja). **JANGAN pakai sharpening (Jendral menolak) dan
jangan pakai AI upscale (terlalu lambat). JANGAN pakai LUT/efek warna
apa pun (Jendral menolak 15 Nov 2026 — LUT mengubah warna produk,
risiko pelanggaran TikTok). Pipeline tetap polos: crop + upscale
lanczos saja.**

### Langkah 8 — Upload Cloudinary + catat sheet + serahkan
**Otomatis, tanpa tanya persetujuan dulu:** begitu Gate 3 lolos,
LANGSUNG upload + LANGSUNG catat "Siap tayang". Pengecualian: video
yang Jendral sendiri tandai cacat TIDAK dicatat sampai ada versi
perbaikannya.
- Upload video (curl, preset unsigned):
```
curl -X POST "https://api.cloudinary.com/v1_1/<cloud>/video/upload" \
  -F "file=@<final>.mp4" -F "upload_preset=<preset>" -F "public_id=<KodeVideo>"
```
  `public_id` = Kode Video (contoh: `CardiganPita-Duduk-V1`). Ambil
  `secure_url` dari respons JSON.
- Catat ke sheet tab "Video Fashion" (kolom A–H: No | Kode Video |
  Produk | Harga | Link Shopee | Durasi | Link Cloudinary | Status):
  Harga KOSONG untuk produk batch (bukan barang sendiri, fokus
  pemasaran saja — keputusan Jendral). Status = "Siap tayang".
  Setelah tulis, BACA ULANG barisnya untuk verifikasi.
- Tulis NOTES.md di folder produk (desain produk, referensi yang
  dipakai, set gerakan, hasil Gate 1/3, cacat, Cloudinary + No sheet).
- Serahkan ke Jendral (aturan 15 Nov 2026 20:45 WITA):
  **PRODUKSI = GAMBAR SAJA — kirim FOTO ASLI SELLER + FRAME-0
  (gambar awal video) sebagai lampiran gambar, disertai nama produk,
  link Cloudinary, dan nomor baris sheet. JANGAN kirim file video ke
  chat.** Alasannya: Jendral mau bandingkan sendiri kecocokan
  produknya; QC (Gate 1 + Gate 3) ketat tapi BUKAN jaminan 100% —
  penilai terakhir tetap dia.
  **PERCOBAAN/TES = video WAJIB dikirim ke chat sebagai file video,**
  supaya Jendral bisa lihat langsung hasilnya.

---

## 4. Mode produksi

| Mode | Kapan dipakai | Format | Base | Gerakan |
|---|---|---|---|---|
| 1. Duduk (UTAMA) | Atasan tunggal | Vertikal 9:16, medium shot (mulut–paha tengah), model duduk di tepi kasur sepanjang video | base_pita_v3_*_cahaya.jpg (prop dirotasi) | Set A–E (lihat bagian 5) |
| 2. Berdiri vertikal | Atasan, variasi hari lain | Vertikal 9:16, medium shot (mulut–paha tengah) | lala_berdiri_vertikal_flow_base_cahaya.jpg | Set Berdiri F |
| 3. Berdiri horizontal | Atasan, variasi hari lain | Horizontal 16:9, kamar | lala_berdiri_horizontal_base_v2_cahaya.jpg | Resep "review outfit" |
| 4. Mirror selfie | SETELAN (atasan + bawahan panjang) | Vertikal 9:16, full-body di dalam cermin | lala_berdiri_fullbody_mirror_base_cahaya.jpg | Prompt Jendral verbatim |

Satu produk bisa dapat 1 video per mode, tayang di HARI BERBEDA.
**ROTASI MODE (aturan Jendral 16 Nov 2026):** produksi merotasi mode
ANTAR PRODUK — 1 duduk, 1 berdiri vertikal, 1 horizontal, diulang.
JANGAN semua gaya di 1 produk. Setelan tetap mirror (tidak ikut
rotasi). Mode yang sudah dipakai tiap produk dicatat di kolom Mode
(Antrian Link) supaya kelihatan mana yang sudah pernah.
**MODE DUDUK DI-PAUSE SEMENTARA (Jendral, 17 Nov 2026 ~11:29 WITA):**
video duduk berubah banyak, prioritaskan mode lain dulu — atasan
rotasi HANYA Berdiri Vertikal ↔ Horizontal sampai Jendral bilang
lanjut.

### Mode 2 — Berdiri vertikal (Set Berdiri F)
Urutan: tangan kanan di pinggang → kedua tangan ke kerah/pita →
tangan terbuka lebar di dada atas (UJUNG JARI saja, jangan telapak
datar — lihat aturan dada) → kedua tangan ke hem peplum (cubit/usap)
→ usap sisi rok → putar badan pelan ~30–45° (kepala TETAP menghadap
kamera) → balik depan, kedua tangan di pinggang → tangan santai di
sisi → ending peace sign ✌️ di level dada.
- Kamera locked-off total, background beku. Kepala tetap tegak,
  tidak nunduk/miring jauh. Tidak ada langkah maju/mundur, tidak ada
  bungkuk.
- Peace dirotasi pipi ↔ dada antar video (1 video = SATU peace saja).
  Mode dada: "forearm bent across her waist, hand staying below her
  collarbone with fingertips far below her chin" + Negative "never
  rises above the chest, never goes near cheek/chin/mouth/ear".
  Tinggi peace itu lotre — cuma 1 dari 4 percobaan yang mendarat di
  dada; kalau mendarat di bahu, terima saja (bukan gagal).
- Gate 3 cek khusus: putaran 5s kepala tidak ikut mutar (profil =
  gagal); peace 9.5s di dada, bukan di pipi.

### Mode 3 — Berdiri horizontal (resep "review outfit", Jendral 15 Nov 2026)
Resep ini LOLOS Gate 3 ~96% (b18_01 v4) dan terkonfirmasi di produk
ke-2 (b18_02, ~97%). Prompt review Jendral (verbatim, bahasa Indonesia):
"buat gerakan realistis dan natural seperti sedang mereview outfit baju
yang dipakai. maju satu langkah kedepan lalu membungkuk tujuannya untuk
memperlihatkan deta jahitan di bagian kerah bajunya, dan menggosok
dengan kedua tangan di bagian dada bajunya. setelah itu kembali ke
posisi frame awal lalu menyampingkan badannya tujuannya untuk
memperlihatkan outfit yang dipakai dan menarik bajunya di bagian perut.
jangan ada voice"
- **TAPI implementasinya disesuaikan (pelajaran v1–v4):**
  - TETAP berdiri di tempat TANPA melangkah maju (langkah maju =
    framing mengecil, kelihatan kayak kamera gerak). Condongkan badan
    sedikit ke depan (bukan membungkuk dalam) untuk perlihatkan detail
    kerah.
  - GOSOK LEMBUT dan perlahan dengan kedua tangan di dada (ujung jari
    menyentuh kain, tidak menekan keras, tidak cepat — gosok kencang +
    telapak datar = ditolak Jendral: "digosok lembut aja itu baju,
    jangan digosok gosok kenceng banget").
  - Kembali ke posisi awal, putar badan perlahan ~30° ke samping +
    tarik baju di perut, kepala TETAP menghadap kamera dan tidak
    pernah menunduk, tanpa voice.
- Kamera COMPLETELY STATIC (framing tidak berubah sama sekali dari
  frame pertama sampai terakhir — klausul diperkuat: "no zoom, no
  push-in, no pan, no tilt, no drift, the shot scale stays exactly
  the same").
- Putar penuh 90° DILARANG: kepala ikut berputar + menunduk, wajah
  masuk frame. Putar yang jalan = ~30° + kepala tetap menghadap kamera.
- Poster dinding kanan yang drift/nambah sendiri DITERIMA, tidak
  masalah — yang penting gerakan karakternya benar (Jendral).
- **ATURAN VARIASI:** setelah pembuka "condong + gosok lembut",
  LANJUTANNYA HARUS BERVARIASI tiap video supaya tidak repetitif dan
  tidak kelihatan spam. Rotasi lanjutan (pilih/adaptasi per produk,
  seperti Set A–E): putar 30° kiri / putar 30° kanan, sentuh
  kerah/syal, rapikan hem, tangan di pinggang, usap turun ke hem,
  tarik baju di perut. Pembuka tetap sama, lanjutan dirotasi.

### Mode 4 — Mirror selfie (setelan, RESEP BAKU 16 Nov 2026)
**Prompt Jendral (verbatim Inggris, dipakai apa adanya, tanpa tambahan):**
"Create a realistic, casual full-body mirror selfie video of a young
woman standing in a bedroom in front of a tall mirror. She is wearing
a [deskripsi setelan]. She stands naturally, smartphone held directly
in front of her face, hiding all facial features. Then she takes one
small, natural step forward toward the mirror. She pauses, then gently
turns her upper body slightly to the LEFT. Then she slowly rotates her
upper body slightly to the RIGHT. Then she returns to front-facing and
holds the pose. Her other hand stays inside her jeans pocket the whole
time. The phone covers her entire face throughout the video. Static
camera, no zoom, no cuts. Preserve the bedroom and mirror reflection.
Consistent lighting and background. Photorealistic smartphone aesthetic.
Avoid exaggerated movements, dancing, unnatural twisting, walking away,
or revealing the face."
- **ATURAN SAKU (Jendral, 17 Nov 2026 ~09:25 WITA) — BAHAYA kalau celana/rok tidak ada saku:** kalimat "Her other hand stays inside her jeans pocket" HANYA dipakai kalau foto seller JELAS menunjukkan ada saku (kelihatan lubang/kantong saku). Kalau setelan TIDAK ada saku (celana pendek elastis, rok, piyama, dress) — GANTI kalimatnya jadi "Her other hand rests relaxed at her side, never pressed against her hip or thigh." JANGAN biarkan kalimat saku masuk ke prompt. Alasan: generator bisa render tangan "masuk saku" padahal tidak ada saku = tangan menempel/masuk ke pinggul-paha, kelihatan sugestif, risiko pelanggaran TikTok. Gate 3 wajib cek posisi tangan bebas di semua frame.
- **DUA BASE MIRROR (Jendral, 17 Nov 2026 ~09:26 WITA — akar masalahnya foto jangkar):** base mirror lama tangannya masuk saku jeans, jadi pose saku itu kebawa ke semua frame-0 walau prompt diganti. Sekarang ada DUA base: (1) `lala_berdiri_fullbody_mirror_base_cahaya.jpg` — tangan di saku, PAKAI INI kalau setelan JELAS ada saku; (2) `lala_berdiri_fullbody_mirror_base_tangan_santai_cahaya.jpg` — tangan rileks di sisi badan, PAKAI INI kalau setelan TIDAK ada saku (celana pendek elastis, rok, piyama, dress). Link Cloudinary base tangan santai: https://res.cloudinary.com/dpllb7idh/image/upload/v1794890106/lala_berdiri_fullbody_mirror_base_tangan_santai_cahaya.jpg — Pilih base SESUAI foto seller, sebelum generate frame-0.
- Peace sign 1x di AKHIR (revisi Jendral 16 Nov 2026 ~14:25 WITA): setelah kembali depan, tangan bebas (bukan tangan HP) angkat peace ✌️ di level dada, jauh di bawah dagu, jauh dari HP/wajah, tahan sampai video habis. HP TETAP menutupi wajah sepanjang video. TANPA maju-mundur lama. Satu tangan pegang HP (menutupi wajah SEPANJANG video), tangan lain di saku (kalau setelan pakai rok/celana tanpa saku: tangan lain rileks di sisi badan).
- **Rotasi setelan (Jendral 16 Nov 2026 ~15:41 WITA, "yap bener"):** setelan JUGA dirotasi — variasinya di dalam mode mirror: arah putar (kiri/kanan, satu sisi per video), tangan bebas (di saku / rileks di sisi badan / sentuh kancing-hem), posisi peace (dada/pipi, dirotasi). Jangan dua setelan berurutan pakai variasi yang sama persis.
- **Dress = mirror juga (Jendral 16 Nov 2026 ~15:46 WITA):** dress full-length kayak setelan, butuh full-body biar kelihatan utuh — kalau pakai mode atasan (medium shot), roknya kepotong. Jadi dress masuk MIRROR SELFIE, ikut rotasi variasi mirror.
- Framing BERUBAH sedikit setelah langkah maju DITERIMA sebagai natural
  (mengencang 2–6.5s, kaki sedikit kepotong, lalu melebar lagi 8–9.5s).
- Putar kiri+kanan runtuh jadi SATU sisi (sisi kiri jelas, sisi kanan
  tidak ada) — sama seperti mode full-body lama; terima satu sisi.
- Gate 1+3 wajib cek: HP selalu menutupi wajah + produk ≥95% +
  hitung kancing/saku.
- Mode ini faceless PALING AMAN dari semua mode (HP selalu menutupi
  wajah).

---

## 5. Set gerakan

### Set duduk (A–E) — TEMPLATE, bukan urutan tetap
PILIH/ADAPTASI dari ciri produk, BUKAN urutan tetap. Pemetaan ciri →
beat: pita/kancing depan → sentuh pita/kancing; manset flare → angkat
manset; hem scalloped/renda → cubit/telusuri hem; leher V/renda →
sentuh leher; rajut tebal → usap dada/lengan; pinggang fitted →
tangan di pinggang; tali pita → sentuh tali. Rotasi A→B→C→D→E→A
hanya FALLBACK kalau produk tanpa ciri menonjol. Set yang sama TIDAK
BOLEH dipakai di dua video berurutan. Catat set di NOTES.md.
- **Set A (baseline):** pinggang/rambut → leher → dada (terbuka) →
  hem/rok → pangkuan → putar badan pelan → peace.
- **Set B (detail showcase):** rambut → angkat satu manset →
  sentuh pita/kancing atas → cubit hem → rok → pangkuan → peace.
- **Set C (fit/pinggang):** bahu → dada → pinggang/hem (tangan di
  pinggang) → rok → putar badan pelan → peace + wave kecil.
  (Peace di ~8s + wave di 9.5s DITERIMA — preseden b17_04/b17_24.)
- **Set D (satu tangan jangkar):** satu tangan nempel di pinggang
  sepanjang video; tangan satunya: leher → pita → hem → manset →
  pangkuan → peace.
- **Set E (slow reveal):** tangan mulai bersilang di pangkuan →
  naik ke leher → terbuka di dada → satu tangan telusuri hem →
  kedua tangan di rok → putar badan pelan → peace.
  ("Terbuka di dada" harus ditulis sebagai ujung jari di
  kancing/fitur, jangan telapak datar — aturan dada.)
- **Set F (berdiri):** lihat Mode 2 di bagian 4.

### Pose akhir
Finger heart 🫰 atau peace sign ✌️, dirotasi. Peace 1x saja per video
(mode duduk/berdiri: di level dada; mode mirror: peace 1x di akhir,
tangan bebas, level dada — revisi Jendral 16 Nov 2026 ~14:25 WITA).

---

## 6. Aturan keras (tidak boleh dilanggar)

1. **Produk ≥95% identik** dengan foto asli seller di frame-0 DAN
   di semua frame video. Ragu = tidak dibuat/di-upload.
2. **Frame-0 WAJIB.** Video tanpa frame-0 GAGAL (terbukti 15 Nov 2026).
   Jangan pernah coba generate video langsung dari base + foto seller.
3. **Foto HANYA dari link persis yang Jendral kirim.** Jangan pernah
   substitusi foto dari marketplace lain — foto salah bisa bikin
   akun TikTok Jendral kena banned. Kalau link tidak bisa diambil,
   laporkan gagal.
4. **Resleting HARUS tertutup penuh** kerah sampai hem di semua
   frame-0 dan video — slider di ATAS (tepat di bawah kerah), kedua
   panel depan bertemu rapat, TIDAK ADA kulit/dada kelihatan.
   Resleting terbuka = konten sugestif = risiko banned. Klausul
   prompt: "the silver zipper is FULLY CLOSED and zipped all the way
   up to the collar, the slider sits at the very top just below the
   collar, both front panels meet completely, NO bare skin is visible,
   NO cleavage". Gate 1 dan Gate 3 wajib cek resleting.
5. **Faceless.** Hidung/mulut ngintip sekilas dalam gerakan BOLEH;
   wajah penuh + mata jelas dan menetap TIDAK BOLEH. Wajah penuh
   hanya untuk FOTO PROFIL, bukan video.
6. **Tas ikut hukum fisika.** Tas TIDAK BOLEH tiba-tiba muncul,
   hilang, terbang, atau pindah bahu. Kalau dipakai, tas menggantung
   di bahu yang SAMA dengan talinya, kena gravitasi, sepanjang video.
   Default video atasan: TIDAK PAKAI TAS. Pengecualian: di video
   SETELAN, kalau foto produk ada tasnya, tas DIPAKAI (tas adalah
   bagian dari produk). Tas yang cuma properti styling di foto model
   (tidak ada di nama produk) tetap TIDAK dipakai.
7. **Dada.** Tangan TIDAK BOLEH menekan rata di dada — sentuh dada
   hanya dengan UJUNG JARI (pita/kancing), lalu langsung ke hem.
   Prompt wajib bawa "bust stays naturally high and lifted, no
   sagging/drooping/flattening" + Negative "never press flat, never
   spread palms over chest".
8. **Kepala tegak (video duduk).** Kepala TETAP TEGAK, dagu sedikit
   terangkat, TIDAK BOLEH nunduk — beat cubit hem bisa menarik kepala
   ke bawah dan wajah masuk frame.
9. **Penolakan generator tidak pernah di-retry** (lihat langkah 4).
10. **Peace sign 1x saja per video**, di akhir, di level dada (mode
    duduk/berdiri DAN mode mirror — mirror diakhiri peace 1x tangan
    bebas level dada, revisi Jendral 16 Nov 2026 ~14:25 WITA). 2x peace
    = GAGAL.
11. **Video silent, 10 detik, final 720x1280 (atau 1280x720
    horizontal).** Musik ditambahkan pas posting di TikTok Studio,
    bukan di video.
12. **Bawahan ikut foto seller dulu.** Kalau foto ada celana → pakai
    celana itu; ada rok → pakai rok itu. Kalau foto cuma atasan →
    baru pakai rotasi rok (lihat bagian 7). Styling lain di foto
    (topi, tas selempang) TIDAK dipakai — cuma bawahan yang ngikutin.
13. **Aksesoris (produk lengan pendek):** boleh tambah gelang/jam
    tipis supaya tangan tidak sepi; kalung boleh ganti model; gelang
    + jam boleh beda kanan-kiri. Syarat: tidak mengubah produk,
    tidak menutupi detail produk, Gate 3 cek aksesoris tetap menempel.
14. **Dinding tetap maroon hangat** (mode duduk). Jangan ajukan ganti
    background kecuali Jendral yang mulai.
15. **Harga TIDAK diisi ke sheet** (bukan barang sendiri).
16. **TIDAK ADA LUT/efek warna.** Video polos (crop + upscale lanczos
    saja). LUT mengubah warna produk = risiko pelanggaran TikTok.
17. **JANGAN pakai video_count profil web untuk cek tayang.**
    Count web TikTok TELAT update (stale) — video yang sudah tayang
    bisa tidak kelihatan di count berjam-jam. Cek tayang HANYA di
    TikTok Studio (Posts) — itu sumber yang benar.

---

## 7. Rotasi (supaya video tidak monoton)

- **Prop lantai (mode duduk):** tas hitam → kacamata → tumbler hitam
  → tas... (satu prop per video, bergantian).
- **Rok (kalau foto cuma atasan):** ruffle putih → plisket putih →
  A-line putih polos → denim → midi krem → kembali ke ruffle.
  Tulis rok EKSPLISIT di prompt (jangan cuma "rok putih").
- **Set gerakan duduk (A–E):** lihat bagian 5. Set yang sama TIDAK
  BOLEH dipakai di dua video berurutan.
- **Mode (ROTASI PRODUKSI, aturan Jendral 16 Nov 2026):** produksi
  merotasi mode ANTAR PRODUK — 1 duduk, 1 berdiri vertikal,
  1 horizontal, diulang. Satu produk satu mode per pass; JANGAN semua
  gaya di 1 produk. Setelan tetap mirror (tidak ikut rotasi).
  Mode yang sudah dipakai tiap produk dicatat di kolom Mode
  (Antrian Link) — kalau produk dibuat video ke-2/ke-3 nanti, pilih
  mode yang BELUM dipakai.
- **Mode (ROTASI JADWAL):** lineup yang dijadwalkan ke TikTok juga
  rotasi mode (duduk → berdiri vertikal → horizontal → ...). Karena
  produksi sudah merotasi mengikuti urutan antrean, jadwal yang ambil
  baris dari atas ke bawah otomatis ikut rotasi. Kalau ada video yang
  tidak bisa dijadwalkan, jangan isi slotnya dengan video bermode sama
  dengan video sebelumnya kalau masih ada mode lain.
- **Pose akhir:** finger heart 🫰 atau peace sign ✌️, dirotasi.
- **Musik TikTok (pas posting):** 5 teratas Favorites di TikTok
  Studio. Cek ulang sebelum tiap penjadwalan — lagu baru yang disimpan
  Jendral langsung ada di paling atas (saat tutorial ini ditulis, lagu
  teratas: "suara asli - ncus syakilla" — salma; sebelumnya
  "Tante Holic" — Velett Key).
- **Caption TikTok:** SEFEMINIM mungkin, sesuai produk (contoh:
  "cardigan lucu 👉👈"). Rumus: caption feminim + 1 hashtag nama
  produk + war keyword (mis. "cardigan rajut"). PENDEK, jangan
  jelasin fitur. EMOJI MAKSIMAL 2. Nama tampil: hapus nama toko,
  max 30 karakter.

---

## 8. Sistem produksi massal (Antrian Link + cron)

Produksi jalan OTOMATIS dari antrean, bukan dari chat. Jendral hanya
cari link; produksi + penjadwalan jalan sendiri.

- **Spreadsheet "Stok Video Reels Pure By Nature"**, tab **"Antrian Link"**:
  kolom A No | B Link Produk | C Nama Produk | D Mode | E Status |
  F Kode Video | G Link Video | H Catatan | I Dijadwalkan.
  Data mulai baris 3 (baris 2 petunjuk). Jendral tempel link di kolom B
  + Status "Pending", atau kirim link ke chat dan AI yang mencatat.
- **Urutan antrean:** atasan dulu (Duduk) → setelan (Full-body/mirror)
  → ribet (Duduk ribet) → Skip (hijab, tidak dibuat).
- **Cron produksi** (`produksi-harian-antrian-link`): jalan tiap 4 jam,
  tiap run MAKSIMAL 4 link (jatah media per run: max 4 gambar +
  6 video), total ~20 video/hari. Per link: ikuti pipeline bagian 3
  (frame-0 dulu, Gate 1, Gate 3, upload Cloudinary, catat "Video
  Fashion", update baris antrean Status "Selesai" + Kode Video + Link
  Video + Mode yang dipakai di kolom D). Skip → Status "Skip" + alasan
  di Catatan. Laporan tiap run ke chat utama: GAMBAR SAJA (foto seller
  + frame-0 per video), JANGAN kirim file video.
- **Cron penjadwalan** (`jadwalkan-tiktok-studio-harian`): tiap pagi
  ~05:42 WITA, ambil MAKSIMAL 20 baris Status "Selesai" yang belum
  dijadwalkan, jadwalkan 1/jam 07:00–02:00 (PUBLIC, label AI JANGAN
  dicentang, musik rotasi 5 Favorites, produk Showcase ID cocok
  persis, anti-duplikat via cek daftar Posts). Isi kolom I dengan
  tanggal + jam slot. Kalau sesi Studio habis/minta login, JANGAN
  login sendiri — laporkan ke Jendral (dia login ulang lewat QR).
- **Alur harian:** produksi seharian (tiap 4 jam, 4 video) → besok
  pagi 05:42 dijadwalkan semuanya sekalian (1 jam 1 video). Video
  Senin dijadwalkan Selasa pagi, video Selasa dijadwalkan Rabu pagi,
  begitu terus.
- **Kalau antrean habis:** laporkan ke chat utama supaya Jendral tahu
  harus tambah link.

---

## 9. Posting TikTok (setelah video jadi)

- Posting/penjadwalan HANYA via TikTok Studio (browser cloud, akun
  @lala.coquette). JANGAN login dari browser lain (bisa menendang sesi
  cloud).
- Produk dipasang HARUS SAMA PERSIS dengan di video; kalau tidak ada
  yang persis, JANGAN pasang mirip — laporkan gagal.
- Produk HARUS ada di Showcase dulu (pemilih produk Studio HANYA
  tab "Showcase products"; produk baru masuk Showcase lewat aplikasi
  TikTok, Studio desktop tidak bisa).
- **Label "AI-generated content" JANGAN dicentang pas upload/jadwalkan
  (aturan Jendral 15 Nov 2026 20:52 WITA — DIBALIK dari aturan lama).
  TikTok kasih label AI otomatis pas video sudah ke-upload. Label
  otomatis itu cuma kelihatan di HP (aplikasi TikTok), tidak kelihatan
  di TikTok web.**
- Caption: rumus bagian 7. Musik: dari Favorites (cek ulang).
  Jadwal: 1 video per jam, PUBLIC (video privat tidak bisa dijadwalkan).
- Aman: 15–20 video/hari. Trial berjalan: posting tiap hari selama
  ~1 bulan (sejak 14 Nov 2026), lalu nilai hasilnya.
- **Cek tayang:** JANGAN pakai video_count profil web (stale).
  Cek di TikTok Studio (Posts) — lihat video + caption + jamnya.

---

## 10. Batas kerja (caps) dan cara kerja batch

- **Max 4 gambar + 6 video per pesan** (satu pesan = satu batch).
  1 produk normalnya butuh 1 gambar (frame-0) + 1 video, jadi
  maksimal 4 produk per batch kalau semua lolos sekali jalan.
  Kalau ada yang gagal Gate 1/3, jatahnya kepakai buat perbaikan,
  jadi produk yang jadi bisa kurang dari 4. Jatah reset tiap pesan
  baru dari Jendral. Cron produksi: tiap run = satu batch (max 4
  gambar + 6 video).
- **Kredit Flow adalah batas keras terpisah**: 3 video/hari di 720p/10dtk
  (45 kredit dari saldo 50/hari, refresh 20:14 WITA). Kalau saldo Flow
  habis, berhenti — tunggu refresh. Jangan beli kredit. Detail di skill
  `flow_fashion_video`.
- **Kerjakan batch ~4 produk per pesan, jangan tanya "lanjut?"** —
  serahkan hasil + progress, Jendral yang bilang lanjut kalau mau.
- **Satu row dikerjakan tuntas sebelum lanjut** (isolasi: file temp
  unik per produk, jangan ada kontaminasi antar produk).
- **Verifikasi independen:** foto terpilih dicek ulang oleh langkah
  terpisah ("apakah ini benar produk X?"), bukan oleh yang memilih.

---

## 11. Contoh nyata (bukti resep ini jalan)

- **Rompi Jeans (b17_13):** frame-0 v1 gagal Gate 1 (kancing 5,
  harus 6 — dibuktikan crop+perbesar foto asli); v2 fresh re-edit
  lolos ~97%; video v1 lolos Gate 3 sekali jalan.
- **Denim Crop Putih (b17_14):** video v1 GAGAL Gate 3 (wajah penuh
  di 6.5s — kepala menunduk saat cubit hem); v2 + klausul kepala
  tegak lolos ~97%. Bukti klausul kepala tegak wajib.
- **Polo Jersey (b17_56):** frame-0 v1 gagal (resleting kepanjangan);
  v2 edit bedah GAGAL TOTAL (editor mengembalikan FOTO SELLER ASLI);
  v3 fresh re-edit lolos ~97%. Bukti fresh re-edit lebih disukai
  daripada edit bedah untuk frame-0.
- **FLORA mirror (b17_61, 16 Nov 2026):** frame-0 v1/v2/v3 GAGAL
  Gate 1 (selalu 4 kancing tengah, harus 5); v4 LOLOS pakai frame-0
  FLORA LAMA v2 (yang sudah benar 7 kancing) sebagai referensi baju.
  Video v1 (gerakan sederhana) lolos Gate 3 ~97%; video v2 (prompt
  Jendral verbatim) lolos ~96%, Jendral: "bagus kok ini lumayan
  natural juga sesuai keinginan aku". Bukti: pakai frame-0 lama yang
  benar kalau flat-lay kehilangan hitungan; prompt Jendral jadi resep
  baku mode mirror.
- **Polo Scarf horizontal (b18_01):** frame-0 horizontal v1 lolos
  Gate 1 ~97%. v1 (prompt Jendral verbatim + langkah maju) lolos
  Gate 3 ~96% tapi framing mengencang banyak; v2 (tanpa langkah,
  kamera statis) GAGAL Gate 3 (wajah penuh di 6.5s — putar 90°);
  v3 (putar 30°) lolos ~95% tapi gosok terlalu kencang (ditolak
  Jendral); v4 (gosok lembut ujung jari) lolos ~96% — RESEP YANG
  BENAR. Dijadwalkan Selasa 17 Nov 07:00, Jendral cek preview di
  aplikasi: "Jujur bagus aja kok gak kalah jauh sama flow".
- **Nabel Puff horizontal (b18_02):** frame-0 v1 + video v1 lolos
  Gate 3 ~97% sekali jalan (resep v4 + variasi lengan puff).
  Bukti resep horizontal bisa dipakai massal untuk atasan.
- **Vintage Diamond Vest (b17_08):** frame-0 v3 lolos Gate 1 ~96%
  (tepat 3 beruang), tapi 4 video (v1–v4) SEMUA gagal Gate 3 dengan
  cara yang sama — generator nambah beruang ke-4 di sel kiri bawah.
  Keputusan: STOP, jangan buang cap media lagi. Opsi Jendral:
  fallback crop faceless foto asli, atau generator lain.
- **Tank Top Stripe (b17_27) + LADYLUXE Tanktop (b17_34) + Cut Out
  Ribbon (b17_79):** frame-0 DITOLAK image generator (integrity
  check) — tidak pernah di-retry. Kemungkinan penyebab: crop top +
  perut kelihatan / V-neck dalam + tank top fitted / cut-out dada.
  Opsi Jendral: coba lagi nanti dengan penyesuaian (bawahan
  high-waist / inner putih) atau generator lain.
- **Tes TANPA frame-0 (b17_50, 15 Nov 2026):** video langsung dari
  base + foto seller GAGAL total (perut terbuka semua frame, wajah
  masuk 9.5s, framing berubah, pose berubah). Bukti frame-0 WAJIB.

---

## 12. Kegagalan yang sudah diketahui (jangan ulangi)

- Lengan off-shoulder/lepas padahal aslinya nempel → klausul
  attachment eksplisit.
- Hem V tajam padahal aslinya lekuk U lembut → tulis geometri.
- Pita/kancing/bunga ditambah atau membesar di tengah video →
  Gate 3 per frame.
- Ruffle/frill muncul di sambungan pinggang → tambahkan "waist seam
  is flat and smooth, no ruffle trim, no frill" ke prompt video.
- Dagu/mulut ngintip di tepi atas (paling sering di detik akhir) →
  ditoleransi, laporkan; top-crop ~60px sebagai pengaman.
- Background lompat di 0–0.6 detik → klausul freeze + cek 0 vs 0.6.
- Video lebih lembut dari frame-0 → cek ketajaman di Gate 3; jangan
  sharpening (Jendral menolak).
- Tas pindah bahu / hilang / melayang / muncul tiba-tiba → aturan
  fisika tas (bagian 6).
- Dinding jadi terracotta padahal base maroon (Yukika b17_57, 3x
  re-edit gagal) → terima sebagai cacat, laporkan ke Jendral,
  jangan buang cap lagi.
- Arah putar kiri/kanan tidak deterministik; ending peace pipi bisa
  narik wajah masuk → cek frame 5s (arah) + potong sebelum peace
  kalau ending gagal.
- Langkah maju ke kamera = framing mengencang (kelihatan kayak kamera
  gerak) → mode horizontal: condong di tempat, jangan melangkah.
  Mode mirror: langkah maju DITERIMA sebagai natural (sudah disetujui
  Jendral).
- Putar penuh 90° = kepala ikut mutar + nunduk, wajah masuk frame →
  putar ~30° + kepala tetap menghadap kamera.
- Poster dinding kanan (base horizontal) drift/nambah sendiri →
  DITERIMA, bukan gagal (Jendral).
- LUT/efek warna mengubah warna produk → DITOLAK Jendral, jangan pakai.
- video_count profil web stale → JANGAN pakai untuk cek tayang;
  cek TikTok Studio (Posts).
- Edit bedah frame-0 bisa mengembalikan foto seller asli (b17_56) →
  lebih suka fresh re-edit.
- Flat-lay bisa kehilangan hitungan (kancing) berulang kali → pakai
  frame-0 lama yang benar sebagai referensi (FLORA mirror).

---

## 13. Catatan untuk AI lain yang memakai tutorial ini

- **File dan path di tutorial ini adalah milik mesin Igris.**
  Kalau kamu bekerja di mesin/akun lain, path `~/workspace/...`,
  script `fetch_one.py`, file base, dan akses sheet/Cloudinary di
  atas TIDAK otomatis ada — minta Jendral kirim file base + script,
  atau sesuaikan dengan setup kamu sendiri, dan beri tahu Jendral
  apa yang kamu ubah.
- **Kredensial (Cloudinary, Sheets) adalah milik Jendral.** Jangan
  minta password/token di chat; pakai jalur aman yang disediakan
  sistem kamu, atau minta Jendral yang menyiapkannya.
- **Aturan di sini berasal dari koreksi Jendral yang berulang.**
  Kalau Jendral mengoreksi kamu, catat koreksinya sebagai aturan
  tetap (seperti yang dilakukan tutorial ini) — jangan ulangi
  kesalahan yang sama.
- **Kalau ragu, jangan nebak.** Tandai RAGU/PENDING dan laporkan ke
  Jendral. Satu video yang salah produk lebih mahal daripada satu
  video yang tertunda.
- **Bekerja dengan Jendral:** bahasa Indonesia kasual, singkat dan
  to the point, humor/roasting boleh. Ngobrol santai kayak teman,
  jangan kaku/formal. Jangan bertele-tele. Kerjakan dulu, laporkan
  hasil + progress, jangan banyak tanya.
- **Perubahan sejak v1 (15 Nov 2026):** base horizontal v2 (cermin),
  base setelan jadi mirror selfie (ganti FLORA lama), resep horizontal
  v4, prompt Jendral jadi resep baku mirror, frame-0 WAJIB (tes tanpa
  frame-0 gagal), fresh re-edit lebih disukai, LUT ditolak, label AI
  JANGAN dicentang (dibalik), delivery produksi = gambar saja (foto
  seller + frame-0, bukan file video), rotasi mode produksi +
  penjadwalan, sistem Antrian Link + cron, video_count web tidak bisa
  dipakai cek tayang.
