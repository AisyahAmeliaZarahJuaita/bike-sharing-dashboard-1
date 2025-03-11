import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt  

# Load dataset
day_df = pd.read_csv("data/day (1).csv")

# Konversi tanggal
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Mapping hari libur
day_df['holiday_label'] = day_df['holiday'].map({0: 'bukan hari libur', 1: 'hari libur'})

# Mapping musim
season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
day_df["season_label"] = day_df["season"].map(season_labels)

# Tambahkan kolom bulan dan tahun
day_df['month'] = day_df['dteday'].dt.month
day_df['year'] = day_df['dteday'].dt.year
bulan_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agt', 'Sep', 'Okt', 'Nov', 'Des']

# Sidebar untuk filter
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun", options=sorted(day_df['year'].unique()))
selected_month = st.sidebar.selectbox("Pilih Bulan", options=range(1, 13), format_func=lambda x: bulan_labels[x-1])
selected_season = st.sidebar.selectbox("Pilih Musim", options=season_labels.values())
selected_holiday = st.sidebar.radio("Tampilkan Data Hari Libur?", ['Semua', 'hari libur', 'bukan hari libur'])
selected_years_trend = st.sidebar.multiselect("Pilih Tahun untuk Tren", options=sorted(day_df['year'].unique()), default=[2011, 2012])

# Filter data
filtered_df = day_df[(day_df['year'] == selected_year) & (day_df['month'] == selected_month) & (day_df['season_label'] == selected_season)]
if selected_holiday != 'Semua':
    filtered_df = filtered_df[filtered_df['holiday_label'] == selected_holiday]

# --- UI Utama ---
st.title("Bike Sharing Dashboard")
st.markdown("### Analisis Data Penyewaan Sepeda")

# --- Tabs untuk Visualisasi ---
tabs = st.tabs(["Hari Libur", "Kelembapan", "Tren Tahunan"])

# --- 1. Pengaruh Hari Libur ---
with tabs[0]:
    st.markdown("Pengaruh Hari Libur terhadap Penyewaan Sepeda")
    avg_rentals = filtered_df.groupby('holiday_label')['cnt'].mean()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=avg_rentals.index, y=avg_rentals.values, ax=ax, palette="viridis")
    ax.set_title("Rata-rata Peminjaman Sepeda pada Hari Libur dan Hari Biasa")
    st.pyplot(fig)

# --- 2. Hubungan Kelembapan dengan Penyewaan ---
with tabs[1]:
    st.markdown("Pengaruh Kelembapan terhadap Peminjaman Sepeda")
    selected_humidity = st.slider("Pilih Rentang Kelembapan (%)", 0.0, 1.0, (0.2, 0.8))

    # Gunakan filtered_df agar menyesuaikan dengan pilihan filter lainnya
    hum_filtered_df = filtered_df[(filtered_df['hum'] >= selected_humidity[0]) & (filtered_df['hum'] <= selected_humidity[1])]
    
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(x=hum_filtered_df['hum'], y=hum_filtered_df['cnt'], alpha=0.5, color='blue', ax=ax)
    ax.set_title("Hubungan Kelembapan Udara terhadap Penyewaan Sepeda")
    st.pyplot(fig)

# --- 3. Tren Penggunaan Sepeda Sepanjang Tahun ---
with tabs[2]:
    st.markdown("Tren Penggunaan Sepeda Sepanjang Tahun")

    # Gunakan filtered_df agar menyesuaikan dengan pilihan filter lainnya
    trend_df = filtered_df[filtered_df['year'].isin(selected_years_trend)]
    trend_df = day_df[day_df["year"].isin(selected_years_trend)]
    chart = alt.Chart(trend_df).mark_line(point=True).encode(
        x=alt.X('month:O', title='Bulan', sort=list(range(1, 13)), axis=alt.Axis(labelAngle=0), scale=alt.Scale(zero=False)),
        y=alt.Y('mean(cnt):Q', title='Rata-rata Penyewaan Sepeda'),
        color='year:N',
        tooltip=['year', 'month', 'mean(cnt)']
    ).properties(width=800, height=400, title="Tren Penyewaan Sepeda Per Bulan")
    
    st.altair_chart(chart, use_container_width=True)

# --- Footer ---
st.markdown("*Dibuat oleh Aisyah Amelia Zarah Juaita | Data Analysis Project*")
