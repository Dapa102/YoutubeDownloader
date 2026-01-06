#!/usr/bin/env python3
"""
YouTube Downloader menggunakan yt-dlp
Tutorial: Cara membuat YouTube downloader sederhana
"""

import yt_dlp  
import os


def download_video(url, output_path='downloads'):
    """
    Download video dari YouTube
    
    Args:
        url (str): URL video YouTube
        output_path (str): Folder tujuan download (default: 'downloads')
    """
    # Buat folder downloads jika belum ada
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Konfigurasi download
    ydl_opts = {
        'format': 'best',  # Download kualitas terbaik
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Template nama file
        'progress_hooks': [progress_hook],  # Hook untuk menampilkan progress
    }
    
    try:
        print(f"\n🎬 Memulai download dari: {url}\n")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Ambil info video
            info = ydl.extract_info(url, download=False)
            print(f"📹 Judul: {info.get('title', 'Unknown')}")
            print(f"👤 Channel: {info.get('uploader', 'Unknown')}")
            duration = info.get('duration', 'Unknown')
            if duration != 'Unknown':
                print(f"⏱️  Durasi: {duration} detik\n")
            else:
                print(f"⏱️  Durasi: Tidak tersedia\n")
            
            # Download video
            ydl.download([url])
            
        print(f"\n✅ Download selesai! File tersimpan di folder '{output_path}'/\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}\n")


def progress_hook(d):
    """
    Menampilkan progress download
    """
    if d['status'] == 'downloading':
        # Tampilkan progress
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"⏬ Progress: {percent} | Speed: {speed} | ETA: {eta}", end='\r')
    
    elif d['status'] == 'finished':
        print("\n🔄 Download selesai, memproses file...")


def download_audio_only(url, output_path='downloads'):
    """
    Download audio saja (MP3) dari YouTube
    
    Args:
        url (str): URL video YouTube
        output_path (str): Folder tujuan download
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'progress_hooks': [progress_hook],
    }
    
    try:
        print(f"\n🎵 Memulai download audio dari: {url}\n")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"📹 Judul: {info.get('title', 'Unknown')}")
            print(f"👤 Channel: {info.get('uploader', 'Unknown')}\n")
            
            ydl.download([url])
            
        print(f"\n✅ Download audio selesai! File tersimpan di folder '{output_path}'/\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}\n")


def main():
    """
    Fungsi utama - menu interaktif
    """
    print("=" * 50)
    print("🎬 YOUTUBE DOWNLOADER")
    print("=" * 50)
    
    print("\nPilih mode download:")
    print("1. Download Video (kualitas terbaik)")
    print("2. Download Audio saja (MP3)")
    print("3. Keluar")
    
    choice = input("\nPilihan Anda (1/2/3): ").strip()
    
    if choice == '1':
        url = input("\nMasukkan URL YouTube: ").strip()
        download_video(url)
        
    elif choice == '2':
        url = input("\nMasukkan URL YouTube: ").strip()
        print("\n⚠️  Catatan: Download audio memerlukan ffmpeg terinstall di sistem Anda")
        download_audio_only(url)
        
    elif choice == '3':
        print("\n👋 Terima kasih!\n")
        return
        
    else:
        print("\n❌ Pilihan tidak valid!\n")


if __name__ == "__main__":
    main()
