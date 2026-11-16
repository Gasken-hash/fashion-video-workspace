# Standar Baru Video Fashion (berlaku mulai 12 Nov 2026)

Tujuan: video tidak salah produk. Setiap video fashion baru WAJIB
melewati semua langkah ini, berurutan. Satu langkah gagal = berhenti,
jangan lanjut ke langkah berikutnya.

## Langkah-langkah

**0. Identitas produk.** Sebutkan balik nama produk + harga + link
Shopee ke Jendral, dan pakai foto asli seller dari link kanonik
`shopee.co.id/product/{id_toko}/{id_produk}` (bukan shortlink).
Tanpa foto asli, tidak ada produksi.

**1. Satu foto dasar.** Pakai SATU foto model dasar yang sama untuk
semua produk. Format VERTIKAL 9:16 (keputusan Jendral 12 Nov 2026
18:46 WITA, berlaku untuk video selanjutnya — cocok buat
TikTok/Reels). Foto dasar vertikal tanpa tas SUDAH ADA sejak tes
Priscila 12 Nov 18:47 WITA:
`~/workspace/fashion_test/vertical_test_priscila/media-generation-base-vertical-no-bag-0-b5a9403c-a835-4074-a827-40d4753fd196.webp`
(1152x2048, model + kamar pink sama, tanpa tas). Ganti HANYA bajunya;
background, pose, rok jangan disentuh. Tidak ada tas di foto dasar.
Foto asli seller SELALU disertakan sebagai gambar referensi di setiap
edit — AI harus MELIHAT bentuknya, bukan cuma baca deskripsi.

**2. Generate gambar frame-0 dulu.** Bukan video. Tulis bentuk
dengan kata geometri + larangan eksplisit, contoh: "hem lekuk U
lembut, lebih panjang di tengah, tanpa titik tajam" dan "lengan
nempel di bahu, bukan off-shoulder, bukan lengan lepas". Kata kabur
diisi AI dengan versi fashion standarnya sendiri.

**3. GATE 1 — cek frame-0 lawan foto asli.** Checklist detail per
detail: warna, pola, bentuk leher, lengan (nempel/lepas, panjang),
pita/detail (jumlah, ukuran, posisi), bentuk hem, fit
(ketat/longgar). Satu menyimpang = BELUM LOLOS, video tidak boleh
dibuat.

**4. Kalau belum sama: edit bedah.** Ubah HANYA bagian yang salah
pada foto yang sudah bagus itu, maksimal 2x percobaan. Jangan
generate ulang dari nol (itu mengacak semua detail lagi).

**5. Kalau 2x bedah gagal: fallback foto asli.** Pakai foto asli
seller di-crop faceless (cara LILO). Bentuk 100% asli; background
jadi ikut foto seller. Jangan paksakan generate.

**6. GATE 2 — baru generate video.** Hanya kalau frame-0 LOLOS.
Resep video (gaya referensi @eveyourmine_ "blouse fav akuu", keputusan
Jendral 12 Nov 2026): VERTIKAL 9:16 (704x1248), 10 detik, MEDIUM SHOT
(dagu sampai paha tengah, baju memenuhi frame — BUKAN full-body sampai
kaki), kamera lock-off diam, model DIAM di tempat tanpa melangkah maju,
tangan yang bercerita: pinggang → pita/dada → bahu → peplum → muter
samping → pinggang → akhir playful (opsional), tanpa suara (musik
ditambah di editing). Format vertikal berlaku mulai 12 Nov 2026 18:46
WITA (keputusan Jendral); video-video landscape yang sudah jadi tetap
apa adanya, tidak dibuat ulang.

**Aturan wajah (Jendral 12 Nov 2026 19:14 WITA):** PRIORITAS muka
JANGAN kelihatan (faceless, wajah ter-crop di luar frame) — TAPI dagu/
mulut yang ngintip DIKIT di tepi atas masih BOLEH (ditoleransi, cukup
dilaporkan). Yang TIDAK BOLEH: mata atau wajah penuh keliatan jelas.
Dagu ngintip yang dulu dicatat sebagai cacat framing sekarang masuk
toleransi, bukan lagi kegagalan.

**Komposisi kasur (Jendral 12 Nov 2026, dari koreksi berantai):**
kasur HARUS nempel di kaki model (bukan jauh di belakang dengan lantai
di antaranya — itu keliatan aneh), dan sisi panjang kasur HARUS
kelihatan (kasur di samping kiri model, sisi kasur + seprai + bantal di
ujung kiri keliatan, model berdiri di lantai di tepi sisi kasur). Model
JANGAN berdiri di atas kasur.

**Pencahayaan (Jendral 12 Nov 2026 20:06 WITA):** cahaya HARUS
directional dari jendela (hangat, dari kiri): badan model menjatuhkan
bayangan lembut di kasur dan lantai ke arah berlawanan, ada bayangan
kontak di bawah kaki, shading lembut di sisi badan yang jauh dari
jendela, dan bayangan di lipatan kain. Gambar tanpa bayangan jatuh
(karakter tidak membumi, cahaya merata) = BELUM LOLOS.

**7. GATE 3 — QC frame video lawan foto asli.** Cek frame 0 / 2 /
3,5 / 6,5 / 9,5 detik. Detail produk harus TETAP SAMA sepanjang
video. Video bisa mengarang detail sendiri dari frame-0 yang bersih
(bukti: HYLE — pita pergelangan muncul di video padahal tidak ada
di frame-0). Kalau video mengarang detail = video GAGAL, jangan
dikirim sebagai final; perbaiki frame-0 atau buat ulang.

**8. Serah terima.** Kirim per produk: foto asli seller + frame-0 +
video + frame detik 2, plus daftar jujur perbedaannya. Cacat
framing (mis. dagu ngintip) dilaporkan apa adanya, bukan
disembunyikan.

## Aturan tas — hukum fisika (12 Nov 2026)

Tas TIDAK BOLEH tiba-tiba muncul, hilang, terbang, atau pindah bahu
di tengah video. Rekam jejak: tas pindah bahu (Adelia v2), tas hilang
saat muter (HYLE 6,5 dtk), strap menggantung tanpa tas (Luluna v2
6,5 dtk), tas muncul tiba-tiba (MH). Keputusan default: TIDAK PAKAI
TAS — foto dasar sekarang versi tanpa tas. Kalau suatu saat tas dipakai
lagi, tas harus menggantung di bahu yang SAMA dengan talinya, kena
gravitasi, sepanjang video; Gate 1 dan Gate 3 wajib cek tas di semua
frame (bahu yang sama, tali nyambung, menggantung ke bawah, tidak
melayang, tidak muncul tiba-tiba).

## Catatan

- Standar ini lahir dari: aturan Jendral 12 Nov 00:19 (gambar dulu,
  cek, baru video), swap-test Lunelly v1-v3, dan audit 11 video
  12 Nov 00:34 (9 lolos, 2 gagal: swap v1 dan HYLE).
- Aturan lama yang tetap berlaku: video silent, durasi 10 dtk,
  sebelum-after comparison di setiap pengiriman.
- Format berubah 12 Nov 2026 18:46 WITA (Jendral: "buat yang vertikal
  aja mungkin ya untuk selanjutnya"): semua video fashion SELANJUTNYA
  VERTIKAL 9:16. Satu-satunya video vertikal sebelumnya: Adelia v1
  (704x1248). Semua video lain (Adelia v2/v3, Batch 5, HYLE fix,
  Luluna swap, MH) landscape dan tetap apa adanya.
- Format KEMBALI ke HORIZONTAL 12 Nov 2026 22:38 WITA (Jendral:
  "kita kembali kesana aja", pilihan widget "Priscila horizontal,
  model lama"): semua video fashion SELANJUTNYA HORIZONTAL 16:9
  (1280x720), model lama (base Adelia landscape tanpa tas), resep
  lama yang dapat "Oke sekarang bagus". Era vertikal (18:46-22:38 WITA
  12 Nov: Priscila vertikal, medium shot, kamar baru, karakter baru)
  BERHENTI — video-video vertikal yang sudah dibuat tetap apa adanya,
  tidak dihapus. Priscila horizontal pertama: priscila_horizontal/
  (frame-0 + video lolos Gate 1+3 percobaan pertama).

## Update 13 Nov 2026 — produksi berjalan pakai duduk LILO vertikal

(Catatan ditambahkan 13 Nov 2026, 14:45 WITA — aturan lengkapnya ada
di skill `fashion_video_fidelity`, bagian "Aturan 13 Nov 2026".)

Produksi sejak 13 Nov 00:44 WITA (Katie dst, 7 video Korean Style +
Zipper Leather) pakai resep duduk LILO VERTIKAL 9:16, base frame-0
Pita v3 1536x2752, dinding maroon hangat (ganti dinding pink muda
pucat DIBATALKAN Jendral 13 Nov 11:03 WITA). Jangan balik ke horizontal
tanpa perintah Jendral. Aturan keras baru: (1) foto HANYA dari link
persis yang Jendral kirim, jangan substitusi marketplace lain
(risiko banned TikTok); (2) resleting HARUS tertutup penuh di semua
frame, slider di atas (risiko banned TikTok); (3) prop lantai
dirotasi tas → kacamata → tumbler; (4) video final di-upscale ke
720x1280 (ffmpeg lanczos, crf 18) — disetujui Jendral 13 Nov 13:59
WITA ("begini jadi bagus"). Pemetaan bawahan ikut warna atasan
masih USULAN, belum diputuskan Jendral.
