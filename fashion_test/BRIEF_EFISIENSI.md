# BRIEF: Cara Kerja Efisien (Anti-Boros) — Video Fashion Try-On

Untuk AI yang mengerjakan produksi video fashion. Tutorial lengkap ada di
`fashion_video_tutorial/SKILL.md` (781 baris). Brief ini khusus soal
**DISIPLIN GENERASI** — supaya tidak boros. Ikuti brief ini di samping
tutorial.

## Prinsip utama

**Iterasi di frame-0 (gambar), BUKAN di video.**

- Frame-0 = gambar awal video. Kalau frame-0 sudah ≥95% sama dengan foto
  asli seller, video hampir selalu lolos di percobaan pertama (v1).
- Video itu cuma menganimasikan frame-0. Kalau frame-0 goyang, video
  pasti goyang — diulang berapa kali pun tetap lotre.
- Jadi: habiskan usaha di frame-0. Video cukup 1x.

Patokan nyata (batch-17, 47 video): rata-rata ~1,2 gambar + ~1,05 video
per produk. Yang butuh video v2 cuma 1 produk (b17_14, wajah masuk).
Sisanya video v1 semua.

## Aturan retry (wajib)

1. **JANGAN auto-retry.** Kalau generate gagal, BERHENTI. Cari tau dulu
   kenapa gagalnya, baru generate ulang.
2. **Retry hanya kalau ada perbaikan spesifik.** Contoh: gagal karena
   kepala nunduk → tambah klausul kepala tegak → retry 1x. Gagal karena
   hem kepanjangan → sebut panjang hem yang benar → retry 1x.
3. **JANGAN retry prompt yang sama tanpa perubahan.** Itu cuma lotre,
   buang-buang generasi.
4. **Maksimal 2x perbaikan per langkah.** Frame-0 max 3x total (v1 + 2
   perbaikan). Video max 2x (v1 + 1 perbaikan). Kalau masih gagal →
   STOP, jangan buang cap lagi.
5. **Kalau gagal dengan cara yang SAMA 2x berturut-turut → STOP.**
   Laporkan ke Jendral + tawarkan opsi (fallback crop foto asli /
   generator lain / skip produk). Contoh nyata: b17_08 beruang ke-4 —
   4 video gagal dengan cara yang sama, distop, tidak buang cap lagi.
6. **Penolakan generator (integrity check) TIDAK PERNAH di-retry.**
   Sekali ditolak = produk SKIP. Jangan rombak kata-katanya, jangan
   coba lewat tool/endpoint lain.

## Anggaran normal (patokan)

- 1 produk = 1 frame-0 + 1 video = **2 generasi**. Itu yang normal.
- Kalau sampai 5 gambar + 5 video untuk 3 produk (contoh VM1380), itu
  sudah boros — tandanya frame-0 kurang dikontrol.
- Per batch (1 pesan): max 4 gambar + 6 video. Kalau jatah habis sebelum
  produk selesai, berhenti dan laporkan — jangan paksakan.

## Urutan kerja yang benar

1. Frame-0 dulu. Gate 1 (cek ≥95% lawan foto asli). Kalau gagal →
   perbaiki frame-0. **Fresh re-edit lebih disukai daripada edit bedah**
   (edit bedah bisa mengembalikan FOTO SELLER ASLI — terbukti b17_56).
2. Video HANYA kalau Gate 1 lolos. Generate 1x. Gate 3 (cek frame
   0 / 0.6 / 2 / 3.5 / 6.5 / 9.5 detik).
3. Kalau video gagal Gate 3 → diagnosis dulu (apa yang berubah? kepala?
   putaran? peace? produk drift?) → perbaiki SATU hal itu → retry 1x.
   Kalau gagal lagi dengan cara sama → stop.

## Yang paling sering bikin boros (hindari)

- **Frame-0 base berubah** (background jadi studio, pose berubah, wajah
  masuk) → kunci base di prompt: "keep the same model, pose, background,
  framing and camera angle exactly".
- **Generate video dari frame-0 yang belum lolos Gate 1** → video pasti
  gagal, buang 1 generasi. Jangan pernah.
- **Retry video tanpa ubah apa-apa** → lotre. Jangan.
- **Putar 90°** (kepala ikut mutar, wajah masuk) → pakai ~30° + kepala
  tetap menghadap kamera.
- **Langkah maju** (framing mengencang, kelihatan kayak kamera push-in)
  → mode horizontal: condong di tempat, jangan melangkah.
- **Gosok terlalu kencang** (telapak datar, motion blur) → gosok lembut,
  ujung jari, perlahan.

## Kalau ragu, jangan nebak

Tandai RAGU/PENDING dan laporkan ke Jendral. Satu video yang salah
produk lebih mahal daripada satu video yang tertunda.
