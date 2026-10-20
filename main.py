tugas = float(input("Nilai tugas : "))
uts = float(input("Nilai UTS   : "))
uas = float(input("Nilai UAS   : "))
kehadiran = float(input("Kehadiran : "))

nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)
print(f"\nNilai Akhir : {nilai_akhir}")

if nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    print("Status      : LULUS DENGAN PREDIKAT")
elif nilai_akhir >= 75 and kehadiran >= 80:
    print("Status      : LULUS")
else:
    print("Status      : BELUM LULUS")
