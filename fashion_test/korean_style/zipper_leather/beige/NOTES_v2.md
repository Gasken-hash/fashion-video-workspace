# Beige Zipper Leather — NOTES v2 (remake)

## Produk
- **MAMAMARA - Cardigan Rajut Wol Zipper Leather Elegant Knit Jaket**
- Foto referensi (DARI LINK TOKOPEDIA Jendral): `tokopedia/tok_03_1e6a7dd63d95.jpg` — beige/sand ribbed knit, kerah kulit coklat pointed, resleting silver penuh, lengan panjang, hem lurus, fitted.
- Base: `cable_knit/base_pita_v3_frame0.jpg` (frame-0 Pita v3: dinding maroon, celana putih tali serut, tas hitam di lantai, cepol).

## v1 — GAGAL aturan baru (Jendral, 13 Nov 13:19 WITA)
- v1 (`beige_duduk_lilo_v1_silent.mp4`) lolos Gate 1 + Gate 3 versi lama, TAPI Jendral menemukan resleting TERBUKA DI ATAS (slider di tengah dada, dada kelihatan) — "ini bahaya kwkwk, jangan dibuka resletingnya, ntar kena banned wkkw".
- **ATURAN BARU (KERAS): resleting HARUS TERTUTUP PENUH kerah→hem di frame-0 DAN video — slider di ATAS tepat di bawah kerah, kedua panel bertemu rapat, TIDAK ADA kulit/dada kelihatan. Resleting terbuka = konten sugestif = risiko akun TikTok kena banned.** Gate 1 + Gate 3 wajib cek ini.

## v2 — Frame-0
- File: `media-generation-frame0-beige-duduk-lilo-v2-0-e127f5b4-c81d-418d-87ac-8cdec70fd06e.webp` (1168×2112)
- Fresh edit dari base + referensi, klausul eksplisit "silver zipper is FULLY CLOSED and zipped all the way up to the collar, slider at the very top just below the collar, both front panels meet completely, NO bare skin, NO cleavage".
- **Gate 1 LOLOS.** Cek resleting (zoom crop dada + hem): slider ATAS tepat di bawah kerah di antara flap kerah; garis resleting lurus dan tertutup penuh sampai hem; panel bertemu rapat; TIDAK ADA cleavage/kulit dada — yang kelihatan di atas kerah hanya LEHER (bawaan desain kerah kemeja, bukan bukaan). Slider kedua di hem = resleting dua arah; di foto referensi tok_03 juga ada slider bawah kecil di hem (dua arah, tertutup penuh) — jadi v2 cocok dengan referensi. Warna beige ✓, kerah kulit coklat ✓, lengan panjang ✓, hem lurus ✓, fitted ✓, framing mouth-cut tanpa mata ✓, celana/dinding/lantai/tas ✓.

## v2 — Video
- File mentah: `media-generation-beige-duduk-lilo-v2-0-69072dba-03ba-4a6d-b3ac-b21c5c2ba533.mp4` (640×1168, 10,0 dtk, ada audio AAC).
- Final: `beige_duduk_lilo_v2_silent.mp4` — **640×1110, 10,0 dtk, video-only (bisu, terverifikasi ffprobe; crop 58px atas, -an, crf 18)**.
- Koreografi: Set B (detail showcase) — rambut → angkat manset → sentuh kerah → telusuri resleting → cubit hem → pangkuan → peace sign. Prompt video membawa klausul resleting tertutup penuh + "hands only touch the closed zipper, never pull it or open it".
- **Gate 3 LOLOS.** Resleting TERTUTUP PENUH di SEMUA frame (0 / 0,6 / 2 / 3,5 / 6,5 / 9,5 dtk): slider tetap di atas, panel bertemu, tidak ada kulit dada. Background 0 vs 0,6 dtk identik (mean abs diff 6,54). Ketajaman: frame-0 69,8 → video 219,3 (0s) / 356,2 (0,6s) / 389,7 (2s) / 377,9 (3,5s) / 318,6 (6,5s) / 408,9 (9,5s) — video JAUH lebih tajam, tidak perlu unsharp. Mata tidak ada di frame manapun (top 9,5 dtk diperbesar: hanya mulut + dagu + peace sign). Badan tenang, hanya tangan bergerak. Beats lengkap kecuali "telusuri resleting" kurang crisp (lihat cacat).

## Cacat jujur
1. Chin/mouth peek di tepi atas — DITOLERANSI per aturan, dilaporkan.
2. Beat "telusuri resleting" tidak crisp — tidak ada momen jari tunggal menelusuri resleting atas→bawah yang tertangkap di frame sampel (sama seperti v1); tangan menyentuh kerah/resleting atas di 3,5 dtk.
3. Kalung emas tipis (bawaan base, bukan produk) terlihat di frame-0 dan semua frame.
4. Frame-0 agak lembut (69,8), tapi video jauh lebih tajam — detail tetap terbaca.
5. Slider kedua di hem (resleting dua arah) — cocok dengan referensi, bukan cacat.

## Status
- v2 SELESAI, Gate 1 + Gate 3 LOLOS, resleting tertutup penuh di semua frame.
- BELUM di-upload ke Cloudinary, BELUM dicatat di sheet — menunggu perintah parent.
- v1 (`beige_duduk_lilo_v1_silent.mp4`) TIDAK BOLEH dipakai — resleting terbuka di atas, bahaya banned.
