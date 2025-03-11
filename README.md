# Bike Sharing Dashboard

## Deskripsi
Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis data penyewaan sepeda berdasarkan dataset "Bike Sharing Dataset". Dashboard ini menyediakan visualisasi interaktif untuk mengeksplorasi pengaruh hari libur, kelembapan, dan tren tahunan terhadap jumlah penyewaan sepeda.

## Fitur
- **Pengaruh Hari Libur:** Menampilkan perbandingan rata-rata penyewaan sepeda pada hari libur dan hari biasa. 
- **Pengaruh Kelembapan:** Scatter plot yang menunjukkan hubungan antara kelembapan udara dan jumlah penyewaan sepeda.
- **Tren Tahunan:** Visualisasi tren penyewaan sepeda sepanjang tahun berdasarkan bulan.
- **Filter Interaktif:** Filter berdasarkan tahun, bulan, musim, dan hari libur.

## Instalasi & Menjalankan Aplikasi

### 1. Clone Repository (Opsional jika menggunakan Git)
```sh
git clone <repository_url>
cd <repository_folder>
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)
```sh
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate  # Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Jalankan Streamlit App
```sh
streamlit run dashboard.py
```

## Struktur Folder
```
📂 bike_sharing_project
 ├── 📄 dashboard.py        # File utama aplikasi
 ├── 📄 requirements.txt    # Dependensi Python
 ├── 📄 README.md           # Dokumentasi proyek
 ├── 📄 url.txt             # URL terkait proyek
 ├── 📂 data                # Folder dataset
 │   ├── day.csv            # Dataset utama
 └── 📂 assets              # (Opsional) Folder gambar/icon
```

## Dataset
Dataset yang digunakan dalam proyek ini adalah "Bike Sharing Dataset" yang berisi informasi tentang jumlah penyewaan sepeda harian berdasarkan faktor cuaca, musim, dan hari libur.

## Lisensi
Proyek ini bersifat open-source dan dapat digunakan sesuai dengan lisensi yang berlaku.
