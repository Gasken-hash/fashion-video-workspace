# 01 Tank Top — NOTES (batch-16, duduk, LILO)

## Produk
- Tank Top Wanita Bahan Adem Motif Bunga, Polkadot & Marble | Inner Kerut Smock Pleats Top High Neck Anti Nerawang | Tank Top Dalaman Baju Hijab Stretch Melar | Singlet Wanita LD 60-115
- Tokopedia ID 1736879989853553817 | shortlink ZS9fqPBmffLDQ-l9Ac9 | Showcase: SUDAH ADA
- Ref: `tok_00.jpg` (600×800) — tank top TANPA LENGAN hitam motif bunga pink, high neck dengan ruffle kecil di leher, badan kerut/smock penuh, hem peplum/ruffle melebar; rok plisket mini hitam.
- TIDAK ada resleting di produk ini.

## Base
- `~/workspace/fashion_test/bases/base_pita_v3_tas.jpg` (1536×2752) — duduk, dinding maroon hangat, lantai speckled, tas hitam di lantai kanan bawah (prop statis; giliran TAS per rotasi).

## Frame-0 v1 — GATE 1 LOLOS (percobaan pertama, tanpa perbaikan)
- File: `media-generation-frame0-tanktop-v1-0-052841a5-7b67-4a7a-a3c2-3c9ba64e6ca9.webp`
- Cek detail vs tok_00.jpg: warna HITAM ✓; motif bunga pink kecil tersebar ✓; high neck dengan ruffle kecil ✓; smock/kerut horizontal penuh dari leher sampai hem ✓; tanpa lengan (bahu + lengan telanjang, armhole melengkung halus) ✓; tanpa kancing/pita ✓; hem melebar ruffle lembut ✓; rok plisket mini hitam, lipatan vertikal rapi, waistband halus ✓; framing potong mulut/dagu, mata TIDAK kelihatan ✓; rambut cepol tinggi longgar + helai depan ✓; pose duduk, dinding maroon, lantai, tas di lantai — semua dipertahankan ✓.

## Video — GATE 3 LOLOS
- Raw: `media-generation-tanktop-duduk-lilo-v1-0-24d307e4-c92b-4250-ab1f-ce8603d99ad9.mp4` (640×1168, 24fps, 10.0s; bawa track audio AAC — dibuang di final).
- Gerakan (Set B adaptasi fitur): rambut → sentuh tali bahu → sentuh high neck → telusuri kerut smock di dada → hem → rok → pangkuan → peace sign di akhir.
- Cek frame 0 / 0.6 / 2 / 3.5 / 6.5 / 9.5 dtk:
  - Background 0 vs 0.6 dtk: IDENTIK (dinding maroon, lantai speckled, tas kanan bawah tidak bergerak) ✓
  - Produk IDENTIK di semua frame (smock, motif bunga, leher ruffle, rok plisket) — tidak ada detail yang diciptakan/dihilangkan ✓
  - Mata/wajah penuh: TIDAK ADA di frame mana pun; cek bagian atas frame 9.5 dtk yang diperbesar (`g3_top95.jpg`) = mulut + dagu saja ✓
  - Ketajaman (Laplacian): frame-0 99,9; video 2 dtk 324,1; 3,5 dtk 234,1; 9,5 dtk 311,0 — video TIDAK lebih lembut dari frame-0, tanpa unsharp ✓
  - Peace sign jelas terbentuk di 9,5 dtk di level dada (bukan dekat wajah) ✓
  - Gerakan tenang, bahu/dada diam, tangan saja yang bergerak ✓

## Post-proses (deterministik)
- Crop atas 58px (~5%, pengaman mata drift) → buang audio → upscale 720×1280 (ffmpeg lanczos, libx264, crf 18, preset slow).
- Final: `tanktop_duduk_lilo_v1_upscale720.mp4` — 720×1280, 10.0 dtk, h264, video-only (silent), ~3,5 MB. Terverifikasi ffprobe.
- Frame 3,5 dtk final: `tanktop_3.5s.jpg` (diambil dari file final).

## Daftar cacat jujur
1. Kalung emas tipis dari base kelihatan di kerah di semua frame (artefak base; model di foto referensi juga memakai kalung tipis, jadi bukan ketidakcocokan produk).
2. Mulut/dagu ngintip di tepi atas sepanjang video (dalam toleransi Jendral).
3. Tangan motion-blur saat bergerak di 0,6 / 2 / 3,5 dtk (blur gerakan normal; tangan terbaca jelas di 6,5 / 9,5 dtk).
4. Beat "telusuri kerut smock" di 3,5 dtk sebagian tertutup tangan yang bergerak — smocking tetap terlihat penuh di frame lain.
5. Tangan kanan bertumpu di pinggang di frame-0/0 dtk (pose bawaan base, bukan cacat).

## Status
- Video SELESAI dan lolos Gate 1 + Gate 3. Belum di-upload ke Cloudinary, belum dicatat ke sheet — menunggu persetujuan Jendral (sesuai tugas).
