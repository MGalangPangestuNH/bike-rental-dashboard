import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("data/main_data.csv")

# Konversi ke tipe data yang sesuai
df['dteday'] = pd.to_datetime(df['dteday'])

# Sidebar
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim", ["Semua", "1 - Spring", "2 - Summer", "3 - Fall", "4 - Winter"])
if selected_season != "Semua":
    season_map = {"1 - Spring": 1, "2 - Summer": 2, "3 - Fall": 3, "4 - Winter": 4}
    df = df[df['season'] == season_map[selected_season]]

# Judul utama
st.title("Dashboard Bike Sharing Dataset")
st.write("Dashboard ini menampilkan analisis terhadap data penyewaan sepeda berdasarkan faktor-faktor utama seperti musim, cuaca, dan suhu.")

# 1. Visualisasi Korelasi Variabel
st.header("Korelasi antara Variabel dengan Jumlah Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df[['temp_daily', 'hum_daily', 'windspeed_daily', 'cnt_daily']].corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)
st.write("Insight: Suhu memiliki korelasi positif terhadap jumlah penyewaan sepeda, sedangkan kelembaban dan kecepatan angin memiliki korelasi negatif.")

# 2. Hubungan antara Suhu dan Penyewaan Sepeda
st.header("Hubungan Suhu dan Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 6))
sns.regplot(x='temp_daily', y='cnt_daily', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'}, ax=ax)
st.pyplot(fig)
st.write("Insight: Penyewaan sepeda meningkat seiring dengan kenaikan suhu, menunjukkan bahwa pengguna lebih aktif saat cuaca lebih hangat.")

# 3. Distribusi Penyewaan Sepeda Berdasarkan Musim
st.header("Distribusi Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='season', y='cnt_daily', data=df, palette='coolwarm', ax=ax)
ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig)
st.write("Insight: Penyewaan sepeda lebih tinggi pada musim panas dan gugur dibandingkan musim lainnya.")

# 4. Tren Jumlah Penyewaan Sepeda per Bulan
st.header("Tren Jumlah Penyewaan Sepeda per Bulan")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='mnth', y='cnt_daily', data=df, estimator='mean', ci=None, marker='o', color='b', ax=ax)
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig)
st.write("Insight: Penyewaan sepeda cenderung meningkat selama pertengahan tahun dan menurun pada bulan-bulan dingin.")

# 5. Penyewaan Sepeda Berdasarkan Kondisi Cuaca
st.header("Distribusi Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(x='weathersit', y='cnt_daily', data=df, palette='viridis', ax=ax)
ax.set_xticklabels(['Clear', 'Cloudy', 'Light Rain/Snow', 'Heavy Rain/Snow'])
st.pyplot(fig)
st.write("Insight: Penyewaan sepeda lebih tinggi saat cuaca cerah dan berkurang drastis saat hujan atau salju.")

# Kesimpulan
st.header("Kesimpulan")
st.markdown("""
- **Faktor utama yang memengaruhi penyewaan sepeda adalah suhu udara**, di mana suhu yang lebih tinggi meningkatkan penyewaan.
- **Penyewaan sepeda berfluktuasi berdasarkan musim dan cuaca**. Penyewaan tertinggi terjadi di musim panas dan berkurang di musim dingin atau saat cuaca buruk.
- Penyedia layanan dapat **menyesuaikan operasional dan strategi pemasaran** dengan meningkatkan ketersediaan sepeda di bulan-bulan dengan permintaan tinggi.
""")
