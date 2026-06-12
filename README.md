# 🧪 ChemInsight

ChemInsight adalah aplikasi analisis dan perhitungan kimia berbasis web yang dikembangkan menggunakan Streamlit. Aplikasi ini dirancang untuk membantu siswa, mahasiswa, guru, dosen, peneliti, dan praktikan laboratorium dalam melakukan berbagai perhitungan kimia, analisis data, serta visualisasi hasil eksperimen secara cepat, akurat, dan interaktif.

---

## 🎯 Tujuan Aplikasi

ChemInsight bertujuan untuk mempermudah proses pembelajaran dan analisis kimia dengan menyediakan berbagai alat perhitungan dan pengolahan data laboratorium dalam satu platform yang mudah digunakan.

---

## ✨ Fitur Utama

### 📊 Perhitungan pH
Menghitung tingkat keasaman atau kebasaan suatu larutan berdasarkan konsentrasi ion hidrogen (H⁺).

**Rumus:**

pH = -log[H⁺]

pOH = -log[OH⁻]

pH + pOH = 14

---

### ⚗️ Molaritas dan Normalitas
Menghitung konsentrasi larutan berdasarkan jumlah mol zat terlarut dan volume larutan.

**Rumus Molaritas:**

M = n / V

Keterangan:
- M = Molaritas (mol/L)
- n = jumlah mol zat
- V = volume larutan (L)

**Rumus Normalitas:**

N = Ekivalen / V

Keterangan:
- N = Normalitas (N)
- Ekivalen = jumlah gram ekivalen zat
- V = volume larutan (L)

---

### 💧 Pengenceran Larutan
Menghitung volume atau konsentrasi larutan setelah proses pengenceran.

**Rumus:**

M₁V₁ = M₂V₂

Keterangan:
- M₁ = konsentrasi awal
- V₁ = volume awal
- M₂ = konsentrasi akhir
- V₂ = volume akhir

---

### 🧫 Analisis Titrasi
Menghitung konsentrasi larutan berdasarkan data titrasi asam-basa.

**Rumus:**

MaVa = MbVb

Keterangan:
- Ma = molaritas asam
- Va = volume asam
- Mb = molaritas basa
- Vb = volume basa

---

### 📁 Upload Data CSV
Memungkinkan pengguna mengunggah data hasil praktikum atau penelitian dalam format CSV.

Fitur:
- Membaca file CSV
- Menampilkan data dalam bentuk tabel
- Mengolah data eksperimen
- Menyimpan hasil analisis

---

### 📈 Visualisasi Grafik
Menyajikan data dalam bentuk grafik untuk mempermudah interpretasi hasil eksperimen.

Jenis grafik:
- Scatter Plot
- Histogram
- Grafik Garis (Line Chart)
- Grafik Batang (Bar Chart)
- Box Plot

---

### 📋 Statistik Data Laboratorium
Menyediakan analisis statistik dasar untuk data eksperimen.

Analisis yang tersedia:
- Mean (Rata-rata)
- Median
- Modus
- Varians
- Standar Deviasi
- Nilai Minimum
- Nilai Maksimum

**Rumus Mean:**

x̄ = Σx / n

**Rumus Varians:**

s² = Σ(xᵢ − x̄)² / (n − 1)

**Rumus Standar Deviasi:**

s = √[Σ(xᵢ − x̄)² / (n − 1)]

---

## 🛠️ Teknologi yang Digunakan

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib

---

## 📂 Struktur Project

```text
ChemInsight/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│
└── images/
```

---

## 📦 Instalasi

Clone repository:

```bash
git clone https://github.com/username/ChemInsight.git
```

Masuk ke folder project:

```bash
cd ChemInsight
```

Install library yang diperlukan:

```bash
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Aplikasi

Jalankan perintah berikut:

```bash
streamlit run app.py
```

Aplikasi akan terbuka secara otomatis melalui browser.

---

## 🎓 Manfaat Aplikasi

- Membantu proses pembelajaran kimia.
- Mempercepat perhitungan laboratorium.
- Mengurangi kesalahan perhitungan manual.
- Memudahkan analisis data eksperimen.
- Menyajikan data dalam bentuk visual yang mudah dipahami.

---

## 👨‍🔬 Pengembang

**ChemInsight**

Aplikasi pembelajaran dan analisis kimia berbasis web yang dikembangkan menggunakan Streamlit untuk mendukung kegiatan akademik, penelitian, dan praktikum laboratorium.

---

© 2026 ChemInsight. All Rights Reserved.
