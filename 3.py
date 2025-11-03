#1
ad=input("Ad:")
soyad=input("Soyad:")
print(ad+" "+(soyad))
#2
sayı=int(input("sayı girin 1="))
sayı1=int(input("sayı girin 2="))
print(sayı + sayı1)
print(sayı * sayı1)
print(sayı - sayı1)
#3
yas=int(input("yasınızı giriniz:"))
print(yas>=18)
#4
dikdörtgen=int(input("uzunluğu giriniz:"))
dikdörtgen1=int(input("genişliği giriniz:"))
print(dikdörtgen*dikdörtgen1 ,"alanı")
print(dikdörtgen*dikdörtgen1*2 ,"çevresi")
#5
sayı3=int(input("sayı girin:"))
print(0<=sayı3)
#6
ör=input("kelime giriniz:")
print(ör[0:3])
print(ör[-2:])
#7
sayı4=int(input("sayı gir:"))
print(float(sayı4/2))
#8
sayı5=int(input("sayı gir"))
sayı6=int(input("sayı gir1"))
if(sayı5 %2==0) and (sayı6 %2==0):
 print(f"başarılı girdiniz")
else:
 print(f"başarısız")
#9
x=("merhaba"())
print(x.upper())
#10
sayı7=int(input("yarıçap:"))
sayı8=int(3.14)
print(float(sayı7*sayı8*2))
#11
sayı9=int(input("sayı:"))
sayı10=int(input("sayı:"))
if sayı9 == sayı10:
    print("birbirine eşit.")
elif sayı9 > sayı10:
    print("Birinci büyüktür.")
else:
    print("İkinci büyüktür.")
#12
sayı11=int(input("sayı gir"))
if(sayı11 %3==0) and (sayı11 %5==0):
     print(f"bölünür")
else:
 print(f"bölünmez")