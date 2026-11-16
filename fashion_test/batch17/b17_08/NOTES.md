# b17_08 — Vintage Diamond Pattern Cartoon Knitted Vest

- Tokopedia ID: (lihat products.json b17_08)
- Shortlink: https://vt.tokopedia.com/t/ZS9fsA2fMu86r-21F7a/
- Full name: Vintage Diamond Pattern Cartoon Knitted Vest for Women Outerwear Top Vest
- Mode: DUDUK (sitting, maroon wall, LILO). Base: base_pita_v3_tas.jpg (prop tas — rotasi tumbler -> tas).
- Bottoms: jeans biru (ngikutin foto seller tok_00).
- **STATUS: BELUM SELESAI — video GAGAL Gate 3 tiga kali (v1, v2, v3), semua karena generator nambah beruang outline di sel wajik kiri bawah. TIDAK di-upload, TIDAK dicatat di sheet. Perlu pendekatan lain di batch berikutnya.**

## Produk (dari galeri, 10 foto, tok_00..tok_09)
- Referensi: tok_00.jpg (model pakai vest hijau+beige + jeans biru, full shot) + tok_01.jpg (vest di gantungan, pola paling jelas).
- Vest RAJUT TANPA LENGAN, motif WAJIK/ARGYLE HIJAU + BEIGE (krem).
- **TEPAT 3 beruang kartun** di sel wajik (masing-masing ada hati di perutnya): (1) beruang HIJAU BESAR di dada kiri (hati putih outline), (2) beruang BEIGE di dada kanan (hati hijau), (3) beruang HIJAU di bawah tengah (hati putih). **VERIFIKASI crop+perbesar foto asli (tok_00_lower2x.jpg + tok_01_lower2x.jpg, 15 Nov 17:05): sel wajik beige di KIRI BAWAH POLOS, tidak ada beruang — jadi beruang ke-4 di video adalah karangan AI, bukan produk asli.**
- Leher V dengan trim ribbed; trim ribbed di armhole + hem ribbed.
- Dipakai di atas KEMEJA PUTIH berkerah (lengan panjang, kerah lancip polos) — layer styling, tapi penting buat tampilan produk (vest V-neck selalu dipakai di atas kemeja di foto seller).
- Varian: hijau + beige (tok_00/tok_01, utama), hitam + putih (tok_02).
- Pita hitam di leher kemeja (tok_01) + jam coklat (tok_02) = styling, BUKAN produk (tidak dipakai di video).

## Frame-0 (Gate 1)
- v1: LOLOS Gate 1 ~95-96% sekali jalan. Wajik hijau+beige, 3 beruang (posisi/warna/hati benar), V-neck, ribbed trim, kemeja putih, jeans biru, dinding MAROON benar, tas hitam di lantai kanan bawah. **Cacat minor: beruang di frame-0 LEBIH BESAR dari aslinya (menjangkau ~2 baris wajik, aslinya ~1 sel) — dicatat, kemungkinan ini pemicu drift video.** File: media-generation-frame0-b17-08-v1-0-5ab94524-7e77-4400-86de-32c0f1ba3cd3.webp

## Video (Gate 3) — GAGAL 3x, pola drift yang sama
- **v1 (Set B, detail showcase)**: GAGAL Gate 3. Mulai 2s, vest nambah DUA beruang OUTLINE (kiri bawah + kanan bawah) — jumlah beruang 3 -> 5. Pola wajik, V-neck, kemeja, jeans, dinding, faceless semua benar; peace 1x di 9.5s benar. Tapi jumlah beruang salah = produk tidak identik.
- **v2 (Set B, prompt diperkuat "tepat 3 beruang, tidak ada outline")**: GAGAL Gate 3. Lebih baik (beruang outline kanan bawah hilang), tapi beruang OUTLINE KIRI BAWAH tetap ada dari 2s sampai 9.5s — jumlah beruang 3 -> 4. Peace 1x di 9.5s benar.
- **v3 (koreografi diubah: tangan TIDAK sentuh beruang/wajik, cuma rambut -> hem -> jeans -> peace; prompt tambah "sel wajik kiri bawah KOSONG dan polos")**: GAGAL Gate 3. Di 2s beruang masih 3 (benar!), tapi di 3.5s beruang outline kiri bawah MUNCUL LAGI dan bertahan sampai 6.5s (peace malah muncul lebih awal di 6.5s). Drift muncul saat tangan menyentuh hem (bagian bawah vest) — generator me-render ulang vest dan nambah beruang outline di sel kiri bawah.
- **v4 (frame-0 v3, koreografi tangan TIDAK sentuh vest sama sekali — cuma rambut, pangkuan, jeans, peace)**: GAGAL Gate 3. Generator tetap nambah **beruang BEIGE KECIL (penuh, bukan outline) di sel wajik kiri bawah** dari 2s sampai 6.5s — jumlah beruang 3 -> 4. Jadi "tangan tidak sentuh vest" TIDAK mencegah drift. **KESIMPULAN (15 Nov ~17:45 WITA): generator ini secara konsisten nambah beruang ke-4 di sel kiri bawah untuk produk ini, apapun frame-0 / prompt / koreografinya (4 video v1-v4, 3 frame-0 v1-v3, semua gagal pola yang sama). Produk ini DI-SKIP sementara — jangan buang cap media lagi. Opsi ke depan: (a) fallback crop faceless foto asli seller (aturan LILO) jadi video statis/slideshow, atau (b) coba lagi nanti dengan generator lain. Keputusan di tangan Jendral.**
- File video mentah: media-generation-b17-08-duduk-v1-0-4098731a-59fe-4a4a-aa33-b3f3c2cf0119.mp4, media-generation-b17-08-duduk-v2-0-747e3269-d1b9-49a2-877c-2b70f66b3b29.mp4, media-generation-b17-08-duduk-v3-0-3bb33d55-249b-42b0-a51b-04c08a18176e.mp4, media-generation-b17-08-duduk-v4-0-8702f89c-b21d-4ccb-afa2-572a69e23cf2.mp4 (semua TIDAK di-upload, TIDAK dicatat).
- Frame-0: v1 lolos Gate 1 ~95-96% (3 beruang besar, kerah polos); v2 GAGAL Gate 1 (kerah scallop + pita hitam dari referensi tok_01 — styling, bukan produk); v3 LOLOS Gate 1 ~96% (kerah polos, 3 beruang, beruang kiri masih agak besar — cacat minor). File v3: media-generation-frame0-b17-08-v3-0-4a602045-f941-4597-8aff-58ef805a2024.webp
- Showcase: BELUM terverifikasi.
