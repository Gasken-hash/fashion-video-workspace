# Bedah video AI fashion maroon polkadot (11 Nov 2026)

Sumber: `workspace/user/media_library/video/91/91d1daddec10ddf96ebb7f5edb53c382ea77220f7756e858c69de2456b2da4cf.mp4`
Frame diekstrak 2 fps ke `frames/f_01..f_20.jpg` (854x480).

## Teknis
- 10,05 detik, 1920x1080 LANDSCAPE 16:9, 24 fps, 241 frame, HEVC.
- Audio AAC stereo 44,1 kHz full durasi, mean -14,1 dB, max -3,7 dB.
  Spektrogram: energi full spektrum kontinu + transient beat reguler + bass
  kuat = musik latar, bukan VO/narasi. Judul lagu tidak teridentifikasi.
- Scene detect (threshold 0,4): NOL cut. Satu take utuh.

## Format / style
- UGC try-on haul, FACELESS total (wajah di luar frame sepanjang video,
  framing leher sampai paha), satu lokasi kamar tidur, tanpa teks, tanpa VO.
- Estetika coquette/feminine: atasan maroon polkadot, pita tie-front +
  keyhole, ruffle hem, rok putih, tas bahu hitam, perhiasan gold, kuku
  maroon senada atasan, kamar pink + boneka plush, cahaya hangat lembut.

## Koreografi (3 beat, satu take)
1. 0-5 dtk: kedua tangan naik ke dada, telapak terbuka, jari menyebar,
   mengusap area pita/keyhole lalu naik ke tulang selangka/leher.
   Beat terpanjang, fokus ke detail tie-front.
2. 5-7,5 dtk: tangan meluncur turun ke torso, mencubit dan merapikan
   ruffle hem, menahan ujung bawah atasan. Fokus ke hem + fit.
3. 7,5-10 dtk: tangan kiri di pinggang, badan muter ~30-45 derajat ke
   samping (siluet samping + rok kelihatan), tahan, lalu balik ke depan.
   Pose akhir: depan, tangan kiri di pinggang.

## Kamera
- Klaim visual: lock-off tripod. Fakta: BREATHING.
  0 dtk medium (leher-paha) -> 2-4,5 dtk push-in sampai dada-pinggang,
  bahu kepotong -> 5-7 dtk pull-back ke medium -> 7,5-10 dtk stabil.
- Bukan gerakan yang direncanakan, ini drift generator (kasus sama seperti
  klip Mary Jane yang nge-zoom sendiri di tengah).

## Jejak AI / artefak (frame by frame)
- Tangan/jari: f_02 motion blur berat; f_07 jari kanan menyatu; f_13 jari
  kanan memanjang/blur; f_14 jempol kiri menyatu dengan kain. Jumlah dan
  panjang jari goyang antar frame, kuku maroon konsisten.
- Pita tie-front: bentuk loop berubah tiap frame (f_01 rapi kecil,
  f_07 loop gepeng, f_11 ukuran loop beda), panjang tali goyang.
- Polkadot + ruffle hem: motif tidak nempel tetap di kain, bentuk ruffle
  berubah antara f_14 dan f_15.
- Kalung liontin matahari: rantai hilang-timbul (f_14, f_18 ketutup rambut).
- Tas hitam: bentuk dan detail ring/klasp berubah (f_13 lebih gepeng),
  sempat hilang di balik badan pas muter (f_18, oklusi wajar).
- Background stabil secara umum; frame foto di dinding pink dan lampu meja
  baru kelihatan pas model muter badan (oklusi, wajar).
- Kulit/tangan agak waxy, khas AI.

## Catatan fidelity (kalau direplikasi)
- Paling rawan menyimpang: warna maroon, bentuk pita, ruffle hem, siluet
  pinggang (framing ketat bikin torso kelihatan lebih ramping).
- Format landscape 16:9, bukan vertikal 9:16. Buat Reels/Pinterest mesti
  crop, dan crop akan makan sisi kiri-kanan (kasur/plush atau pintu).
- Aturan fidelity gate draft (11 Okt, belum diputuskan Jendral) tetap
  berlaku sebagai acuan: animasikan foto asli seller sebagai frame awal,
  cek side-by-side warna/fit/detail, satu menyimpang = tidak lolos.

## Tes replikasi 2 (11 Nov 2026, Adelia Blouse burgundy)

- Produk pilihan (Jendral: "kamu aja yang pilihkan"): Adelia Blouse Motif
  Polkadot Lengan Panjang, Nies.Collection, Rp74.545, rating 4,93/5 (228).
  Link: https://shopee.co.id/product/251632492/56165517759
  BUKAN produk sheet, tes format saja (sama seperti Flatere).
- Alasan pilih: paling mirip referensi — V-neck + pita tie polkadot di
  leher + ruffle hem polkadot berlapis + burgundy + lengan panjang.
  Beda: badan solid burgundy (referensi full maroon polkadot), fit loose
  LD 90-120 (referensi fitted), ruffle putih polkadot (referensi maroon).
- Ditolak: Lunelly Daisy Ribbon (halter + 2 pita kecil di bahu, tanpa
  keyhole/ruffle, varian maroon polos bukan polkadot).
- Foto seller: semua gantungan di depan cermin, bukan model-worn. Foto
  burgundy terpilih: product/adelia/id-11134207-81ztn-mrjnml921og285.jpg
  (ada watermark "by niescollection" di area ruffle).
- Alur: foto seller -> foto model faceless generate
  (media-generation-adelia-model-faceless-0-19c9c6bb....webp) ->
  image-to-video 1x (media-generation-adelia-tryon-v1-0-647ebaea....mp4).
- Video: 10,0 dtk, 704x1248 vertikal 9:16, 24 fps, h264, SILENT
  (mean -50,7 dB). Referensi ada musik, ini tidak ada.
- QC (frame 0 / 0,5 / 3,5 / 6,5 / 8 / 9,5 dtk, di qc/q_*.jpg):
  - Kamera BENAR-BENAR LOCKED: background (pintu, jendela, boneka,
    tanaman) identik di semua frame. Menang lawan referensi yang breathing.
  - Beat 1 (tangan ke dada/pita) dan beat 2 (cubit hem) jalan. Beat 3
    (muter samping) terlalu halus, sekitar 10-15 derajat, bukan 30-45.
  - Warna burgundy, pita tie, ruffle konsisten sepanjang video.
  - CACAT: dagu + bibir bawah ngintip di tepi atas sepanjang video
    (sudah ada di foto model frame awal; cacat yang sama seperti Flatere).
  - Tangan: jari kiri sempat menyatu/blur pas adegan hem (6,5 dtk),
    tidak ada jari ekstra yang kelihatan.
  - Frame 0 bersih, tidak ada garble.
- Before-after: foto seller vs frame q_08 (beat 1) + q_20 (pose akhir)
  disampaikan ke Jendral bareng video. Verdict Jendral masih pending.

## v2 landscape (11 Nov 2026 malam, atas permintaan Jendral)

- Jendral: v1 "bagus", minta versi landscape seperti referensi.
- Foto model baru 16:9 (media-generation-adelia-model-landscape-0-1936c196....webp):
  komposisi sama seperti referensi (kasur kiri, pintu kanan), crop di
  leher sehingga dagu/mulut TIDAK kelihatan sama sekali. Tas jadi tali
  rantai (v1 tali polos), minor.
- Video: media-generation-adelia-tryon-landscape-v2-0-e25cd3a1....mp4,
  10,0 dtk, 1248x704 landscape 16:9, 24 fps, h264, SILENT (mean -46,7 dB).
- QC (qc2/r_01..r_20.jpg):
  - Landscape beneran, dagu tidak kelihatan di frame mana pun.
  - Pita tie, ruffle, warna burgundy konsisten. Pose akhir tangan di
    pinggang bagus.
  - Beat jalan LEBIH CEPAT dari prompt: tangan sudah di hem di 3,5 dtk,
    muter badan 6,5 dtk, ~2 dtk terakhir hampir diam di pose tangan di
    pinggang.
  - Kamera hampir diam, tapi ada drift sedikit pas adegan muter badan
    (tidak se-lock v1 yang pixel-identik).
  - Tas pindah ke bahu sebelahnya dibanding foto awal.
  - Framing sedikit lebih ketat dari foto awal, lutut kepotong.
  - Frame 0 bersih, tidak ada garble.
- Verdict Jendral atas v2 masih pending.

## v3 landscape + langkah maju (11 Nov 2026 malam, arahan Jendral)

- Arahan Jendral: tiap prompt dikasih "maju 1 langkah untuk memamerkan
  bajunya ke kamera, seperti video referensinya". Catatan bedah: yang
  kubaca sebagai "camera breathing" di referensi ternyata kemungkinan
  memang modelnya yang melangkah maju. Koreksi cara baca: push-in
  referensi = gerakan model, bukan (hanya) drift kamera.
- Prompt v3: beat 1 (0-5 dtk) = 1 langkah maju pelan ke kamera sambil
  kedua tangan naik ke dada/pita; ditegaskan kamera tidak zoom, framing
  dekat HANYA dari langkahnya. Beat 2-3 sama seperti v2.
- Foto awal sama seperti v2 (landscape, tanpa dagu).
- Video: media-generation-adelia-tryon-landscape-v3-step-0-89fd9ecf....mp4,
  10,0 dtk, 1248x704 landscape 16:9, 24 fps, SILENT (mean -48,9 dB).
- QC (qc3/s_01..s_20.jpg):
  - Langkah maju JELAS: di 2 dtk framing sudah ketat dada-ke-pinggang,
    tangan di pita, mirip momen terketat referensi. Background tidak
    ikut membesar, jadi kamera memang diam.
  - Beat 1 (tangan ke dada sambil melangkah) dan beat 2 (tangan ke hem)
    jalan. Beat 3 tangan di pinggang + muter dikit jalan.
  - Dagu aman 0-9 dtk, TAPI ngintip lagi di ~1 dtk terakhir (frame 9,5
    dtk: dagu + bibir kelihatan).
  - Dia balik mundur sendiri ke jarak medium di 6,5 dtk (tidak ada di
    prompt), jadi close-up hanya di paruh awal video.
  - Frame 0 bersih, tidak ada garble. Pita/ruffle/warna konsisten.
- Verdict Jendral atas v3 masih pending.
