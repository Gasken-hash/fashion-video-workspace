# LUCY Top (batch-16 #09) — NOTES

**Produk:** Atasan Wanita LUCY TOP Polka Top Korean Styles — Tokopedia ID 1736817298189354449, showcase SUDAH ADA.
**Referensi:** `tok_00.jpg` (800×800) — atasan tanpa lengan, dasar putih, polkadot hitam kecil, leher bulat lis renda HITAM, EXACTLY 7 kancing kecil hitam di depan tengah, hem peplum/ruffle lis renda HITAM di tepi bawah, rok mini hitam. Varian putih.

## KOREKSI PENTING — catatan refs SALAH, foto yang benar
BATCH16_REFS.md dan brief awal menulis "5 kancing" dan "lis renda PUTIH". Setelah diperbesar (crop torso + leher), foto asli membuktikan:
- **Kancing = 7 buah** (bukan 5), kecil hitam, jarak rata dari bawah kerah sampai jahitan pinggang/peplum.
- **Lis renda = HITAM** (bukan putih), di leher bulat DAN di tepi bawah ruffle peplum.
Frame-0 dan video dibuat dengan angka yang BENAR (7 kancing, renda hitam). Kalau ikut catatan yang salah, produknya jadi beda dan Gate 1 yang benar akan gagal — ini persis jenis kesalahan yang memicu pelanggaran TikTok.

## Base
`~/workspace/fashion_test/bases/base_pita_v3_kacamata.jpg` (1536×2752, Pita v3 frame-0, kacamata di lantai kanan bawah, dinding maroon, lantai speckled).

## Gate 1 — LOLOS (frame-0 v1, tanpa perbaikan)
File: `media-generation-frame0-lucy-v1-0-c526f55e-bd8f-4370-93fd-0c0bd45eca47.webp`
- Dasar putih ✓, polkadot hitam kecil rapat rata ✓, leher bulat lis renda HITAM ✓, EXACTLY 7 kancing kecil hitam jarak rata ✓, bodice fitted ✓, peplum ruffle mengembang di pinggang dengan lis renda HITAM di tepi bawah ✓, tanpa lengan ✓, rok mini hitam plisket ✓.
- Framing potong mulut/dagu, mata tidak kelihatan ✓; cepol tinggi longgar + helai depan membingkai wajah ✓; dinding maroon + lantai + kacamata dipertahankan ✓.
- **Penilaian identitas (aturan 95%): ~97–98%.** Tidak ada penyimpangan atribut produk. Satu-satunya penyimpangan render: lis renda di lubang lengan sedikit lebih menonjol/berenda dibanding foto asli (di foto asli trim lubang lengan tipis); pola dot sedikit lebih besar. Bukan perubahan atribut produk.

## Video — v1 (tanpa regen)
File raw: `media-generation-lucy-duduk-lilo-v1-0-62db2010-67d8-459f-9064-8f1059f9a5e9.mp4` (640×1168, 10,0 dtk, 24fps, h264, ada audio stream bawaan generator).
Gerakan (Set B adaptasi fitur): rambut → sentuh kerah renda → sentuh kancing → telusuri polkadot di dada → hem renda → rok → pangkuan → peace sign di level dada (9,5 dtk).
Post-proses: crop atas 58px → buang audio → upscale lanczos 720×1280, crf 18, preset slow.
**Final:** `lucy_duduk_lilo_v1_upscale720.mp4` — 720×1280, h264, 24fps, 10,0 dtk, video-only (silent, 1 stream video), 4.097.866 byte. Terverifikasi ffprobe.

## Gate 3 — LOLOS (video v1)
- Background 0 vs 0,6 dtk identik (beku); dinding/lantai/kacamata tidak bergerak.
- Produk IDENTIK ≥95% di semua frame 0/2/3,5/6,5/9,5 dtk: 7 kancing tetap 7 di semua frame, renda hitam tetap hitam, dot kecil rapat, peplum + rok mini hitam tidak berubah. Tidak ada detail diciptakan/dihilangkan di tengah jalan.
- Mata/wajah penuh tidak ada di frame mana pun. Cek bagian atas frame 9,5 dtk yang diperbesar: mulut + dagu + UJUNG HIDUNG saja di tepi atas (dalam toleransi kalibrasi Jendral 14 Nov 13:31 — hidung boleh, full face tidak); setelah crop 58px terpotong lebih jauh.
- Ketajaman (Laplacian): frame-0 193,3; video 2 dtk 922,2; 3,5 dtk 838,8; 6,5 dtk 864,3; 9,5 dtk 869,4 — video TIDAK lebih lembut dari frame-0, tanpa unsharp (angka tinggi didominasi pola polkadot yang rapat, sama seperti Batik).
- **Penilaian identitas video (aturan 95%): ~97–98%, sama seperti frame-0.** Beat "sentuh kancing" di 3,5 dtk menutupi sebagian kancing atas dengan jari — kancing tetap terlihat penuh dan utuh di frame lain.

## Daftar cacat jujur
1. Kalung emas tipis dari base kelihatan di kerah di semua frame (artefak base; model di foto referensi juga memakai kalung tipis, jadi bukan ketidakcocokan produk).
2. Mulut/dagu ngintip di tepi atas sepanjang video (dalam toleransi); ujung hidung tampak sekilas di 9,5 dtk (dalam toleransi kalibrasi, terpotong oleh crop atas di final).
3. Tangan motion-blur saat bergerak di 2 dtk (sentuh rambut); terbaca jelas di frame berikutnya.
4. Beat "sentuh kancing" di 3,5 dtk menutupi sebagian kancing atas — kancing tetap utuh di frame lain.
5. Tangan kanan bertumpu di pinggang di frame-0/0 dtk (pose bawaan base).
6. Lis renda lubang lengan sedikit lebih berenda/menonjol dari foto asli (render, bukan atribut produk).

## Status
- TIDAK di-upload ke Cloudinary, TIDAK dicatat ke sheet (menunggu persetujuan Jendral).
- Satu video ini saja — tidak ada produk lain yang dikerjakan.
