nama = input("masukan nama:")
nilai_algoritma = int(input("masukan nilai algoritma:"))
nilai_agama = int(input("masukan nilai agama:"))
nilai_basisdata = int(input("masukan nilai basisdata:"))
nilai_pancasila = int(input("masukan nilai pancasila:"))
nilai_bahasa_indonesia = int(input("masukan nilai b.indo:"))
nilai_bahasa_ingris = int(input("masukan nilai b.inggris:"))
nilai_logika_informatika = int(input("masukan nilai logika informatika:"))

# menghitung rata_rata

rata_rata = (nilai_algoritma + nilai_agama + nilai_basisdata + nilai_pancasila + nilai_bahasa_indonesia + nilai_bahasa_ingris + nilai_logika_informatika)



# penentuan lulus atau tidak>=80 and nilai<=100:
if rata_rata >= 90 and rata_rata <=100 :
    # kondisi jika terpenuhi
    # maka
    print("Nilai : A")
elif rata_rata >=80 and rata_rata <=90:
    print("Nilai: 8")
elif rata_rata  >50 and rata_rata <=70:
    print("Nilai: C")
elif rata_rata >=50 and rata_rata <=60 : 
    print("Nilai : D:)")
else: 
    print("nilai : E")