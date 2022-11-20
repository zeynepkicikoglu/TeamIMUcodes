#10 adet öğrenciye ait verileri(boy,kilo) alın ve bu verileri grafik olarak çizdirin

import matplotlib.pyplot as plt

ogr1boy = int(input("1. öğrencinin boyunu girin:"))
ogr1kilo = int(input("1. öğrencinin kilosunu girin:"))
ogr2boy = int(input("2. öğrencinin boyunu girin:"))
ogr2kilo = int(input("2. öğrencinin kilosunu girin:"))
ogr3boy = int(input("3. öğrencinin boyunu girin:"))
ogr3kilo = int(input("3. öğrencinin kilosunu girin:"))
ogr4boy = int(input("4. öğrencinin boyunu girin:"))
ogr4kilo = int(input("4. öğrencinin kilosunu girin:"))
ogr5boy = int(input("5. öğrencinin boyunu girin:"))
ogr5kilo = int(input("5. öğrencinin kilosunu girin:"))
ogr6boy = int(input("6. öğrencinin boyunu girin:"))
ogr6kilo = int(input("6. öğrencinin kilosunu girin:"))
ogr7boy = int(input("7. öğrencinin boyunu girin:"))
ogr7kilo = int(input("7. öğrencinin kilosunu girin:"))
ogr8boy = int(input("8. öğrencinin boyunu girin:"))
ogr8kilo = int(input("8. öğrencinin kilosunu girin:"))
ogr9boy = int(input("9. öğrencinin boyunu girin:"))
ogr9kilo = int(input("9. öğrencinin kilosunu girin:"))
ogr10boy = int(input("10. öğrencinin boyunu girin:"))
ogr10kilo = int(input("10. öğrencinin kilosunu girin:"))


kilo = [ogr1kilo, ogr2kilo, ogr3kilo, ogr4kilo, ogr5kilo, ogr6kilo, ogr7kilo, ogr8kilo, ogr9kilo, ogr10kilo]
boy = [ogr1boy, ogr2boy, ogr3boy, ogr4boy, ogr5boy, ogr6boy, ogr7boy, ogr8boy, ogr9boy, ogr10boy]

def bubbleSort(arr):
    n = len(arr)
    temp = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                temp = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not temp:
            return

bubbleSort(kilo)

print("Sıralanmış liste:")
for i in range(len(kilo)):
    print("% d" % kilo[i], end=" ")

bubbleSort(boy)

print("\nSıralanmış liste:")
for i in range(len(boy)):
    print("% d" % boy[i], end=" ")



plt.plot(kilo, boy)
plt.show()

