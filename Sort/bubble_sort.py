# Coding With Kien

def BubbleSort(array, n):
  for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

array = [5.5, 5.8, 4.6, 2.8]
n = len(array)
BubbleSort(array, n)

print("Sorted array is:")
for i in range(n):
    print(array[i], end = "\t")
