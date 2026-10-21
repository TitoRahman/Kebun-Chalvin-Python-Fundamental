n = int(input("Banyak test case: "))

for i in range(n):
    jumlah_deretan = int(input("Enter a deretan: "))
    deretan = ""
    jumlah_angka = [0]*10
    for j in range(jumlah_deretan):
        deretan = deretan + str(j+1)

    for angka in deretan:
        jumlah_angka[int(angka)] += 1
    print(*jumlah_angka)
