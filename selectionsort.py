#karışık sıra ile verilen bir listeyi selection sort ile sıralama

def selectionSort(array, size):
    for i in range(size):
        minimum = i

        for j in range(i + 1, size):
            if array[j] < array[minimum]:
                minimum = j

        (array[i], array[minimum]) = (array[minimum], array[i])


arr = [45, 0, 11, -9, 88, 187]
size = len(arr)
selectionSort(arr, size)
print('Sıralanmış liste:')
print(arr)