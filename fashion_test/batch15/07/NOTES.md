# Product 07 — Cardigan Rajut Wol Ruffle Tali Depan — DONE

**Produk:** MAMAMARA Cardigan Rajut Wol Ruffle Tali Depan Knit Lengan Panjang Lembut Daily Wear
**Product ID:** 1734405129335178836
**Link (Jendral):** https://vt.tokopedia.com/t/ZS9fQg8u4nTjV-k5QqH/
**Referensi:** `tok_00.jpg` (dari link Tokopedia Jendral via curl-cffi; BUKAN Shopee)
**Base:** `bases/base_pita_v3_tas.jpg` (Pita v3 frame-0, tas hitam di lantai kanan bawah)
**Gerakan:** Set E adaptasi — tangan silang di pangkuan → sentuh tali pita leher → dada → telusur hem → pangkuan → muter samping pelan → peace sign
**Tanggal:** 13 Nov 2026

## Gate 1 — LULUS (frame-0 pertama, tanpa perbaikan)

Frame-0: `frame0_ruffle_tali.jpg` (1168x2112, ketajaman 38.6 — agak lembut, tapi video jauh lebih tajam)
Cek detail lawan referensi `tok_00.jpg`:
- Warna kuning pucat / krem ✓
- Kerah bulat ribbed ✓
- Tali pita di leher depan, diikat jadi bow + 2 ekor gantung ✓ (1 tali, posisi benar)
- Kancing: 5 kancing bulat kecil di tengah depan ✓ (sama jumlahnya dengan referensi)
- Kabel vertikal: 2 kolom braided di kedua sisi kancing ✓
- Lengan panjang, menempel di bahu, manset ribbed polos (tanpa ruffle) ✓
- Hem ribbed, panjang sampai pinggul ✓
- Fit agak longgar, rajut fuzzy lembut ✓
- 6 pita pink base HILANG semua, kancing mutiara HILANG, manset ruffle HILANG ✓
- Rambut cepol (diikat ke atas, bukan terurai seperti base) ✓
- Framing potong mulut — mata tidak kelihatan ✓
- Base dipertahankan: dinding maroon, celana putih drawstring, tas hitam di lantai kanan bawah, lantai speckled, pose duduk, tangan di pinggang ✓

## Gate 3 — LULUS

Video mentah: `media-generation-ruffle-tali-duduk-lilo-v1-0-a5aa83ea-89ba-4240-800f-5b45b9128e41.mp4` (640x1168, 24fps, 10.0s, h264 + audio AAC bawaan generator — di-strip di final)
- Background 0 vs 0.6 dtk: identik ✓ (dinding, lantai, tas tidak bergerak)
- Mata/wajah penuh: tidak muncul di frame manapun — top 9.5 dtk diperbesar, cuma mulut + dagu ✓; top 6.5 dtk juga dicek ✓
- Detail produk utuh di semua frame (0/2/3.5/6.5/9.5): tali pita, 5 kancing, kabel, warna — tidak ada detail inventaris (tidak ada pita tambahan, tidak ada pita pergelangan) ✓
- Beat gerakan: 2 dtk tangan kanan sentuh tali pita, 3.5 dtk kedua tangan di tali pita, 6.5 dtk kedua tangan telusur hem, 9.5 dtk peace sign jelas ✓
- Ketajaman: frame-0 36.6 → video 2 dtk 132.6, 3.5 dtk 147.0, 6.5 dtk 108.2, 9.5 dtk 125.9 — video JAUH lebih tajam dari frame-0, tanpa unsharp ✓
- Gerakan tenang, hanya tangan; torso/bahu/dada diam ✓

## Final

**`ruffle_tali_duduk_lilo_v1_upscale720.mp4`** — 720x1280, 24fps, 10.0s, 3.68 MB, video-only (audio di-strip, ffprobe: hanya stream h264, tidak ada audio).
Finishing: crop atas 60px (drift guard) + upscale lanczos crf 18 preset slow.
Ketajaman frame 3.5 dtk final: 105.4.
Frame 3.5 dtk final: `g3_final_3.5s.jpg`.

## Cacat jujur
1. Kalung emas kecil dari base kelihatan di kerah (artefak base, sama kayak Krem/Beige/Hitam).
2. Bow tali pita di frame-0/video agak lebih besar dan longgar dari referensi (bow kecil rapi di foto asli), ekornya lebih panjang — desainnya sama (1 tali, bow di leher, 2 ekor), cuma ukurannya sedikit lebih besar.
3. Framing di 6.5 dtk sedikit lebih rapat dari frame-0 (model tampak sedikit lebih dekat) — background tetap beku, produk utuh.
4. Frame-0 sendiri agak lembut (ketajaman 38.6), tapi videonya jauh lebih tajam, jadi final tidak kelihatan lembut.
5. Dagu/mulut ngintip di tepi atas (ditoleransi).
6. Beat "muter samping pelan" halus saja — tidak ada putaran samping yang kentara; beat hem-trace yang paling jelas.

## Pemakaian
- 1 image call (frame-0) + 1 video call. Tidak ada penolakan generator, tidak ada retry.
- Belum di-upload ke Cloudinary / dicatat di sheet — menunggu persetujuan Jendral (aturan: upload + log hanya setelah approval).
