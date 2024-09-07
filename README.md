# User-Agent-List

**User-Agent-List** adalah script Python yang digunakan untuk mengumpulkan daftar User-Agent dari dua situs web populer: **WhatMyUserAgent** dan **user-agents.net**. Script ini akan menampilkan pilihan brand dan model perangkat, lalu menyimpan User-Agent yang terkait ke dalam file teks.

## Fitur

- **Mengambil Brand dari WhatMyUserAgent**: Mendapatkan daftar brand dari situs web WhatMyUserAgent.
- **Mengambil Model dari Brand yang Dipilih**: Mendapatkan daftar model dari brand yang dipilih oleh pengguna.
- **Menyimpan User-Agent**: User-Agent dari model yang dipilih akan disimpan ke dalam file `nama-model.txt`.
- **Mengambil User-Agent dari user-agents.net**: Mengambil daftar User-Agent secara acak dari user-agents.net dengan batasan yang ditentukan oleh pengguna dan menyimpannya ke dalam file `user_agents_random.txt `.

## Prasyarat

Sebelum menjalankan script ini, pastikan kamu telah menginstal semua dependensi yang dibutuhkan:

```bash
pkg update && pkg upgrade
pip install requests
pip install requests beautifulsoup4
git clone https://github.com/Fajarxyta/User-Agent-List
```

## Cara Penggunaan

1. Clone repositori ini
2. Jalankan script dengan perintah:

```bash
cd User-Agent-List
python3 agent.py
```
3. Pilih opsi yang diinginkan:
  - **Whatmyuseragent**: Untuk mengambil User-Agent berdasarkan brand dan model perangkat.
  - **User-agents.net**: Untuk mengambil User-Agent secara acak dari situs user-agents.net.

4. Ikuti instruksi selanjutnya yang muncul di terminal.

## Contoh Output

- **WhatMyUserAgent**: 
    Setelah memilih brand dan model, User-Agent akan disimpan ke nama-model.txt dan ditampilkan di terminal.
- **user-agents.net**:
    Setelah menentukan jumlah User-Agent yang diinginkan, mereka akan disimpan ke user_agents_random.txt dan ditampilkan di terminal.
    
# x

<img src="https://raw.githubusercontent.com/Fajarxyta/User-Agent-List/main/img/20240907_194342.png"/>
