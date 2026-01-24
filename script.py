import time
import sys
import random
from datetime import datetime

def digital_vibration(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def main():
    # Daftar Surah Acak
    surat_list = [
        {"nama": "Al-Ikhlas", "ayat": ["قُلْ هُوَ اللَّهُ أَحَدٌ", "اللَّهُ الصَّمَدُ", "لَمْ يَلِدْ وَلَمْ يُولَدْ", "وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ"]},
        {"nama": "Al-Falaq", "ayat": ["قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ", "مِن شَرِّ مَا خَلَقَ", "وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ", "وَمِن شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ", "وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ"]},
        {"nama": "An-Nas", "ayat": ["قُلْ أَعُوذُ بِرَبِّ النَّاسِ", "مَلِكِ النَّاسِ", "إِلَهِ النَّاسِ", "مِن شَرِّ الْوَسْوَاسِ الْخَنَّاسِ", "الَّذِي يُوَسْوِسُ فِي صُدُورِ النَّاسِ", "مِنَ الْجِنَّةِ وَالنَّاسِ"]}
    ]
    
    surah = random.choice(surat_list)
    keluarga = [
        "Ayahanda Mahmud Nur", "Ibunda Sitti Salmah", "Ayahanda Rahman Mahmud", 
        "Ibunda Nurhayati Zubair", "Adinda Muhammad Ikram", "Kakanda Zakaria Sasilia", 
        "Ibunda Sitti Sarah", "Ibunda Hatijah", "Ibunda Banunah"
    ]
    
    doa_ampunan = "\n\"Ya Allah, ampunilah dosa-dosa mereka, kasihanilah mereka, sejahterakanlah mereka, dan maafkanlah kesalahan mereka.\"\n"

    print("--- Memulai Eksekusi Pembacaan Harian ---")
    print(f"Surah Terpilih: {surah['nama']}\n")
    print("Niat dikirimkan pahalanya untuk:")
    for nama in keluarga:
        print(f"- {nama}")
    
    print(doa_ampunan)
    
    # Efek Getaran Digital
    for verse in surah['ayat']:
        digital_vibration(verse, 0.15)
        time.sleep(0.5)

    # Membuat/Mengupdate Laporan TXT
    waktu_sekarang = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{waktu_sekarang}] Pembacaan Surah {surah['nama']} selesai. Diniatkan untuk keluarga.\n")

if __name__ == "__main__":
    main()
