# Katie Berdiri Vertikal — Flow Base (TEST 1x)

Produk: **KATIE cardigan** (MAMAMARA, ID 26911445693) — pink lembut,
tepat 5 pita HITAM kecil di depan (satu kolom vertikal) + manik mutiara
di tiap pita, manset flare/bell, hem U scalloped, kerah bulat.
Ref asli: `~/workspace/fashion_test/korean_style/katie_cardigan/ref_katie_original.jpg`
Base UJI: `~/workspace/fashion_test/bases/lala_berdiri_vertikal_flow_base.jpg`
(foto Flow Jendral, 768x1365, potret 9:16 — BUKAN base horizontal lama).
Tanggal: 15 Nov 2026, 01:53 WITA. Status: TEST — belum diupload/dicatat.

## Gate 1 — LOLOS (frame-0 v1, identitas produk ~97%)
Frame-0: `media-generation-frame0-katie-berdiri-vertikal-0-9013dcc1-c300-4353-94f8-d3af3aea6883.webp`
(1184x2096, sharpness 82.8 — sama dengan frame-0 Katie horizontal v9: 83.4).
- Pink lembut + rib halus ✓, kerah bulat ✓, TEPAT 5 pita HITAM satu kolom
  tengah + mutiara di tiap pita ✓, manset flare + tepi scalloped (kanan
  terlihat jelas) ✓, hem U scalloped ✓, cropped ✓.
- TIDAK ada kontaminasi dari baju base: pita PINK base hilang total,
  TIDAK ada kancing yang muncul (base punya 5 kancing) ✓.
- Framing potong mulut/dagu ✓, cepol rendah + helai depan ✓,
  celana putih drawstring ✓, dinding kuning pucat + kasur + boneka
  plush + bantal pink + poster JOYFUL ✓ (background base utuh).
- Cacat kecil: selip kulit pinggang tipis antara hem scalloped dan
  waistband celana (statis, kecil); manset flare kiri belum kelihatan
  di frame-0 karena lengan kiri keluar frame (baru terverifikasi di 2s+).

## Gate 3 — LOLOS (video v1, ~96-97%)
Raw: `media-generation-katie-berdiri-vertikal-flow-v1-0-998501d1-a6c1-47e1-a2b9-537dedeb9af6.mp4`
(704x1248, 24fps, 10.0s, ada audio bawaan — dibuang di post-proses).
Sharpness video: 0s 125.3, 0.6s 92.2, 2s 104.0, 3.5s 98.0, 6.5s 98.7,
9.5s 112.9 — video TIDAK lebih lembut dari frame-0 (82.8).
- Background 0 vs 0.6s IDENTIK (beku) ✓.
- Produk IDENTIK ≥95% di semua frame 0/2/3.5/6.5/9.5s: 5 pita hitam
  utuh, tidak ada detail diciptakan/dihilangkan. Pita ke-4 sempat
  tertutup jari di 3.5s, pita ke-3 sebagian tertutup cuff tangan di
  9.5s — tangan menutupi sesaat, bukan produk berubah (semua pita
  jelas di frame lain).
- Gerakan: 2s telusuri pita atas, 3.5s sentuh pita bawah/hem,
  6.5s tangan di pinggang, 9.5s finger heart 🫰 JELAS di level dada,
  tangan kiri di pinggang. Kepala tidak pernah menunduk/menoleh.
- Wajah: mulut/dagu saja di semua frame; top 9.5s diperbesar 2x =
  mulut + senyum tipis saja, TANPA mata, TANPA hidung — dalam
  kalibrasi (hidung sekilas saja sudah boleh; di sini bahkan tidak ada).
- Post-proses: crop atas 62px (~5%) → buang audio → upscale lanczos
  720x1280, crf 18. Final: `katie_berdiri_vertikal_flow_v1_upscale720.mp4`
  (720x1280, h264, 10.0s, 1 stream video saja = silent, 2.9 MB).

## Daftar cacat jujur
1. Framing mengencang sedikit ke arah akhir (kepala lebih besar di
   9.5s); poster JOYFUL tampak berlapis/double di tepi kanan atas
   9.5s — drift background kecil di ending (0–6.5s bersih).
2. Selip kulit pinggang tipis antara hem dan waistband celana di
   semua frame (juga di frame-0; statis, kecil).
3. Kalung emas tipis dari base kelihatan di kerah (artefak base).
4. Motion blur tangan kanan di 6.5s saat bergerak ke hem.
5. Lengan kiri keluar frame di 0s (pose base); manset flare kiri
   baru kelihatan mulai 2s.

## Base Flow: apa yang jalan vs base horizontal lama
JALAN:
- Framing mouth-cut bertahan penuh (tidak ada mata di frame mana pun,
  bahkan di 9.5s) — lebih stabil dari horizontal v1–v8 yang berulang
  kali bocor wajah.
- Swap produk lolos sekali jalan, tanpa kontaminasi pita pink/kancing
  dari baju base.
- Ketajaman TIDAK turun di video (malah di atas frame-0) — horizontal
  Katie v2 dulu sempat soft di 0.6s.
- Suasana kamar Flow (dinding kuning pucat + kasur quilted putih +
  boneka plush) terbaca hangat dan beda dari dinding maroon duduk
  maupun kamar krem horizontal — variasi visual baru yang bagus.
- Choreography review + finger heart di dada terbaca jelas.
TIDAK JALAN / PERHATIAN:
- Framing mengencang di akhir (kecenderungan yang sama seperti base
  horizontal) — crop atas ~5% tetap wajib sebagai pengaman.
- Poster JOYFUL ghosting di ending — background Flow punya elemen
  yang lebih "hidup" (poster) dibanding kamar krem horizontal.
- Resolusi base lebih rendah (768x1365 vs 2752x1536 horizontal),
  tapi output generator sama saja (704x1248), jadi tidak ada rugi
  praktis.
- Lengan kiri keluar frame di pose awal base — manset kiri tidak
  bisa dicek di frame-0.

## Verdict
**Base Flow LAYAK dipakai lagi** — sekali jalan Gate 1 + Gate 3 lolos,
produk ≥95%, faceless bertahan. Rekomendasi: jadikan base berdiri
vertikal kedua (pendamping base horizontal), dipakai bergantian.
Aturan berdiri tetap berlaku penuh (kepala tidak menunduk, crop atas
~5%, Gate 3 cek mata di 9.5s yang diperbesar).

---

# Set Berdiri F — TEST 1x (15 Nov 2026, 02:08 WITA)
Produk sama: KATIE. Frame-0 DIPAKAI ULANG dari v1 (sudah lolos Gate 1, ~97%) — yang dites murni gerakannya.
Raw: `media-generation-katie-berdiri-vertikal-flow-se-0-5ad59929-541c-43b6-9e98-7cd21853533b.mp4` (704x1248, 24fps, 10.0s, ada audio bawaan — dibuang).
Final: `katie_berdiri_vertikal_flow_setF_v1_upscale720.mp4` (720x1280, h264, 10.0s, silent, 4.4 MB).
Frame 3.5s: `katie_berdiri_vertikal_flow_setF_3.5s.jpg` (QC di `setF/g3_*.jpg`).

## Gate 3 — LOLOS (produk ~96-97%, faceless aman) DENGAN 1 CACAT GERAKAN
- Background 0 vs 0.6s IDENTIK (beku) ✓.
- Produk ≥95% di semua frame 0/2/3.5/6.5/9.5s: 5 pita hitam utuh, pink rib, kerah bulat, manset flare + tepi scalloped, hem U scalloped, cropped. Pita ke-1 sempat tertutup jari di 2s, pita ke-5 tertutup tangan di 3.5s — sesaat, bukan berubah (jelas di frame lain).
- Gerakan: 0s tangan kanan di pinggang ✓; 2s kedua tangan ke pita atas — manset flare kelihatan jelas ✓; 3.5s kedua tangan di hem/pinggang bawah ✓; 6.5s putar badan ke samping ✓ (TAPI putarannya ~80-90 derajat, jauh dari 30 derajat yang diminta — sisi + lengan kelihatan bagus, kepala tetap menghadap kamera jadi tidak ada profil wajah); 9.5s peace sign ✌️ TERBENTUK JELAS ✓.
- Wajah: mulut/dagu saja di semua frame; top 9.5s diperbesar 2x = mulut saja, TANPA mata, TANPA hidung, TANPA full face — dalam kalibrasi ✓.

## Cacat jujur
1. **Peace sign NAIK KE PIPI, bukan di dada** (9.5s) — melanggar klausul Set F; tangan kanan terangkat sampai pipi/telinga. Tidak sampai bikin wajah masuk (tidak ada mata), tapi posisinya salah. Kalau mau peace ketat di dada, perlu v2 dengan klausul lebih keras.
2. Framing mengencang ke arah akhir (model makin besar; 9.5s paling rapat) — sama seperti v1.
3. Frame 3.5s paling lembut (motion blur tangan di hem) — detail produk masih terbaca.
4. Poster JOYFUL double / plush kanan muncul di ending (drift background kecil 2s+).
5. Selip kulit pinggang tipis antara hem dan waistband (statis, dari frame-0); kalung emas base kelihatan; lengan kiri keluar frame di 0s (pose base).
- Status: BELUM diupload/dicatat. Menunggu penilaian Jendral.

---

# Set Berdiri F — 2 MODE PEACE SIGN (Jendral, 15 Nov 2026 02:33 WITA)
"peace sign-nya dibuat 2 mode aja gantian ada yang di pipi ada yang di dada gitu" — rotasi resmi: pipi ↔ dada.

## v2 DADA (percobaan 1) — GAGAL jadi mode dada
Raw: `media-generation-katie-berdiri-vertikal-flow-se-0-4159fc4f-bdb0-448b-9307-dfdda05913a1.mp4` (704x1248, 10s). Final: `katie_berdiri_vertikal_flow_setF_v2_dada_upscale720.mp4` (720x1280, 10s, silent, 4.3 MB). QC di `setF2/g3_*.jpg`.
- Produk ~96-97%, faceless aman (mulut saja di 9.5s, tanpa mata/hidung) — videonya sendiri tidak rusak.
- TAPI peace sign-nya BUKAN di dada: tangan KANAN naik sampai bahu, jari sampai level mulut. Bukan pipi, bukan dada — mode bahu.
- Beat putar badan juga HILANG di v2: 3.5s dan 6.5s sama-sama cubit hem depan, tidak ada side turn.
- Status: DIBUANG dari rotasi — bukan mode. Pelajaran: klausul "mid-chest, elbow bent down" saja tidak cukup; generator tetap menaikkan tangan.

## v3 DADA (percobaan 2, klausul diperkeras) — LOLOS, mode dada RESMI
Raw: `media-generation-katie-berdiri-vertikal-flow-se-0-67a80fe9-d6ab-4f10-bc3c-5926d28bf4fd.mp4` (704x1248, 10s). Final: `katie_berdiri_vertikal_flow_setF_v3_dada_upscale720.mp4` (720x1280, 10s, silent, 3.7 MB). QC di `setF3/g3_*.jpg`. Frame 3.5s: `katie_berdiri_vertikal_flow_setF_v3_3.5s.jpg`.
- Gate 3 LOLOS: produk ~96-97% di semua frame (5 pita hitam utuh; pita ke-1 tertutup jari di 2s, pita ke-3 tertutup tangan peace di 9.5s — sesaat, jelas di frame lain); background 0 vs 0.6s beku.
- Peace sign DI DADA ✓: tangan KIRI di tengah dada, jari menunjuk ke atas sampai level tulang selangka, ujung jari jauh di bawah dagu, jauh dari wajah. Tangan kanan di pinggang. Klausul yang jalan: "forearm bent across her waist, hand staying below her collarbone with fingertips far below her chin" + Negative: "never rises above the chest, never goes near cheek/chin/mouth/ear, no hand near her head".
- Gerakan: 2s tangan ke pita atas (manset flare jelas) ✓; 3.5s tangan terbuka di dada bawah/hem, 5 pita kelihatan semua ✓; 6.5s putar badan ~90 derajat (kepala ikut mutar — profil bawah wajah saja, TANPA mata, masih dalam kalibrasi); 9.5s peace dada ✓.
- Wajah: mulut/dagu saja di semua frame; top 9.5s diperbesar = mulut saja, tanpa mata, tanpa hidung ✓.
- Cacat: putaran 6.5s kepala ikut mutar (profil); framing mengencang ke akhir; selip kulit pinggang tipis (statis, dari frame-0); kalung emas base kelihatan.
- Status: BELUM diupload/dicatat. Pasangan rotasi lengkap: v1 = mode pipi, v3 = mode dada.

---

# Bentuk dada TURUN di v3 — PERBAIKAN (Jendral, 15 Nov 2026 03:48 WITA)
Jendral, menunjuk frame 3.5s v3: "payudaranya kok turun gitu ya, gawat banget ini kalau gak dibenerin".
DIAGNOSIS (banding frame): frame-0 + v3 2s/6.5s/9.5s bentuk dada normal dan terangkat; HANYA v3 3.5s yang turun. Penyebab: beat "tangan terbuka lebar di dada" mendarat sebagai telapak tangan menekan rata di dada bawah — tangan menekan dan generator me-render kain + bentuk dada jadi melorot ke bawah. v1/v2 3.5s (tangan di hem) bentuknya bersih — pembandingnya membuktikan beat-nya yang salah, bukan bajunya.
PERBAIKAN: beat dada-terbuka DIHAPUS. Pengganti: ujung jari saja menyentuh pita atas, telusuri kolom pita TANPA menekan dada, lalu cubit hem di pinggang. Plus klausul fit: "bust stays naturally high and lifted, no sagging, no drooping, no flattening" + Negative "hands never press flat against her bust, never spread their palms over her chest".

## v4 (Set F v4, mode dada fix percobaan 1) — BENTUK DADA BERSIH, peace meleset ke bahu
Raw: `media-generation-katie-berdiri-vertikal-flow-se-0-aed203b2-251a-433c-af6c-4b1f72ff3353.mp4` (704x1248, 10s). Final: `katie_berdiri_vertikal_flow_setF_v4_dada_fix_upscale720.mp4` (720x1280, 10s, silent, 4.1 MB). QC di `setF4/g3_*.jpg`. Frame 3.5s: `katie_berdiri_vertikal_flow_setF_v4_3.5s.jpg`.
- BENTUK DADA BERSIH di SEMUA frame 0/2/3.5/6.5/9.5s: terangkat, halus, sama seperti frame-0. Di 3.5s tangan cubit hem (bukan menekan dada) ✓. Produk ~96-97%, background 0 vs 0.6s beku, faceless aman (mulut saja di 9.5s, tanpa mata/hidung).
- Putar badan 6.5s ~45-60 derajat, kepala tetap menghadap kamera ✓.
- CACAT: peace sign 9.5s meleset ke BAHU (tangan kiri terangkat, jari sampai level pipi/telinga) — bukan dada seperti v3. Jadi v4 BUKAN mode dada bersih; nilainya sebagai bukti perbaikan bentuk dada.

## v5 (Set F v5, mode dada fix percobaan 2) — BENTUK DADA BERSIH JUGA, peace tetap di bahu
Raw: `media-generation-katie-berdiri-vertikal-flow-se-0-c91f5413-4f76-4999-a352-2709cee63868.mp4` (704x1248, 10s). Final: `katie_berdiri_vertikal_flow_setF_v5_dada_fix_upscale720.mp4` (720x1280, 10s, silent, 4.4 MB). QC di `setF5/g3_*.jpg`.
- Bentuk dada BERSIH di semua frame (3.5s tangan di hem, dada halus terangkat) ✓ — perbaikan beat TERBUKTI 2x (v4 + v5 sama-sama bersih).
- CACAT: peace 9.5s tetap di bahu (telapak di tulang selangka, jari sampai dagu); putar badan 6.5s kebablasan ~90 derajat + kepala ikut mutar (profil bawah wajah saja, tanpa mata).
- KESIMPULAN: tinggi peace sign itu LOTRE — cuma v3 dari 4 percobaan yang mendarat di dada (v2/v4/v5 semua di bahu). v3 tetap satu-satunya mode dada murni, TAPI frame 3.5s-nya cacat turun. Belum ada video yang sekaligus dada-bersih + peace-di-dada. Menunggu penilaian Jendral: pakai v4 (dada bersih, peace bahu) atau coba lagi.

## Upload + catat OTOMATIS (Jendral, 15 Nov 2026 03:56 WITA)
Aturan baru: selesai generate langsung upload + catat, tanpa tanya dulu. Diterapkan ke tunggakan: Flow v1 → Cloudinary `Katie-Berdiri-Vertikal-Flow-V1` (v1794686255), sheet No 37; Set F v1 (pipi) → `Katie-Berdiri-Vertikal-SetF-V1` (v1794686260), No 38; Set F v4 (dada fix, peace bahu) → `Katie-Berdiri-Vertikal-SetF-V4` (v1794686263), No 39. Semua "Siap tayang", Harga 99900, read-back terverifikasi. Set F v3 TIDAK diupload/dicatat (cacat dada turun 3.5s); Set F v5 cadangan v4, tidak dicatat.
