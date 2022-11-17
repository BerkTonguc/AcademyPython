# #! kullanıcıdan girdi almak
# #! karar blokları
# #! döngüler

# print("2. gün başlangıç")

# # userInput = input()
# # print(f"Girilen değer: {userInput}")

# #! type conversion
# numberStr = "10";
# print(type(numberStr))
# number = int(numberStr)
# print(number+10)
# print(type(number))

# userInput = input()
# lessonNote=float(userInput)
# print(f"Ders notunuz : {lessonNote}")

# # indent
# # n adet conditional bağlı karar bloğu

# if lessonNote>50:
#     print("Başarıyla Geçtiniz")
# elif lessonNote == 50:
#     print("Sınırda Geçtiniz")
# elif lessonNote == 49:
#     print("Sınırda Kaldınız")
# else:
#     print("Kaldınız")

# vize ve final hesaplama algoritması yazınız.

vize = float(input("Lütfen vize notunuzu giriniz : "))
final = float(input("Lütfen final notunuzu giriniz : "))
sonuc = vize*0.4+final*0.6

if sonuc>=0 and sonuc<=49:
    print(f"Hesaplanan notunuz : {sonuc} , Harf notunuz FF ")
elif sonuc>=50 and sonuc<=60:
    print(f"Hesaplanan notunuz : {sonuc} , Harf Notunuz DD ")
elif sonuc>=61 and sonuc<70:
    print(f"Hesaplanan notunuz : {sonuc} , Harf notunuz CC ")
elif sonuc>=71 and sonuc<80:
    print(f"Hesaplanan notunuz : {sonuc} , Harf notunuz BB ")
else:
    print(f"Hesaplanan notunuz : {sonuc} , Harf notunuz AA ")





    