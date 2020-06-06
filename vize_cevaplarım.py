#soru 2 cevabım

import random

d = []

e = 0
while e != 6:
    n= random.randint(1, 50)

    if n not in d:
        e += 1
        d.append(n)

    else:
        print("Sayı dizide geçtiği için yeniden sayı seçildi.")

print(d)

#soru 3 cevabım

d= input("En fazla iki basamaklı bir sayı giriniz:\n")

e= " soru3.txt "
n = open(e, 'w+')

def degerlerToplam(z):
    toplam=0
    for i in str(z):
        toplam += int(i)

    if toplam % 2 == 1:
        print("sayı: " + str(z) + "  basamak değeri toplamı:" + str(toplam))
        n.write(str(z) + "\n")

try:
    for i in range(1, int(d)):
        degerlerToplam(i)
except ValueError:
    print("aralıkta olmayan bir değer girdiniz.")

n.close

#soru 4 cevabım

from functools import reduce

soyad=['Aygun','Çiçek','Deniz','Atar','Dener','Yılmaz']
toplam_satis_miktari = [['Ayse', 3,6,7],['Ece', 5,2,4],['Arya', 6,5],['Ali', 3],['Can',5,7,9,11],['Aybar',2,3]]


tsm_sonuc = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a+b, x[1:] )], toplam_satis_miktari))

sonuc = list(map(lambda x , y , z: [ x[0] + " " + y[0:6] ] + [z[1]] , tsm_sonuc , soyad , tsm_sonuc))

print(sonuc)















