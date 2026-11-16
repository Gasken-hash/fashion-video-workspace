# Perbaikan HYLE Nissa Blouse — siap eksekusi (spec, 12 Nov 2026 pagi)

Satu-satunya video batch 5 yang TIDAK LOLOS audit aturan baru (9/11 lolos).
Spec ini disiapkan supaya perbaikan jalan sekali jalan lewat standar baru
(`STANDAR_VIDEO_FASHION.md`): frame-0 dulu, Gate 1, baru video, Gate 3.

## Produk
- HYLE Nissa Blouse Polkadot, pink — Rp49.000, HYLE Official Store
- Link kanonik: https://shopee.co.id/product/792629758/48012557736
- Foto asli seller: `~/workspace/fashion_test/batch5/hyle/p1.jpg` (varian pink,
  dipakai sebagai referensi utama) dan `p0.jpg` (varian putih, untuk detail
  kerah + tali samping).

## Yang salah (terverifikasi visual lawan foto asli, 12 Nov pagi)
Frame-0 lama: `~/workspace/fashion_test/batch5/frame0/media-generation-batch5-hyle-model-0-3df82764-c280-42d4-a64b-4f77bdd5d348.webp`
Video lama: `~/workspace/fashion_test/batch5/media-generation-batch5-hyle-tryon-0-a8706f54-4891-4862-98e1-5c3cb8f364a0.mp4`
1. Frame-0 membawa pita/bow BESAR di tengah depan pinggang + 2 tali panjang
   menjuntai ke rok putih. Di foto asli TIDAK ADA pita depan sama sekali.
2. Kerah frame-0 bundar rendah berkerut. Aslinya kerah TINGGI (mock-neck,
   menutup leher) dengan kerutan/gather di sekeliling leher.
3. Video menambah pita di KEDUA pergelangan (frame QC h_05) — tidak ada di
   frame-0 maupun di foto asli. Manset aslinya kerut elastis polos, tanpa pita.
4. Tali pinggang aslinya: tali KECIL dan RATAH di SAMPING/belakang (adjustable,
   terlihat di p0 varian putih), bukan pita depan.

## Cara perbaiki (metode swap, seperti Lunelly v2/v3 yang terbukti)
- Foto dasar: foto model Adelia landscape, kamar pink
  (`~/workspace/fashion_test/batch5/swap-test/media-generation-adelia-model-landscape-0-1936c196-9190-4231-bac5-f08611c4c057.webp`)
- Edit HANYA bajunya jadi HYLE Nissa, sertakan `hyle/p1.jpg` sebagai gambar
  referensi di setiap edit. Background, pose, rok putih, tas JANGAN disentuh.
- Deskripsi bentuk (kata geometri + larangan, sesuai best practice):
  "pink muda, polkadot hitam kecil rapat; kerah TINGGI mock-neck berkerut
  (gathered) menutup leher; lengan balon panjang, manset kerut elastis polos;
  badan longgar bloused dengan pinggang kerut elastis; TIDAK ADA pita di
  pinggang depan, TIDAK ADA pita di pergelangan, TIDAK ADA tali di depan —
  bukan kerah bundar rendah, bukan pita depan, bukan pita pergelangan."
- Maks 2x edit bedah kalau masih ada yang menyimpang; jangan generate ulang
  dari nol.

## Gate 1 — cek frame-0 lawan p1.jpg (satu menyimpang = belum lolos)
- [ ] Warna pink + polkadot hitam kecil sama
- [ ] Kerah tinggi berkerut, menutup leher (bukan bundar rendah)
- [ ] Lengan balon, manset kerut elastis polos, tanpa pita
- [ ] Pinggang kerut elastis, TANPA pita/bow depan, TANPA tali menjuntai
- [ ] Tali samping kecil-ratah saja (boleh tidak kelihatan dari depan)
- [ ] Background identik foto dasar Adelia, faceless

## Gate 2 — video (hanya kalau Gate 1 lolos)
Resep v3: landscape 16:9, 10 dtk, langkah maju 1x di beat 1, kamera lock-off,
faceless, silent. Beat 2: tangan merapikan kerah/hem (bukan pita — tidak ada
pita di produk ini).

## Gate 3 — QC frame video lawan p1.jpg (0 / 2 / 3,5 / 6,5 / 9,5 dtk)
Waspadai dua drift yang sudah terbukti di HYLE: (a) pita pergelangan muncul
sendiri, (b) pita pinggang depan balik lagi. Salah satu muncul = video GAGAL,
jangan dikirim sebagai final.

## Fallback (kalau 2x bedah gagal) — catatan jujur
Crop faceless dari foto asli seller (cara LILO) memakai p1.jpg, TAPI p1
membawa watermark besar "HYLE" di tengah torso — watermark akan ikut
kelihatan di blouse pada frame hasil crop. Jadi fallback HYLE lebih lemah
dari LILO; swap/bedah adalah jalur utama.

## Serah terima (sesuai aturan baru)
Per produk: foto asli seller + frame-0 + video + frame detik 2 + daftar
cacat jujur.

---

## Lanjutan swap ke 3 produk lain (pilihan kedua, bukan perbaikan)
Lunelly sudah beres lewat swap v3. Yang tersisa dari tawaran 12 Nov 00:12:
- Luluna Peplum kuning — video batch 5 LOLOS bersih, dagu aman semua frame.
  Swap = pemanis penyatuan background saja, risiko rendah.
- Kamila YUKA krem — video batch 5 LOLOS, dagu aman; cacat hanya hem
  kepotong saat framing terdekat. Swap = pemanis, risiko rendah.
- LILO Lucia Top maroon — SARAN: JANGAN di-swap. Frame-0-nya sudah foto
  ASLI seller (bentuk 100% asli); digambar ulang berisiko kehilangan
  keakuratan itu. Satu-satunya cacat videonya: pita bahu membesar dari
  3,5 dtk. Kalau mau diperbaiki, jalurnya bedah video/frame, bukan swap.
