import time
import sys
import random

def digital_vibration(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def main():
    # Daftar Surah Acak (Bisa Anda tambah sesuai keinginan)
    surat_list = [
        {
            "nama": "Al-Ikhlas",
            "ayat": ["قُلْ هُوَ اللَّهُ أَحَدٌ", "اللَّهُ الصَّMَدُ", "لَمْ يَلِدْ وَلَمْ يُولَدْ", "وَلَمْ يَكُن لَّهُ كُفُوًا أَحَدٌ"]
        },
        {
            "nama": "Al-Falaq",
            "ayat": ["قُلْ أَعُوذُ بِرَبِّ الْفَلَقِ", "مِن شَرِّ مَا خَلَقَ", "وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ", "وَمِن شَرِّ النَّفَّاثَاتِ فِي الْعُقَدِ", "وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ"]
        }
    ]
    
    surah = random.choice(surat_list)
    
    niat = (
        "Niat pembacaan hari ini dikirimkan pahalanya untuk: "
        "Ayahanda Mahmud Nur, Ibunda Sitti Salmah, Ayahanda Rahman Mahmud, "
        "Ibunda Nurhayati Zubair, Adinda Muhammad Ikram, Kakanda Zakaria Sasilia, "
        "Ibunda Sitti Sarah, Ibunda Hatijah, dan Ibunda Banunah."
    )

    print("--- Memulai Pembacaan Digital ---")
    print(f"Surah: {surah['nama']}\n")
    print(niat + "\n")
    
    for verse in surah['ayat']:
        digital_vibration(verse, 0.15)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
