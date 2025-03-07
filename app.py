import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    df_day = pd.read_csv("D:\submission\data\day.csv")
    df_hour = pd.read_csv("D:\submission\data\hour.csv")
    return df_day, df_hour

df_day, df_hour = load_data()

# Title
st.title("📊 Dashboard Analisis Penyewaan Sepeda")

# Sidebar Filter
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
selected_season = st.sidebar.selectbox("Pilih Musim", list(season_mapping.values()))

# Konversi nama musim ke angka
selected_season_num = list(season_mapping.keys())[list(season_mapping.values()).index(selected_season)]

# 1️⃣ Visualisasi: Pola Penyewaan Berdasarkan Musim
st.subheader("Pola Penyewaan Sepeda Berdasarkan Musim")
season_data = df_day[df_day['season'] == selected_season_num]
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='season', y='cnt', data=season_data, palette="Blues", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Penyewaan")
ax.set_title(f"Penyewaan Sepeda Selama {selected_season}")
st.pyplot(fig)

# 2️⃣ Visualisasi: Tren Penyewaan Sepeda per Jam
st.subheader("Tren Penyewaan Sepeda per Jam")
df_hour_grouped = df_hour.groupby('hr')['cnt'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='hr', y='cnt', data=df_hour_grouped, marker='o', color="blue", ax=ax)
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_title("Rata-rata Penyewaan Sepeda per Jam")
st.pyplot(fig)

# Insight
st.markdown("### 🔍 Insight")
st.markdown("""
1. **Penyewaan sepeda memiliki pola musiman** – Pada musim panas dan gugur, jumlah penyewaan lebih tinggi dibandingkan musim lainnya.
2. **Pola waktu harian menunjukkan lonjakan pada jam sibuk** – Penyewaan sepeda meningkat signifikan pada pagi (07:00-09:00) dan sore (17:00-19:00), kemungkinan karena jam kerja dan pulang kantor.
""")
