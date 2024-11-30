import random
import time

class Kumanda():
    def __init__(self, tv_durum = 'Kapali', tv_ses = 0, kanal_listesi = ['TRT'], kanal = 'TRT'):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):

        if(self.tv_durum == 'Acik'):
            print("Televizyon zaten acik")
        else:
            print("Televizyon Aciliyor...")
            self.tv_durum = 'Acik'
            
    def tv_kapat(self):
        if(self.tv_durum == 'Kapali'):
            print('Televizyon zaten kapali...')
        else:
            print("Televizyon kapaniyor")
            self.tv_durum = 'Kapali'

    def ses_ayarlari(self):
        
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Arttir:'>'\nCikis:'cikis'")

            if cevap == '<':
                if(self.tv_ses != 0):
                   self.tv_ses -= 1

                print(f"SES: {self.tv_ses}")
            elif (cevap == '>'):
                if (self.tv_ses != 31):
                    self.tv_ses += 1
                    print(f"SES: {self.tv_ses}")
            else:
                print(f"Ses Güncellendi: {self.tv_ses}")
                break # döngüyü sonlandir anlamina gelir

    def kanal_ekle(self, kanal_ismi):
        print("Kanal Ekleniyor")
        time.sleep(1) # 1 saniye bekletiyoruz
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi...")

    def rastgele_kanal(self):
        rastgele_index = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele_index]

        print(f"Suan ki Kanal: {self.kanal}")
    
    def __len__(self):
        return len(self.kanal_listesi)
    
    def __str__(self) -> str:
        return f"TV Durumu: {self.tv_durum}\nKanal Listesi: {self.kanal_listesi}\nSuan ki Kanal: {self.kanal}"

kumanda = Kumanda()

"""

Televizyon Uygulamasi


1. Tv Ac

2. Tv Kapat

3. Ses Ayarlari

4. Kanal Ekle

5. Kanal Sayisini Ögrenme

6. Rastgele Kanala Gecme

7. Televizyon Bilgileri

Çikmak için 'q' ya basin.

"""


while True:

    islem = input("İşlemi Seciniz:")

    if (islem == "q"):
        print("Program Sonlandiriliyor...")
        break

    elif (islem == "1"):
        kumanda.tv_ac()
    elif (islem == "2"):
        kumanda.tv_kapat()

    elif (islem == "3"):
        kumanda.ses_ayarlari()

    elif (islem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayirarak girin:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (islem == "5"):

        print("Kanal Sayisi:",len(kumanda))

    elif (islem == "6"):
        kumanda.rastgele_kanal()
    elif (islem == "7"):
        print(kumanda)

    else:
        print("Gecersiz İslem......")