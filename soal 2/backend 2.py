# Buatlah sebuah program yang meminta pengguna untuk memasukan jumlah jam
# kerja dan tarif per jam, lalu menghitung dan menampilkan gaji karyawan. Jika
# karyawan yang bekerja lebih dari 40 jam dalam seminggu, maka hitunglah gaji
# lembur dengan tarif 1.5 kali lipat.

jam_kerja = int(input("Masukkan Jumlah Jam Keja = "))
upah_per_jam = int(input("Masukkan Jumlah Upah Per-jam = "))

gaji = 0
# asumsikan bekerja dalam 5 hari saja
if jam_kerja * 5 > 40 :
    print("jam kerja lebih dari 40 jam perminggu (5 hari kerja)")
    gaji = upah_per_jam * jam_kerja
    # ditambah gaji lembur yang merupakan selisih jam_kerja total dengan jam_kerja minimal dikalikan dengan gaji lembur
    gaji += (jam_kerja * 5 - 40) * upah_per_jam * 1.5
else :
    print("jam kerja kurang atau sama dengan 40 jam perminggu (5 hari kerja)")
    gaji = upah_per_jam * jam_kerja * 5

print("Gaji Per-minggu (bekerja selama 5 hari) = " + str(gaji))

# nb : jika ingin menghitung gaji bulanan, maka diperlukan data detail untuk gaji perminggunya sehingga diperlukan fungsi for dalam perhitungannya