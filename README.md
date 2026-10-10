# Laptop Recommendation with Binary Tree

Aplikasi web sederhana untuk merekomendasikan laptop berdasarkan kebutuhan pengguna. Data laptop disimpan dalam struktur data **Binary Search Tree (BST)** yang diurutkan berdasarkan harga, sehingga pencarian rekomendasi dalam rentang harga tertentu bisa memangkas cabang pohon yang tidak relevan.

Dibangun dengan **Python (Flask)** untuk backend dan HTML/CSS/JavaScript untuk tampilan.

## Fitur

- Filter rekomendasi berdasarkan:
  - Merek prosesor (Intel, AMD, Apple)
  - Seri prosesor (daftar dimuat dinamis sesuai merek yang dipilih)
  - RAM minimum dan penyimpanan minimum
  - Tipe laptop: gaming (memiliki VGA) atau non-gaming
  - Rentang harga (minimum dan maksimum)
- Halaman detail produk berisi spesifikasi lengkap: layar, baterai, bobot, OS, Wi-Fi, Bluetooth, keyboard, kamera, port, deskripsi, tautan video YouTube, dan tautan pembelian.
- Angka harga ditampilkan dengan format pemisah ribuan.

## Cara Kerja Binary Tree

Setiap laptop dibungkus dalam `ProductNode` dan dimasukkan ke `ProductBinaryTree` dengan aturan:

- Harga **lebih kecil atau sama** dengan harga node saat ini → masuk ke **anak kiri**
- Harga **lebih besar** → masuk ke **anak kanan**

Saat pencarian (`recommend_products`), pohon ditelusuri secara rekursif dan setiap node diperiksa terhadap kriteria pengguna. Cabang kiri hanya ditelusuri jika harga node masih `>= min_price`, dan cabang kanan hanya jika harga node `<= max_price`, sehingga cabang di luar rentang harga dilewati.

## Struktur Proyek

```
.
├── wqdw.py                 # Aplikasi Flask, kelas Product, ProductNode, ProductBinaryTree, dan data laptop
├── templates/
│   ├── index.html          # Halaman utama (form pencarian)
│   └── product_detail.html # Halaman detail produk
└── static/
    └── images/             # Gambar laptop
```

## Menjalankan Aplikasi

1. Pastikan Python 3 sudah terpasang.
2. Pasang Flask:

   ```bash
   pip install flask
   ```

3. Jalankan aplikasi:

   ```bash
   python wqdw.py
   ```

4. Buka `http://localhost:5000` di browser.

## Endpoint

| Method | Endpoint | Fungsi |
|--------|----------|--------|
| GET | `/` | Halaman utama |
| GET | `/get_processors/<brand>` | Daftar seri prosesor untuk merek tertentu (JSON) |
| POST | `/search` | Mengembalikan daftar laptop yang cocok dengan kriteria (JSON) |
| GET | `/product/<name>` | Halaman detail laptop berdasarkan nama |

Contoh isi body untuk `POST /search`:

```json
{
  "brand": "Intel",
  "processor": "Intel Core i5",
  "ram": 8,
  "storage": 512,
  "type": "gaming",
  "vga": "",
  "minPrice": 10000000,
  "maxPrice": 15000000
}
```

## Menambah Data Laptop

Tambahkan objek `Product` baru ke dalam daftar `laptops` di `wqdw.py`, lalu letakkan gambarnya di `static/images/` dan isi `image_url` dengan path-nya. Laptop non-gaming dibedakan dengan mengosongkan field `vga`.

## Catatan

- `secret_key` dan mode `debug=True` di `wqdw.py` ditujukan untuk pengembangan. Ganti keduanya sebelum aplikasi dipakai secara publik.
