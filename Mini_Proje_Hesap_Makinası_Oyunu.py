#kodu yazan Oğuzhan Demirbaş
#Kodun yazılma tarihi 28.11.2023
#Kodun konusu:Çarpım tablosu oyunu yaptık.
try:
    import random#rastgele sayı üretebilmek için random kütüphanesini çağırdık
    def rastgele_sayı_kolay():
        return random.randint(1,10)#rastgele sayı üretmek için random.randit modülünü kullandık
    sayı_1 = rastgele_sayı_kolay()
    sayı_2 = rastgele_sayı_kolay()

    def rastgele_sayı_orta():
        return random.randint(1,20)#rastgele sayı üretmek için random.randit modülünü kullandık

    sayı_1= rastgele_sayı_orta()
    sayı_2=rastgele_sayı_orta()
    def rastgele_sayı_zor():
        return random.randint(1,50)#rastgele sayı üretmek için random.randit modülünü kullandık

    sayı_1= rastgele_sayı_zor()
    sayı_2=rastgele_sayı_zor()
    def rastgele_sayı_Cok_Zor():
        return random.randint(1,200)#rastgele sayı üretmek için random.randit modülünü kullandık

    sayı_1 = rastgele_sayı_Cok_Zor()
    sayı_2 = rastgele_sayı_Cok_Zor()

    print("\nSeviye seçin\n1--Kolay\n2--Orta\n3--Zor\n4--Çok zor")
    sec=int(input("Seçiminizi girin :"))

    if(sec==1):
        sayı_1=rastgele_sayı_kolay()#Fonksiyon çağırdık
        sayı_2=rastgele_sayı_kolay()
        print(f"{sayı_1}*{sayı_2}")
        cvp=int(input("Cevabınızı girin :"))
        hsp_kolay = sayı_1 * sayı_2
        if(cvp==hsp_kolay):
            print(f"Tebrikler {cvp} cevabınız doğru")
        else:
            print(f"Malesef {cvp} cevabınız yanlış,DOĞRU cevap {hsp_kolay} ")
    elif(sec==2):
        sayı_1 = rastgele_sayı_orta()
        sayı_2 = rastgele_sayı_orta()
        print(f"{sayı_1}*{sayı_2}")
        cvp=int(input("Cevabınızı girin :"))
        hsp_orta=sayı_1 * sayı_2
        if (cvp==hsp_orta):
            print(f"Tebrikler {cvp} cevabınız doğru")
        else:
            print(f"Malesef {cvp} cevabınız yanlış,DOĞRU cevap {hsp_orta}")
    elif(sec==3):
        sayı_1 = rastgele_sayı_zor()
        sayı_2 = rastgele_sayı_zor()
        print(f"{sayı_1}*{sayı_2}")
        cvp = int(input("Cevabınızı girin :"))
        hsp_zor = sayı_1 * sayı_2
        if (cvp == hsp_zor):
            print(f"Tebrikler {cvp} cevabınız doğru")
        else:
            print(f"Malesef {cvp} cevabınız yanlış,DOĞRU cevap {hsp_zor}")
    elif(sec==4):
        sayı_1 = rastgele_sayı_Cok_Zor()
        sayı_2 = rastgele_sayı_Cok_Zor()
        print(f"{sayı_1}*{sayı_2}")
        cvp = int(input("Cevabınızı girin :"))
        hsp_CokZor = sayı_1 * sayı_2
        if (cvp == hsp_CokZor):
            print(f"Tebrikler {cvp} cevabınız doğru")
        else:
            print(f"Malesef {cvp} cevabınız yanlış,DOĞRU cevap {hsp_CokZor}")
except ValueError:#Kullanıcının boş değer girmesini engelledik hata mesajı döndürdük
    print("Geçerli bir değer giriniz !!")










