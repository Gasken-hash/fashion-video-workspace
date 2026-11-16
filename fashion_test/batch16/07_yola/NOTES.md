# YOLA — batch-16 #07 — NOTES

Produk: YOLA t-shirt Off Shoulder Gaya Korea (hitam), Tokopedia ID 1738268288670401577.
Ref: `tok_00.jpg` (varian hitam, foto utama). Bawahan ikut ref: jeans gelap wash.
Jendral menyetujui percobaan YOLA 14 Nov 2026 ~23:50 WITA ("coba yola itu").
Base: `~/workspace/fashion_test/bases/base_pita_v3_tumbler.jpg` (duduk, dinding maroon hangat, tumbler hitam).

## Produk (dicek visual dari tok_00.jpg)
- T-shirt hitam solid, slim fit, LENGAN PENDEK, crop (hem tepat di atas pinggang jeans).
- Off-shoulder ASIMETRIS by design: bahu KANAN model terbuka dengan tali gingham biru-putih tipis di atas bahu; bahu KIRI tertutup lengan pendek hitam (lengan sisi terbuka menjuntai di lengan atas).
- Pinggang SERUT: kerutan vertikal (ruched) di kedua sisi pinggang.
- Hem bawah: ruffle flounce lebar motif kotak gingham biru-putih.
- Bawahan: jeans gelap wash. Tanpa resleting.

## Gate 1 — LOLOS (frame-0 v1, pertama jalan)
File: `media-generation-frame0-yola-v1-0-20b90d1d-7303-42c4-b00a-100cfef25752.webp` (ketajaman Laplacian 208,7).
Cocok detail per detail lawan tok_00.jpg: hitam solid ✓, lengan pendek ✓, off-shoulder asimetris + tali gingham ✓, pinggang serut ✓, ruffle gingham di hem ✓, crop ✓, jeans gelap ✓, slim fit ✓, cepol tinggi longgar + helai depan ✓, framing potong mulut/dagu (mata tidak kelihatan) ✓, dinding maroon + lantai + tumbler ✓.
Gelang emas tipis di pergelangan KANAN ✓ (aturan aksesoris lengan pendek, Jendral 14 Nov 23:49 WITA — YOLA kandidat pertama).
**Penilaian identitas produk ≥95%: ~96%.**
Observasi (bukan penyimpangan produk): sisi bahu yang terbuka TERCERMIN dari referensi — di foto asli bahu kanan yang terbuka, di frame-0 bahu kiri. Desainnya sama persis (satu bahu terbuka + tali gingham, satu lengan pendek), cuma kiri-kanan kebalik karena pose duduk menghadap depan. Artefak pose, sama seperti hem diagonal MOKA yang tercermin dan tetap lolos.

## Gate 3 — LOLOS (video v1, tanpa regen)
Raw: `media-generation-yola-duduk-lilo-v1-0-40994323-3cc1-4b8f-a4c8-5b17d0b05a88.mp4` (640×1168, 10,0 dtk, audio dibuang).
- Background 0 vs 0,6 dtk identik (beku) ✓.
- Produk IDENTIK ≥95% di semua frame 0/2/3,5/6,5/9,5 dtk — hitam tetap, off-shoulder + tali gingham tetap, serut tetap, ruffle gingham tetap, jeans tetap; tidak ada detail diciptakan/dihilangkan di tengah jalan.
- Ketajaman (Laplacian): frame-0 208,7; video 0s 315,2; 0,6s 294,7; 2s 318,8; 3,5s 372,8; 6,5s 255,5; 9,5s 355,6 — video tidak lebih lembut dari frame-0, tanpa unsharp.
- Mata/wajah penuh tidak ada di frame mana pun; bagian atas frame 9,5 dtk yang diperbesar 2x = mulut + dagu saja, tanpa mata (dalam toleransi kalibrasi).
- Gerakan tenang, bahu/dada diam, tangan saja: 2 dtk sentuh rambut, 3,5 dtk sentuh ruffle/dada, 6,5 dtk cubit ruffle hem, 9,5 dtk peace sign jelas di level dada.
- GELANG: gelang emas tipis di pergelangan KANAN terlihat di semua frame yang pergelangannya kelihatan (0s tangan di pinggang, 2s tangan di rambut, 3,5s tangan di dada, 6,5s tangan di hem, 9,5s tangan di pangkuan) — menempel, tidak melayang/hilang ✓.
- Beat "telusuri pinggang serut" tidak tertangkap sebagai beat terpisah (tangan langsung dada → hem), tapi pinggang serut terlihat jelas di semua frame.

## Post-proses
Crop atas 58px → buang audio → upscale lanczos 720×1280, crf 18, preset slow.
Final: `yola_duduk_lilo_v1_upscale720.mp4` — ffprobe: 720×1280, h264, 24fps, 10,0 dtk, 4,1 MB, 1 stream video saja (tidak ada stream audio = silent).
Frame 3,5 dtk: `yola_3.5s.jpg`.

## Daftar cacat jujur
1. Kalung emas tipis dari base kelihatan di kerah di semua frame (artefak base; model di foto referensi juga memakai kalung tipis, bukan ketidakcocokan produk).
2. Mulut/dagu ngintip di tepi atas sepanjang video (dalam toleransi).
3. Sisi bahu terbuka tercermin dari referensi (lihat observasi Gate 1).
4. Rantai emas tipis TAMBAHAN di pergelangan KIRI (generator menambahkan; base punya jam di pergelangan kiri). Tipis, tidak menutupi produk, konsisten menempel di semua frame — bukan produk, tidak dihitung ke persen identitas.
5. Tangan kiri motion-blur saat bergerak di 2 dtk; terbaca jelas di frame berikutnya.
6. Tangan kanan bertumpu di pinggang di frame-0/0 dtk (pose bawaan base).

## Status
Tidak di-upload ke Cloudinary, tidak dicatat ke sheet (menunggu persetujuan Jendral).
Batch-16: 9/10 video selesai. Tersisa 10 HAILEY (dihold, halterneck, menunggu keputusan Jendral).
