# Batch 5 — 5 produk fashion, resep Adelia v3 (11 Nov 2026 malam)

Permintaan Jendral: "buset bagus banget, bisa gk kamu buatkan aku 5 produk
berbeda lagi" (setelah v3 Adelia). Semua landscape 16:9, 10,0 dtk, 24 fps,
langkah maju di beat 1, kamera lock-off, faceless, SILENT (perlu lagu
sebelum tayang). Bukan produk sheet — tes format seperti Adelia/Flatere.

## Produk (semua galeri dibaca via browser.open, foto susercontent)
1. Lunelly Daisy Ribbon, pink polkadot — Rp56.793, shop 1622295998 /
   product 42772516876. Halter, 2 pita kecil di tali bahu, fit. Referensi:
   foto model seller pink polkadot (product/id-11134207-81ztc-
   mux1df34aeir1d.jpg). Foto awal: generate (kamar pink).
2. LILO Lucia Top, maroon — Rp169.000, shop 17876062 / product
   24101850311. One-shoulder, pita bahu, tali ikat pinggang samping, fit.
   Foto awal: CROPPED foto asli seller p1 (crop y=240, 1248x704) —
   produk asli, bukan generate. Ruang tamu putih, rok plisket hitam.
3. HYLE Nissa Blouse Polkadot, pink — Rp49.000, shop 792629758 /
   product 48012557736. Micro-polka, kerah tinggi berkerut, lengan balon,
   tali pinggang samping. Foto seller ada watermark HYLE di torso, jadi
   foto awal: generate (kamar pink).
4. Luluna Blouse Peplum, kuning — Rp69.997, shop 1620814604 / product
   48715333163. Kemeja micro-polka, kerah klasik, kancing depan, peplum.
   Foto awal: generate dari foto hanger kuning (kamar pink).
5. Kamila YUKA Blouse Highneck, krem — Rp197.143, shop 282379994 /
   product 57111110076. Polkadot coklat besar, high-neck, longgar. Foto
   awal: generate dari foto hanger krem (kamar pink).

Ditolak: Kamila sempat dipertimbangkan turun prioritas (foto utama grup
3 model + teks, desain longgar); HYLE watermark; Luluna longgar/hijab —
tetap dipakai demi variasi 5 produk. Alternatif gagal: Nuboutique
Clemence, SHEILA POLKA, IWEARGRACIE Liora — galeri tidak render (slug
maupun kanonik, hanya shell Shopee), tidak dipakai.

## Produksi
- Frame awal: 4 foto model generate (batas 4 image call/turn, pas) +
  1 crop foto seller (LILO). Crop LILO butuh 3x percobaan (y=180 dan
  y=220 masih nunjukin dagu/bibir; y=240 bersih, pita bahu tetap utuh).
- Video: 5 subagent paralel, masing-masing max 1 video + QC frame
  (2 fps, baca 0/2/3,5/6,5/9,5 dtk). Total 5 video = dalam batas 6/pesan.
- Spot-check Igris: 5 file video ada (ffprobe 10,0 dtk semua; Lunelly
  1280x720, lainnya 1248x704) + 5 frame detik 2 dibaca langsung,
  laporan worker terkonfirmasi.

## Hasil QC per produk
- Lunelly: media-generation-batch5-lunelly-tryon-0-144b01e6....mp4,
  1280x720, mean -56,2 dB. Langkah maju jelas, tangan ke 2 pita.
  Dagu aman 0-9 dtk, ngintip di ~1 dtk terakhir (pola Adelia v3).
  Jari kanan agak kaku saat muter.
- LILO: media-generation-batch5-lilo-tryon-0-f7e881ab....mp4, 1248x704,
  mean -42,0 dB. Langkah maju kelihatan, muter badan paling tegas
  (30-45 derajat). Dagu ngintip sebentar di 3,5 dtk. Pita bahu membesar
  dari aslinya mulai 3,5 dtk. Jari agak menyatu saat cubit tali.
- HYLE: media-generation-batch5-hyle-tryon-0-a8706f54....mp4, 1248x704,
  mean -41,2 dB. Paling bersih: dagu aman semua frame, beat 1-3 jalan.
  Drift: pita muncul di pergelangan lengan (tidak ada di foto awal),
  tali pinggang sempat geser ke tengah saat muter.
- Luluna: media-generation-batch5-luluna-tryon-0-02f10715....mp4,
  1248x704, mean -41,4 dB. Langkah maju jelas dan bertahan paling lama
  (masih dekat di 6,5 dtk). Dagu aman semua frame. Muter badan agak
  singkat di akhir.
- Kamila: media-generation-batch5-kamila-tryon-0-423ecb94....mp4,
  1248x704, mean -43,7 dB. Langkah maju jelas, dagu aman semua frame,
  tas tidak pindah bahu. Framing terdekat sangat ketat sampai hem
  kepotong.

## Pola umum (dicatat untuk batch berikutnya)
- Semua model balik mundur sendiri ke jarak medium di ~6,5 dtk (tidak
  ada di prompt) — close-up hanya di paruh awal.
- Beat jalan lebih cepat dari timestamp prompt (beat 2 sudah di 3,5 dtk).
- Dagu ngintip di 2 dari 5 video (Lunelly akhir, LILO 3,5 dtk) — cacat
  berulang dari Adelia v3, belum ada fix yang andal.
- Semua video bisu; musik harus ditambah di editing sebelum tayang.

## File
- Video: ~/workspace/fashion_test/batch5/media-generation-batch5-*-tryon-*.mp4
- Frame awal: ~/workspace/fashion_test/batch5/frame0/
- QC frame: ~/workspace/fashion_test/batch5/qc-{lunelly,lilo,hyle,luluna,kamila}/
- Foto seller: ~/workspace/fashion_test/batch5/{kamila,hyle,lilo,luluna}/

Verdict Jendral atas batch 5 masih pending.
