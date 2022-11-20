#Girilen sayının bütün tam bölenlerini bulan kod

sayı=int(input("Bir sayı giriniz:"))
bölenleri=[]

for i in range(1,sayı):
    if sayı % i == 0:
        bölenleri.append(i)
    else:
        continue

print("Tam bölenleri:",bölenleri)