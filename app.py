import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
df = pd.read_csv("data/main_data.csv")

# Judul dashboard
st.title("Dashboard Analisis Penyewaan Sepeda")

# Menampilkan informasi dataset
st.subheader("Informasi Dataset")
st.write(df.describe())  # Menampilkan statistik deskriptif

# Menampilkan grafik distribusi penyewaan berdasarkan musim
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Musim")
fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.boxplot(x="season", y="cnt_day", data=df, palette="coolwarm", ax=ax1)
ax1.set_xlabel("Musim")
ax1.set_ylabel("Jumlah Penyewaan")
ax1.set_title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig1)

# Menampilkan grafik distribusi penyewaan berdasarkan cuaca
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Cuaca")
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.boxplot(x="weathersit", y="cnt_day", data=df, palette="coolwarm", ax=ax2)
ax2.set_xlabel("Kondisi Cuaca")
ax2.set_ylabel("Jumlah Penyewaan")
ax2.set_title("Distribusi Penyewaan Sepeda Berdasarkan Cuaca")
st.pyplot(fig2)

# Menampilkan grafik penyewaan berdasarkan musim
st.subheader("Penyewaan Sepeda Berdasarkan Musim")
fig3, ax3 = plt.subplots(figsize=(12, 6))
season_group = df.groupby('season')['cnt_day'].sum().sort_values(ascending=False)
season_group.plot(kind="bar", ax=ax3, color=sns.color_palette("coolwarm", len(season_group)))
ax3.set_xlabel("Musim")
ax3.set_ylabel("Total Penyewaan")
ax3.set_title("Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig3)

# Menampilkan grafik penyewaan berdasarkan cuaca
st.subheader("Penyewaan Sepeda Berdasarkan Cuaca")
fig4, ax4 = plt.subplots(figsize=(12, 6))
weather_group = df.groupby('weathersit')['cnt_day'].sum().sort_values(ascending=False)
weather_group.plot(kind="bar", ax=ax4, color=sns.color_palette("coolwarm", len(weather_group)))
ax4.set_xlabel("Kondisi Cuaca")
ax4.set_ylabel("Total Penyewaan")
ax4.set_title("Penyewaan Sepeda Berdasarkan Cuaca")
st.pyplot(fig4)

# Menambahkan kategori penyewaan
st.subheader("Distribusi Kategori Penyewaan Sepeda")
df['rent_category'] = pd.cut(df['cnt_day'], bins=[0, 4000, 8000, 12000], labels=["Rendah", "Sedang", "Tinggi"])
fig5, ax5 = plt.subplots(figsize=(8, 6))
sns.countplot(x='rent_category', data=df, palette="viridis", ax=ax5)
ax5.set_xlabel("Kategori Penyewaan")
ax5.set_ylabel("Jumlah Hari")
ax5.set_title("Distribusi Kategori Penyewaan Sepeda")
st.pyplot(fig5)

# Menyediakan penjelasan analisis
st.subheader("Kesimpulan")
st.write("""
1. Penyewaan sepeda cenderung lebih tinggi pada musim-musim tertentu, terutama musim panas, dan lebih rendah saat musim dingin atau cuaca buruk seperti hujan.
2. Kondisi cuaca cerah berkontribusi terhadap peningkatan penyewaan sepeda, sementara cuaca buruk (seperti hujan atau salju) menyebabkan penurunan penyewaan secara signifikan.
3. Fluktuasi dalam jumlah penyewaan sepeda menunjukkan bahwa faktor eksternal seperti musim dan cuaca memainkan peran penting dalam permintaan sepeda.
""")
