
def sifrele(mesaj, anahtar):
    sifrelenmis_metin = ""
    for harf in mesaj:
        if harf.isalpha():
            kaydirma = anahtar % 26
            yeni_harf_kodu = ord(harf) + kaydirma
            
            if harf.islower() and yeni_harf_kodu > ord('z'):
                yeni_harf_kodu -= 26
            elif harf.isupper() and yeni_harf_kodu > ord('Z'):
                yeni_harf_kodu -= 26
                
            sifrelenmis_metin += chr(yeni_harf_kodu)
        else:
   
            sifrelenmis_metin += harf 
    return sifrelenmis_metin

def sifre_coz(sifreli_mesaj, anahtar):
    return sifrele(sifreli_mesaj, -anahtar)


print("--- T.C. GÜVENLİ HABERLEŞME TERMİNALİ ---")
print("Durum: AKTİF | Şifreleme Protokolü: Simetrik Kaydırma\n")

orijinal_mesaj = input("Merkeze iletilecek mesajı girin: ")
guvenlik_anahtari = 7 


sifreli_veri = sifrele(orijinal_mesaj, guvenlik_anahtari)
print(f"\n[📡 RADAR ÇIKIŞI] Şifrelenmiş Veri: {sifreli_veri}")

cozulmus_veri = sifre_coz(sifreli_veri, guvenlik_anahtari)
print(f"[🛡️ MERKEZ ÜS] Çözülen Orijinal Veri: {cozulmus_veri}")