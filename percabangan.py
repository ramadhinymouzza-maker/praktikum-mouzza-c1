# variabel dan tipe data
nama_mhs = input("Masukkan Nama :")
nilai_algoritma = int(input("Masukkan Nilai Algoritma :"))
nilai_basisdata = int(input("Masukkan Nilai Basis Data :"))
nilai_logika_informatika = int(input("Masukkan Nilai Logika Informatika :"))
nilai_agama = int(input("Masukkan Nilai Agama :"))
nilai_bahasa_indonesia = int(input("Masukkan Nilai B.Indonesia :"))
nilai_bahasa_inggris = int(input("Masukkan Nilai B.Inggris :"))
nilai_pancasila = int(input("Masukkan Nilai Pancasila :"))

# hitung rata-rata - minimal 7
rata_rata = (nilai_algoritma + nilai_basisdata + nilai_logika_informatika + nilai_agama + nilai_bahasa_indonesia + nilai_bahasa_inggris + nilai_pancasila) / 7

# penentuan lulus atau tidak - tidak boleh lebih dari 100
print(f"\nNama: {nama_mhs}")
print(f"Rata-rata: {rata_rata}")

if rata_rata >=80 and rata_rata <=100:
    # kondisi jika terpenuhi
    # maka
    print("Nilai : A")
elif rata_rata >=70 and rata_rata <80:
    print("Nilai : B")
elif rata_rata >=50 and rata_rata <70:
    print("Nilai : C")
else:
    # cukup menampilkan hasil
    # maka
    print("Nilai Lebih dari 100 atau dibawah 50")