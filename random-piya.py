import random
angka = random.randrange(1,100)
tebakan = 0
tebakan_saudara = int(input("tebak angka yang sudah dibangkitkan antara 1 s.d 100: "))
while tebakan_saudara != angka:
    tebakan +=1
    if tebakan_saudara > angka:
        print("tebakan saudara terlalu tinggi.")
    elif tebakan_saudara < angka:
        print("tebakan saudara terlalu rendah.")
    if tebakan > 2:
        print("kamu gagal")
        break
    elif tebakan == angka:
        print("\nBagus! Saudara menebak dalam", tebakan, "tebakan")
        break
    tebakan_saudara = int(input("tebak lagi : "))