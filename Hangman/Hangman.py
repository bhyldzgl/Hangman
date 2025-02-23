import random

# Zorluk seviyelerine göre kelime listeleri
kolay_kelimeler = ["elma", "masa", "kedi", "köpek", "araba"]
orta_kelimeler = ["bilgisayar", "yazilim", "ekran", "klavye", "internet"]
zor_kelimeler = ["mühendislik", "programlama", "veritabani", "matematik", "teknoloji"]

# Kullanıcıdan zorluk seviyesi seçmesini iste
while True:
    zorluk = input("Zorluk seviyesi seç (Kolay, Orta, Zor): ").lower()
    if zorluk in ["kolay", "orta", "zor"]:
        break
    print("Lütfen geçerli bir seviye gir! (Kolay, Orta, Zor)")

# Zorluk seviyesine göre kelime ve hak belirleme
if zorluk == "kolay":
    kelime = random.choice(kolay_kelimeler)
    hak = 8  # Kolay modda 8 hak
elif zorluk == "orta":
    kelime = random.choice(orta_kelimeler)
    hak = 6  # Orta modda 6 hak
else:
    kelime = random.choice(zor_kelimeler)
    hak = 4  # Zor modda 4 hak

tahmin_edilen = ["_"] * len(kelime)
harfler = []

# ASCII Adam Asmaca Çizimleri
adam_asmaca = [
    """
      ------
      |    |
      |    
      |   
      |    
      |   
    ------
    """,
    """
      ------
      |    |
      |    O
      |   
      |    
      |   
    ------
    """,
    """
      ------
      |    |
      |    O
      |    |
      |    
      |   
    ------
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |    
      |   
    ------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |    
      |   
    ------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / 
      |   
    ------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |   
    ------
    """
]

print(f"\n🎮 {zorluk.capitalize()} Mod: Adam Asmaca Oyununa Hoş Geldin!")
print(adam_asmaca[0])  # Boş çizimi göster
print(" ".join(tahmin_edilen))

while hak > 0 and "_" in tahmin_edilen:
    harf = input("\nBir harf tahmin et: ").lower()

    if harf in harfler:
        print("Bu harfi zaten denedin!")
        continue

    harfler.append(harf)

    if harf in kelime:
        print(f"Evet! '{harf}' harfi var.")
        for i in range(len(kelime)):
            if kelime[i] == harf:
                tahmin_edilen[i] = harf
    else:
        print(f"Hayır! '{harf}' harfi yok.")
        hak -= 1

    print(adam_asmaca[min(6, 8 - hak)])  # Yanlış sayısına göre adam çizimini göster
    print(" ".join(tahmin_edilen))
    print(f"Kalan hakkın: {hak}")

if "_" not in tahmin_edilen:
    print("\n🎉 Tebrikler! Kelimeyi buldun:", kelime)
else:
    print("\n😢 Kaybettin! Doğru kelime:", kelime)