# MERGE_SORT(arr)
# 1. Jika ukuran arr <= 1, return arr.
# 2. Bagi arr menjadi dua bagian: left_half dan right_half.
# 3. Panggil MERGE_SORT(left_half).
# 4. Panggil MERGE_SORT(right_half).
# 5. Merge left_half dan right_half menjadi array yang terurut menggunakan fungsi MERGE.
# 6. Return arr.

# MERGE(left, right)
# 1. Buat array kosong result.
# 2. While left dan right tidak kosong:
#    a. Jika elemen pertama left <= elemen pertama right, tambahkan elemen pertama left ke result.
#    b. Jika tidak, tambahkan elemen pertama right ke result.
# 3. Tambahkan elemen yang tersisa dari left atau right (jika ada) ke result.
# 4. Return result.

# Analisis Kompleksitas Merge Sort
# Big O (Kasus Terburuk): Array dibagi menjadi dua hingga ukuran terkecil (log n) dan setiap pembagian memerlukan penggabungan semua elemen (n). Kompleksitas total adalah 𝑂(𝑛 log n).
# Big Theta (Kasus Rata-rata): Struktur pembagian dan penggabungan tetap sama untuk kasus rata-rata. Kompleksitas tetap  Θ(𝑛 log n).


# BUBBLE_SORT(arr):
# 1. Untuk i dari 0 hingga n-1:
#    a. Untuk j dari 0 hingga n-i-2:
#       i. Jika arr[j] > arr[j+1], maka tukar arr[j] dengan arr[j+1].
# 2. Return arr.

# Analisis Kompleksitas Bubble Sort
# Big O (Kasus Terburuk): Pada kasus terburuk, setiap elemen dibandingkan dengan semua elemen lainnya, membutuhkan n−1 iterasi luar dan (n−i−2) iterasi dalam.
# Total perbandingan adalah n(n−1)/2, sehingga kompleksitas adalah O(n^2)
# Big Theta (Kasus Rata-rata): Bahkan pada kasus rata-rata, setiap elemen dibandingkan dengan elemen lainnya seperti pada kasus terburuk. Kompleksitas tetap Θ(𝑛^2).


import random
import time


# Implementasi Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Implementasi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Membuat data acak
X = [random.randint(1, 1000) for _ in range(100)]

# Merge Sort dengan pengukuran waktu
arr_merge = X[:]
start_time_merge_sort = time.perf_counter()
arr_merge = merge_sort(arr_merge)
end_time_merge_sort = time.perf_counter()
time_complexity_merge = end_time_merge_sort - start_time_merge_sort

# Bubble Sort dengan pengukuran waktu
arr_bubble = X[:]
start_time_bubble_sort = time.perf_counter()
bubble_sort(arr_bubble)
end_time_bubble_sort = time.perf_counter()
time_complexity_bubble = end_time_bubble_sort - start_time_bubble_sort

# Hasil
print(f"Data awal: {X}\n")
print(f"Hasil Merge Sort: {arr_merge}\n")
print(f"Hasil Bubble Sort: {arr_bubble}\n")

print(f"Time Complexity untuk Merge Sort: {time_complexity_merge:.10f} detik \n")
print(f"Time Complexity untuk Bubble Sort: {time_complexity_bubble:.10f} detik \n")
