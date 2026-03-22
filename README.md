

## **1.penjelasan konsep array menghitung nilai 10 mahasiswa**

Array adalah struktur data yang digunakan untuk menyimpan banyak data dalam satu variabel, dengan tipe data yang biasanya sama.

Contoh di Python:

```python
nilai = [80, 75, 90, 60]
```

 **Ciri-ciri Array**

* Menyimpan banyak nilai dalam satu tempat
* Data tersusun berurutan
* Memiliki index (dimulai dari 0)
* Bisa diakses menggunakan index

Contoh akses:

```python
print(nilai[0])  # output: 80
```

 **Fungsi Array**

Array digunakan untuk:

* Menyimpan kumpulan data (misalnya nilai mahasiswa)
* Mempermudah pengolahan data (looping)
* Melakukan perhitungan seperti:

  * nilai tertinggi → `max()`
  * nilai terendah → `min()`
  * rata-rata → `sum() / jumlah data`

 **Kelebihan Array**

* Praktis untuk banyak data
* Mudah diolah dengan perulangan
* Lebih rapi dibanding banyak variabel

---


   

# 2.screenshot hasil eksekusi

input data

   <img width="202" height="131" alt="input data" src="https://github.com/user-attachments/assets/7f40163e-c628-48ad-a5ae-c92ca927ac26" />



#
hasil

<img width="407" height="92" alt="hasil" src="https://github.com/user-attachments/assets/46ee0685-c4ac-4957-bcbc-f44bd0b3b56e" />

#
perbandingan nilai

<img width="311" height="245" alt="GRAFIK 1" src="https://github.com/user-attachments/assets/9a9537d8-5258-4698-bc0e-fdd979bd3ea6" />

#
data kelulusan

<img width="315" height="248" alt="GRAFIK 2" src="https://github.com/user-attachments/assets/90aec744-c079-4ab5-9a51-e3d2e9c8e6bd" />





## **3.Analisis Kompleksitas**

Misal jumlah data = **n (jumlah nilai mahasiswa)**

 1. Input data

Program melakukan perulangan untuk memasukkan nilai sebanyak n kali
→ Kompleksitas: **O(n)**



 2. Mencari nilai tertinggi & terendah

Menggunakan `max()` dan `min()` yang membaca seluruh data
→ Kompleksitas: **O(n)**


 3. Menghitung rata-rata

Menggunakan `sum()` lalu dibagi jumlah data
→ Kompleksitas: **O(n)**

 4. Menghitung jumlah lulus

Melakukan pengecekan setiap nilai (loop/filter)
→ Kompleksitas: **O(n)**


 5. Pembuatan grafik

Data tetap harus dibaca terlebih dahulu
→ Kompleksitas: **O(n)**



---

## **4.Refleksi Pembelajaran**

Dari tugas ini, saya memahami bagaimana menggunakan array (list) dalam Python untuk menyimpan dan mengolah data. Saya belajar cara mencari nilai tertinggi, terendah, menghitung rata-rata, serta menentukan jumlah data yang memenuhi kriteria tertentu.

Selain itu, saya juga memahami dasar visualisasi data menggunakan grafik sehingga data lebih mudah dibaca dan dipahami. Saya jadi lebih paham bahwa struktur data sangat membantu dalam membuat program menjadi lebih rapi dan efisien.

Kendala yang saya alami adalah dalam memahami alur logika program dan penggunaan grafik, tetapi dengan mencoba dan memperbaiki kode, saya bisa lebih mengerti cara kerjanya.

Ke depannya, saya ingin lebih mendalami pengolahan data dan membuat program yang lebih kompleks.




  
      
     

