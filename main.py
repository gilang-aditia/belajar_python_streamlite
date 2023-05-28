import streamlit as st

st.write("""
# Aplikasi Luas Segitiga
Ini adalah aplikasi luas menghitung segitiga sederhana menggunakan streamlite
""")

alas = st.number_input("masukan alas", 0)
tinggi = st.number_input("masukan tinggi", 0)
hitung = st.button("hitung luas segitiga")

if hitung:
    luas = 0.5 * alas * tinggi
    st.success(f"luas segitiganya adalah {luas}")
    st.balloons()