# Selenium | Whatsapp Non/Active Number Scanner

Proyek ini adalah skrip Python untuk memeriksa status nomor WhatsApp aktif atau tidak dari daftar link whatsapp web. Skrip ini menggunakan **Selenium WebDriver** dengan **Microsoft Edge** untuk membuka WhatsApp Web dan mendeteksi apakah nomor aktif atau tidak.

Hasil pengecekan akan disimpan di file `nomoraktif.txt` dengan format:
```
6281210327367, aktif
6281210327368, tidak aktif
```


## **Isi Folder**
````
├─ main.py             # Skrip utama Python
├─ msedgedriver.exe    # WebDriver untuk Microsoft Edge
├─ linkwa.txt          # File berisi daftar link WhatsApp
├─ nomoraktif.txt      # File output hasil pengecekan
├─ requirements.txt    # File dependency Python
└─ readme.md           # Dokumentasi proyek
````


## **Instalasi dan Persiapan**

1. **Pasang Python**  
   Pastikan Python 3.9+ sudah terpasang di sistem.

2. **Install dependencies**  
   Jalankan perintah berikut di terminal:

```
pip install -r requirements.txt
````

3. **Siapkan WebDriver Edge**

   * Pastikan `msedgedriver.exe` sesuai dengan versi Microsoft Edge yang terpasang.
   * Letakkan file `msedgedriver.exe` di folder yang sama dengan `main.py`.

4. **Siapkan daftar link WhatsApp**
   Buat file `linkwa.txt` dan masukkan setiap link WhatsApp per baris, misalnya:

   ```
   https://web.whatsapp.com/send/?phone=6263634636222&text&type=phone_number&app_absent=0
   https://web.whatsapp.com/send/?phone=6282454546663&text&type=phone_number&app_absent=0
   ```
## **Cara Menggunakan**

1. Jalankan skrip Python:

```
python main.py
```
2. Program akan otomatis membuka **WhatsApp Web**.
3. **Scan QR code** menggunakan aplikasi WhatsApp di ponsel untuk login.
4. Skrip akan memproses semua link di `linkwa.txt`.
5. Hasilnya akan disimpan di `nomoraktif.txt`.

## **Catatan Penting**
* Pastikan koneksi internet stabil saat menjalankan skrip.
* Jangan tutup browser sebelum skrip selesai.
* WebDriver harus sesuai dengan versi Edge.
* Nomor yang sudah diblokir atau tidak terdaftar akan ditandai sebagai `tidak aktif`.

## **Requirements.txt**

```
selenium>=4.10.0
```

* Selenium digunakan untuk mengotomatisasi browser.
* Pastikan versi Selenium kompatibel dengan Microsoft Edge terbaru.


## **Lisensi**

MIT License. Bebas digunakan, dimodifikasi, dan didistribusikan dengan credit : https://github.com/rudy-wind
