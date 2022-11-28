--Veri seçme listeleme
--Sytax => yazım kuralları
--case sensitive değil!
SELECT name, id from categories;

-- Tüm alanları seçmek => *
SELECT * FROM categories;

-- Sıralama 
-- Ürünleri stok adetine göre büyükten küçüğe sırala
-- ORDER
-- Default olarak küçükten büyüğe sıralar => ASCENDING (ASC)
SELECT * FROM products
ORDER BY stock;
--Bu ikisi aynı
SELECT * FROM products
ORDER BY stock ASC;
--
SELECT * FROM products
ORDER BY stock DESC;
-- Order by sadece matematiksel sıralama yapmaz! Alfabetik sıralama da yapar.
Select  * from products
ORDER BY name DESC;

--Highlight etmeden çalıştıracaksak her bir sorgunun sonuna noktalı virgül koyarsak sadece sonuncu sorguyu çalıştırır.

--Filter
--Stok adedi en az 60 olan verileri göster
SELECT * FROM products
where stock > 60;

--Birden fazla filtre birleştirme
-- AND - OR
--Stok adeti en az 60 olan ve category_id si 2 olan verileri getir.

SELECT * FROM products
WHERE stock > 60 AND category_id=2;

--Stok adeti en az 60 olan veya category_id si 2 olan verileri getir.

SELECT * FROM products
WHERE stock > 60 OR category_id=2;

-- İsmi şort veya Tişört olan ürünleri getir.
SELECT * from products
WHERE name = 'Şort' or name = 'Tişört';

-- IN() Fonsksiyonu
-- İçerisine parametre olarak verilen n kadar veri ile ilgili alanın uyuşmasını bekler.
SELECT * FROM PRODUCTS
WHERE NAME IN('Şort','Tişört','Mont','Ayakkabı');

SELECT * from products
WHERE stock IN(30,40,50,100);

-- Between keywordü
-- Sınırdaki değerler de dahil

SELECT * FROM products
WHERE stock BETWEEN 40 and 70;

SELECT * FROM products
WHERE stock <=70 AND STOCK >=40;

-- LIKE keyword'ü
-- İsminin içinde 't' geçen tüm ürünleri getir
Select * from products
WHERE name LIKE '%t%';

-- lower => tüm harfleri küçük hale getirir
SELECT* FROM products
WHERE LOWER(name) LIKE 't%';

-- _ => karakter atlama
-- üçüncü harfi 'r' rolan tüm ürünleri
-- eğer % yi kaldırırsak
SELECT * from products
WHERE LOWER(name) LIKE '__r%';

-- içinde r ve r'yi takip eden en az 1 karakter olan sorgu
SELECT * FROM products
WHERE LOWER(name) LIKE '%_r%';





