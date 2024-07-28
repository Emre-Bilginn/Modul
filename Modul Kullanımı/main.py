import my_module

carpanlar = my_module.asal_carpanlar(54)
for a in carpanlar:
    print(a)

print("----------------------------")

toplam = 0
harfler = "abcdefghijklmnopqrstuvwxyz"
metin = (input("Metin giriniz:"))
harf_sayisi = my_module.harf_adeti(metin)

for harf,sayi in harf_sayisi.items():
    if (harf in harfler):
        toplam += sayi

for harf,sayi in harf_sayisi.items():
    if (harf in harfler):
        print(f"'{harf}' : {sayi} adet  => %{((100*sayi)/toplam):.2f}")

print("----------------------------")

en_uzun_kelime,kelime_uzunuğu = my_module.en_uzun_kelime_bulma(metin)
print("En uzun kelime : ",en_uzun_kelime)
print("Kelimenin uzunluğu : ",kelime_uzunuğu)

print("----------------------------")

my_module.bilgi("Emre","Bilgin","211220059","Savaşı sonlandırın, barışı sağlayın; Dünya daha güzel bir yer olacak")

print("----------------------------")