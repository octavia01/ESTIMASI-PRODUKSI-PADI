import pickle
import streamlit as st

model = pickle.load(open('estimasi_produksi.sav', 'rb'))

st.title('Estimasi')
st.subheader('Jumlah Jumlah Produksi Tanaman Padi Di Sumatera, Indonesia')


LuasPanen = st.number_input('Input LuasPanen')
Curahhujan = st.number_input('Input Curahhujan')
Kelembapan = st.number_input('Input Kelembapan')
SuhuRataRata = st.number_input('Input SuhuRataRata')


predict = ''

if st.button('Jumlah Produksi'):
    predict = model.predict(
        [[LuasPanen,Curahhujan,Kelembapan,SuhuRataRata]]
    )
    st.write ('Estimasi jumlah Produksi Tanaman Padi Di Sumatera : ', predict)