import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
df = pd.read_csv("D:\submission\dashboard\main_data.csv")

# Judul Dashboard
st.title("Dashboard Penyewaan Sepeda")
st.write("Analisis data penyewaan sepeda berdasarkan musim dan waktu.")

# Menampilkan data awal
st.subheader("Data Awal")
st.write(df.head())

# Statistik Deskriptif
st.subheader("Statistik Deskriptif")
st.write(df.describe())

# Visualisasi: Distribusi Penyewaan Sepeda Berdasarkan Musim
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Musim")
plt.figure(figsize=(8, 5))
sns.barplot(x='season', y='cnt_day', data=df, palette="Blues")
plt.xlabel("Musim")
plt.ylabel("Total Penyewaan")
plt.title("Pola Penyewaan Sepeda Berdasarkan Musim")
st.pyplot()

# Visualisasi: Korelasi Antar Fitur
st.subheader("Korelasi Antar Fitur")

# Menghapus kolom non-numerik sebelum menghitung korelasi
numeric_df = df.select_dtypes(include=['number'])  # Hanya memilih kolom numerik
correlation_matrix = numeric_df.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Korelasi Antar Fitur")
st.pyplot()

# Pilihan interaktif untuk filter data berdasarkan musim
st.subheader("Filter Data Berdasarkan Musim")
season_filter = st.selectbox("Pilih Musim", df['season'].unique())
filtered_df = df[df['season'] == season_filter]
st.write(f"Data Penyewaan Sepeda untuk Musim {season_filter}", filtered_df)