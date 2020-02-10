d={}

def Tanya():
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
                print('Terima kasih telah menggunakan aplikasi sederhana ini')
                exit()
        except ValueError:
            print ('Mohon masukkan huruf bukan angka')

def isi():
    a = 'key'
    key = (a.center(20,' '))
    b = 'value'
    value = (b.center(20,' '))
    for x,y in d.items():
        print ('|',key,'|',value,'|')
        print ('|',(x.center(20,' ')),'|',(str(y).center(20,' ')),'|' )

def MenuDict():
    a = 'key'
    key = (a.center(20,' '))
    b = 'value'
    value = (b.center(20,' '))
    print ('|',key,'|',value,'|')
    for x,y in d.items():
        print ('|',(x.center(20,' ')),'|',(str(y).center(20,' ')),'|' )
    Tanya()

def TambahDict():
    isi()
    try:
        dataInput = int(input('Berapa kali masukan dictionary: '))
    except UnboundLocalError:
        print('Masukan angka!')
        
    for i in range(0,dataInput):
        i= dataInput-1
        Tipe = int(input('Pilih tipe Dictionary: \n 1) String \n 2) Number \n Pilih: '))
        try:
            if Tipe == 1:
                            
                key_baru = input('Key:  ')
                value_baru_str = str(input('Value: '))
                key_baru = key_baru.capitalize()
                d[str(key_baru)] = str(value_baru_str)
            elif Tipe == 2:
                
                key_baru = input('Key:  ')
                value_baru = int(input('Value: '))
                key_baru = key_baru.capitalize()
                d[str(key_baru)] = int(value_baru)        
            else:
                print ('Input Salah! ')
        except ValueError:
            print('Masukkan angka!')

    MenuDict()

def CariDict():
    cariKata= input('Cari kata berdasarkan Key: ')
    cariKata= cariKata.capitalize()
    a = 'key'
    key = (a.center(20,' '))
    b = 'value'
    value = (b.center(20,' '))
    print ('|',key,'|',value,'|')
    for x,y in d.items():
        if cariKata == x or cariKata == y:
            print ('|',(cariKata.center(20,' ')),'|',(str(y).center(20,' ')),'|' )
        else:
            print (' ')
    Tanya()

def menu():
    x = 'PILIH MENU'
    print(x.center(20,'.'))
    try:
        menu = (int(input(' 1) Show Dictionary \n 2) Add Dictionary \n 3) Search Dictionary \n 4) Exit \n Masukkan pilihan menu anda: ')))
        if menu == 1:
            MenuDict()
        elif menu ==2:
            TambahDict()
        elif menu ==3:
            CariDict()
        elif menu ==4:
            print('Terima kasih telah menggunakan aplikasi sederhana ini')
            exit()
        else:
            print('Invalid Input')
        
    except ValueError:
        print('Mohon Masukan Nilai yang Tepat')

while True:
    menu()