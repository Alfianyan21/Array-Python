import numpy as np

#array 1
arr1 = np.array([
    [11, 12, 13],
    [14, 15, 16]
    ])
print("Matriks A 2x3")
print(arr1)

#array2
arr2 = np.array([
    [6, 35, 12],
    [27, 17, 9]
])
print("Matriks B 2x3")
print(arr2)

#array 3
arr3 = np.array ([
    [1, 2],
    [3, 4],
    [5, 6]
])
print("Matriks C 2x2")
print(arr3)

#Penjumahan 
penjumlahan = arr1 + arr2
print("Hasil Penjumlahan : ")
print(penjumlahan)

#Pengurangan 
pengurangan = arr1 - arr2
print("HAsil Pengurangan : ")
print(pengurangan)

#Perkalian
perkalian = arr1 * arr2
print("Hasil Perkalian : ")
print(perkalian)

#Pangkat
pangkat = arr3 ** 2
print("Hasil Pangkat : ")
print(pangkat)