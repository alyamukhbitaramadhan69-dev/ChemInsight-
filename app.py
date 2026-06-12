import streamlit as st

st.set_page_config(page_title="ChemInsight", page_icon="🧪")

st.title("🧪 ChemInsight")
st.write("Selamat datang di ChemInsight, aplikasi pembelajaran kimia berbasis Streamlit.")

menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Beranda", "Materi Kimia", "Kuis"]
)

if menu == "Beranda":
    st.header("Beranda")
    st.write("ChemInsight membantu pengguna mempelajari konsep-konsep kimia secara interaktif.")

elif menu == "Materi Kimia":
    st.header("Materi Kimia")
    st.write("Contoh materi: Sistem Buffer, Asam Basa, dan Stoikiometri.")

elif menu == "Kuis":
    st.header("Kuis Sederhana")
    jawaban = st.radio(
        "pH larutan netral adalah ...",
        ["5", "7", "9"]
    )
    if st.button("Periksa Jawaban"):
        if jawaban == "7":
            st.success("Benar!")
        else:
            st.error("Jawaban kurang tepat.")
