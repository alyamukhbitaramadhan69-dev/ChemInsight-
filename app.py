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
        #1e3a8a 40%,
        #7c3aed 100%
    );
}

h1, h2, h3, h4, h5, h6 {
    color: white !important;
}

p, label, div {
    color: white !important;
}

[data-testid="stSidebar"] {
    background-color: rgba(15, 23, 42, 0.95);
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    background-color: #2563eb;
    color: white;
    border: none;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================
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
        
# =====================
# BERANDA
# =====================

if menu == "🏠 Beranda":

    # =====================
    # BANNER
    # =====================

    st.markdown("""
    # 🧪 ChemInsight

    ### Smart Chemistry Calculator & Laboratory Data Analysis

    Membantu perhitungan kimia, analisis data laboratorium, dan visualisasi grafik secara cepat dan akurat.
    """)

    st.markdown("---")

    # =====================
    # KARTU FITUR
    # =====================

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

    Aplikasi ini menyediakan berbagai fitur yang mendukung pembelajaran, penelitian, dan praktikum laboratorium.

    ---

    ### 🔍 Fitur Utama

    #### 📊 Perhitungan pH
    Menghitung pH, pOH, konsentrasi H+ dan OH-.

    **Rumus Asam**
    - pH = -log(H+)

    **Rumus Basa**
    - pOH = -log(OH-)
    - pH = 14 - pOH

    #### ⚗️ Molaritas dan Normalitas

    Menghitung konsentrasi larutan.

    **Rumus**
    - M = n / V
    - N = ekivalen / V

    #### 💧 Pengenceran Larutan

    Menggunakan persamaan:

    M1V1 = M2V2

    #### 🧫 Analisis Titrasi

    Menghitung konsentrasi larutan melalui titrasi.

    MaVa = MbVb

    #### 📁 Upload Data CSV

    Membaca dan menampilkan data eksperimen.

    #### 📈 Visualisasi Grafik

    Menampilkan grafik data secara interaktif.

    #### 📋 Statistik Data

    Menampilkan:
    - Mean
    - Median
    - Modus
    - Standar Deviasi
    - Nilai Minimum
    - Nilai Maksimum
    """)

    # =====================
    # KARTU FITUR
    # =====================

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

    Aplikasi ini menyediakan berbagai fitur yang mendukung pembelajaran, penelitian, dan praktikum laboratorium.
    """)
    ---
    ### 🔍 Fitur Utama

    ### Perhitungan pH
    Rumus Asam:
    pH = -log(H+)

    Rumus Basa:
    pOH = -log(OH-)

    pH + pOH = 14

    #### ⚗️ Molaritas dan Normalitas
    Menghitung konsentrasi larutan.

    Rumus:
    - M = n / V
    - N = ekivalen / V

    #### 💧 Pengenceran Larutan
    Menggunakan persamaan:

    M1V1 = M2V2

    #### 🧫 Analisis Titrasi
    Menghitung konsentrasi larutan melalui titrasi.

    MaVa = MbVb

    #### 📁 Upload Data CSV
    Membaca dan menampilkan data eksperimen.

    #### 📈 Visualisasi Grafik
    Menampilkan grafik data secara interaktif.

    #### 📋 Statistik Data
    Menampilkan:
    - Mean
    - Median
    - Modus
    - Standar Deviasi
    - Nilai Minimum
    - Nilai Maksimum
    """)
    
# =====================
# PERHITUNGAN PH
# =====================

elif menu == "📊 Perhitungan pH":

    st.header("📊 Perhitungan pH")

    st.markdown("""
    ### Tentang Perhitungan pH

    pH digunakan untuk menentukan tingkat keasaman atau kebasaan suatu larutan.

    **Rumus Larutan Asam:**

    pH = -log(H+)

    **Rumus Larutan Basa:**

    pOH = -log(OH-)

    pH = 14 - pOH
    """)

    jenis = st.selectbox(
        "Pilih Jenis Larutan",
        ["Asam", "Basa"]
    )

    if jenis == "Asam":

        st.subheader("🧪 Perhitungan pH Asam")

        h = st.number_input(
            "Masukkan Konsentrasi H⁺ (mol/L)",
            min_value=0.000000000001,
            value=0.001000,
            format="%f"
        )

        if st.button("Hitung pH Asam"):

            ph = -np.log10(h)

            # Membatasi nilai pH antara 0 - 14
            ph = max(0, min(ph, 14))

            st.success(f"Nilai pH = {ph:.2f}")

            if ph < 7:
                st.info("Larutan bersifat Asam")
            elif ph == 7:
                st.info("Larutan bersifat Netral")

    else:

        st.subheader("🧪 Perhitungan pH Basa")

        oh = st.number_input(
            "Masukkan Konsentrasi OH⁻ (mol/L)",
            min_value=0.000000000001,
            value=0.001000,
            format="%f"
        )

        if st.button("Hitung pH Basa"):

            poh = -np.log10(oh)

            ph = 14 - poh

            # Membatasi nilai pH antara 0 - 14
            ph = max(0, min(ph, 14))

            st.success(f"Nilai pH = {ph:.2f}")

            if ph > 7:
                st.info("Larutan bersifat Basa")
            elif ph == 7:
                st.info("Larutan bersifat Netral")

# =====================
# MOLARITAS
# =====================

elif menu == "⚗️ Molaritas & Normalitas":

    st.header("⚗️ Molaritas dan Normalitas")

    pilihan = st.selectbox(
        "Pilih Perhitungan",
        ["Molaritas", "Normalitas"]
    )

    if pilihan == "Molaritas":

        mol = st.number_input("Jumlah Mol", min_value=0.0)

        volume = st.number_input(
            "Volume Larutan (L)",
            min_value=0.0001
        )

        if st.button("Hitung Molaritas"):

            m = mol / volume

            st.success(
                f"Molaritas = {m:.4f} M"
            )

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

            st.success(
                f"Normalitas = {n:.4f} N"
            )

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

        st.success(
            f"Volume Akhir (V2) = {v2:.2f} mL"
        )

# =====================
# TITRASI
# =====================

elif menu == "🧫 Analisis Titrasi":

    st.header("🧫 Analisis Titrasi")

    vb = st.number_input(
        "Volume Basa (mL)",
        min_value=0.0
    )

    mb = st.number_input(
        "Molaritas Basa",
        min_value=0.0
    )

    va = st.number_input(
        "Volume Asam (mL)",
        min_value=0.0001
    )

    if st.button("Hitung Molaritas Asam"):

        ma = (mb * vb) / va

        st.success(
            f"Molaritas Asam = {ma:.4f} M"
        )

# =====================
# UPLOAD CSV
# =====================

elif menu == "📁 Upload Data CSV":

    st.header("📁 Upload Data CSV")

    file = st.file_uploader(
        "Upload File CSV",
        type=["csv"]
    )

    if file is not None:

        df = pd.read_csv(file)

        st.dataframe(df)

# =====================
# VISUALISASI
# =====================

elif menu == "📈 Visualisasi Grafik":

    st.header("📈 Visualisasi Grafik")

    file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if file is not None:

        df = pd.read_csv(file)

        st.dataframe(df)

        kolom = df.select_dtypes(
            include=np.number
        ).columns

        if len(kolom) > 0:

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

# =====================
# STATISTIK
# =====================

elif menu == "📋 Statistik Data":

    st.header("📋 Statistik Data Laboratorium")

    file = st.file_uploader(
        "Upload CSV Statistik",
        type=["csv"]
    )

    if file is not None:

        df = pd.read_csv(file)

        st.dataframe(df)

        numerik = df.select_dtypes(
            include=np.number
        )

        st.subheader("Ringkasan Statistik")

        st.write(
            numerik.describe()
        )

        st.subheader("Statistik Tambahan")

        st.write(
            f"Median:\n{numerik.median()}"
        )

        st.write(
            f"Standar Deviasi:\n{numerik.std()}"
        )

        st.write(
            f"Varians:\n{numerik.var()}"
        )
