daftarMenu = [
    '1. Tampilkan data penjualan',
    '2. Tambah data penjualan',
    '3. Ubah data penjualan',
    '4. Hapus data penjualan',
    '5. Kedatangan produk',
    '6. Penambahan produk baru',
    '7. Cek stok produk',
    '8. Exit'
]

penjualan = [
    {'Invoice' : '001', 'Produk' : 'Beras', 'Qty' : '5', 'UoM' : 'Karung', 'Tipe' : 'Online', 'Harga' : '500000', 'Total' : '2500000'},
    {'Invoice' : '002', 'Produk' : 'Minyak', 'Qty' : '10', 'UoM' : 'Liter', 'Tipe' : 'Offline', 'Harga' : '10000', 'Total' : '100000'},
    {'Invoice' : '003', 'Produk' : 'Gas', 'Qty' : '3', 'UoM' : 'Tabung', 'Tipe' : 'Offline', 'Harga' : '70000', 'Total' : '210000'},
    {'Invoice' : '004', 'Produk' : 'Telur', 'Qty' : '4', 'UoM' : 'Peti', 'Tipe' : 'Offline', 'Harga' : '450000', 'Total' : '1800000'},
    {'Invoice' : '005', 'Produk' : 'Gula', 'Qty' : '1', 'UoM' : 'Karung', 'Tipe' : 'Online', 'Harga' : '800000', 'Total' : '800000'}
]

daftarProduk = [
    {'Produk' : 'Beras', 'Stok' : '50', 'UoM' : 'Karung', 'Harga' : '500000'},
    {'Produk' : 'Minyak', 'Stok' : '45', 'UoM' : 'Liter', 'Harga' : '10000'},
    {'Produk' : 'Gas', 'Stok' : '48', 'UoM' : 'Tabung', 'Harga' : '70000'},
    {'Produk' : 'Telur', 'Stok' : '73', 'UoM' : 'Peti', 'Harga' : '450000'},
    {'Produk' : 'Gula', 'Stok' :  '66', 'UoM' : 'Karung', 'Harga' : '800000'}
]

# Tabel seluruh data
def tabelData():
    print("\n============================== Seluruh Data Penjualan ==============================\n")
    print(f"{('Invoice').ljust(8)}| {('Produk').ljust(12)}| {('Qty').ljust(5)}| {('UoM').ljust(12)}| {('Tipe').ljust(12)}|{('Harga').rjust(12)} | {('Total').rjust(12)}")
    print("-" * 85)
    for values in penjualan:
        print(f'''{values['Invoice'].ljust(8)}| {values['Produk'].ljust(12)}| {values['Qty'].ljust(5)}| {values['UoM'].ljust(12)}| {values['Tipe'].ljust(12)}|{values['Harga'].rjust(12)} | {values['Total'].rjust(12)}''')

# Tabel daftar produk
def tabelProduk():
    print("\n============= Seluruh Data Produk =============\n")
    print(f"{('Produk').ljust(12)}| {('Stok').ljust(5)}| {('UoM').ljust(12)}| {('Harga').rjust(12)}")
    print("-" * 47)
    for values in daftarProduk:
        print(f'''{values['Produk'].ljust(12)}| {values['Stok'].ljust(5)}| {values['UoM'].ljust(12)}| {values['Harga'].rjust(12)}''')

# Validasi nama produk
def prod(namaProduk):
    for produk in daftarProduk:
        if produk['Produk'] == namaProduk:
            return produk
    else:
        return None

# Menu : 1. Tampilkan data penjualan
def dataPenjualan():
    userMenu1 = '1'
    while userMenu1 != '3':
        print("\n=========== Data Penjualan ===========\n")
        print("1. Tampilkan seluruh data penjualan")
        print("2. Tampilkan data berdasarkan invoice")
        print("3. Kembali ke menu utama")
        userMenu1 = input("Ketik Menu Anda (pilih 1-3): ")
        if userMenu1 == '1':
            if len(penjualan) == 0:
                print("\nData kosong")
            else:
                tabelData()
            continue
        elif userMenu1 == '2':
            if len(penjualan) == 0:
                print("\nData kosong")
            else:
                invoiceInput = input("Ketik Nomor Invoice: ")
                for values in penjualan:
                    if values['Invoice'] == invoiceInput:
                        print(f"{('Invoice').ljust(8)}: {values['Invoice']}\n{('Produk').ljust(8)}: {values['Produk']}\n{('Qty').ljust(8)}: {values['Qty']}\n{('UoM').ljust(8)}: {values['UoM']}\n{('Tipe').ljust(8)}: {values['Tipe']}\n{('Harga').ljust(8)}: {values['Harga']}\n{('Total').ljust(8)}: {values['Total']}")
                        break
                else:
                    print(f"\nData tidak ditemukan")
        elif userMenu1 == '3':
            break
        else:
            print("\nMenu yang Anda masukkan salah")
        
# Menu : 2. Tambah data penjualan
def addPenjualan():
    userMenu2 = '1'
    while userMenu2 != '2':
        print("\n======= Tambah Data Penjualan ======\n")
        print("1. Tambah data baru")
        print("2. Kembali ke menu utama")
        userMenu2 = input("Masukkan Menu Anda (pilih 1-2): ")
        if userMenu2 == '1':
            if len(penjualan) == 0:
                print("\nData kosong")
            else:
                addInvoice = input("Masukkan nomor invoice: ")
                if len(addInvoice) != 3:
                    print("\n Nomor invoice harus terdiri dari 3 digit angka")
                    continue            
                elif any(values['Invoice'] == addInvoice for values in penjualan):
                    print("\nData sudah ada")
                    continue
                else:
                    addProduk = input("Ketik nama produk: ")
                    produkData = prod(addProduk)
                    if not produkData:
                        print(f"\nNama produk tidak ada dalam data")
                        print(f"\nMasukkan nama produk yang tersedia:")
                        for produk in daftarProduk:
                            print(f"{produk['Produk']}, stok: {produk['Stok']}")
                        continue
                    
                    addQty = input("Masukkan jumlah produk: ")
                    stokNow = int(produkData['Stok'])
                    if int(addQty) > stokNow:
                        print(f"\nStok tidak cukup, tersedia: {stokNow}")
                        continue

                    addTipe = input("Masukkan tipe penjualan (Online / Offline): ")
                    addUoM = produkData['UoM']
                    addHarga = produkData['Harga']
                    addTotal = int(addQty) * int(addHarga)
                    dataBaru = {'Invoice' : addInvoice,  'Produk' : addProduk, 'Qty' : addQty, 'UoM' : addUoM, 'Tipe' : addTipe, 'Harga' : str(addHarga), 'Total' : str(addTotal)}
                    simpanInput = input("Apakah anda ingin menyimpan data? (y/n): ")
                    if simpanInput == 'y':
                        penjualan.append(dataBaru)
                        produkData['Stok'] = str(stokNow - int(addQty))
                        tabelData()
                        print(f"\nData berhasil disimpan")
                        continue
                    else:
                        print(f"\nPenembahan data dibatalkan")
                        continue
        elif userMenu2 == '2':
            break
        else:
            print("\nMenu yang Anda masukkan salah")

# Menu : 3. Ubah data penjualan
def updatePenjualan():
    userMenu3 = '1'
    while userMenu3 != '2':
        print("\n======= Ubah Data Penjualan ======\n")
        print("1. Ubah data")
        print("2. Kembali ke menu utama")
        userMenu3 = input("Ketik Menu Anda (pilih 1-2): ")
        if userMenu3 == '1':
            if len(penjualan) == 0:
                print("\nData kosong")
                continue
            updateInvoice = input("Ketik nomor invoice: ")
            if len(updateInvoice) != 3:
                print("\nNomor invoice harus terdiri dari 3 digit angka")
                continue
            found = False
            for item in penjualan:
                if item['Invoice'] == updateInvoice:
                    found = True
                    print(f"\nData yang ditemukan:")
                    for key, value in item.items():
                        print(f"{key}: {value}")

                    print("\nPilih data yang akan diubah:")
                    print("1. Produk")
                    print("2. Qty")
                    print("3. UoM")
                    print("4. Tipe")
                    print("5. Harga")
                    dataUbah = input("Masukkan pilihan (1-5): ")

                    if dataUbah == '1':
                        item['Produk'] = input("Masukkan nama produk baru: ")
                    elif dataUbah == '2':
                        newQty = input("Masukkan jumlah baru: ")
                        if newQty.isdigit():
                            item['Qty'] = newQty
                            item['Total'] = str(int(item['Harga']) * int(newQty))
                            for produk in daftarProduk:
                                if produk['Produk'] == item['Produk']:
                                    produk['Stok'] = str(int(produk['Stok']) - int(newQty))
                                    break
                        else:
                            print("Qty harus berupa angka")
                            continue
                    elif dataUbah == '3':
                        item['UoM'] = input("Masukkan satuan baru: ")
                    elif dataUbah == '4':
                        item['Tipe'] = input("Masukkan tipe penjualan baru: ")
                    elif dataUbah == '5':
                        newHarga = input("Masukkan harga baru: ")
                        if newHarga.isdigit():
                            item['Harga'] = newHarga
                            item['Total'] = str(int(newHarga) * int(item['Qty']))
                            break
                        else:
                            print("Harga harus berupa angka")
                            continue
                    else:
                        print("\nPilihan yang Anda masukkan salah")
                        continue
                    simpanUbah = input("Apakah anda ingin menyimpan data? (y/n): ")
                    if simpanUbah == 'y':
                        tabelData()
                        print(f"\nData berhasil disimpan")
                        continue
                    else:
                        print(f"\nPerubahan data dibatalkan")
                        continue
            if not found:
                print("\nData tidak ditemukan")
        elif userMenu3 == '2':
            break
        else:
            print("\nMenu yang Anda masukkan salah")                      

# Menu : 4. Hapus data penjualan
def deletePenjualan():
    userMenu4 = '1'
    while userMenu4 != '3':
        print("\n======= Hapus Data Penjualan ======\n")
        print("1. Hapus data berdasarkan nomor invoice")
        print("2. Kembali ke menu utama")
        userMenu4 = input("Ketik Menu Anda (pilih 1-2): ")
        if userMenu4 == '1':
            if len(penjualan) == 0:
                print("\nData kosong")
            else:
                delInvoice = input("Ketik Nomor Invoice: ")
                for i, item in enumerate(penjualan):
                    if item['Invoice'] == delInvoice:
                        print("\nData ditemukan")
                        for key, value in item.items():
                            print(f"{key}: {value}")
                            continue
                        konfirmasi = input("Yakin hapus data ini? (y/n): ")
                        if konfirmasi == 'y':
                            penjualan.pop(i)
                            for produk in daftarProduk:
                                if produk['Produk'] == item['Produk']:
                                    produk['Stok'] = str(int(produk['Stok']) + int(item['Qty']))
                                    break
                            tabelData()
                            print(f"\nData berhasil dihapus")
                            continue
                        else:
                            print(f"\nPenghapusan data dibatalkan")
                            continue  
                    else:
                        print(f"\nData tidak ditemukan")
                        continue
        else:
            break

# Menu : 5. Kedatangan produk
def datangProduk():
    userMenu5 = '1'
    while userMenu5 != '2':
        print("\n======= Kedatangan Produk ======\n")
        print("1. Tambah stok produk kedatangan baru")
        print("2. Kembali ke menu utama")
        userMenu5 = input("Ketik Menu Anda (pilih 1-2): ")
        if userMenu5 == '1':
            if len(daftarProduk) == 0:
                print("\nData kosong")
            else:
                tabelProduk()
                produkDatang = input("\nMasukkan nama produk: ")
                incoming = prod(produkDatang)
                if not incoming:
                    print(f"\n Nama produk salah")
                    continue

                stokDatang = int(input("Masukkan jumlah produk: "))
                if stokDatang <= 0:
                    print(f"\nJumlah kedatangan tidak boleh nol")
                    continue

                simpanDatang = input(f"\nSimpan data kedatangan? (y/n): ")
                if simpanDatang == 'y':
                    incoming['Stok'] = str(int(incoming['Stok']) + stokDatang)
                    tabelProduk()
                    print(f"\nData berhasil ditambahkan")
                else:
                    print(f"\nPenambahan data kedatangan dibatalkan")
                    continue
        elif userMenu5 == '2':
            break
        else:
            print("\nMenu yang Anda masukkan salah")

# Menu : 6. Penambahan produk baru
def baru():
    userMenu6 = '1'
    while userMenu6 != '2':
        print("\n======= Penambahan Produk Baru ======\n")
        print("1. Tambah produk baru")
        print("2. Kembali ke menu utama")
        userMenu6 = input("Masukkan Menu Anda (pilih 1-2): ")
        if userMenu6 == '1':
            if len(daftarProduk) == 0:
                print("\nData kosong")
            else:
                produkBaru = input(f"\nMasukkan nama produk baru: ")
                if any(values['Produk'] == produkBaru for values in daftarProduk):
                    tabelProduk()
                    print(f"\nData sudah ada\nMasukkan Produk selain yang terdapat pada tabel")
                    continue
                stokBaru = input(f"Masukkan jumlah produk baru: ")
                uomBaru = input(f"Masukkan UoM produk baru: ")
                hargaBaru = input(f"Masukkan harga produk baru: ")
                new_produk = {'Produk' : produkBaru, 'Stok' : stokBaru, 'UoM' : uomBaru, 'Harga' : hargaBaru}
                simpanProdukBaru = input("Apakah anda ingin menyimpan data? (y/n): ")
                if simpanProdukBaru == 'y':
                    daftarProduk.append(new_produk)
                    tabelProduk()
                    print(f"\nData berhasil disimpan")
                    continue
                else:
                    print(f"\nPenambahan produk dibatalkan")
                    continue
        elif userMenu6 == '2':
            break
        else:
            print("\nMenu yang Anda masukkan salah")

# Menu : 7. Cek stok produk
def cek():
    tabelProduk()
    userMenu7 = input("\nKembali ke menu utama (y): ")
    if userMenu7 != 'y':
        quit
    else:
        quit

# Menu : 8. Exit
def exitPenjualan():
    print("\n========== Anda telah keluar dari sistem ==========\n")

# Main Menu
def mainMenu():
    userInput = 8
    while userInput != '8':
        print("\n==== Sistem Data Penjualan ====\n")
        
        for menu in daftarMenu:
            print(menu)
        
        userInput = input("Ketik Menu Anda (pilih 1-8): ")
        if userInput == '1':
            dataPenjualan()
        elif userInput == '2':
            addPenjualan()
        elif userInput == '3':
            updatePenjualan()
        elif userInput == '4':
            deletePenjualan() 
        elif userInput == '5':
            datangProduk()
        elif userInput == '6':
            baru()
        elif userInput == '7':
            cek()
        elif userInput == '8':
            exitPenjualan()
        else:
            print("Menu tidak sesuai")

mainMenu()