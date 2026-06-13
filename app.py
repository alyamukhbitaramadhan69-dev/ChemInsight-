import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================
# KONFIGURASI HALAMAN
# =====================

st.set_page_config(
    page_title="ChemInsight",
    page_icon="🧪",
    layout="wide"
)

# =====================
# CUSTOM BACKGROUND
# =====================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e3a8a 35%,
        #4f46e5 70%,
        #7c3aed 100%
    );
    background-attachment: fixed;
}

/* Judul */
h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF !important;
    font-weight: bold;
    text-shadow: 2px 2px 6px rgba(0,0,0,0.8);
}

/* Teks */
p, label, li, span {
    color: #FFFFFF !important;
    text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: rgba(15, 23, 42, 0.95);
}

/* Tulisan sidebar */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Tombol */
.stButton > button {
    width: 100%;
    border-radius: 12px;
    background-color: #2563eb;
    color: white !important;
    border: none;
    font-weight: bold;
}

/* Input */
.stNumberInput input,
.stTextInput input {
    background-color: rgba(255,255,255,0.95) !important;
    color: black !important;
    font-weight: bold;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background-color: rgba(255,255,255,0.95) !important;
    color: black !important;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    background-color: rgba(255,255,255,0.95);
    border-radius: 10px;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background-color: rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)
# SIDEBAR
# =====================

st.sidebar.title("🧪 ChemInsight")

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "🏠 Beranda",
        "📊 Perhitungan pH",
        "⚗️ Molaritas & Normalitas",
        "💧 Pengenceran Larutan",
        "🧫 Analisis Titrasi",
        "📁 Upload Data CSV",
        "📈 Visualisasi Grafik",
        "📋 Statistik Data"
    ]
)

# =====================
# BERANDA
# =====================

if menu == "🏠 Beranda":

    st.markdown("""
    # 🧪 ChemInsight

    ### Smart Chemistry Calculator & Laboratory Data Analysis

    Membantu perhitungan kimia, analisis data laboratorium, dan visualisasi grafik secara cepat dan akurat.
    """)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📊 Perhitungan pH")
        st.info("⚗️ Molaritas & Normalitas")
        st.info("💧 Pengenceran Larutan")
        st.info("🧫 Analisis Titrasi")

    with col2:
        st.info("📁 Upload Data CSV")
        st.info("📈 Visualisasi Grafik")
        st.info("📋 Statistik Data Laboratorium")

    st.markdown("---")

    st.markdown("""
## Selamat Datang di ChemInsight

ChemInsight adalah aplikasi analisis dan perhitungan kimia berbasis web yang membantu pengguna melakukan perhitungan kimia, analisis data laboratorium, dan visualisasi hasil eksperimen secara cepat dan akurat.

### 🔍 Fitur Utama

#### 📊 Perhitungan pH
- pH = -log(H⁺)
- pOH = -log(OH⁻)
- pH = 14 - pOH

#### ⚗️ Molaritas dan Normalitas
- M = n / V
- N = ekivalen / V

#### 💧 Pengenceran Larutan
- M₁V₁ = M₂V₂

#### 🧫 Analisis Titrasi
- NaVa = NbVb

#### 📁 Upload Data CSV
Membaca dan menampilkan data eksperimen.

#### 📈 Visualisasi Grafik
Menampilkan grafik data secara interaktif.

#### 📋 Statistik Data
Menampilkan:
- Mean
- Median
- Standar Deviasi
- Varians
- Nilai Minimum
- Nilai Maksimum
""")

# =====================
# PERHITUNGAN PH
# =====================

elif menu == "📊 Perhitungan pH":

    st.header("📊 Perhitungan pH")

    jenis = st.selectbox(
        "Pilih Jenis Larutan",
        ["Asam", "Basa"]
    )

    if jenis == "Asam":

        h = st.number_input(
            "Masukkan Konsentrasi H⁺ (mol/L)",
            min_value=1e-12,
            value=0.001
        )

        if st.button("Hitung pH Asam"):

            ph = -np.log10(h)
            ph = max(0, min(ph, 14))

            st.success(f"Nilai pH = {ph:.2f}")

            if ph < 7:
                st.info("Larutan bersifat Asam")
            elif ph == 7:
                st.info("Larutan bersifat Netral")

    else:

        oh = st.number_input(
            "Masukkan Konsentrasi OH⁻ (mol/L)",
            min_value=1e-12,
            value=0.001
        )

        if st.button("Hitung pH Basa"):

            poh = -np.log10(oh)
            ph = 14 - poh
            ph = max(0, min(ph, 14))

            st.success(f"Nilai pH = {ph:.2f}")

            if ph > 7:
                st.info("Larutan bersifat Basa")
            elif ph == 7:
                st.info("Larutan bersifat Netral")

# =====================
# MOLARITAS & NORMALITAS
# =====================

elif menu == "⚗️ Molaritas & Normalitas":

    st.header("⚗️ Molaritas dan Normalitas")

    pilihan = st.selectbox(
        "Pilih Perhitungan",
        ["Molaritas", "Normalitas"]
    )

    if pilihan == "Molaritas":

        mol = st.number_input(
            "Jumlah Mol",
            min_value=0.0
        )

        volume = st.number_input(
            "Volume Larutan (L)",
            min_value=0.0001
        )

        if st.button("Hitung Molaritas"):

            m = mol / volume
            st.success(f"Molaritas = {m:.4f} M")

    else:

        ekuivalen = st.number_input(
            "Jumlah Ekuivalen",
            min_value=0.0
        )

        volume = st.number_input(
            "Volume Larutan (L)",
            min_value=0.0001
        )

        if st.button("Hitung Normalitas"):

            n = ekuivalen / volume
            st.success(f"Normalitas = {n:.4f} N")

# =====================
# PENGENCERAN
# =====================

elif menu == "💧 Pengenceran Larutan":

    st.header("💧 Pengenceran Larutan")

    m1 = st.number_input("M1", min_value=0.0)
    v1 = st.number_input("V1 (mL)", min_value=0.0)
    m2 = st.number_input("M2", min_value=0.0001)

    if st.button("Hitung V2"):

        v2 = (m1 * v1) / m2
        st.success(f"Volume Akhir (V2) = {v2:.2f} mL")

# =====================
# ANALISIS TITRASI
# =====================

elif menu == "🧫 Analisis Titrasi":

    st.header("🧫 Analisis Titrasi")

    vtitran = st.number_input(
        "Volume Titran (mL)",
        min_value=0.0
    )

    ntitran = st.number_input(
        "Normalitas Titran (N)",
        min_value=0.0
    )

    vtitrat = st.number_input(
        "Volume Titrat (mL)",
        min_value=0.0001
    )

    if st.button("Hitung Normalitas Titrat"):

        ntitrat = (ntitran * vtitran) / vtitrat

        st.success(
            f"Normalitas Titrat = {ntitrat:.4f} N"
        )
        
# =====================
# UPLOAD CSV
# =====================

elif menu == "📁 Upload Data CSV":

    st.header("📁 Upload Data CSV")

    st.info("""
Upload file CSV yang berisi data hasil praktikum atau eksperimen.

Contoh format CSV:

No,Sampel,Konsentrasi,pH
1,A,0.10,3.5
2,B,0.20,4.1
3,C,0.30,4.8

Setelah file diupload, data akan ditampilkan dalam bentuk tabel.
""")

    file = st.file_uploader(
        "Upload File CSV",
        type=["csv"]
    )

    if file is not None:

        try:
            df = pd.read_csv(file)

            st.success("✅ File berhasil diupload")

            st.subheader("Data CSV")
            st.dataframe(df)

        except Exception as e:
            st.error(f"Error membaca file: {e}")
            
# =====================
# VISUALISASI
# =====================

elif menu == "📈 Visualisasi Grafik":

    st.header("📈 Visualisasi Grafik")
    st.info("""
Upload file CSV yang memiliki minimal 2 kolom numerik untuk dibuat grafik.

Contoh format:

Waktu,Suhu
0,25
10,30
20,35
30,40

atau

Konsentrasi,Absorbansi
0.1,0.15
0.2,0.31
0.3,0.47

Pilih kolom yang akan digunakan sebagai sumbu X dan sumbu Y.
""")
    file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if file is not None:

        try:
            df = pd.read_csv(file)

            st.dataframe(df)

            kolom = df.select_dtypes(
                include=np.number
            ).columns

            if len(kolom) > 1:

                x = st.selectbox(
                    "Pilih Kolom X",
                    kolom
                )

                y = st.selectbox(
                    "Pilih Kolom Y",
                    kolom
                )

                fig, ax = plt.subplots()

                ax.scatter(df[x], df[y])

                ax.set_xlabel(x)
                ax.set_ylabel(y)

                st.pyplot(fig)

            else:
                st.warning("Minimal harus ada 2 kolom numerik.")

        except Exception as e:
            st.error(f"Error: {e}")
            
# =====================
# STATISTIK
# =====================

elif menu == "📋 Statistik Data":

    st.header("📋 Statistik Data Laboratorium")

    st.info(
        """
Upload file CSV yang berisi data numerik untuk dianalisis.

Contoh format:

Sampel,Kadar_Fe,pH
A,12.5,3.4
B,13.1,3.6
C,12.8,3.5
D,13.4,3.7

Aplikasi akan menampilkan:
• Mean
• Median
• Standar Deviasi
• Varians
• Nilai Minimum
• Nilai Maksimum
"""
    )

    file = st.file_uploader(
        "Upload CSV Statistik",
        type=["csv"]
    )

    if file is not None:

        try:
            df = pd.read_csv(file)

            st.dataframe(df)

            numerik = df.select_dtypes(include=np.number)

            st.subheader("Ringkasan Statistik")
            st.write(numerik.describe())

            st.subheader("Median")
            st.write(numerik.median())

            st.subheader("Standar Deviasi")
            st.write(numerik.std())

            st.subheader("Varians")
            st.write(numerik.var())

        except Exception as e:
            st.error(f"Error: {e}")
