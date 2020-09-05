import time
class Hayvan():

    def __init__(self, isim="", yemek_durumu="Aç", yem="", güç=["hızlı koşmak", "uçmak", "ısırmak"]):
        self.yemek_durumu = yemek_durumu
        self.yem = yem
        self.güç = güç
        self.isim = isim
    def __str__(self):
        return f"İsim: {self.isim}\nYemek durumu: {self.yemek_durumu}\nYem: {self.yem}\nGüç: {self.güç}"

    def __len__(self):
        return len(self)

    def yemek_ye(self):
        if self.yemek_durumu == "Aç":
            print(f"{self.isim} Yemek arıyor...")
            time.sleep(1)
            print("Yemek bulundu :)")
            print("Yemek yiyor....")
            time.sleep(1)
            self.yemek_durumu = "Tok"
        print(self.yemek_durumu)

    def güç_kullan(self):
        güç = input("Güç: ")
        kullanılan_güç = self.güç.index(güç)
        if güç == self.güç[kullanılan_güç]:
            print(f"{self.isim} {self.güç[kullanılan_güç]} gücünü kullanıyor...")
        else:
            print("Böyle bir güç mevcut değil!!!")