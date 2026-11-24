# Panduan Pasang — Script Pemantau Tugas (untuk tiap AI pembantu)

Sistem ini bikin tugas dari Igris sampai ke AI pembantu dalam hitungan menit,
tanpa email dan tanpa ada yang harus mengecek manual.

## Cara kerja singkat

1. Igris menulis file tugas `tasks/<slug-ai>.json` di repo GitHub
   `Gasken-hash/fashion-video-workspace` (lihat `TUGAS_FORMAT.md`).
2. Script pemantau di AI pembantu mengecek file itu tiap 5 menit.
3. Ada tugas baru (`status: "baru"`) → script membangunkan agent → agent kerjakan
   tugasnya → hasil dicatat ke sheet seperti biasa.

## Langkah pasang (sekali saja, ~5 menit)

1. Salin `watcher-script.sh` ke `~/hooks/scripts/tugas-watch.sh`.
2. Ubah `SLUG_AI="CONTOH-AI-1"` di baris atas script dengan slug kamu
   (slug = nama file tugasmu di folder `tasks/`, tanpa `.json`).
   Slug ditentukan Igris saat pertama kali memberi tugas.
3. Jadikan executable: `chmod +x ~/hooks/scripts/tugas-watch.sh`
4. Daftarkan hook (lewat tool hooks):
   - id: `tugas-watch`
   - script_path: `~/hooks/scripts/tugas-watch.sh`
   - poll_interval_secs: `300` (5 menit; boleh 120 kalau mau lebih cepat)
   - prompt (instruksi saat bangun — salin apa adanya):
     > Ada tugas video baru dari Igris di file tugasmu (URL ada di payload wake).
     > Baca file tugas itu, kerjakan SEMUA tugas berstatus "baru" satu per satu
     > mengikuti briefing di repo (folder custom-skills, baca
     > fashion_video_tutorial/SKILL.md) dan TUGAS_FORMAT.md: generate video
     > 10 detik dari frame-0 yang dikirim (jangan buat frame-0 sendiri), cek
     > frame 0/0.6/2/3.5/6.5/9.5 detik, upload yang lolos ke Cloudinary,
     > catat ke sheet "Stok Video Reels Pure By Nature" (Video Fashion +
     > Antrian Link, klaim dulu, baca sheet fresh sebelum menulis, read-back).
     > Kalau gagal (frame ditolak / produk tidak cocok), catat Skip + alasan
     > di Antrian Link dan lanjut ke tugas berikutnya. Laporkan ringkas hasil
     > tiap tugas ke chat utama.
5. Tes dulu dengan `hooks.dry_run` (harus `silent` kalau belum ada tugas),
   lalu `hooks.enable`.

## Yang perlu diingat

- Script ini TIDAK butuh login, kredensial, atau akses sheet — dia cuma baca
  file publik di GitHub lewat curl. Semua kerja berat tetap dilakukan agent
  saat bangun.
- Kalau file tugas tidak bisa dijangkau (repo down / internet putus), script
  diam saja dan coba lagi 5 menit kemudian — tidak ada yang rusak.
- Jatah: maksimal 3 tugas per hari per AI. Kalau tugas hari ini sudah habis,
  file tugas berikutnya baru muncul besok pagi.
- Shadow (email-bot) TIDAK pakai sistem ini — dia tetap lewat email.
