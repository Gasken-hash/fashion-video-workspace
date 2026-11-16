# Rotasi gerakan batch-17 — rencana setelah protes Jendral 15 Nov 16:33 WITA

## Diagnosis (terverifikasi dari NOTES.md, 15 Nov 16:37 WITA)

Jendral benar: 11 video Tier 1 pertama (b17_28, 40, 03, 23, 43, 01, 22, 21, 35, 02, 05)
pakai SATU kerangka gerakan yang sama, cuma detail yang disentuh yang diganti:

> tangan kanan di pinggang → sentuh detail produk (pita/kancing/bunga, ujung jari)
> → tangan kiri sentuh detail kedua → kedua tangan cubit/usap hem/peplum
> → tangan kanan kembali ke pinggang → peace 1x tangan kiri di level dada

Set A–E dari skill (fashion_video_fidelity) TIDAK dipakai satu pun di 11 video itu:
tidak ada angkat manset (B), tidak ada tangan di pinggang + putar badan (C),
tidak ada satu tangan jangkar (D), tidak ada slow reveal dari pangkuan (E).
Yang berubah cuma NAMA detailnya (pita besar, kancing mutiara, bunga magenta...),
jadi di mata penonton gerakannya identik. Aturan "pilih/adaptasi gerakan dari ciri
produk" (13 Nov 08:53 WITA) hanya jalan di level kata, bukan di level koreografi.

## Perbaikan yang SUDAH jalan (main chat, jangan diulang)

- b17_12 LNR Vest — SET C (fit/waist): bahu → kancing → pinggang → hem → rok
  → putar badan pelan → peace + wave kecil. Cloudinary LNRVest-Duduk-V1,
  sheet No 59 "Siap tayang" (16:35 WITA).
- b17_16 Belvana Vest — SET D (satu tangan jangkar), terlihat dari frame video:
  tangan kiri nempel di pangkuan sepanjang video; tangan kanan kerah (2s)
  → kancing (3.5s) → hem (6.5s) → peace (9.5s). Beda jelas dari template lama.
  NOTES.md belum ditulis saat rencana ini dibuat (video baru jadi 16:37 WITA);
  pastikan NOTES-nya mencatat "GERAKAN: SET D" seperti b17_12.

## Rencana 4 berikutnya (urutan produksi: b17_32 → b17_57 → b17_66 → b17_73)

Aturan: JANGAN pakai kerangka 11-video di atas lagi. Satu produk = satu set,
dan set yang sama tidak boleh dipakai di dua video berurutan. Set dicatat di
NOTES.md tiap produk ("GERAKAN: SET X") supaya bisa diaudit — pola b17_12.

| Produk | Set | Alasan (dari nama produk — KONFIRMASI dari galeri dulu) |
|---|---|---|
| b17_32 Cardigan Kancing Sweater Rajut | E (slow reveal) | Kancing full depan; tangan mulai bersilang di pangkuan → naik ke kancing → dada → hem → rok → putar pelan → peace. Start dari pangkuan = pembeda paling jelas dari template lama |
| b17_57 Yukika Vilmei Top (pita + kerah denim) | B (detail showcase) | Ciri menonjol = pita + kerah denim → sentuh pita/kerah, angkat manset, cubit hem → peace |
| b17_66 Cardigan Rajut Biru Muda (polos) | A (baseline) | Tanpa ciri menonjol dari namanya → fallback A, sesuai aturan (rotasi A–E hanya fallback kalau produk tanpa ciri khas) |
| b17_73 CARDIGAN ASHLEY Knit | C (fit/waist) | Cek galeri dulu: kalau fit-nya fitted/ramping → C (bahu → dada → pinggang → hem → putar → peace + wave). Kalau longgar/oversize, ganti ke D (satu tangan jangkar) |

## Set yang sudah terpakai di batch-17 (audit trail)

- C = b17_12 (LNR Vest) ✓
- D = b17_16 (Belvana Vest) ✓ (dari frame; konfirmasi di NOTES saat ditulis)
- E → b17_32, B → b17_57, A → b17_66, C/D → b17_73 (rencana di atas)

## Guard supaya tidak kambuh (untuk produksi selanjutnya)

1. Sebelum generate video, tulis dulu SET-nya di NOTES.md + bandingkan kerangkanya
   dengan video sebelumnya — kalau urutan beat-nya sama persis, ganti set.
2. "Adaptasi fitur" harus mengubah URUTAN/posisi tangan, bukan cuma nama detail
   yang disentuh. Sentuh-pita + sentuh-kancing dengan urutan yang sama = tetap sama.
3. Ending peace 1x boleh tetap (aturan 15 Nov), tapi tangan peace + levelnya
   ikut set (C: kanan + wave; D: tangan yang bebas; E: setelah putar badan).
