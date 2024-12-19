import sqlite3
import os

my_db = 'intern_test.db'
conn = sqlite3.connect(my_db)

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Mahasiswa (
                   NIM INTERGER PRIMARY KEY,
                   Nama TEXT NOT NULL,
                   Alamat TEXT NOT NULL,
                   Jurusan TEXT NOT NULL,
                   Umur INTERGER NOT NULL
                   )
                   ''')

NIM_1 = [123456, 234567, 345678, 456789, 567890, 678901, 789012]
nama = ["John", "Alice", "Bob", "Cindy", "David", "Emily", "Frank"]
alamat = ["Jl. Merdeka No 1", "Jl. Gatot Subroto", "Jl. Sudirman No. 5", "Jl. Pahlawan No. 2", "Jl. Diponegoro No. 3", "Jl. Cendrawasih No. 4", "Jl. Ahmad Yani No. 6"]
jurusan = ["Teknik Informatika", "Sistem Informatika", "Teknik Informatika", "Manajemen", "Teknik Elektro", "Manajemen", "Teknik Informatika"]
umur = [21, 23, 20, 22, 25, 24, 19]

for i in range(len(NIM_1)):
    cursor.execute('''
                   INSERT INTO Mahasiswa (NIM, Nama, Alamat, Jurusan, Umur) VALUES (?, ?, ?, ?, ?)
                   ''', (NIM_1[i], nama[i], alamat[i], jurusan[i], umur[i]))  

conn.commit()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS Mata_Kuliah (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   Mata_Kuliah TEXT NOT NULL,
                   NIM INTERGER NOT NULL,
                   Nilai INTERGER NOT NULL,
                   Dosen_Pengajar TEXT NOT NULL
                   )
                   ''')

mata_kuliah = ["Pemograman Web", "Basis Data", "Jaringan Komputer", "Sistem Operasi", "Manajemem Proyek", "Bahasa Inggris", "Statistika", "Algoritma", "Pemograman Java"]
NIM_2 = [123456, 234567, 345678, 123456, 456789, 567890, 678901, 789012, 123456]
nilai = [85, 70, 75, 90, 80, 85, 75, 65, 95]
dosen_pengajar = ["Pak Budi", "Ibu Ani", "Pak Dodi", "Pak Budi", "Ibu Desi", "Ibu Eka", "Pak Farhan", "Pak Galih", "Pak Budi"]

for i in range(len(NIM_2)):
    cursor.execute('''
                   INSERT INTO Mata_Kuliah (Mata_Kuliah, NIM, Nilai, Dosen_Pengajar) VALUES (?, ?, ?, ?)
                   ''', (mata_kuliah[i], NIM_2[i], nilai[i], dosen_pengajar[i]))  

conn.commit()

print("\nTabel Mahasiswa")

cursor.execute('SELECT * FROM Mahasiswa')
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\nTabel Mata_Kuliah")

cursor.execute('SELECT * FROM Mata_Kuliah')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Soal Nomor 1
print("\nsoal nomor 1\n")
print("\nSebelum Update")

cursor.execute('SELECT * FROM Mahasiswa')
rows = cursor.fetchall()
for row in rows:
    print(row)
    
cursor.execute('''
               UPDATE Mahasiswa
               SET Alamat = ?
               WHERE NIM = ?
               ''', ("Jl. Raya No.5", 123456))

print("\nSesudah Update")

cursor.execute('SELECT * FROM Mahasiswa')
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\n")

# Soal Nomor 2
print("\nsoal nomor 2\n")
cursor.execute('''
               SELECT Mahasiswa.NIM, Mahasiswa.Nama, Mahasiswa.Jurusan, Mata_Kuliah.Dosen_Pengajar
               FROM Mahasiswa
               INNER JOIN Mata_Kuliah ON Mahasiswa.NIM = Mata_Kuliah.NIM
               WHERE Mahasiswa.Jurusan = ?
               ''', ("Teknik Informatika",))

rows = cursor.fetchall()
for row in rows:
    print(row)
# cursor.execute('''
#                SELECT NIM, Nama, Jurusan FROM Mahasiswa
#                WHERE Jurusan = ?
#                ''', ("Teknik Informatika",))

# from_mahasiswa = cursor.fetchall()
# all_result = []
# from_mata_kuliah = []
# # print(from_mahasiswa)
# for nim in from_mahasiswa:
#     nim_value = nim[0]  
#     print(nim_value)
#     cursor.execute('''
#                    SELECT Mahasiswa.NIM, Mahasiswa.Nama, Mahasiswa.Jurusan, Mata_Kuliah.Dosen_Pengajar
#                    FROM Mahasiswa
#                    INNER JOIN Mata_Kuliah ON Mahasiswa.NIM = Mata_Kuliah.NIM
#                    ''')
    
#     from_mata_kuliah = cursor.fetchall()
#     # all_result = from_mahasiswa.append(from_mata_kuliah)
#     # print(all_result)

# print(from_mahasiswa)
# print(from_mata_kuliah)
# # print(all_result)

print("/n")

# No 3
print("\nsoal nomor 3\n")
cursor.execute('''
               SELECT Mahasiswa.Nama, Mahasiswa.Umur
               FROM Mahasiswa
               ORDER BY Mahasiswa.Umur DESC
               ''')

rows = cursor.fetchall()
for row in rows:
    print(row)

print("/n")

# No 4
print("\nsoal nomor 4\n")
cursor.execute('''
               SELECT Mahasiswa.Nama, Mata_Kuliah.mata_kuliah, Mata_Kuliah.Nilai
               FROM Mahasiswa
               INNER JOIN Mata_Kuliah ON Mahasiswa.NIM = Mata_Kuliah.NIM
               WHERE Mata_Kuliah.Nilai > 70 
               ORDER BY Mata_Kuliah.Nilai DESC
               ''')

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()