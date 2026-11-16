# Katie — Berdiri Horizontal (test base baru Lala) — 14 Nov 2026

## Produk
- Katie cardigan, baris 1 Korean Style. ID 26911445693, Rp99.900.
- https://shopee.co.id/product/689122241/26911445693
- Desain: soft pink, 5 pita HITAM kecil di depan, manik mutiara di tiap pita, manset flare/bell, hem scalloped.
- Foto asli: `ref_katie_original.jpg` (di folder induk, 800x800).

## Base (BARU)
- Foto Lala baru kiriman Jendral 14 Nov 11:57 WITA (`jangkar-gaya-try-on.jpg`).
- `~/workspace/fashion_test/bases/lala_berdiri_horizontal_base.jpg` — 2752x1536 landscape.
- Model berdiri, medium shot (mulut ke paha tengah), tangan kanan di pinggang + tangan kiri terulur ke kamera, cepol rendah + helai depan, celana putih, gelang emas tipis kanan, kalung emas.
- Background kamar asli: dinding krem, pintu kayu, AC, kasur kanan (bed cover kotak ungu + boneka plush).

## Frame-0 — LOLOS Gate 1 percobaan pertama
- File: `media-generation-frame0-katie-berdiri-0-879c67ba-2fd9-4e5d-9a96-afec1d6ef5d3.webp`
- Cek lawan foto asli: warna pink ✓, EXACTLY 5 pita hitam ✓, mutiara di tiap pita ✓, manset flare + hem scalloped ✓, framing mulut/dagu ✓, background identik ✓, celana putih + gelang ✓.
- Catatan: kalung emas dari base hampir tidak kelihatan di frame-0 (rantai samar) — bukan cacat produk.

## Video v1 — GAGAL Gate 3 (wajah penuh di 9.5 dtk)
- File mentah: `media-generation-katie-berdiri-v1-0-60cb1507-e421-4d0d-9313-94952eea7ae5.mp4` (1168x640, 10.0 dtk).
- Produk + background 0-6.5 dtk bagus semua (background 0 vs 0.6 dtk identik, ketajaman video malah lebih tajam dari frame-0).
- Cacat fatal: framing drift ke atas di akhir — wajah PENUH kelihatan di 9.5 dtk (mata kelihatan, senyum). Penyebab: beat akhir peace sign di dekat pipi + kamera seolah zoom out.
- v1 DIBUANG, tidak dipakai.

## Video v2 — LOLOS Gate 3 ✅ (FINAL)
- File: `katie_berdiri_v2_silent.mp4` (1168x640, 10.0 dtk, bisu) → upscale `katie_berdiri_v2_upscale720.mp4` (1280x720, 10.0 dtk, bisu).
- Perbaikan v2: klausul lock-off lebih keras (kamera tidak gerak/zoom/tilt sama sekali, framing tidak berubah) + beat akhir diganti (tangan di pinggang + wave RENDAH di pinggang, tidak naik ke wajah).
- Gate 3: background 0 vs 0.6 dtk identik ✓; 5 pita hitam + mutiara + manset flare + hem scalloped utuh di semua frame ✓; wajah HANYA mulut/dagu di semua frame, tidak ada mata/hidung/wajah penuh (9.5 dtk aman) ✓; ketajaman frame 2 dtk 102.1 vs frame-0 83.4 (lebih tajam, tanpa unsharp) ✓; tidak ada tas ✓; bisu ✓.
- Koreografi (berdiri): pinggang → sentuh pita dada → bentang dua tangan → angkat manset flare → muter samping dikit → pinggang + wave rendah.
- Cacat jujur v2: frame 0.6 dtk agak lembut (motion blur awal, sharpness 57.9) — tidak kelihatan saat diputar normal; pita ke-5 sempat ketutup tangan di 3.5 dtk (alami, bukan cacat); pose tangan kanan terulur dekat kamera = pose asli base, dipertahankan.

## Status
- Video final SIAP, belum di-upload ke Cloudinary, belum dicatat di sheet. Menunggu putusan Jendral.
- Base berdiri baru TERBUKTI JALAN (1 produk, 1 regen video karena wajah).

## Video v3 — koreografi review outfit Jendral — GAGAL Gate 3 (14 Nov ~12:30 WITA)
- Prompt Jendral (diterjemahkan ke prompt video + klausul lock-off/faceless): maju 1 langkah + membungkuk lihat jahitan kerah, gosok kedua tangan di dada, menyampingkan badan + tarik baju di perut, tanpa voice.
- File: `media-generation-katie-berdiri-v3-0-af6c7f60-a3aa-4b9a-9f4f-eef55b34d22e.mp4` → `katie_berdiri_v3_silent.mp4` (1168x640, 10.0 dtk, bisu).
- Cacat fatal: (1) kamera ZOOM IN jadi close-up dada di 2-3.5 dtk — produk tidak kelihatan utuh (cuma 2-4 pita, tanpa hem/manset/celana); (2) wajah PENUH + mata kelihatan di 9.5 dtk (kepala nunduk); hidung + pipi kelihatan di 6.5 dtk; (3) kulit perut ngintip dikit di pinggang 6.5 + 9.5 dtk (hem ketarik); (4) framing tidak terkunci (zoom in lalu zoom out). Background 0 vs 0.6 dtk identik ✓, beat gosok dada + tarik hem kebaca ✓.
- v3 DIBUANG.

## Video v4 — koreografi review DILEMAHKAN — GAGAL Gate 3 juga (14 Nov ~12:35 WITA)
- Perbaikan: maju 1 langkah KECIL + bungkuk SEDIKIT saja, kepala tetap tegak menghadap depan (tidak nunduk), tarik hem diganti sentuh/ratakan hem tanpa narik ke atas, tambah klausul "medium shot utuh tiap frame, kamera tidak zoom close-up".
- File: `media-generation-katie-berdiri-v4-0-13dccc59-3612-4cd6-b075-3a20156cba0b.mp4` → `katie_berdiri_v4_silent.mp4` (1168x640, 10.0 dtk, bisu).
- Cacat fatal: (1) wajah PENUH + mata kelihatan di 9.5 dtk LAGI (framing melebar/zoom out di akhir, kepala masuk frame); (2) muter samping di 3.5 dtk KEJAUHAN (profil 90°, pita depan tidak kelihatan sama sekali); (3) kulit perut ngintip dikit di pinggang 6.5 + 9.5 dtk; (4) framing tidak terkunci (lebih dekat di 2 dtk — hem + pita ke-5 kepotong bawah, lebih lebar di 9.5 dtk). Background 0 vs 0.6 dtk identik ✓, beat gosok dada + sentuh hem kebaca ✓.
- v4 DIBUANG. Dua kali gagal dengan arah koreografi yang sama = berhenti, lapor ke Jendral.

## DIAGNOSA (penting)
- Koreografi review (maju + bungkuk + nunduk lihat baju + tarik hem) BERTENTANGAN dengan 2 aturan keras: FACELESS dan KAMERA TERKUNCI. Generator menafsirkan "maju" sebagai zoom in, "bungkuk/nunduk" sebagai kepala masuk frame, "tarik hem" sebagai kulit ngintip.
- Bukti pola: v2 (TANPA maju/bungkuk, cuma gerakan tangan) LOLOS; v1 (peace sign dekat pipi) gagal wajah; v3 + v4 (maju + bungkuk) gagal wajah + framing.
- Opsi ke depan (menunggu Jendral): (a) pakai v2 sebagai video berdiri final; (b) coba koreografi review di format DUDUK (framing duduk jauh lebih stabil, sudah terbukti lolos Gate 3 berkali-kali); (c) koreografi review versi tangan saja sambil berdiri diam (tanpa maju/bungkuk).

## SOLUSI WAJAH — v4 dipotong ekor + crop atas (Jendral minta solusi 14 Nov ~12:29 WITA)
- Masalah: v4 "mundur kejauhan" di akhir — wajah mulai masuk di 8 dtk (hidung kelihatan), wajah PENUH + mata di 9-9.5 dtk.
- Solusi (deterministik, tanpa generate ulang): potong ekor di frame terakhir yang aman (7.5 dtk — mulut/dagu saja, tanpa hidung) + crop atas ~5% (32px dari 640) sebagai pengaman drift, lalu upscale 1280x720.
- File final: `katie_berdiri_v4_final_7s5.mp4` (1280x720, 7.5 dtk, bisu). Verifikasi frame akhir 7.4 dtk: TIDAK ADA wajah (potongan di leher/dagu), 5 pita ✓, background identik ✓; frame 0 setelah crop tetap utuh ✓.
- Cacat sisa (jujur): durasi 7.5 dtk bukan 10 dtk; ~3.5 dtk muter samping penuh 90° jadi pita depan tidak kelihatan ~1 dtk; ~2 dtk hem + pita ke-5 sempat kepotong bawah; kulit perut ngintip dikit di 2 frame saat sentuh hem.
## Video v5 — akhir DIAM total 3 dtk — GAGAL Gate 3 juga (14 Nov ~12:40 WITA)
- Jendral minta 10 dtk (v4 final cuma 7.5 dtk). v5: koreografi review 0-7 dtk + 3 dtk akhir DIAM TOTAL (tangan di pinggang, tanpa mundur, tanpa gerak kepala) + klausul "tidak pernah mundur, framing 10 dtk identik dengan 0 dtk".
- File: `media-generation-katie-berdiri-v5-0-ba4a7c67-1b62-430e-9a33-ab4add17eba2.mp4` → `katie_berdiri_v5_silent.mp4` (1168x640, 10.0 dtk, bisu).
- Cacat fatal: wajah masuk LAGI — hidung di 8 dtk, wajah PENUH + mata di 9.5 dtk — walau akhir diam total. Generator tetap menarik framing melebar di akhir (poster dinding kanan berubah/ganti gambar — background ikut drift). Background 0 vs 0.6 dtk identik ✓, produk utuh ✓, ketajaman semua frame ≥ frame-0 ✓.
- v5 DIBUANG. Pola akhir: video berdiri gagal wajah 4 dari 5 percobaan (v1, v3, v4, v5); hanya v2 (tanpa maju/bungkuk) yang lolos. Generator SELALU menarik framing melebar di akhir video berdiri dan memasukkan wajah, apapun koreografinya.

## Video v6 — prompt Jendral + NEGATIVE PROMPT jangan mundur — GAGAL Gate 3, tapi mundur TERATASI (14 Nov ~12:50 WITA)
- Jendral (12:37 WITA): "Coba prompt aku tadi itu dipakai lagi tapi kamu tambahkan negatif prompt untuk tidak mundur 1 langkah gitu, karna di video ini aku liat karakternya mundur 1 langkah, itu yang membuatnya menjadi kelihatan wajahnya" — diagnosis Jendral BENAR.
- Catatan: tool generate_video TIDAK punya kolom negative prompt terpisah — negatif prompt ditulis sebagai bagian "NEGATIVE PROMPT" tersendiri di dalam prompt.
- File: `media-generation-katie-berdiri-v6-0-f0c8a350-07f5-48c9-9a9c-3d868efb97a7.mp4` → `katie_berdiri_v6_silent.mp4` (1168x640, 10.0 dtk, bisu). Background 0 vs 0.6 dtk identik ✓, produk utuh di frame awal ✓, ketajaman ≥ frame-0 kecuali 2 dtk (75.0 vs 83.4, ~10% lebih lembut — masih OK).
- HASIL: negatif prompt BEKERJA untuk mundur — framing TIDAK melebar di akhir, tidak ada langkah mundur. TAPI gagal di sumbu baru: kepala NUNDUK saat membungkuk — wajah kelihatan dari samping/profil di 8 dtk (mata menunduk + hidung + bibir kelihatan) dan 9.5 dtk (wajah profil menunduk, mata kelihatan sebagian), PLUS muter samping penuh 90° (pita depan tidak kelihatan) dan kulit perut ngintip dikit. v6 DIBUANG.
- Pelajaran: dua penyebab wajah masuk di video berdiri adalah (1) MUNDUR (framing melebar) — sudah teratasi oleh negatif prompt; (2) NUNDUK saat membungkuk — belum teratasi, kepala harus tetap tegak.
- Ambil `katie_berdiri_v4_final_7s5.mp4` (7.5 dtk, faceless, 1280x720) + tahan frame terakhir 2.5 dtk (ffmpeg tpad stop_mode=clone).
- File final: `katie_berdiri_review_final_10s.mp4` (1280x720, 10.0 dtk, bisu). Verifikasi frame 9.5 dtk: frame beku yang sama dengan 7.4 dtk — TIDAK ADA wajah ✓, 5 pita ✓, background identik ✓.
- Cara pakai: 7.5 dtk gerakan review + 2.5 dtk tahan di pose akhir (tangan di hem). Trade-off jujur: 2.5 dtk terakhir itu gambar diam, kelihatan kalau diperhatikan — tapi wajah dijamin tidak muncul dan durasi pas 10 dtk.
- Pelajaran tetap: video berdiri SELALU rawan wajah masuk di akhir (generator mundur/melebarkan framing) — solusinya potong ekor di frame aman + freeze-frame sampai 10 dtk, JANGAN generate ulang berkali-kali.

## Video v7 — negatif prompt + kepala tegak — GAGAL Gate 3 di 2 titik singkat (14 Nov ~13:00 WITA)
- Kombinasi kedua perbaikan: prompt Jendral + negatif prompt (jangan mundur) + bungkuk hanya badan (kepala tegak, tidak nunduk) + muter samping hanya ~30°.
- File: `media-generation-katie-berdiri-v7-0-0568175c-7a9a-434d-8872-62550a774061.mp4` → `katie_berdiri_v7_silent.mp4` (1168x640, 10.0 dtk, bisu). Ketajaman semua frame ≥ frame-0 ✓, background 0 vs 0.6 dtk identik ✓.
- KEMAJUAN: negatif prompt BEKERJA — tidak ada mundur, framing tidak melebar, AKHIR video (9.5 dtk) BERSIH faceless ✓, 5 pita ✓.
- GAGAL di 2 titik singkat: (1) detik 2 — HIDUNG kelihatan (maju 1 langkah bikin framing makin dekat, wajah membesar masuk frame); (2) detik 8 — MATA profil kelihatan (muter samping, kepala ikut muter ke kamera, mata menunduk kelihatan). v7 DIBUANG.
- Verifikasi ulang video freeze 10 dtk (`katie_berdiri_review_final_10s.mp4`): frame 2 dan 6.5 dtk dicek ulang — hanya mulut/dagu di tepi atas, TIDAK ada hidung/mata — video itu FACELESS sepanjang durasi, aman dipakai.
- Pola akhir (5x gagal koreografi review di format berdiri): v3/v4/v5 gagal mundur di akhir; v6 gagal nunduk; v7 gagal hidung di 2 dtk + mata profil di 8 dtk. Setiap perbaikan menutup satu celah tapi membuka celah lain. Opsi ke Jendral: (a) pakai freeze 10s (sudah jadi, faceless); (b) coba review di format DUDUK (framing stabil); (c) coba sekali lagi berdiri tanpa maju + kepala kunci hadap depan saat muter.

## Video v8 — TANPA maju/mundur + kepala kunci hadap depan — GAGAL Gate 3 (14 Nov ~13:05 WITA)
- Jendral (12:47 WITA) soal video freeze 10 dtk: "10 detik tapi kamu freeze kan ini di detik detik akhir kwkw -_-" — freeze DITOLAK, minta video gerak beneran. v8: berdiri diam di tempat (TANPA maju/mundur sama sekali), bungkuk hanya badan kepala tegak, muter torso ~30° dengan kepala KUNCI hadap depan + negatif prompt diperluas (jangan maju, jangan mundur, jangan mendekat/menjauh, kepala jangan muter).
- File: `media-generation-katie-berdiri-v8-0-3c2c0c79-ea16-4056-8162-d8495a814eb5.mp4` → `katie_berdiri_v8_silent.mp4` (1168x640, 10.0 dtk, bisu). Ketajaman semua frame jauh ≥ frame-0 ✓, background 0 vs 0.6 dtk identik ✓.
- GAGAL: (1) detik 2 — HIDUNG kelihatan (dia tetap mendekat ke kamera walau prompt bilang jangan maju/mendekat); (2) detik 9.5 — PROFIL PENUH 90° (muter kejahuan, tidak balik ke depan, wajah profil kelihatan, pita depan tidak kelihatan). Tengah video (6.5 + 8 dtk) BERSIH — kepala kunci hadap depan BEKERJA saat muter, tapi generator tetap mendekat di awal dan muter penuh di akhir. v8 DIBUANG.
- KESIMPULAN (6x gagal koreografi review di format berdiri: v3, v4, v5, v6, v7, v8): setiap perbaikan menutup satu celah, generator membuka celah lain. Koreografi review (maju/bungkuk/muter) di format berdiri TIDAK BISA dijaga faceless dengan andal oleh generator ini. Berhenti generate versi berdiri — sisa opsi: (a) freeze 10s (satu-satunya video review 10 dtk yang faceless, tapi Jendral tidak suka ending bekunya); (b) coba koreografi review di format DUDUK (framing duduk terbukti stabil, semua video Korean Style lolos Gate 3).

## Video v9 — prompt v8 + TAG Jendral (/novoice /topfitcheck /fabricstroke /faceless) — GAGAL Gate 3 (14 Nov ~13:10 WITA)
- Jendral (12:53 WITA): "coba tabahkan ini di prompt kita itu /novoice /topfitcheck /fabricstroke /faceless" — tag ditambahkan verbatim sebagai entri teks tersendiri di akhir prompt, base prompt = v8 (berdiri diam, kepala kunci hadap depan + negatif prompt).
- File: `media-generation-katie-berdiri-v9-0-3c122de3-dd3f-4989-bb5d-a30b5923363b.mp4` → `katie_berdiri_v9_silent.mp4` (1168x640, 10.0 dtk, bisu). Ketajaman semua frame ≥ frame-0 (kecuali 6.5 dtk 81.2 vs 83.4, ~3% — abaikan) ✓, background 0 vs 0.6 dtk identik ✓.
- GAGAL: (1) detik 2 — HIDUNG kelihatan + framing terlalu dekat (hem + pita bawah kepotong di bawah frame); (2) detik 8 — PROFIL PENUH 90° (wajah profil kelihatan, pita depan tidak kelihatan). Bersih: 0.6, 6.5, 9.5 dtk. v9 DIBUANG.
- KESIMPULAN: tag TIDAK mengubah pola gagalnya — generator tetap mendekat di awal dan muter penuh di tengah video. Total 7x gagal koreografi review di format berdiri (v3-v9). Berhenti generate versi berdiri. Sisa opsi: freeze 10s (Jendral sudah tolak) atau coba review di format DUDUK.

## Video v9 — DISETUJUI Jendral (14 Nov ~12:56 WITA): "ini bagus dan memang gini harusnya"
- Jendral nonton video v9 langsung (bukan cuma frame QC) dan menilai BAGUS — "memang gini harusnya". Putusan Jendral MENGALAHKAN Gate 3 Igris: hidung di 2 dtk + mata profil di 8 dtk DINILAI BISA DITERIMA dalam gerakan — QC frame-per-frame Igris lebih ketat dari mata Jendral.
- Kalibrasi penting: yang TIDAK bisa diterima Jendral = wajah PENUH + mata yang jelas dan menetap (v3/v4/v5 di 9.5 dtk) dan framing melebar/mundur. Yang BISA diterima = momen wajah singkat saat bergerak (hidung sekilas, profil sekilas). Gate 3 ke depan: bedakan "wajah menetap/jelas" (GAGAL) vs "wajah sekilas saat bergerak" (toleransi, tanya Jendral).
- v9 = video review berdiri FINAL Katie: `katie_berdiri_v9_upscale720.mp4` (1280x720, 10.0 dtk, bisu). Upload Cloudinary `Katie-Berdiri-V9` (https://res.cloudinary.com/dpllb7idh/video/upload/v1794632205/Katie-Berdiri-V9.mp4) + dicatat di sheet Video Fashion No 25 (baris 26), "Siap tayang".
- Resep review berdiri yang JALAN (terbukti di v9): base foto Lala berdiri + prompt review (maju/bungkuk/gosok dada/menyamping/tarik hem) + negatif prompt (jangan mundur/maju/mendekat, kepala jangan nunduk/muter) + tag /novoice /topfitcheck /fabricstroke /faceless. Format berdiri TERBUKTI JALAN untuk produksi (v2 + v9 lolos di mata Jendral).
