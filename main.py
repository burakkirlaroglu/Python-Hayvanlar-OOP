from OOP.HayvanlarAlemi.at import At
from OOP.HayvanlarAlemi.kuş import Kuş
from OOP.HayvanlarAlemi.köpek import Köpek
import time



def eğitim():
    at = At()
    kuş = Kuş()
    köpek = Köpek()

    print("""
    SANAL HAYVAN EĞTİMİ UYGULAMASI
    ******************************
    At eğitimi için At
    
    Köpek eğitimi için Köpek
    
    Kuş eğitimi için Kuş
    ******************************
    """)

    while True:
        işlem = input("Eğitim seç: ")

        if işlem == "q":
            print("Programdan çıkılıyor...")
            break
        elif işlem == "At":
            at.isim = "Fast Navy"
            at.yem = "Arpa"
            print(at)
            at.yemek_ye()
            print("Antreman için hazır")
            time.sleep(2)
            at.antrenman_yap()
            time.sleep(4)
            print("TEBRİKLER EĞİTİM SONA ERDİ...")
        elif işlem == "Köpek":
            köpek.isim = "Karabaş"
            köpek.yem = "Et"
            print(köpek)
            print("ilk eğitim başlamak üzere")
            time.sleep(2)
            köpek.yemek_ye()
            print("Yemek eğitimi bitti.")
            time.sleep(1)
            print("Güç eğitimi başlıyor.")
            köpek.güç_kullan()
            time.sleep(3)
            print("Güç eğitimi bitti")
            time.sleep(2)
            print("Koklama eğitimi başlıyor.")
            time.sleep(2)
            köpek.kokla()
            print("Koklama eğitimi bitti")
            time.sleep(2)
            print("TEBRİKLER EĞİTİM BAŞARIYLA SONA ERDİ...")
        elif işlem == "Kuş":
            kuş.isim = "Güvercin"
            kuş.yem = "Çekirdek"
            print(kuş)
            kuş.güç_kullan()
            kuş.yemek_ye()
            print(kuş)
            print("TEBRİKLER EĞİTİM SONA ERDİ...")
        else:
            print("Geçersiz işlem !!!")



if __name__ == '__main__':
    eğitim()



