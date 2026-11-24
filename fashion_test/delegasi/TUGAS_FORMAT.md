# Format File Tugas — Delegasi Video ke AI Pembantu

Tugas dari Igris (koordinator) ke AI pembantu ditulis sebagai file JSON di repo
`Gasken-hash/fashion-video-workspace`, folder `tasks/`, satu file per AI.

URL mentah yang dipantau script pemantau:
`https://raw.githubusercontent.com/Gasken-hash/fashion-video-workspace/main/tasks/<slug-ai>.json`

## Contoh: `tasks/contoh-ai-1.json`

```json
{
  "ai": "contoh-ai-1",
  "diperbarui": "2026-11-25T02:00:00+08:00",
  "tugas": [
    {
      "id": "tugas-2026-11-25-01",
      "produk": "Belloure.id - Lucca Vest Top",
      "link_produk": "https://vt.tokopedia.com/t/ZS9fsKxcPjvdD-9fqE8/",
      "frame0_url": "https://res.cloudinary.com/dpllb7idh/image/upload/v1795491494/lucca_frame0.jpg",
      "foto_seller_url": "https://res.cloudinary.com/dpllb7idh/image/upload/v1795491494/lucca_seller.jpg",
      "mode": "Horizontal",
      "antrian_no": 264,
      "detail_produk": "Vest sleeveless fitted maroon, kerah bulat, tepat 3 kancing mutiara putih kecil, 2 saku patch rendah tanpa kancing, hem depan terbelah dua ujung lancip, celana putih wide-leg.",
      "gerakan": "Kamera statis penuh. Maju 1 langkah kecil, membungkuk sedikit, usap halus 2 tangan di dada (ujung jari saja, jangan digosok/menekan), mundur kembali — saat mundur framing wajib tetap di bawah mata (hidung boleh kelihatan, wajah penuh/mata jelas = gagal), putar badan ~30 derajat kepala menghadap kamera, tarik hem di perut, kembali depan, akhir rileks. Tanpa suara.",
      "status": "baru"
    }
  ]
}
```

## Aturan file tugas

- `status` hanya diisi `"baru"` oleh Igris. AI pembantu TIDAK mengubah file tugas —
  hasil dikembalikan lewat sheet (lihat bawah), bukan lewat repo.
- Frame-0 SELALU dibuat Igris dan di-upload ke Cloudinary (gambar) — URL-nya ada di
  `frame0_url`. AI pembantu HANYA generate video 10 detik dari frame-0 itu.
- Foto seller HANYA dari link yang dikirim. Jangan pernah substitusi dari marketplace lain.
- Maksimal 3 tugas per file per hari (jatah per AI). Kerjakan 1 produk sampai tuntas
  sebelum lanjut ke produk berikutnya.
- Aturan keras (selengkapnya di `briefing-ai-pembantu.md`): produk ≥95% identik di
  semua frame, resleting tertutup penuh, faceless, tas ikut fisika, dada ujung jari,
  kepala tegak, peace 1x, video silent 10 detik 720p, tanpa LUT/sharpening,
  penolakan generator tidak pernah di-retry.

## Cara mengembalikan hasil (AI pembantu)

1. Generate video dari `frame0_url` sesuai `mode` + `gerakan`.
2. Cek sendiri frame 0/0.6/2/3.5/6.5/9.5 detik — kalau ada yang menyimpang dari
   `detail_produk`, JANGAN kirim. Tulis alasannya di sheet.
3. Upload video yang lolos ke Cloudinary (cloud `dpllb7idh`, preset `ml_default`).
4. Catat ke sheet "Stok Video Reels Pure By Nature":
   - Tab "Video Fashion": baris kosong berikutnya (baca fresh sebelum menulis),
     Status "Siap tayang", kolom I (AI) = nama AI kamu, kolom J (Mode) = mode.
   - Tab "Antrian Link": baris `antrian_no` → Status "Selesai", isi Kode Video (F)
     + Link Video (G). Kalau gagal → Status "Skip" + alasan di Catatan (H).
5. Igris yang Gate 3 final + laporkan ke Jendral. Video yang tidak lolos Gate 3
   tidak tayang.
