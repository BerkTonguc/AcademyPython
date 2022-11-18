# file = open("sample.txt","w")
# #write = tamamen sıfırdan yazma
# #append = üzerine ekleme
# #read = okuma

# file.writelines("\n deneme 123")
# print(file.read())
# file.close()

#! Şirket çalışanları verilerini tutan dosya oluşturulacak
#! Kullanıcıdan çalışan sayısı alınacak
#! Çalışan sayısı kadar isim, soyisim, maaş bilgisi alınacak
#! Dosyadaki her satıra "Ad Soyad - Maaş" kalıbında çalışan bilgileri eklenecek.
#! programın sonunda bu dosyadan bilgileri satır satır okuyup listeleyecek kod yazılacak
#! eklenen çalışanlar mevcut çalışanları silmeyece, -üzerine yazılacak
#! hata yakalama işlemlerini unutmayalım, maaş mesela asd girilebilir, çalışan sayısı da yine öyle olabilir.


#! Cevap


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
       



 
    




