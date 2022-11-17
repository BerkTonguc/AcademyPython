# #! kullanıcıdan girdi almak
# #! karar blokları
# #! döngüler

print("2. gün başlangıç")

# userInput = input()
# print(f"Girilen değer: {userInput}")

#! type conversion
numberStr = "10";
print(type(numberStr))
number = int(numberStr)
print(number+10)
print(type(number))

userInput = input()
lessonNote=float(userInput)
print(f"Ders notunuz : {lessonNote}")

# indent
# n adet conditional bağlı karar bloğu

if lessonNote>50:
    print("Başarıyla Geçtiniz")
elif lessonNote == 50:
    print("Sınırda Geçtiniz")
elif lessonNote == 49:
    print("Sınırda Kaldınız")
else:
    print("Kaldınız")

#vize ve final hesaplama algoritması yazınız.

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


####################################

# Kullanicidan vize ve final notları
# Vize %40 final %60 etkili
# vize ve final notları 50.5 gibi ondalıklı olabilir
# Uygulama ortalamayı hesaplayacak ve ortalamaya göre
# 0-49 FF
# 50-60 DD
# 60-70 CC
# 70-80 BB
# 80-100 AA
# Not ortalamasını ve not harfini kullanıcıya göster.

# Ödev1
midtermGrade = float(input("Midterm Notunuzu Giriniz: "))
finalGrade = float(input("Final Notunuzu Giriniz: "))
meanGrade = (0.40 * midtermGrade) + (0.60 * finalGrade)

if 0<=meanGrade<=49:
    print(f"Not ortalamaniz {meanGrade} ve Harf Notunuz: FF")
elif 50<=meanGrade<=60:
    print(f"Not ortalamaniz {meanGrade} ve Harf Notunuz: DD")
elif 60<meanGrade<=70:
    print(f"Not ortalamaniz {meanGrade} ve Harf Notunuz: CC")
elif 70<meanGrade<=80:
    print(f"Not ortalamaniz {meanGrade} ve Harf Notunuz: BB")
elif 80<meanGrade<=100:
    print(f"Not ortalamaniz {meanGrade} ve Harf Notunuz: AA")
else:
    print("Geçersiz Not Değerleri Girdiniz.")

# Ödev2
failed = 0
success = 0
lessonCount = int(input("Ders Sayinizi Giriniz: "))

for i in range(1,lessonCount+1):
    midtermGrade = float(input(f"{i}. Dersinizin Midterm Notunuzu Giriniz: "))
    finalGrade = float(input(f"{i}. Dersinizin Final Notunuzu Giriniz: "))
    meanGrade = (0.40 * midtermGrade) + (0.60 * finalGrade)
    if meanGrade <=50:
        print(f"{i}. Dersi Geçemediniz ve Not Ortalamaniz {meanGrade}")
        failed +=1
    elif 50<meanGrade<=100:
        print(f"{i}. Dersi Geçtiniz ve Not Ortalamaniz {meanGrade}")
        success +=1
    else:
        print("Geçersiz Not Değerleri Girdiniz")    
print(f"Toplamda {failed} dersten kaldiniz")
print(f"Toplamda {success} dersten geçtiniz")


##############################################


for i in range(6):
    print(i)


students = ["Nilüfer","Özlem","Berk","Zakir"]
for i in students:
    print(i)


#! infinite loop
# while True:
#     print("I am infinite!!")

i = 0
while i < 10:
    print(i)
    i+=1


#### 2. gün, gün sonu grup ödevi ;

failed = 0
success = 0
lessonCount = int(input("Ders Sayinizi Giriniz: "))

sonuc = []
failedDict = {"Ders ve Ortalamasi":sonuc}
sonuc1= []
passedDict = {"Ders ve Ortalamasi":sonuc1}
for i in range(1,lessonCount+1):
    midtermGrade = float(input(f"{i}. Dersinizin Midterm Notunuzu Giriniz: "))
    finalGrade = float(input(f"{i}. Dersinizin Final Notunuzu Giriniz: "))
    meanGrade = (0.40 * midtermGrade) + (0.60 * finalGrade)
    if meanGrade <=50:
        failed +=1
        sonuc.append([i,meanGrade])
    elif 50<meanGrade<=100:
        success +=1
        sonuc1.append([i,meanGrade])
    else:
        print("Geçersiz Not Değerleri Girdiniz")    

print(f"Kaldiğiniz Ders/Dersler ve Bilgileri: {failedDict}")
print(f"Gectiğiniz Ders/Dersler ve Bilgileri: {passedDict}")

    