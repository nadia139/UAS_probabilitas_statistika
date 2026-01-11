<img width="1254" height="219" alt="image" src="https://github.com/user-attachments/assets/fbc3a85d-ef64-4294-b78a-7686664a192c" />

# Penjelasan:

Menampilkan 5 restoran pertama dari total 148 data
Terlihat ada 7 kolom: name, online_order, book_table, rate, votes, approx_cost, listed_in(type)
Kolom rate masih dalam format "4.1/5" (string) - perlu dibersihkan
Semua 5 restoran ini bertipe Buffet
Jalsa memiliki online order + book table
Spice Elephant & San Churro hanya online order
Addhuri Udupi & Grand Village tidak ada layanan online/booking
# Kesimpulan: 
Data masih mentah, rating perlu konversi ke angka agar bisa dihitung.


<img width="1229" height="226" alt="image" src="https://github.com/user-attachments/assets/a7e366ad-2348-482c-b3bb-7d1c6bec83b3" />


# Penjelasan:
Perubahan: Kolom rate berubah dari "4.1/5" menjadi 4.1 (angka desimal)
Format /5 sudah dihilangkan
Sekarang kolom rate bertipe float64 sehingga bisa digunakan untuk kalkulasi matematika
Data lainnya tetap sama
# Kesimpulan: 
Proses cleaning berhasil, data siap untuk analisis statistik.


<img width="742" height="419" alt="image" src="https://github.com/user-attachments/assets/3090c648-e99b-4581-b271-2ab30ce6fc13" />


# Penjelasan
Jumlah Data:
148 entries (0 sampai 147) = Total 148 restoran
Struktur Kolom:
7 kolom total
Tipe Data:
object (4 kolom): name, online_order, book_table, listed_in(type) - berisi teks/kategori
float64 (1 kolom): rate - angka desimal untuk rating
int64 (2 kolom): votes, approx_cost - angka bulat
Non-Null Count:
Semua kolom = 148 non-null → Tidak ada data yang hilang!
Memory Usage:
Dataset hanya butuh 8.2 KB - sangat kecil dan efisien
# Kesimpulan:
Data 100% lengkap, tidak ada missing values
Tipe data sudah sesuai untuk analisis
Dataset ringan dan mudah diproses

<img width="511" height="263" alt="image" src="https://github.com/user-attachments/assets/4ed86a93-f574-43b4-8681-a2a6176506c9" />

# Penjelasan:
Menampilkan jumlah nilai kosong/null di setiap kolom
Semua kolom = 0 → Tidak ada satupun data yang hilang
Ini adalah data quality yang sangat baik
Tidak perlu melakukan imputasi (pengisian data kosong)
# Kesimpulan: 
Data sangat bersih, siap 100% untuk analisis tanpa treatment tambahan.


<img width="534" height="143" alt="image" src="https://github.com/user-attachments/assets/3d0d822e-7d4b-4e4d-810f-add004230bff" />


# Penjelasan:
Restoran paling populer: Empire Restaurant
Berada di index 38 (baris ke-39 dalam dataset)
Total votes: 4,884 votes - angka yang SANGAT TINGGI
Untuk perbandingan: rata-rata votes per restoran sekitar 330 (4884/148)
Empire Restaurant mendapat votes hampir 15x lipat dari rata-rata!
# Kesimpulan:
Empire Restaurant adalah market leader yang sangat dominan
Popularitasnya jauh melampaui kompetitor
Bisa dijadikan benchmark untuk restoran lain


<img width="452" height="319" alt="image" src="https://github.com/user-attachments/assets/134bb076-53ea-4303-a479-228e69558996" />


# Penjelasan:
No (Offline only): 90 restoran = 60.8%
Yes (Online enabled): 58 restoran = 39.2%
# Breakdown:
Mayoritas restoran (lebih dari setengah) masih belum adopsi online order
Hanya 4 dari 10 restoran yang sudah online
Gap masih besar: 90 vs 58 (selisih 32 restoran)
# Kesimpulan:
Peluang transformasi digital masih BESAR
90 restoran adalah target potensial untuk onboarding online
Tren menunjukkan online order semakin penting untuk kompetitif


<img width="813" height="409" alt="image" src="https://github.com/user-attachments/assets/27bc6756-e583-47ed-8b03-e9aff7f56052" />




