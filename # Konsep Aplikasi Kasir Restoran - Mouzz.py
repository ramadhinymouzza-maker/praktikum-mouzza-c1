# Konsep Aplikasi Kasir Restoran - Mouzza Shamadhiny 2609010112

print("="*40)
print("   APLIKASI KASIR RESTORAN")
print("="*40)

# 1. Mulai Program - Inisialisasi total
total = 0

# Daftar harga
menu = {
    1: ("Nasi Goreng", 25000),
    2: ("Mie Ayam", 15000),
    3: ("Ayam Geprek", 20000),
    4: ("Sate Ayam", 30000),
    5: ("Bakso", 18000)
}

# 2, 3, 4. Perulangan untuk tampilkan menu & proses pemesanan
while True:
    # 2. Tampilkan Menu
    print("\n--- Daftar Menu Makanan ---")
    print("1. Nasi Goreng  - Rp25.000")
    print("2. Mie Ayam     - Rp15.000")
    print("3. Ayam Geprek  - Rp20.000")
    print("4. Sate Ayam    - Rp30.000")
    print("5. Bakso        - Rp18.000")
    print("0. Selesai Memilih")
    print("---------------------------")
    print(f"Total sementara: Rp{total}")

    try:
        pilihan = int(input("Pilih menu (0-5): "))
    except:
        print("Input harus angka!")
        continue

    # 4. Apakah Pilihan 0 ?
    if pilihan == 0:
        break  # Ya -> keluar loop, lanjut hitung diskon
    
    # 3. Proses Pemesanan
    if pilihan in menu:
        nama, harga = menu[pilihan]
        try:
            jumlah = int(input(f"Jumlah {nama} : "))
            if jumlah <= 0:
                print("Jumlah harus > 0")
                continue
        except:
            print("Jumlah harus angka!")
            continue
        
        subtotal = harga * jumlah
        total += subtotal
        print(f"-> {jumlah}x {nama} = Rp{subtotal} | Ditambahkan ke total")
    else:
        print("Pilihan tidak valid! Pilih 0-5")
        continue

# 5. Hitung Diskon
if total > 200000:
    diskon_persen = 20
else:
    diskon_persen = 0

potongan = total * diskon_persen // 100
total_bayar = total - potongan

# 6. Tampilkan Struk Pembayaran
print("\n" + "="*40)
print("      STRUK PEMBAYARAN")
print("="*40)
print(f"Total Belanja  : Rp{total}")
print(f"Diskon         : {diskon_persen}%")
print(f"Potongan       : Rp{potongan}")
print("-"*40)
print(f"Total Bayar    : Rp{total_bayar}")
print("="*40)
print("        Terima Kasih!")
print("="*40)