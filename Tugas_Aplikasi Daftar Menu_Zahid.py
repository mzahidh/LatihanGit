#Variabel Global untuk menyimpan list produk
produk = {'Jeruk' : '1000', 'Apel' : '3000', 'Semangka' : '3000'}

def barang():
    for x,y in produk.items():
        print (x +' Rp'+ y)
        
#Fungi memperlihatkan produk
def show_produk(): 
    barang()
    while True:
        try:
            back = input('Balik ke menu awal? (y/n)')
            if back == 'y':
                menu()
            elif back != 'y' and back != 'n':
                print ('Mohon masukkan huruf y / n')
                while True:
                    break
            elif back == 'n':
                exit()
        except ValueError:
            print ('Mohon masukkan huruf bukan angka')

#Fungsi tambahkan produk
def tambah_produk():
    barang()
    try:
        produk_baru = input('Nama produk yang akan ditambahkan:  ')
        harga_produk_baru = int(input('Harganya: '))
    except UnboundLocalError:
        print ('Mohon masukkan huruf bukan angka')

    produk_baru = produk_baru.capitalize()
    produk[str(produk_baru)] = str(harga_produk_baru)

    for x,y in produk.items():
        print (x +' Rp'+ y)

    while True:
        try:
            back = input('Balik ke menu awal? (y/n)')
            if back == 'y':
                menu()
            elif back != 'y' and back != 'n':
                print ('Mohon masukkan huruf y / n')
                while True:
                    break
            elif back == 'n':
                exit()
        except ValueError:
            print ('Mohon masukkan huruf bukan angka')

#Fungsi Update Harga
def update_harga():
    barang()
    while True:
        try:
            indeks = (input('tuliskan buah yg ingin diupdate harganya: '))
            harga_baru = (input('masukkan harga baru: '))
        except ValueError:
            print ('Mohon masukkan huruf bukan angka')
        indeks = indeks.capitalize()

        if indeks in produk:
            produk[str(indeks)] = str(harga_baru)
            print (indeks +' Rp'+ harga_baru)
            menu()
        else:
            print('Masukkan buah yang benar')

    while True:
        try:
            back = input('Balik ke menu awal? (y/n)')
            if back == 'y':
                menu()
            elif back != 'y' and back != 'n':
                print ('Mohon masukkan huruf y / n')
                while True:
                    break
            elif back == 'n':
                exit()
        except ValueError:
            print ('Mohon masukkan huruf bukan angka')

#Fungsi mengurangi produk
def kurangi_produk():
    barang()
    # print (show_produk())
    indeks = (input("Tulis buah yg ingin dihapus: "))
    indeks = indeks.capitalize()

    for x,y in list(produk.items()):
        if (indeks == x):
            del produk[x]

    for x,y in produk.items():
        # del produk[str(indeks)]
        print (x +' Rp'+ y)

    while True:
        try:
            back = input('Balik ke menu awal? (y/n)')
            if back == 'y':
                menu()
            elif back != 'y' and back != 'n':
                print ('Mohon masukkan huruf y / n')
                while True:
                    break
            elif back == 'n':
                exit()
        except ValueError:
            print ('Mohon masukkan huruf bukan angka')

#Fungsi menu

def menu():
    x = 'MENU'
    print(x.center(20,'.'))
    try:
        menu = (int(input(' 1) Show Produk \n 2) Tambahkan Produk \n 3) Update Harga \n 4) Hapus Produk \n 5) Exit \n Masukkan pilihan menu anda: ')))
        if menu == 1:
            show_produk()
        elif menu ==2:
            tambah_produk()
        elif menu ==3:
            update_harga()
        elif menu ==4:
            kurangi_produk()
        elif menu ==5:
            exit()
        else:
            print('Invalid Input')
        
    except ValueError:
        print('Mohon Masukan Nilai yang Tepat')

while True:
    menu()