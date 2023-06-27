def main():
    print("==========Boutique===========")
    nama=input("Nama Pembeli     :")
    telp=input("No.Telpon        :")
    alamat=input("Alamat Pembeli   :")

    print("\n-----List Produk-----")
    print("1. Gamis Rempel Peach")
    print("2. Dress Overall")
    print("3. Jumpsuit Denim")
    print("4. One Set Rayon Motif Polka")
    print("5. Blouse Dusty")

    pilihan=int(input("Masukkan Pilihan          :"))
    jml_produk=int(input("Masukkan Jumlah Pembelian :"))

    if pilihan==1:
        harga=599000
        nama_produk="Gamis Rempel Peach"
    elif pilihan==2:
        harga=350000
        nama_produk="Dress Overall"
    elif pilihan==3:   
        harga=225000
        nama_produk="Jumpsuit Denim"
    elif pilihan==4:    
        harga=145000
        nama_produk="One Set Rayon Motif Polka"
    elif pilihan==5:    
        harga=190000
        nama_produk="Blouse Dusty"
    else:
        print("Barang tidak ditemukan..!")
        
    jml_harga=jml_produk*harga
    print("Total yang harus anda bayar=Rp. ",jml_harga)
    bayar=int(input("Uang anda= Rp. "))

    if jml_harga>=800000:
        diskon=int(0.1*jml_harga)
    elif jml_harga>=500000:
        diskon=int(0.07*jml_harga)
    elif jml_harga>=200000:
        diskon=int(0.05*jml_harga)
    else:
        diskon=0

    total=jml_harga-diskon
    kembalian=bayar-total

    print("total:",total)
    print("kembalian:",kembalian)

    print("================================================")
    print("====================Boutique====================")
    print("================================================")
    print("Nama Pembeli      :",nama)
    print("No. Telepon       :",telp)
    print("Alamat            :",alamat)
    print("Produk            :",nama_produk)
    print("Jumlah Produk     :",jml_produk)
    print("Jumlah harga      :",jml_harga)
    print("------------------------------------------------")
    print("Diskon            :",diskon)
    print("Total             :",total)
    print("Uang              :",bayar)
    print("Kembalian         :",kembalian)
    print("================================================")
    print("==========terima kasih telah berbelanja=========")
    print("================================================")

    repeat=input("Apakah ingin meng-input lagi...?(y/t").lower()
    if repeat=="y":
        main()
    else:
        exit()
    
    
main()


