# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:35:34 2024

@author: HP
"""

# Step 2: Import semua packages/library yang digunakan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Mengatur konfigurasi dasar untuk plot
sns.set(style="whitegrid")

# Step 1: Menentukan pertanyaan bisnis di bagian Streamlit
st.title('Analisis Polusi Udara di Shunyi (2013 - 2017)')

# Pertanyaan bisnis:
st.markdown("""
### Pertanyaan Bisnis:
1. Apakah ada tren penurunan atau peningkatan pada tingkat polusi udara (PM2.5) di wilayah Shunyi dalam kurun waktu 2013 hingga 2017?
2. Faktor meteorologis apa yang paling berpengaruh terhadap tingkat polusi udara (PM2.5)?
""")

# Step 3: Data Wrangling

# a. Gathering Data
data_path = 'C:/Users/HP/Downloads/PRSA_Data_20130301-20170228/PRSA_Data_Shunyi_20130301-20170228.csv'
data = pd.read_csv(data_path)

# b. Cleaning Data
data.fillna(method='ffill', inplace=True)
data['datetime'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])
data.set_index('datetime', inplace=True)
data.drop(columns=['year', 'month', 'day', 'hour', 'No'], inplace=True)

# Step 4: Exploratory Data Analysis (EDA)

# Sidebar untuk memilih jenis analisis
analysis_type = st.sidebar.selectbox(
    "Pilih Analisis:",
    ['Distribusi PM2.5', 'Tren PM2.5 dari Waktu ke Waktu', 'Hubungan PM2.5 dengan Faktor Meteorologis']
)

# Step 5: Visualization & Explanatory Analysis

# Visualisasi Pertanyaan 1: Distribusi PM2.5
if analysis_type == 'Distribusi PM2.5':
    st.subheader('Distribusi PM2.5 di Shunyi')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data['PM2.5'], kde=True, ax=ax)
    ax.set_title('Distribusi PM2.5')
    ax.set_xlabel('PM2.5')
    st.pyplot(fig)

# Visualisasi Pertanyaan 1: Tren PM2.5 dari waktu ke waktu
elif analysis_type == 'Tren PM2.5 dari Waktu ke Waktu':
    st.subheader('Tren PM2.5 dari Waktu ke Waktu')
    fig, ax = plt.subplots(figsize=(14, 7))
    data['PM2.5'].resample('M').mean().plot(ax=ax)
    ax.set_title('Tren Polusi PM2.5 di Shunyi (2013 - 2017)')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Konsentrasi PM2.5')
    st.pyplot(fig)

# Visualisasi Pertanyaan 2: Hubungan antara PM2.5 dengan faktor meteorologis
elif analysis_type == 'Hubungan PM2.5 dengan Faktor Meteorologis':
    st.subheader('Hubungan Antara PM2.5 dengan Faktor Meteorologis')
    faktor_meteorologis = st.sidebar.selectbox(
        "Pilih Faktor Meteorologis:",
        ['TEMP', 'DEWP', 'PRES', 'WSPM']
    )

    fig, ax = plt.subplots(figsize=(14, 7))
    sns.scatterplot(x=faktor_meteorologis, y='PM2.5', data=data, alpha=0.5, ax=ax)
    ax.set_title(f'Hubungan Antara {faktor_meteorologis} dan PM2.5')
    ax.set_xlabel(faktor_meteorologis)
    ax.set_ylabel('PM2.5')
    st.pyplot(fig)

# Step 7: Konklusi
st.subheader("Kesimpulan")
st.markdown("""
**Pertanyaan 1:**
Berdasarkan analisis tren, tingkat polusi udara (PM2.5) di wilayah Shunyi mengalami fluktuasi dengan pola peningkatan yang jelas selama musim dingin.

**Pertanyaan 2:**
Faktor meteorologi yang paling berpengaruh terhadap tingkat polusi udara adalah temperatur (TEMP) dan titik embun (DEWP), dengan korelasi yang kuat terhadap konsentrasi PM2.5.
""")
