def Topla(x,y):
   return x+y 

def Cikar(x,y):
   return x-y 

def Carp(x,y):
   return x*y 

def Bol(x,y):
   return x/y

def Mod(x,y):
   return x%y


print("Toplama için 1 -- Çıkarma için 2 -- Çarpma için 3 -- Bölme için 4 -- Mod Alma için 5 rakamını giriniz")
print()

try:
   secim = int(input("Seçiminizi giriniz :"))
except ValueError:
   print("1-5 arasında bir sayı girmediniz!")
   
 
sayi1 = float(input("1. Sayı: "))
sayi2 = float(input("2. Sayı: "))
 
if secim == 1:
   print(sayi1,"+",sayi2,"=", Topla(sayi1,sayi2))
 
elif secim == 2:
   print(sayi1,"-",sayi2,"=", Cikar(sayi1,sayi2))
 
elif secim == 3:
   print(sayi1,"*",sayi2,"=", Carp(sayi1,sayi2))
 
elif secim == 4:
   try:
      print(sayi1,"/",sayi2,"=", Bol(sayi1,sayi2))
   except ZeroDivisionError:
      print("Sayı sıfıra bölünemez")

elif secim == '5':
   print(sayi1,"%",sayi2,"=", Mod(sayi1,sayi2))

else:
   print("Hatalı seçim yaptınız!")