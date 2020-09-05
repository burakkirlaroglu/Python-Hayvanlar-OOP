from OOP.HayvanlarAlemi.hayvan import Hayvan
import time

class Köpek(Hayvan):

    Arananlar = ["Oyuncak", "Kalem", "Bardak"]

    def __init__(self):
        super().__init__()

    def kokla(self):
        kokla = input("Ne Arıyorsun ?")
        try:
            kokluyor = self.Arananlar.index(kokla)
            if kokla in self.Arananlar[kokluyor]:
                print(f"{self.isim} kokluyor...")
                time.sleep(1)
                print("istediğiniz objeyi buldu !!!")
        except:
            print("Maalesef arananlar listesinde aradığınız obje yok ! {}".format(self.Arananlar))
