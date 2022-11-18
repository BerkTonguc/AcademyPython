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




