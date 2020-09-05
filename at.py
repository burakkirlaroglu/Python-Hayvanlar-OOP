from OOP.HayvanlarAlemi.hayvan import Hayvan


class At(Hayvan):

    def __init__(self):
        super().__init__()

    def antrenman_yap(self):
        self.güç_kullan()
        print(f"{self.isim} antremanını yaptı yarışa hazır...")