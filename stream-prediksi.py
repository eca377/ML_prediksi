import pickle
import streamlit as st

# Load model
prediksi_model = pickle.load(open('prediksi_model.sav', 'rb'))

# Judul
st.title('Data Mining - Prediksi Kelulusan')


# Input informasi non-prediktif (hanya untuk tampilan)
nim = st.text_input('Masukkan NIM')
nama = st.text_input('Masukkan Nama')

# Imembagi kolom
col1, col2 = st.columns (2)

with col1 :
    ips1 = st.number_input('Masukkan nilai IPS1', min_value=0)

with col2:
    ips2 = st.number_input('Masukkan nilai IPS2', min_value=0)

with col1 :
    ips3 = st.number_input('Masukkan nilai IPS3', min_value=0)

with col2:
    ips4 = st.number_input('Masukkan nilai IPS4', min_value=0)

with col1 :
    ips5 = st.number_input('Masukkan nilai IPS5', min_value=0)

with col2:
    ips6 = st.number_input('Masukkan nilai IPS6', min_value=0)

with col1 :
    ips7 = st.number_input('Masukkan nilai IPS7', min_value=0)

with col2:
    ips8 = st.number_input('Masukkan nilai IPS8', min_value=0)

with col1 :
    ipk  = st.number_input('Masukkan nilai IPK', min_value=0)

# Label hanya untuk referensi jika ingin dibandingkan
label = st.text_input('Label (0 atau 1 - opsional)')

# Tombol prediksi
if st.button('Tes Prediksi Lulus'):
    try:
        # Gunakan hanya fitur yang dipakai saat training (tanpa IPK)
        features = [[ips1, ips2, ips3, ips4, ips5, ips6, ips7, ips8]]
        prediction = prediksi_model.predict(features)

        if prediction[0] == 0:
            hasil = 'Siswa tidak lulus'
        else:
            hasil = 'Siswa lulus'

        st.success(f'Hasil Prediksi untuk {nama} ({nim}): {hasil}')

    except Exception as e:
        st.error(f'Terjadi kesalahan saat prediksi: {e}')

