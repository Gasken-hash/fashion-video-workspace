# MOKA Top — batch-16 #06 — NOTES.md

Produk: Atasan Wanita MOKA TOP Polka Renda Kekinian (Tokopedia ID 1737435938375501265, showcase SUDAH ADA)
Ref: `06_moka/tok_00.jpg` — atasan tanpa lengan polkadot hitam di dasar putih, leher bulat, hem asimetris miring dengan renda putih di sepanjang hem bawah, fit longgar A-line; bawahan celana pendek putih.
Base: `bases/base_pita_v3_tumbler.jpg` (1536x2752, duduk, dinding maroon, tumbler hitam di lantai kanan bawah).
Format: duduk vertikal 9:16, resep LILO. Gerakan disesuaikan fitur produk (leher bulat → polkadot dada → renda hem asimetris → celana → pangkuan → peace sign).

## Gate 1 — LOLOS (frame-0 v1, tanpa perbaikan)
File: `media-generation-frame0-moka-v1-0-2578fa05-86df-47ec-9e06-37d9b220ae3d.webp` (ketajaman Laplacian 229,7)
Cek detail lawan tok_00.jpg:
- Warna: dasar putih, polkadot hitam ✓
- Motif: titik hitam kecil bulat, rapat merata di seluruh atasan ✓
- Kerah: leher bulat (crew neck) ✓
- Lengan: tanpa lengan, lengan telanjang ✓
- Kancing: tidak ada (sesuai ref, tidak ada kancing) ✓
- Hem: ASIMETRIS DIAGONAL, satu sisi lebih panjang, renda putih bunga (scalloped) mengikuti garis diagonal di sepanjang tepi hem ✓
- Fit: longgar A-line, sedikit melebar ke bawah ✓
- Bawahan: celana pendek putih polos ✓
- Framing: potong mulut/dagu, mata tidak kelihatan ✓
- Rambut: cepol tinggi longgar + helai depan membingkai wajah ✓
- Background: dinding maroon + lantai speckled + tumbler dipertahankan ✓
- Penilaian identitas produk: ≥95% — semua fitur penentu produk cocok. Satu observasi (BUKAN penyimpangan produk): arah miring diagonal di frame-0 cermin dari foto referensi — di ref diagonal turun ke sisi kiri model, di frame-0 turun ke sisi kanan model. Ini artefak pose/kamera (model duduk menghadap depan vs model berdiri agak miring di ref); fitur hemnya sendiri (asimetris diagonal + renda putih) hadir penuh dan sama bentuknya.

## Gate 3 — LOLOS (video v1, tanpa regen)
Raw: `media-generation-moka-duduk-lilo-v1-0-5c9cb5e8-b79f-44c5-9974-9a533abcee6d.mp4` (640x1168, 10,0 dtk, 24fps, audio generator -48,9 dB, sudah dibuang)
- Background 0 vs 0,6 dtk IDENTIK (beku) ✓
- Produk IDENTIK ≥95% di semua frame 0/2/3,5/6,5/9,5 dtk: polkadot tetap, leher bulat tetap, hem diagonal + renda tetap, celana pendek putih tetap; tidak ada detail diciptakan/dihilangkan (tanpa kancing, tanpa pita, tanpa trim tambahan) ✓
- Beat tertangkap: 2 dtk tangan di leher bulat; 3,5 dtk telusuri polkadot dada; 6,5 dtk telusuri renda hem → celana; 9,5 dtk peace sign jelas di level dada ✓
- Mata/wajah penuh: TIDAK ADA di frame mana pun; cek bagian atas frame 9,5 dtk yang diperbesar 2x = mulut + dagu saja, tanpa mata, tanpa hidung ✓
- Ketajaman (Laplacian): frame-0 229,7; video 2 dtk 561,7; 3,5 dtk 575,2; 6,5 dtk 792,6; 9,5 dtk 752,4 — video TIDAK lebih lembut dari frame-0, tanpa unsharp ✓
- Gerakan tenang, bahu/dada diam, sesuai resep ✓

## Post-proses
Crop atas 58px (~5%) → buang audio → upscale lanczos 720x1280, crf 18, preset slow.
Final: `moka_duduk_lilo_v1_upscale720.mp4` — terverifikasi ffprobe: 720x1280, h264, 24fps, 10,0 dtk, 1 stream video saja (silent).

## Daftar cacat jujur
1. Kalung emas tipis dari base kelihatan di kerah di semua frame (artefak base, bukan produk — tidak dihitung ke persen identitas produk).
2. Mulut/dagu ngintip di tepi atas sepanjang video (dalam toleransi).
3. Tangan kiri sedikit motion-blur saat bergerak di 3,5 dtk; terbaca jelas di frame lain.
4. Di 2 dtk framing sedikit mengetat saat kepala menengadah (tetap mulut/dagu saja, tanpa mata).
5. Arah miring diagonal hem cermin dari foto referensi (lihat observasi Gate 1) — fitur hemnya sendiri cocok penuh.
6. Tangan kanan bertumpu di pinggang di frame-0/0 dtk (pose bawaan base).

## File
- Frame-0: `media-generation-frame0-moka-v1-0-2578fa05-86df-47ec-9e06-37d9b220ae3d.webp`
- Video final: `moka_duduk_lilo_v1_upscale720.mp4`
- Frame 3,5 dtk: `moka_3.5s.jpg` (+ `g3_f*.jpg` frame QC)
- Foto referensi asli: `tok_00.jpg`
- Tidak ada upload Cloudinary, tidak ada pencatatan sheet (sesuai tugas — urusan parent setelah persetujuan Jendral).
