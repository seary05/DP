import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Gathering Data
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Cleaning Data
datetime_columns =["dteday"]

for column in datetime_columns:
  day_df[column] = pd.to_datetime(day_df[column])
  
datetime_columns = ["dteday"]

for column in datetime_columns:
  hour_df[column] = pd.to_datetime(hour_df[column])
  
day_df = day_df.drop(['temp','atemp','hum','windspeed'], axis=1)
day_df.head()

hour_df = hour_df.drop(['temp','atemp','hum','windspeed'], axis=1)
hour_df.head()

# HEADER
st.title('Analisis Data Bike Sharing')

st.header('Tabel Data Keseluruhan dalam hitungan per hari')
st.dataframe(day_df)

st.header('Tabel Data Keseluruhan dalam hitungan per jam')
st.dataframe(hour_df)
  
# Visualization Data
# DATA 1
st.header('Perkembangan Peminjaman sepeda \nperiode 2011-2012')
perkembangan_df = day_df.resample(rule='M', on= 'dteday').agg({
        "instant": "nunique",
        "cnt": "sum"
})
perkembangan_df.index = perkembangan_df.index.strftime('%x')
     
perkembangan_df = perkembangan_df.reset_index()
perkembangan_df.rename(columns={
    "instant": "hari",
    "cnt": "jumlah_user",
}, inplace=True)

fig1 = plt.figure(figsize=(1, 5)) 
plt.plot(perkembangan_df["dteday"], perkembangan_df["jumlah_user"], marker='o', linewidth=2, color="#72BCD4")
plt.title("Perkembangan peminjaman sepeda \nperiode 2011-2012", loc="center", fontsize=20) 
plt.xticks(fontsize=9, rotation= 30) 
plt.yticks(fontsize=10) 

st.plotly_chart(fig1, use_container_width=True)

# DATA 2
st.header('Jumlah Peminjam Berdasarkan Jam')

pengaruh_jam = hour_df.groupby("hr").cnt.sum().sort_values(ascending=True).reset_index()

fig2, ax = plt.subplots(figsize=(1, 5))
 
sns.barplot(x="hr", y="cnt", data=pengaruh_jam.head(24))
ax.set_ylabel('Jumlah Pengguna')
ax.set_xlabel('Jam')
ax.tick_params(axis ='y', labelsize=12)
 
plt.suptitle("Banyaknya Jumlah Peminjam \n Berdasarkan Jam", fontsize=30)

st.plotly_chart(fig2, use_container_width=True)

# DATA 3
st.header('Jumlah Peminjam Berdasarkan Hari')

pengaruh_hari = day_df.groupby("weekday").cnt.sum().sort_values(ascending=True).reset_index()
fig3, ax = plt.subplots( figsize=(1, 5))
 
sns.barplot(x="weekday", y="cnt", data=pengaruh_hari)
ax.set_ylabel('Jumlah Pengguna')
ax.set_xlabel('Hari', fontsize = 10)
ax.tick_params(axis ='y', labelsize=12)

plt.ylim(400000)
plt.suptitle("Banyaknya Jumlah Peminjam \n Berdasarkan Hari", fontsize=30)

st.plotly_chart(fig3, use_container_width=True)
st.caption("""
           Hari:
- 0: Minggu
- 1: Senin
- 2: Selasa
- 3: Rabu
- 4: Kamis
- 5: Jumat
- 6: Sabtu
""")

# DATA 4
st.header('Jumlah Peminjam Berdasarkan Bulan')

pengaruh_bulan = hour_df.groupby("mnth").cnt.sum().sort_values(ascending=True).reset_index()

fig4, ax = plt.subplots( figsize=(1, 5))
 
sns.barplot(x="mnth", y="cnt", data=pengaruh_bulan.head(24))
ax.set_ylabel("Jumlah Pengguna")
ax.set_xlabel('Bulan')
ax.tick_params(axis ='y', labelsize=12)
 
plt.suptitle("Banyaknya Jumlah Peminjam \n Berdasarkan Bulan", fontsize=30)

st.plotly_chart(fig4, use_container_width=True)
st.caption('''
        Bulan = 
- 1 : Januari
- 2 : Februari
- 3 : Maret
- 4 : April
- 5 : Mei
- 6 : Juni
- 7 : Juli
- 8 : Agustus
- 9 : September
- 10 : Oktober
- 11 : November
- 12 : Desember
        ''')

# DATA 5
st.header('Jumlah Peminjam Berdasarkan Musim')

pengaruh_musim = day_df.groupby("season").cnt.sum().sort_values(ascending=True).reset_index()

fig5, ax = plt.subplots( figsize=(1, 5))
 
sns.barplot(x="season", y="cnt", data=pengaruh_musim.head())
ax.set_ylabel('Jumlah Pengguna (Juta Orang)')
ax.set_xlabel('Musim')

ax.tick_params(axis ='y', labelsize=12)
 
plt.suptitle("Banyaknya Jumlah Peminjam \n Berdasarkan Musim", fontsize=30)
plt.ylim(400000, 1200000)

st.plotly_chart(fig5, use_container_width=True)
st.caption("""
           Musim :
- 1 : Musim Semi
- 2 : Musim Panas
- 3 : Musim Gugur
- 4 : Musim Dingin
""")

# DATA 6
st.header('Jumlah Peminjam Berdasarkan Cuaca')

pengaruh_cuaca = hour_df.groupby("weathersit").cnt.sum().sort_values(ascending=True).reset_index()

fig6, ax = plt.subplots(figsize=(1, 5))
 
sns.barplot(x="weathersit", y="cnt", data=pengaruh_cuaca.head())
ax.set_ylabel('Jumlah Pengguna')
ax.set_xlabel('Musim')
ax.tick_params(axis ='y', labelsize=12)

plt.suptitle("Banyaknya Jumlah Peminjam \n Berdasarkan Cuaca", fontsize=30)

st.plotly_chart(fig6, use_container_width=True)
st.caption("""
           Cuaca : 
- 1: Cerah, Sebagian Berawan, Sebagian Berawan
- 2: Kabut + Berawan, Kabut + Sedikit Berawan, Kabut + Berawan, Kabut
- 3: Hujan Salju Ringan, Hujan Ringan + Hujan Badai + Cukup Berawan, Hujan Ringan + Cukup Berawan
- 4: Hujan Besar + Hujan Es + Hujan Badai + Kabut, Salju + Embun
  """)

# DATA 7
st.header('Perbandingan Peminjam pada Hari Kerja dan Hari Libur')

pengaruh_hari_kerja = pd.DataFrame([['Masuk',2292410],['Libur', 1000269]],columns=['hari_kerja','jumlah'])

fig7 = px.pie(pengaruh_hari_kerja, names='hari_kerja', values='jumlah')
fig7.update_traces(textinfo='percent + value')
fig7.update_layout(title_text='Perbandingan Peminjam saat Hari Kerja dan Hari Libur')
st.plotly_chart(fig7, use_container_width=True)

# DATA 8
st.header('Perbandingan Peminjam Terdaftar dan Peminjam Kasual')

perbandingan_peminjam = pd.DataFrame([['Terdaftar', 2672662],['Kasual',620017]], columns=['jenis_peminjam', 'jumlah'])

fig8 = px.pie(perbandingan_peminjam, names='jenis_peminjam', values='jumlah')
fig8.update_traces(textinfo='percent + value')
fig8.update_layout(title_text='Perbandingan Peminjam Kasual dan Terdaftar')
st.plotly_chart(fig8, use_container_width=True)
