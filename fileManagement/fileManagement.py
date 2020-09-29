def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama > 90:
        harf = "AA"
    elif ortalama > 85 and ortalama <= 89:
        harf = "BA"
    elif ortalama > 80 and ortalama <= 84:
        harf = "BB"
    elif ortalama > 75 and ortalama <= 79:
        harf = "CB"
    elif ortalama > 70 and ortalama <= 74:
        harf = "CC"
    elif ortalama > 65 and ortalama <= 69:
        harf = "DC"
    elif ortalama > 60 and ortalama <= 64:
        harf = "DD"
    else:
        harf = "FF"

    return ogrenciAdi + ": " + harf + "\n"


def ortalamalari_oku():
    with open("Sinav_notları.txt", "r",4) as file:
        for satir in file:
            print(not_hesapla(satir))


def not_gir():
    ad = input("Öğrenci Adı:")
    soyad = input("Öğrenci soyadı:")
    not1 = input("1.Notunuzu giriniz:")
    not2 = input("2.Notunuzu giriniz:")
    not3 = input("3.Notunuzu giriniz:")

    with open("Sinav_notları.txt", "a", encoding="utf-8") as file:
        file.write(ad + " " + soyad + ":" + not1 + "," + not2 + "," + not3 + "\n")


def notlari_kayit_et():
    with open("Sinav_notları.txt", "r", encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = input(" 1-Notları Oku \n 2-Not Gir \n 3- Notları kayıt et  \n 4-Çıkış \n ")
    try:
        if islem == '1':
            ortalamalari_oku()
        elif islem == '2':
            not_gir()
        elif islem == '3':
            notlari_kayit_et()
        else:
            break
    except:
        print("İlk işlem 1. seçim olamaz!")