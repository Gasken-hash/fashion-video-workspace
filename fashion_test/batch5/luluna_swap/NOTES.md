# Swap Luluna Blouse Peplum — eksekusi 12 Nov 2026 (tes standar baru)

Produk: Luluna Blouse Peplum, kuning — Rp69.997
Link: https://shopee.co.id/product/1620814604/48715333163
Foto asli seller: `../luluna/p0.jpg` (gantungan, kuning), `../luluna/p1.jpg`

## Frame-0 (Gate 1: LOLOS, sekali jalan, tanpa bedah)
File: `media-generation-luluna-swap-frame0-0-b465c5ea-1746-41fa-85d9-d28e4c877a79.webp`
Metode: swap dari foto dasar Adelia landscape, edit HANYA baju, `luluna/p0.jpg`
sebagai referensi gambar.
Checklist lawan p0.jpg: kuning pucat + polkadot hitam kecil ✓; kerah klasik
berujung runcing ✓; kancing tengah depan ✓; lengan panjang manset polos ✓;
peplum berkerut di bawah pinggang ✓; tanpa pita/tali ✓; background identik ✓.

## Video v1 (Gate 3: GAGAL — dibuang, bukan final)
File: `media-generation-luluna-swap-video-0-d501e6d6-6951-46c0-8ced-86f85ea81749.mp4`
1248x704, 24 fps, 10,0 dtk, silent (mean -63,4 dB).
QC frame `qc/l_*.jpg`: di 6,5 dan 9,5 dtk video menambah ruffle/krul menonjol
di sambungan pinggang — tidak ada di foto asli maupun frame-0. Standar
menangkap drift ini; v1 TIDAK dikirim sebagai final.

## Video v2 (Gate 2 ulang + Gate 3: LOLOS)
File: `media-generation-luluna-swap-video-v2-0-f2395f2c-f714-4bed-8ba7-f5fdec397004.mp4`
1248x704, 24 fps, 10,0 dtk, silent (mean -46,1 dB).
Perubahan prompt: ditambah "waist seam is flat and smooth against the body,
no ruffle trim, no frill, no wavy ruffle band at the waist".
QC frame `qc2/m_*.jpg` (0 / 2 / 3,5 / 6,5 / 9,5 dtk): sambungan pinggang rata
dan halus di semua frame, peplum konsisten, kerah/kancing/manset sama, dagu
aman semua frame, langkah maju jelas, kamera lock-off.

## Cacat jujur (bukan cacat produk)
- Beat 3: dua tangan di pinggang, padahal prompt minta tangan kiri saja.
  Koreografi, bukan baju.
- Di 6,5 dtk strap tas menggantung aneh dan tas keluar frame. Aksesori.

## Koreksi cacat tas Luluna v2 — dikonfirmasi Jendral (12 Nov 2026, ~13:10 WITA)
- Jendral nonton dan ketawa: tasnya tiba-tiba jatuh. Dicek frame per frame (qc_bag_*.jpg):
  - 6.0 dtk: tas hitam masih ngegantung di bahu kiri, tali rantai kelihatan utuh.
  - 6.5 dtk: badan tas HILANG, tinggal tali rantai menggantung sendirian di sisi kanan.
  - 7.0 dtk: talinya pun ikut hilang, tas lenyap total.
- Jadi cacat QC lama "strap menggantung aneh di 6,5 dtk" ternyata lebih parah: tas jatuh di tengah putaran. Video tetap seperti adanya sesuai keputusan "video berikutnya aja" — tidak dibuat ulang.
