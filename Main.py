import time
import json


def birlesim(dosya1, dosya2):
    with open(dosya1+ ".json", 'r') as f1, open(dosya2+ ".json", 'r') as f2:
        baslangic_zamani = time.perf_counter()
        data1 = json.load(f1)  
        data2 = json.load(f2)
        set1 = set(data1["sayilar"])
        set2 = set(data2["sayilar"])
        sonuc = set1.union(set2)
        print("Birleşim Sonucu:", sonuc)   
        bitis_zamani = time.perf_counter()
        gecen_zaman = str(bitis_zamani - baslangic_zamani) 
        sonucString = json.dumps(list(sonuc))
        with open("islem_sureleri.json", "a") as sure_dosyasi:
            json.dump({"islem": "birlesim","sonuc ":sonucString, "sure":gecen_zaman}, sure_dosyasi)
            sure_dosyasi.write("\n")           
def kesisim(dosya1,dosya2):  
    with open(dosya1+ ".json", 'r') as f1, open(dosya2+ ".json", 'r') as f2:
        baslangic_zamani = time.perf_counter()
        data1 = json.load(f1)  
        data2 = json.load(f2)
        set1 = set(data1["sayilar"])
        set2 = set(data2["sayilar"])
        sonuc = set1.intersection(set2)
        print("Kesişim Sonucu:", sonuc)   
        bitis_zamani = time.perf_counter()
        gecen_zaman = str(bitis_zamani - baslangic_zamani)
        sonucString = json.dumps(list(sonuc))
        with open("islem_sureleri.json", "a") as sure_dosyasi:
            json.dump({"islem": "kesisim","sonuc ":sonucString, "sure": gecen_zaman}, sure_dosyasi)
            sure_dosyasi.write("\n")
def fark1(dosya1,dosya2):
    with open(dosya1+ ".json", 'r') as f1, open(dosya2+ ".json", 'r') as f2:
        baslangic_zamani = time.perf_counter()
        data1 = json.load(f1)  
        data2 = json.load(f2)
        set1 = set(data1["sayilar"])
        set2 = set(data2["sayilar"])
        sonuc = set1.difference(set2)
        print("Fark Sonucu (dosya1 - dosya2):", sonuc)
        bitis_zamani = time.perf_counter()
        gecen_zaman = str(bitis_zamani - baslangic_zamani)
        sonucString = json.dumps(list(sonuc))
        with open("islem_sureleri.json", "a") as sure_dosyasi:
            json.dump({"islem": "fark1","sonuc ":sonucString, "sure": gecen_zaman}, sure_dosyasi)
            sure_dosyasi.write("\n")
def fark2(dosya1,dosya2):
    with open(dosya1 + ".json", 'r') as f1, open(dosya2+ ".json", 'r') as f2:
        baslangic_zamani = time.perf_counter()
        data1 = json.load(f1)  
        data2 = json.load(f2)
        set1 = set(data1["sayilar"])
        set2 = set(data2["sayilar"])
        sonuc = set2.difference(set1)
        print("Fark Sonucu (dosya2 - dosya1):", sonuc)
        bitis_zamani = time.perf_counter()
        gecen_zaman = str(bitis_zamani - baslangic_zamani)
        sonucString = json.dumps(list(sonuc))
        with open("islem_sureleri.json", "a") as sure_dosyasi:
            json.dump({"islem": "fark2","sonuc ":sonucString, "sure": gecen_zaman}, sure_dosyasi)
            sure_dosyasi.write("\n")


while True:

    varMi_yokMu = input("Sayı kumelerini içeren dosyalar mevcut mu? (e/h): ")

    if varMi_yokMu.lower() == 'e':
        dosya1 = input("Birinci dosyanın adını girin: ")
        dosya2 = input("İkinci dosyanın adını girin: ")

    elif varMi_yokMu.lower() == 'h':
        dosyaYeni1 = input("Birinci dosyanın adını girin (uzantısız): ")
        sayilar1 = input("Birinci dosya için sayıları virgülle ayrılmış olarak girin: ")
        dosyaYeni2 = input("İkinci dosyanın adını girin (uzantısız): ")
        sayilar2 = input("İkinci dosya için sayıları virgülle ayrılmış olarak girin: ")
        
        liste1 = [sayi.strip() for sayi in sayilar1.split(',')]
        liste2 = [sayi.strip() for sayi in sayilar2.split(',')]
            
        with open(dosyaYeni1 + ".json", 'w') as f1:
            json.dump({"sayilar": liste1}, f1)
            
        with open(dosyaYeni2 + ".json", 'w') as f2:
            json.dump({"sayilar": liste2}, f2)

    break

while True:
    islem = input("Hangi işlemi yapmak istersiniz? (1- Birleşim, 2- Kesişim, 3- Fark(dosya1 - dosya2), 4- Fark(dosya2 - dosya1)), CIKIS ICIN 'q' : ")
    

    if islem == "1":
        if varMi_yokMu.lower() == 'e':
            birlesim(dosya1, dosya2)
        elif varMi_yokMu.lower() == 'h':
            birlesim(dosyaYeni1, dosyaYeni2)
    elif islem == "2":
        if varMi_yokMu.lower() == 'e':
            kesisim(dosya1, dosya2)
        elif varMi_yokMu.lower() == 'h':
            kesisim(dosyaYeni1, dosyaYeni2)
    elif islem == "3":
        if varMi_yokMu.lower() == 'e':
            fark1(dosya1, dosya2)
        elif varMi_yokMu.lower() == 'h':
            fark1(dosyaYeni1, dosyaYeni2)
    elif islem == "4":
        if varMi_yokMu.lower() == 'e':
            fark2(dosya1, dosya2)
        elif varMi_yokMu.lower() == 'h':
            fark2(dosyaYeni1, dosyaYeni2)
    elif islem == "q":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz işlem seçimi.")
    