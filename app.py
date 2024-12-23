import streamlit as st

# Side Bar Directory
pemasukan = st.Page("./Fitur/pemasukan.py", title="pemasukan")


pg = st.navigation(
    {
        "Menu Utama":[pemasukan],

    }
)

if "Jumlah" not in st.session_state:
    st.session_state["Jumlah"] = []

# Menjalankan Aplikasi
pg.run()

