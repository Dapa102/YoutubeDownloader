# YouTube Downloader

Project sederhana untuk download video/audio dari YouTube menggunakan Python.

## 📋 Requirements

- Python 3.7+
- yt-dlp
- ffmpeg (opsional, untuk download audio/MP3)

## 🚀 Cara Install

1. **Buat & aktifkan virtual environment (disarankan):**
```bash
python3 -m venv venv
source venv/bin/activate      # Linux/Mac
# atau
venv\Scripts\activate        # Windows
```

2. **Install dependencies dari requirements:**
```bash
pip install -r requirements.txt
```

3. **Install ffmpeg (wajib untuk download audio/MP3):**
```bash
# Ubuntu/Debian:
sudo apt install ffmpeg

# macOS:
brew install ffmpeg

# Windows: unduh installer dari https://ffmpeg.org/
```

## 💻 Cara Menggunakan

Jalankan dari root proyek `youtubeDownloader/`.

### Linux/macOS
```bash
# Venv di dalam folder proyek (umum)
./venv/bin/python src/download_videoYT/app.py

# Venv di luar folder proyek (ubah sesuai lokasi venv Anda)
/home/user/python/project/venv/bin/python src/download_videoYT/app.py

# Opsi dengan aktivasi venv (jika diperlukan)
source venv/bin/activate
python3 src/download_videoYT/app.py

# Nonaktifkan venv
deactivate
```
Catatan: jika tidak ada alias `python`, pakai `python3` atau path interpreter venv di atas.

### Windows
```bash
# Venv di dalam folder proyek
venv\Scripts\python src\download_videoYT\app.py

# Venv di luar folder proyek (ubah sesuai lokasi venv Anda)
C:\path\to\venv\Scripts\python src\download_videoYT\app.py

# Opsi dengan aktivasi venv
venv\Scripts\activate
python src\download_videoYT\app.py

# Jika python tidak dikenali, gunakan launcher
py src\download_videoYT\app.py

# Nonaktifkan venv
deactivate
```

### Fitur:

1. **Download Video** - Download video dengan kualitas terbaik
2. **Download Audio** - Download audio saja dalam format MP3

## 📝 Penjelasan Kode

### Fungsi Utama:

- `download_video(url, output_path)` - Download video lengkap
- `download_audio_only(url, output_path)` - Download audio saja (MP3)
- `progress_hook(d)` - Menampilkan progress download

### Konfigurasi yt-dlp:

```python
ydl_opts = {
    'format': 'best',  # Kualitas terbaik
    'outtmpl': '%(title)s.%(ext)s',  # Template nama file
    'progress_hooks': [progress_hook],  # Progress callback
}
```

## 📁 Struktur Folder

```
youtubeDownloader/
├── README.md
├── requirements.txt
├── downloads/                      # Folder hasil download (auto-create)
├── src/
│   └── download_videoYT/           # Paket utama
│       ├── __init__.py
│       ├── __main__.py
│       └── app.py                  # File utama
└── tests/
    ├── __init__.py
    └── test_downloader.py
```

## ⚠️ Catatan Penting

- Gunakan untuk video yang legal dan sesuai kebijakan YouTube
- Pastikan koneksi internet stabil
- Hasil download tersimpan di folder `downloads/`

## 🎓 Tutorial Pembelajaran

Project ini mengajarkan:
- Menggunakan library yt-dlp
- File handling dengan Python
- User input & menu interaktif
- Error handling
- Progress tracking

## 📞 Troubleshooting

**Error saat download:**
- Pastikan URL valid
- Cek koneksi internet
- Update yt-dlp: `pip install -U yt-dlp`

**Audio download gagal:**
- Install ffmpeg terlebih dahulu
- Cek ffmpeg dengan: `ffmpeg -version`