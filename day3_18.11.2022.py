#try catch , hata yakalama
#handled exception

try:
    examGrade = float(input("Lütfen sınav notunuzu giriniz:"))
       
except ValueError:
    print("Deneme 123")
except ZeroDivisionError:
    print("Sayı sıfıra bölünemez")
except:
    print("Doğru bir girdi girmediniz")
finally:
    print("Try except bloğu sona erdi")


#! Şirket çalışanları verilerini tutan dosya oluşturulacak
#! Kullanıcıdan çalışan sayısı alınacak
#! Çalışan sayısı kadar isim, soyisim, maaş bilgisi alınacak
#! Dosyadaki her satıra "Ad Soyad - Maaş" kalıbında çalışan bilgileri eklenecek.
#! programın sonunda bu dosyadan bilgileri satır satır okuyup listeleyecek kod yazılacak
#! eklenen çalışanlar mevcut çalışanları silmeyece, -üzerine yazılacak
#! hata yakalama işlemlerini unutmayalım, maaş mesela asd girilebilir, çalışan sayısı da yine öyle olabilir.


#! Cevap

try:
    workerCount = int(input("Çalışan sayısı giriniz: "))
except:
    print("Düzgün sayı girilmedi..")
    exit()
file = open("employees.txt","a+")
for i in range(workerCount):
    name = input(f"{i+1}. çalışanın adını giriniz: ")
    lastName = input(f"{i+1}. çalışanın soyadını giriniz")
    salary = input(f"{i+1}. çalışanın maaşını giriniz")
    file.write(f"{name} {lastName} - {salary}\n")
file.seek(0) #cursor'u sayfanın başına alır aksi halde sonda olduğu için okuyamaz
print(file.read())
file.close()

#! grup ödevi cevabı 

try:
    employeesCount = int(input("Şirketinizin Çalişan Sayisini Giriniz: "))
    if employeesCount>0:
    
        for i in range(1,employeesCount+1):
            try:
                name = str(input(f"{i}. Çalisaninizin Adini Giriniz: "))
                surname = str(input(f"{i}. Çalisaninizin SoyAdini Giriniz: "))
                salary = float(input(f"{i}. Çalisaninizin Maas Bilgisini Giriniz: "))
            except:
                print("Lütfen Sayi Giriniz")
            file = open("employees.txt","a+")
            try:
                file.writelines(f"{name} {surname} - {salary}\n")
            except:
                print("Hatali giriş tespit edildi.")
        file = open("employees.txt","r")
        line = file.readlines()

        valueList = []
        for i in line:
            clearValues = i.rstrip("\n")
            valueList.append(clearValues)
        print(valueList)
        file.close()
    else:
        print("En az calisan sayiniz 1 olmalidir.")
except:
    print("Yanlis değer girdiniz.")


