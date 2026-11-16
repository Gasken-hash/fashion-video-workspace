# Zipper Leather HITAM — NOTES

## Produk
- **MAMAMARA - Cardigan Rajut Wol Zipper Leather Elegant Knit Jaket**
- Link Jendral (Tokopedia/TikTok Shop): https://vt.tokopedia.com/t/ZS9fQ4E2wY1NS-4HREi/ (produk ID 1733971996534146644)
- Referensi (DARI LINK TOKOPEDIA, bukan Shopee): `tok_02_19a0a7f0642d.jpg` — hitam, kerah kulit coklat, resleting silver, lengan panjang.
- Base: frame-0 Pita v3 (`base_pita_v3_frame0.jpg`) — dinding maroon, celana putih tali serut, tas hitam di lantai, cepol.

## ATURAN KERAS (Jendral, 13 Nov 13:19 WITA)
Resleting HARUS TERTUTUP PENUH kerah→hem di frame-0 DAN video — slider di ATAS tepat di bawah kerah, kedua panel bertemu rapat, TIDAK ADA kulit/dada kelihatan. Resleting terbuka = konten sugestif = akun TikTok bisa kena banned. (Latar: Coklat gagal Gate 1 karena resleting bawah terbuka celah-V; Abu + Beige sempat terbuka di atas.)

## Frame-0
- `media-generation-frame0-hitam-duduk-lilo-v1-0-23098cb0-0b36-4453-8309-4735657f8ed2.webp` (1168x2112)
- **Gate 1 LOLOS** (13 Nov ~13:23 WITA).
- Cek resleting (zoom crop top + bottom): slider ATAS tepat di bawah kerah ✓, gigi resleting menyatu kerah→hem ✓, TIDAK ADA kulit/dada ✓, kerah tertutup di leher ✓.
- Detail lain: hitam ribbed ✓, kerah kulit coklat 2 flap ✓, lengan panjang ✓, hem lurus ✓, fitted ✓, framing mouth-cut tanpa mata ✓, celana putih + dinding/lantai/tas + cepol sama seperti base ✓.
- Cacat minor: (1) hem tengah bawah ada takik kecil (panels tidak 100% rapat di ujung hem, kelihatan celana putih — BUKAN kulit); (2) resleting tampak dua slider (atas + bawah) vs referensi satu slider di atas — sama seperti Abu, minor; (3) kalung emas tipis bawaan base.

## Video
- `hitam_duduk_lilo_v1_silent.mp4` — **640x1110, 10,0 dtk, video-only** (audio di-strip).
- File mentah: `media-generation-hitam-duduk-lilo-v1-0-39403924-d0b9-468a-8781-600a45f90ee0.mp4` (640x1168).
- Koreografi: **Set E (slow reveal), diadaptasi ke fitur Zipper** — tangan bersilang di pangkuan → naik sentuh kerah → bentang di dada → telusuri hem → pangkuan → side turn pelan → peace sign.
- **Gate 3 LOLOS** (13 Nov ~13:24 WITA).
- Resleting di SEMUA frame (0 / 0,6 / 2 / 3,5 / 6,5 / 9,5 dtk): TERTUTUP PENUH, slider di atas, TIDAK ADA kulit kelihatan. Takik hem TIDAK melebar di video.
- Ketajaman: frame-0 47,2 → video 160,0 (0s) / 115,3 (2s) / 105,5 (3,5s) / 150,2 (6,5s) / 107,0 (9,5s) — video LEBIH tajam, tidak perlu unsharp.
- Background 0 vs 0,6 dtk: visual identik (dinding/lantai/tas sama); mean abs diff 16,85 — selisih dari gerakan tangan (blur) + kompresi, bukan lompatan background.
- Mata: TIDAK ADA di frame manapun. Frame 9,5 dtk wajah profil saat side turn (hidung/bibir/dagu kelihatan, area mata terpotong tepi atas / tertutup rambut) — dicek perbesaran 2x dan 3x.
- Badan tenang, hanya tangan bergerak. Beats lengkap (kerah 2-3,5 dtk, dada/pangkuan 6,5 dtk, side turn + peace sign 9,5 dtk).
- Post-process: crop 58 px dari atas (~5%, drift insurance), `-an`, crf 18.

## Cacat jujur
1. Mulut + dagu kelihatan di tepi atas semua frame — framing mouth-cut yang DITOLERANSI Jendral; frame 9,5 dtk wajah profil (hidung/bibir/dagu), mata tidak kelihatan.
2. Takik kecil di hem tengah bawah (dari frame-0) — stabil, tidak melebar; yang kelihatan celana putih, bukan kulit.
3. Resleting dua slider (atas + bawah) vs referensi satu slider — minor, resletingnya sendiri tertutup penuh.
4. Kalung emas tipis bawaan base, konsisten di semua frame, bukan produk.
5. Beat "telusuri hem" tidak tertangkap crisp di frame sampel (tangan di dada/pinggang 6,5 dtk).
6. Frame 0,6 dtk tangan kiri motion blur (bergerak dari pinggang ke pangkuan) — gerakan normal.
7. Frame-0 agak lembut (47,2) tapi video lebih tajam — detail tetap terbaca.

## Status
- SELESAI, Gate 1 + Gate 3 LOLOS. Belum di-upload ke Cloudinary, belum dicatat di sheet — menunggu perintah parent.

## Upload + catat (15 Nov 2026 ~04:00 WITA, aturan otomatis baru)
Hitam v1 di-upload ke Cloudinary `ZipperLeather-Hitam-V1` (v1794686270), dicatat sheet "Video Fashion" No 41 "Siap tayang", Harga kosong (seperti Krem No 11), read-back terverifikasi.
