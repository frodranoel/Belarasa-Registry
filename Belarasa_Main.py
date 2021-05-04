from Class_umat import Umat
import datetime

def waktu():
    x = datetime.datetime.now()
    print(x.strftime('%A') +',', x.strftime('%B'), x.strftime('%d'), x.year)

def tex():
    count_umat[0] += 1
    kuota[0] -= 1

def umat(): #tampilan umat
    if kuota[0] > 0:
        x = datetime.datetime.now()
        print('--------------------------------')
        print('Silahkan mengisi data diri anda:')
        nama = input('Nama: ')
        tgl, bln, thn = map(int, input('Tanggal lahir: ').split())
        ling = input('Lingkungan: St. ')
        wil = input('Wilayah: ')
        alm = input('Alamat: ')
        y = datetime.datetime(thn, bln, tgl)
        delta = x - y
        if thn%4 == 0 or thn%4 ==3: #pendaftar harus berumur minimal 18 tahun
            if delta.days < 6575: 
                print('Maaf, umur belum mencukupi \n')
            else:
                tex()
                daftar_umat[count_umat[0]] = Umat(nama = nama, tanggal = tgl, bulan = bln, tahun = thn, lingkungan = ling, wilayah = wil, alamat = alm)
                print()
                print('Selamat {}, data anda telah diinput! Nomor urut anda adalah {}'.format(nama, count_umat[0]))
                print('--------------------------------------------------------------')       
        else:
            if delta.days < 6574:
                print('Maaf, umur belum mencukupi \n')
            else:
                tex()
                daftar_umat[count_umat[0]] = Umat(nama = nama, tanggal = tgl, bulan = bln, tahun = thn, lingkungan = ling, wilayah = wil, alamat = alm)
                print()
                print('Selamat {}, data anda telah diinput! Nomor urut anda adalah {}'.format(nama, count_umat[0]))
                print('--------------------------------------------------------------')  
    else:
        print('Maaf kuota habis')
        print()

def admin(): #tampilan untuk admin ketika sudah masukkan password dan benar
    print('-------------------')
    print('Silahkan pilih opsi')
    print('1. Ubah Kuota')
    print('2. Lihat Nama Umat')
    print('3. Ubah Password')
    print('4. Kembali')
    
    n = int(input('>> '))
    if n == 1:
        admin_ubah_kuota()
    elif n == 2:
        admin_lihat_nama()
    elif n == 3:
        ubah_password()

def admin_lihat_nama(): #untuk admin melihat nama-nama umat
    for i in daftar_umat.keys():
        print('Nomor', i, daftar_umat[i])
    print('Jumlah umat yang terdaftar', len(daftar_umat), 'orang')
    print('-----------------------------------------------')

def admin_ubah_kuota(): #untuk admin ubah kuota
    print('Silahkan masukkan kuota')
    u = int(input('>> '))
    kuota[0] = u   
    print()
    return kuota

def password(): #untuk input password
    print('Silahkan masukkan password')
    n = str(input('>> '))
    if n == ''.join(password_list):
        admin()
    else:
        print('Maaf password salah')
        print() 

def ubah_password(): #untuk admin ubah password
    print('Silahkan masukkan password baru!')
    n = str(input('>> '))
    password_list.clear()
    for i in n:
        password_list.append(i)
    print('Password telah diubah :)')
    print()
    return password_list

password_list = ['0', '0', '0']     #password default
kuota = [0]                         #kuota default
daftar_umat = {}                    #dictionary untuk nama-nama umat
count_umat = [0]                    #jumlah umat
while True:
    waktu()
    print('Kuota Hari ini: ')
    print(kuota[0])
    print('-------------------------------')
    print('Halo selamat datang di Belarasa')
    print('Silahkan login sebagai')
    print('1. Admin')
    print('2. Umat')
    print('3. Keluar')
    n = int(input('>> '))
    if n == 1:
        password()
    elif n == 2:
        umat()
    else:
        print('Terima kasih!')
        break    

