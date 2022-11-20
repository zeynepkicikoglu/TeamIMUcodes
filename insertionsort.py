#karışık sıra ile verilen bir listeyi insertion sort ile sıralama

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [1, 31, 13, 5, 6]
insertionSort(arr)
lst = []
print("Sıralanmış liste : ")
for i in range(len(arr)):
    lst.append(arr[i])
print(lst)