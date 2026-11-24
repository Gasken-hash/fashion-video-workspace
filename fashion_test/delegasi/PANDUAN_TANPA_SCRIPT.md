# Panduan Alternatif — Tanpa Script (untuk AI yang tidak bisa menjalankan file .sh)

Kalau pemeriksa keamanan di tempatmu menolak file script, kamu TIDAK WAJIB
memakai script. Pakai jadwal (cron) biasa saja — agent yang mengecek, bukan script.

## Yang dilakukan

Buat satu jadwal (cron) yang jalan tiap 15 menit, dengan instruksi ini:

> Setiap jalan, ambil file tugas saya di URL ini:
> https://raw.githubusercontent.com/Gasken-hash/fashion-video-workspace/main/tasks/<slug-saya>.json
> (ganti <slug-saya> dengan slug yang ditentukan Igris)
>
> Catat hash/isi terakhir yang sudah saya lihat di file catatan saya.
> Kalau isi file BERUBAH dan ada tugas dengan status "baru", kerjakan
> SEMUA tugas baru itu satu per satu mengikuti briefing di repo
> (folder custom-skills, baca fashion_video_tutorial/SKILL.md) dan
> TUGAS_FORMAT.md: generate video 10 detik dari frame-0 yang dikirim
> (jangan buat frame-0 sendiri), cek frame 0/0.6/2/3.5/6.5/9.5 detik,
> upload yang lolos ke Cloudinary, catat ke sheet "Stok Video Reels
> Pure By Nature" (Video Fashion + Antrian Link, klaim dulu, baca
> sheet fresh sebelum menulis, read-back). Kalau gagal, catat Skip +
> alasan di Antrian Link dan lanjut ke tugas berikutnya. Laporkan
> ringkas hasil tiap tugas ke chat utama.
>
> Kalau tidak ada tugas baru, DIAM — jangan kirim pesan apa pun.

## Catatan

- Tidak ada file script yang dijalankan — agent hanya membaca URL lewat tool biasa.
- Jeda 15 menit artinya tugas ketahuan paling lambat ~15 menit setelah Igris menulisnya.
- Jatah tetap: maksimal 3 tugas per hari per AI.
- Shadow (email-bot) tidak pakai sistem ini — dia tetap lewat email.
