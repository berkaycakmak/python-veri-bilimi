# =============================================================================
# Zero-to-Python
# =============================================================================

#Sayılar;

#Python'da temel matematiksel işlemler gerçekleştirilebilir.

9+9

9*9

9/9

#Ondalıklı olmayan sayılar 'Integer' yani 'int' tipinde değişkenlerdir.

type(9)

#Ondalıklı olan sayılar 'Float' tipinde değişkenlerdir.

type(9.2)

#Kodların çıktısını ekrana yazdırmak için print('...') kullanılır.

print('Hello World!')

#Yazı değeri taşıyan değişkenler 'String' yani 'str' tipindedir.

type('Hello World!')

#Bazı string uygulamaları;

'a' + 'b'

'a' 'b'

'a' + ' b'

#Uzunluk bilgisi için len() komutu kullanılır.

len('Berkay Cakmak')

#veya;

a = 'Berkay Cakmak'
len(a) #olarak belirli bir string ifadesi a değişkenine atanarak uzunluğu bulunabilir.

#String Metodları - upper() & lower()

a = 'Berkay Cakmak'
a.upper()

a.lower()

#Bir stringin küçük veya büyük harf olmasının kontrolü için;

a = 'Berkay Cakmak'
a.islower()

a.isupper()

#Elimizdeki stringlerin içerisindeki karakterleri değiştirmek için replace() komutu kullanılır.

a = 'Berkay Cakmak'
a.replace('e', 'a')

#Stringlerde istenmeyen komutları kırpmak için strip() komutu kullanılır.

a = '-Berkay Çakmak-'
a.strip('-')

#Üzerinde çalışıyor olduğumuz veri tipine uygulanabilecek olan metotları görebilmek için dir() metodu kullanılır.

a = 'berkay cakmak'
dir(a)

#örneğin;

a = 'berkay cakmak'
a.capitalize()

a.title()

# Stringlerin alt kümeleri (substringler)
# Bir stringden belirli bir bölümü seçmek için [] içerisinde index girilmesi gerekmektedir. Aşağıdaki a değişkeninde 
# 0. index B, 1. index e, 2. index r olmak üzere bu şekilde 0'dan başlayarak indexleme işlemi yapılır.

a = 'Berkay Cakmak'
a[0]

a[1]

a[0:3]

#Son örnekte 0'dan başlayıp 3. indexe kadar seçim yapar. 3. index bu gruba dahil edilmez.

a = 'Berkay Cakmak'
a[3:9]

#Kullanıcıdan bilgi almak için input() metodu kullanılır.

b = input()
c = input()
b + c

#Farkedildiği üzere matematiksel bir toplama işlemi yerine bir string toplaması yapıldı. Bu işlemi matematiksel bir 
#toplama işlemine dönüştürmek için tip dönüşümü yapılır.

b = input()
c = input()
int(b) + int(c)

#Herhangi bir değişkeni başka bir tipe çevirmek için değiştirmek istediğimiz tipin parantezine alırız.

a = int(11.3)
type(a)

b = float(7)
type(b)

c = str(13)
type(c)

d = str(12.4)
type(d)

#print()

print('Berkay','Cakmak')

print('Berkay','Cakmak',sep = '_')

#Fonksiyonların detaylarına ulaşmak için fonksiyon başına ? koyarak yazılır.

?print

?type


# =============================================================================
# Veri Yapıları - Liste: ->Değiştirilebilirdir.  ->Kapsayıcıdır. (Farklı tipte veri tutabilir.) ->Sıralıdır.
# Liste oluşturmak için [] içine liste elemanları yazılabilir veya list() komutu kullanılır.
# =============================================================================

liste1 = [0,30,45,90,180]
type(liste1)

liste2 = ['a','berkay',15,24.3]
type(liste2)

liste3 = [liste1,liste2]
type(liste3)

len(liste3)

#liste3 adlı liste içerisinde 2 liste barındırıyor. Bu nedenle len() komutu ile eleman sayısı arandığında 2 değerine 
#ulaşıyoruz.

#Liste içerisindeki bir elemanın tipini sorgulamak için;

liste1 = [0,30,45,90,180]
type(liste1[1])

liste2 = ['a','berkay',15,24.3]
type(liste2[1])

liste3 = [liste1,liste2]
type(liste3[1])

#Bir değişken silmek için del fonksiyonu kullanılır.

del liste3

#Bir listenin içerisindeki elemanlara ulaşmak için [] içerisinde index sayısı yazılır.

liste1 = [0,30,45,90,180]
liste1[1]

liste1[0:2]

liste1[:2]

liste1[2:]

liste2 = ['a',['berkay',15,24.3]]
liste2[1][0]

#Listelere eleman ekleme, değiştirme ve silme işlemleri;

liste4 = ['ahmet', 'ali', 'veli', 'berkay']
liste4[1] = 'ali_değişti' #Değiştirme

liste4 = liste4 + ['mehmet'] #Ekleme

del liste4[2] #Silme

#Liste Metotları

dir(liste4)

liste4 = ['ahmet', 'ali', 'veli', 'berkay']
liste4.append('cakmak') #Listeye eleman ekler.

liste4.remove('veli') #Listedeki elemanı siler.

#Listeye indexe göre eleman ekleme ve silme;

liste4 = ['ahmet', 'ali', 'veli', 'berkay']
liste4.insert(0, 'ayşe') #Ekleme

liste4.insert(2,'hale') #Ekleme

len(liste4)
liste4.insert(len(liste4), 'ece') #Liste sonuna eleman ekler.

liste4.pop(0) #Silme

#Diğer önemli liste metotları;

liste4 = ['ahmet', 'berkay', 'ali', 'veli', 'berkay']
liste4.count('berkay') #Listedeki seçilen elemanın sayısını gösterir.

liste_yedek = liste4.copy() #Listenin kopyasını başka bir listeye atar.

liste4.extend(['a','b',1]) #Listeye ekler.

liste4.index('berkay') #Seçilen nesnenin listedeki indexini bulur.

liste4.reverse() #Listeyi tersine çevirir.

liste1 = [180,30,90,0,60]
liste1.sort() #Listeyi küçükten büyüğe sıralar.

liste1.clear() #Listenin içini temizler.

#Veri Yapıları - Tuple: ->Kapsayıcıdır. ->Sıralıdır. ->Değiştirilemez.
#Tuple oluşturmak için () içine tuple elemanları yazılabilir,

T = ('berkay','cakmak',1,2,3,15,12.7,[1,2,3])

#veya;

T = 'berkay','cakmak',1,2,3,15,12.7,[1,2,3]

#veya tuple() fonksiyonu kulanılır.

T = ('eleman')
type(T)

#Yukarıdaki tek elemanlı tuple görüldüğü üzere string olarak görülmektedir. Bu sorunun giderilmesi için;

T = ('eleman',)
type(T)

#tek elemanın sonuna ',' eklenir.

#Tuple eleman işlemleri;

T = ('berkay','cakmak',1,2,3,15,12.7,[1,2,3])
T[1]

T[0:3]

T[2] = 99 #Hata verir çünkü tuplelar değiştirilemez.

# Veri Yapıları - Dictionaries (Sözlükler): ->Kapsayıcıdır. ->Sırasızdır. ->Değiştirilebilir.
# Sıralama olmadığı için index işlemleri yapılamaz.
# Sözlük tanımlamak için {} içerisinde değerler yazılır.

Sozluk1 = {'REG' : 'Regresyon Modeli',
          'LOJ' : 'Lojistik Regresyon',
          'CART' : 'Classification and Reg. Tree'}

Sozluk2 = {'A' : 1,
          'B' : 2,
          'C' : 3}

Sozluk3 = {'REG' : ['Regresyon Modeli',10],
          'LOJ' : ['Lojistik Regresyon',20],
          'CART' : ['Classification and Reg. Tree',30]}


#Sözlük elemanlarına erişmek;

Sozluk1 = {'REG' : 'Regresyon Modeli',
          'LOJ' : 'Lojistik Regresyon',
          'CART' : 'Classification and Reg. Tree'}

Sozluk1['REG']

#Sözlüğe eleman eklemek ve değiştirmek;

Sozluk1 = {'REG' : 'Regresyon Modeli',
          'LOJ' : 'Lojistik Regresyon',
          'CART' : 'Classification and Reg. Tree'}

Sozluk1['GBM'] = 'Gradient Boosting Machienes' #Ekleme

Sozluk1['REG'] = 'Coklu Dogrusal Regresyon' #Değiştirme

#Veri Yapıları - Setler: ->Sırasızdır. ->Değerleri eşsizdir. (Tekrar eden değer olamaz) ->Değiştirilebilir.
#Set oluşturmak için set() fonksiyonu kullanılır.

l = [1,'a',12.3]
set1 = set(l)

t = (1,'a',12.3)
set2 = set(t)

a = 'berkay cakmak'
set3 = set(a)

set3 #Görüldüğü üzere her bir karakter 1 adet mevcut. Yani tekrar eden değerler tekilleştirilmiş haldedir.

l2 = ['berkay', 'cakmak','berkay', 'cakmak','berkay', 'cakmak','berkay', 'cakmak','berkay', 'cakmak',]
set4 = set(l2)

set4

set4[1] #Hata verir çünkü setler sırasızdır, index işlemleri yapılamaz.

#Sete eleman ekleme ve çıkarma işlemleri;

l3 = ['berkay', 'cakmak']
set5 = set(l3)

set5.add('python') #Ekleme
set5

set5.remove('python') #Silme (Eğer set içerisinde böyle bir eleman yoksa hata verir.)
set5

set5.discard('python') #Silme (Eğer set içerisinde böyle bir eleman yoksa hata vermez.)
set5

#Setlerde klasik küme işlemleri;

#difference() veya '-' ile iki kümenin farkı,
#intersection() veya '&' ile iki kümenin kesişimi,
#union() ile iki kümenin birleşimi,
#symmetric_difference() ile iki kümede de olmayan elemanlar bulunur.

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)

fark1 = set1 - set2
fark1

set2.difference(set1)

fark2 = set2 - set1
fark2

set1.intersection(set2)

kesisim = set1 & set2
kesisim

set1.union(set2)

set1.symmetric_difference(set2)

#Set sorgu işlemleri;

set1 = set([2,3,5])
set2 = set([1,2,3,4,5,6,7])

set1.isdisjoint(set2) #İki kümenin kesişimi boş olup olmadığının kontrolü

set1.issubset(set2) #set1, set2'nin alt kümesi midir?

set2.issuperset(set1) #set2, set1'i kapsıyor mu?


# =============================================================================
# Fonksiyonlar
# =============================================================================

#Fonksiyon yazmak;

def kare_al(x): #x'e bağlı kare_al adında bir fonksiyon tanımlandı.
    print(x**2) #x'in karesini alma ve ekrana yazdırma işlemi

kare_al(3)

#Bilgi notuyla birlikte çıktı üretmek;

def kare_al(x):
    print('Girilen sayının karesi: ' + str(x**2)) #print fonksiyonunda string ile string birleştirilebilir. Bundan
#dolayı (x**2) işlemi yapıldıktan sonra string tipine dönüştürülmüştür.

kare_al(3)

#İki argümanlı fonksiyon tanımlamak;

def carpma_yap(x, y):
    print('Girilen sayıların çarpımı: ' + str(x*y))

carpma_yap(10, 3)

#Bir fonksiyonun çıktısı 'return' ifadesi ile başka bir yere girdi olarak kullanılabilir.

def hesap(x, y, z):
    return (x+y)/z

hesap(2,3,5)*9 #Burada hesap fonksiyonunun çıktısı bir çarpma işlemine girdi olarak kullanılmıştır.

cikti = hesap(2,3,5) #Burada hesap fonksiyonunun çıktısı bir değişkene atanmıştır.
print(cikti)

#Local ve global değişkenler;

x = 10 #Global değişken
y = 20 #Global değişken

def carpma_yap(x, y): #Fonksiyon argümanları local değişkenlerdir.
    return x*y

#Eğer fonksiyon argümanı olarak x ve y değerleri girilmezse global değişkenler kullanılır.
#Eğer fonksiyon argümanı olarak x ve y değerleri girilirse local değişkenler kullanılır.

#Karar kontrol yapıları;

#True-False sorguları;

a = 5000

a == 4000 #'a = 4000 mi?' sorusudur. Tanımlanan a değeri 5000 olduğu için cevap False çıkar.

5==4 #'5 = 4 mü?' sorusudur.

#if

#Örnek: Çeşitli bölgelerde bazı mağazalar mevcuttur. Bu mağazaların belirli bir gelirin altında veya üstünde olmasına
#göre bu mağazalar seçilmek isteniyor.

sinir = 50000
gelir = 40000

if gelir < sinir: #Eğer gelir sınırdan küçükse;
    print('Gelir sınırdan küçüktür.') #'Gelir sınırdan küçüktür.' yaz.
    
#else

sinir = 50000
gelir = 60000

if gelir < sinir:
    print('Gelir sınırdan küçüktür.')
else: #değilse;
    print('Gelir sınırdan büyüktür.') #'Gelir sınırdan büyüktür.' yaz.

#elif

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir:
    print('Gelir sınırdan büyüktür.')
elif gelir1 < sinir:
    print('Gelir sınırdan küçüktür.')
else:
    print('Gelir sınıra eşittir.')
   
if gelir2 > sinir:
    print('Gelir sınırdan büyüktür.')
elif gelir2 < sinir:
    print('Gelir sınırdan küçüktür.')
else:
    print('Gelir sınıra eşittir.')

if gelir3 > sinir:
    print('Gelir sınırdan büyüktür.')
elif gelir3 < sinir:
    print('Gelir sınırdan küçüktür.')
else:
    print('Gelir sınıra eşittir.')

#Örnek uygulama
    
sinir = 50000
magaza_adi = input('Mağaza adı giriniz.')
gelir = int(input('Mağaza gelirini giriniz.')) #Kullanıcıdan girilen bilgiler hep str tipinde olur. Bu nedenle burada
#int tipine dönüştürmemiz gerekmektedir.
if gelir > sinir:
    print('Tebrikler,' + magaza_adi + ' promosyon kazandınız.')
elif gelir < sinir:
    print('Uyarı! Geliriniz sınırdan küçüktür.')
else:
    print('Geliriniz sınıra eşittir.')

#Döngüler
#for

ogrenci = ['ali','berkay','ışık','ela']
for i in ogrenci:
    print(i)

#for - örnek

maaslar = [1000,2000,3000,4000,5000]
for i in maaslar:
    print(i)

#Döngü ve fonksiyonların birlikte kullanımı;

def zam(x):
    print(x+(x*20/100)) #Girilen sayıya, aynı sayının %20'sini ekleyen fonksiyon    
maaslar = [1000,2000,3000,4000,5000]
for i in maaslar:
    zam(i)

#if, for ve fonksiyonların birlikte kullanılması;

maaslar = [1000,2000,3000,4000,5000]
def maas_ust(x):
    print(x*10/100 + x) #Girilen sayıya, aynı sayının %10'unu ekleyen fonksiyon
def maas_alt(x):
    print(x*20/100 + x) #Girilen sayıya, aynı sayının %20'sini ekleyen fonksiyon
for i in maaslar: #maaslar listesinde gez
    if i < 3000: #Eğer değer 3000'den küçükse;
        maas_alt(i) #maas_alt fonksiyonuna değeri yaz.
    else: #Değilse;
        maas_ust(i) #maas_ust fonksiyonuna değeri yaz.

#break

maaslar = [8000,5000,2000,1000,3000,7000,1000]
maaslar.sort()
for i in maaslar:
    if i == 3000:
        print('Kesildi')
        break #İstediğimiz değere gelindiğinde işlemi bitirmek için kullanılır.
    print(i)

#continue

maaslar = [8000,5000,2000,1000,3000,7000,1000]
maaslar.sort()
for i in maaslar:
    if i == 3000:
        continue #İstediğimiz değere gelindiğinde o değeri atlamak için kullanılır.
    print(i)

#while

sayi = 1

while sayi < 10: #sayi 10'dan küçük olduğu sürece;
    sayi += 1 #sayi'ya 1 ekle.
    print(sayi)

#İsimsiz fonksiyonlar

def old_sum(a, b): #Normal fonksiyon
    return a + b

new_sum = lambda a,b: a + b #İsimsiz fonksiyon

sirasiz_liste = [('b',3),('a',8),('d',12),('c',1)]
sorted(sirasiz_liste, key = lambda x: x[1]) #İsimsiz fonksiyon

#-----------------------------------------------------------------------------
#Vektörel operasyonlar

#Eski bilgiler ile a ve b listelerindeki elemanlar tek tek çarpmak için;
a = [1,2,3,4]
b = [5,6,7,8]
ab = []
for i in range(0,len(a)):
    ab.append(a[1]*b[i])
ab

#Fonksiyonel programlama ile;

import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
a*b
#-----------------------------------------------------------------------------

#map

liste = [1,2,3,4,5]
list(map(lambda x: x + 10, liste))

#filter

liste = [1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x: x % 2 == 0, liste))

#reduce

from functools import reduce
liste = [1,2,3,4]
reduce(lambda a,b: a + b, liste)

#Hata ve istisnalar

a = 10
b = 0
try:
    print(a / b)
except ZeroDivisionError:
    print('Paydada sıfır olamaz.')

a = 10
b = '2'
try:
    print(a / b)
except TypeError:
    print('Sayi ve string problemi')
