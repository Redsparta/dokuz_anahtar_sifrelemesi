import numpy as np                  #numpy kütüphanesi yüklendi
import cv2                          #opencv kütüphanesi yüklendi

cümle="şampiyon"                    #şifrelenecek cümle girildi
cümle_okuma=[]                      #cümle okuma adında boş liste oluşturuldu

for i in cümle:                     #i cümle string i içinde dolaşacak
    cümle_okuma.append(i)           #cümle okuma adındaki listeye i elemanını ekliyoruz
    cümle_okuma=list(cümle_okuma)
print("mesaj=",cümle_okuma)         #cümle okuma listesini yazdırıyoruz

harfler=["a","b","c","ç","d","e","f","g","ğ","h",
         "ı","i","j","k","l","m","n","o","ö","p",
         "r","s","ş","t","u","ü","v","y","z"]
sayılar=[1,2,3,4,5,6,
         7,8,9,10,11,12,
         13,14,15,16,17,
         18,19,20,21,22,
         23,24,25,26,27,
         28,29]


şifre_sayı_dönüşümü=[]

for i in cümle_okuma:                                           #i cümleokuma içinde dolaşacak
    for j in range(len(cümle_okuma)):                           #j cümleokuma uzunluğunda bir dizi içinde dolaşacak
        for k in range(len(harfler)):                           #k harfler uzunluğunda bir dizi içinde dolaşacak
            if cümle_okuma[j]==harfler[k]:                      #eğer cümleokuma nın j elemanı harfler k elemanına eşit ise
                i=sayılar[k]                                    #i sayılar k ya eşit olacak
                şifre_sayı_dönüşümü.append(i)                   #şifresayıdönüşümü listesine i atanacak
                                                                #
şifre_sayı_dönüşümü = şifre_sayı_dönüşümü[0:len(cümle_okuma)]   #cümle okuma sayısı kadar eleman şlfresayıdönüşümü olarak yazıdırılacak

print("mesaj-sayi donusumu=",şifre_sayı_dönüşümü)               # 
  


#k1=input(str("K1 anahtarını giriniz:"))
#k2=input(str("K2 anahtarını giriniz:"))
#k3=input(str("K3 anahtarını giriniz:"))

k1='56546'                          #k1 private key i
k2='36459'                          #k2 private key i 
k3='21663'                          #k3 private key i
print("private key=",k1,k2,k3)      #privae keylerin yazdırılması
a1=k1+k3                            #k1 ve k3 ün toplanması
a1=int(a1)                          #a1 değişkeni integer yapılır
a2=k2+k3                            #k2 ve k3 ün toplanması
a2=int(a2)                          #a2 değişkeni integer yapılır
a3=k1+k2                            #k1 ve k2 nin toplamı
a3=int(a3)                          #a3 değişkeni yapılır
    
a1 = a1%29                          #a1 sayısı a1'in mod 29 lu haline eşittir
a2 = a2%29                          #a2 sayısı a2'in mod 29 lu haline eşittir
a3 = a3%29                          #a3 sayısı a3'in mod 29 lu haline eşittir
print("a1=",a1)
print("a2=",a2)
print("a3=",a3)

çarpan=[]                   
bölen=[]
yggdrasil=[]
xeno=[]
travel=[]
for i in şifre_sayı_dönüşümü:       #şifre sayıdönüşümü içerisinde i harfi dolaşır
    if i<=3:                        # i==3 ise
        if i == 1:
            y = 1
            x = 1
            t = 1 
        elif i==2:
            y = 2
            x = 1
            t = 2
        else:
            y = 3
            x = 2
            t = 3
        yggdrasil.append(y)         #y yggdrasil e atanır
        xeno.append(x)              #x xeno ya atanır
        travel.append(t)            #t travel e atanır
    else:
        for j in range(1,i+1):      #j i den başlanarak liste içerisinde birer birer arttırılır
            if i%j == 0:            #i mod j sıfıra eşitse
                if i==j:            #i j ye eşitse
                    yggdrasil.append(j)     #j yggdrasil e atanacak
                else:
                    çarpan.append(j)        #j çarpanlara atanacak
                    çarpan.sort()           #çarpanlar listesi sıralanacak
                    xeno=çarpan[:len(cümle)]    #xeno listesi çarpan listesinin cümle uzunlupğu kadar ki elemanlarından oluşacak
        t=i%29              # t i mod 29'a eşit olacak
        travel.append(t)    #t travel e atanacak
                    
    
print("yggdrasil=",yggdrasil)
print("xeno=",xeno)
print("travel=",travel)
                
k1=int(k1)#
a1=int(a1)#
a2=int(a2)#   BÜTÜN a VE k DEĞİŞKENLERİ İNTEGER OLARAK EŞİTLENİR
k2=int(k2)#
k3=int(k3)#
a3=int(a3)#

şifre=[]                        
for i in range(len(yggdrasil)):     #i yggdrasil uzunluğunda bir dizi içinde dolanacak
    y=yggdrasil[i]                  
    i=i+1
    for j in range(len(xeno)):      #j xeno uzunluuğunda bir dizi içinde dolanacak
        x=xeno[j]
        j=j+1
        for k in range(len(travel)):    #k travel uzunluğunda bir dizi içerisinde dolanacaktır
            t=travel[k]
            k=k+1
            p=k1*x*a1+k2*y*a2+k3*t*a3   #şifre fonksiyonu P ye eşittir
            p = p % 29                  #her bir P mod 29 a eşit olacaktır
    şifre.append(p)
print("sifre=",şifre)

img = cv2.imread("NFT BESRT-01.png")        #şifrenin gizleneceği resim girilir
img = cv2.resize(img, (1000,1000))          #resim 1000x1000 olacak şekilde yeniden boyutlandırılır
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     #resim tek kanala indirgenir
img1 = cv2.resize(gray,(1000,1000))             #gri resim yeniden boyutlanır   
değişken=0

for x in range(0,1000,50):                #x img 0x0 dan başlanarak yüzer yüzer img 1000x1000 e kadar adım atılır
    for y in range(0,1000,50):             #x img 0x0 dan başlanarak yüzer yüzer img 1000x1000 e kadar adım atılır
        res_şif= şifre[değişken]            
        img1[x,y]=res_şif

cv2.imshow("eski resim", img)    
cv2.imshow("yeni resim", img1)
cv2.waitKey(0)
