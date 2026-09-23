angka1=int(input("Masukkan angka ke-1: "))
angka2=int(input("Masukkan angka ke-2: ")) 
angka3=int(input("Masukkan angka ke-3: "))

if angka1>angka2 and angka1>angka3:
    print("Angka pertama adalah yang terbesar")
elif angka2>angka1 and angka2>angka3:
    print("Angka kedua adalah yang terbesar")
elif angka3>angka1 and angka3>angka2:
    print("angka ketiga adalah yang terbesar")
else:
    print("tidak ada angka yang terbesar")