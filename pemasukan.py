import streamlit as st

st.title("Pemasukan Per-Hari")

# Pemasukan Per-Hari
with st.form("Pemasukan"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    keterangan = st.text_input("Keterangan")
    submit_button = st.form_submit_button(label="Menabung")
    if submit_button:
        st.session_state["Jumlah"].append({
            "Tipe" : "Pemasukan",
            "Nama" : nama,
            "Jumlah" : jumlah,
            "Keterangan": keterangan   
        })
        st.success("Pemasukan berhasil ditambahkan")
    else:
        st.error("Pemasukan gagal ditambahkan")

# Fungsi Untuk Menghitung

def total():
    total_pemasukan = sum(t["Jumlah"] for t in st.session_state ["Jumlah"] if t["Tipe"] == "Pemasukan")
    return f"Total Pemasukan Per-Hari Anda {total_pemasukan}"

st.write(total())