#Kodu yazan Oğuzhan Demirbaş
#Kodun yazılma tarihi 28.11.2023
#proje amacı:Geometrik şekillerin alanlarını hesaplama
import math
def kare(ken):
      print("Karenin alanı = {}".format(ken * ken))
def dikdortgen(ken, uz):
       print("Dikdörtgenin alanı = {}".format(ken * uz))

def yamuk(al_tab, us_tab, yuk):
       print("Yamuğun alanı {}".format(((al_tab + us_tab) * yuk) / 2))

def parelelkenar(ken, yuk):
       print("Parelel kenarın alanı {}".format(ken * yuk))

def EskenarDortgen(alt_k, yan_k):
       print("Eşkenar dörtgenin alanı {}".format(alt_k * yan_k) / 2)

def Cokgen_Teg(ken_s,r,ken_u):
    print("İç teğet çemberinin yarıçapı r olan ÇOKGENİN alanı {}".format(ken_u*ken_s*r/2))

def Cokgen_Cev(ken_s,R):
    print("İç teğet çemberinin yarıçapı r olan ÇOKGENİN alanı {}".format((1/2)*ken_s*R**2*math.sin(360/ken_s)))


try:
    print("\nSeçenekler\n1--Kare\n2--Dikdörtgen\n3--Yamuk\n4--Parelelkenar\n5--Eşkenar\n6--Düzgün Çokgen-1(iç teğet)\n7--Düzgün Çokgen-2(çevrel)")
    sec = int(input("Bir seçim yapın :"))

    if(sec==1):
        ken = float(input("Kenar değeri giriniz :"))
        kare(ken)
    elif(sec==2):
        ken = float(input("Kenar değeri giriniz :"))
        uz = float(input("Uzunluk değeri giriniz :"))
        dikdortgen(ken, uz)
    elif(sec==3):
             yuk = float(input("Yükseklik değeri giriniz :"))
             al_tab = float(input("Alt taban değeri giriniz :"))
             us_tab = float(input("Üst taban değeri giriniz :"))
             yamuk(al_tab, us_tab, yuk)
    elif(sec==4):
             ken = float(input("Kenar değeri giriniz :"))
             yuk = float(input("Yükseklik değeri giriniz :"))
             parelelkenar(ken,yuk)
    elif(sec==5):
             alt_k=float(input("Alt kenar giriniz :"))
             yan_k = float(input("Yan kenar giriniz :"))
             EskenarDortgen(alt_k,yan_k)
    elif(sec==6):
            ken_s=int(input("Çokgenin kenarlarının sayısını giriniz :"))
            r=int(input("İç teğet çemberin yarıçapını 'r' değerini giriniz :"))
            ken_u=int(input("Çokgenin bir kenar uzunluğunu giriniz :"))
            Cokgen_Teg(ken_s, r, ken_u)

    elif(sec==7):
            ken_s = int(input("Çokgenin kenarlarının sayısını giriniz :"))
            R= (input("Çevrel çemberin yarıçapını 'R'' değerini giriniz :"))
            Cokgen_Cev(ken_s,R)
except ValueError:
    print("Boş değer girdiniz !!")



