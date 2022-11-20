#karışık sıra ile verilen bir listeyi bubble sort ile sıralama

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


arr = [64, 34, 25, 12, 90]

bubbleSort(arr)

print("Sıralanmış liste:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")
