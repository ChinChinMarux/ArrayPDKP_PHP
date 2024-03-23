def pangkat(arr):
    if len(arr) < 2:
        return "Array harus memiliki setidaknya dua elemen"

    terkecil = min(arr)
    terbesar = max(arr)

    hasil = terkecil ** terbesar

    return hasil

deret = [2,3,4,5]
hasil = pangkat(deret)
print("Hasil pangkat terendah dengan tertinggi:", hasil)