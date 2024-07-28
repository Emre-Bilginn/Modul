import re


def asal_carpanlar(sayi):
    i=2
    carpanlar =[]
    while i * i <= sayi:
        if sayi % i != 0:
            i+=1
        else:
            sayi = sayi / i
            carpanlar.append(i)
    if sayi > 1:
        carpanlar.append(int(sayi))
    return carpanlar

def harf_adeti(metin):
    harf_sayisi = {}
    for harf in metin:
        harf = harf.lower()
        if harf in harf_sayisi:
            harf_sayisi[harf]+=1
        else:
            harf_sayisi[harf]=1
    return harf_sayisi

def en_uzun_kelime_bulma(metin):
    kelimeler = re.findall(r'\b\w+\b', metin)
    en_uzun_kelime = max(kelimeler,key=len)
    kelime_boyu = len(en_uzun_kelime)
    return en_uzun_kelime,kelime_boyu

def bilgi(name,surname,no,note):
    print(name)
    print(surname)
    print(no)
    print(note.upper())