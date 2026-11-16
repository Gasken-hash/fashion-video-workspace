# b18_01 — Tes Horizontal (prompt review Jendral)

- Produk: Polo collar scarf sleeveless sweater vest (sama dengan tes berdiri vertikal).
- Mode: Berdiri horizontal 16:9, base `lala_berdiri_horizontal_base.jpg` (kamar, low bun).
- Prompt Jendral (dipakai kata-per-kata, ditambah pengaman framing standar):
  "buat gerakan realistis dan natural seperti sedang mereview outfit baju yang dipakai.
  maju satu langkah kedepan lalu membungkuk tujuannya untuk memperlihatkan deta jahitan di bagian kerah bajunya, dan menggosok dengan kedua tangan di bagian dada bajunya.
  setelah itu kembali ke posisi frame awal lalu menyampingkan badannya tujuannya untuk memperlihatkan outfit yang dipakai dan menarik bajunya di bagian perut.
  jangan ada voice"
- Frame-0 horizontal v1: LOLOS Gate 1 ~97% sekali jalan (rompi abu, kerah navy + 2 kancing, syal simpul + 2 ekor, trim navy di armhole, celana hitam).
- Video v1: LOLOS Gate 3 ~96% sekali jalan.
  - Beat yang mendarat: maju 1 langkah (framing jadi jauh lebih dekat di 2-3.5s) → tangan ke kerah/dada (gosok) → kembali ke posisi awal → menyamping (6.5s) + tarik baju di perut → kembali depan (9.5s).
  - "Membungkuk" jadi condong ke depan saja (bukan menunduk dalam) karena klausul kepala tegak — wajah TIDAK masuk frame di semua frame, mata tidak kelihatan.
  - Tangan menempel datar di dada di 2s/3.5s (beat gosok), tapi bentuk bust tetap utuh di semua frame — diterima borderline (preseden b17_42/b17_81), cacat dicatat.
  - Syal sempat tertutup tangan di 2s/3.5s (oklusi sementara, bukan cacat produk).
  - Dekor dinding kanan drift dari 0.6s (poster tambahan muncul).
  - Kalung emas (artefak base).
- Final: `b18_01_horizontal_v1_upscale720.mp4` (1280x720, 10.0s, tanpa suara; frame 9.5s final terverifikasi faceless setelah top-crop 32px).
- BELUM di-upload ke Cloudinary / dicatat di sheet — ini tes, menunggu penilaian Jendral.

## v2 — kamera statis (Jendral, 22:44 WITA: "kameranya gerak di detik awal, bisa gk dibuat statis?")
- Penyebab gerak di v1: beat "maju satu langkah" — model mendekat ke kamera, framing jadi jauh lebih dekat (kelihatan kayak zoom). v2: langkah maju DIHAPUS (tetap berdiri di tempat, cuma condongkan badan), + klausul kamera statis diperkuat ("framing NEVER changes, no zoom/push-in/drift, only the character moves").
- Hasil: kamera BERHASIL statis (framing 0 vs 0.6s stabil, condong di 2-3.5s jauh lebih ringan dari v1).
- TAPI v2 GAGAL Gate 3: di 6.5s, pas putar badan menyamping penuh (90°), kepala ikut menunduk + berputar → WAJAH MASUK (mata + hidung + mulut kelihatan jelas). Video berakhir tetap menyamping (tidak kembali depan).
- v2 TIDAK di-upload/dicatat. File mentah: `media-generation-b18-01-horizontal-v2-0-e1f30e52-a817-4ff5-9244-72a32ed3be8f.mp4`.

## v3 — putar 30° + kepala menghadap kamera (perbaikan v2)
- Putar badan penuh (90°) diganti putar perlahan ~30° + klausul "kepala tetap menghadap kamera, tidak pernah menunduk/berputar ikut badan" (aturan putar Set F).
- Hasil: LOLOS Gate 3 ~95%. Wajah AMAN di semua frame (mulut/dagu saja, mata tidak kelihatan). Kamera tetap statis. Produk ~96-97%.
- Cacat: (1) dekor dinding kanan drift makin banyak (1 poster di 0s → ~6 poster di 6.5s, "YOU'RE" + kucing); (2) tangan datar di dada di 2-3.5s (beat gosok), bust tetap utuh — borderline; (3) syal sempat tertutup tangan di 2-3.5s; (4) video berakhir tetap menyamping (tidak kembali depan); (5) kalung emas (artefak base); (6) hidung sempat mengintip di 2-3.5s (ketutup top-crop di final).
- Final: `b18_01_horizontal_v3_upscale720.mp4` (1280x720, 10.0s, tanpa suara; frame 9.5s final terverifikasi faceless).
- BELUM di-upload ke Cloudinary / dicatat di sheet — menunggu penilaian Jendral.

## v4 — gosok LEMBUT (Jendral, 22:48 WITA: "digosok lembut aja itu baju, jangan digosok gosok kenceng banget itu 🤣")
- Beat gosok diubah jadi "lembut dan perlahan" + klausul "fingertips lightly stroking, never pressing hard, never fast/vigorous".
- Hasil: LOLOS Gate 3 ~96% — versi TERBAIK sejauh ini. Gosoknya mendarat lembut: kedua tangan ujung jari menyentuh kain di dada, tanpa motion blur, tanpa telapak menekan. Bust utuh, dan ini sekaligus memperbaiki pelanggaran telapak-datar di v3.
- Wajah aman di semua frame, kamera tetap statis, produk ~96-97%.
- Cacat tersisa: (1) dekor dinding kanan drift (1 poster → ~5 poster); (2) video berakhir tetap menyamping; (3) hidung sempat mengintip di 2-3.5s (ketutup top-crop di final); (4) kalung emas (artefak base).
- Final: `b18_01_horizontal_v4_upscale720.mp4` (1280x720, 10.0s, tanpa suara; frame 9.5s final terverifikasi faceless).
- DI-UPLOAD + DICATAT 15 Nov 23:07 WITA (Jendral: "mantap upload"): Cloudinary `PoloScarf-Horizontal-V4` (v1794755212), sheet No 96 "Siap tayang".
- DIJADWALKAN 16 Nov 00:51 WITA (Jendral: tes 1 video horizontal dulu buat cek preview di aplikasi): TikTok Studio, Selasa 17 Nov 2026 07:00 WITA, PUBLIC, Everyone, caption "vest gemes 👉👈 #vest", produk TERPASANG (ID 1738192751456519870, Rp60.000, stok 1788, Aktif), musik lagu teratas Favorites saat itu ("suara asli - ncus syakilla" — salma), label AI TIDAK dicentang. Muncul 1x di daftar Postingan (573 → 574). Jendral mau cek preview di aplikasi TikTok: burem atau tidak.
- VERDIK JENDRAL 16 Nov 01:09 WITA (setelah cek preview di aplikasi): "Jujur bagus aja kok gak kalah jauh sama flow" — video horizontal TIDAK burem, kualitasnya tidak jauh dari Flow. Hipotesis Jendral: Flow kelihatan lebih realistis karena by default dia langsung menyesuaikan pencahayaan videonya.
