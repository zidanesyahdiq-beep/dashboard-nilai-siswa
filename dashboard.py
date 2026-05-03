import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login")
    st.write("Silakan login untuk masuk ke dashboard.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "kelompok 5" and password == "6767":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Username atau password salah")
    st.stop()

df = pd.read_csv('student-scores.csv')

st.sidebar.title("Filter Data")
st.sidebar.write("Filter data sesuai kebutuhan kamu.")

if 'gender' in df.columns:
    gender_options = ["Semua"] + df['gender'].unique().tolist()
    selected_gender = st.sidebar.selectbox("Filter Gender:", gender_options)
    if selected_gender != "Semua":
        df = df[df['gender'] == selected_gender]

if 'career_aspiration' in df.columns:
    career_options = ["Semua"] + df['career_aspiration'].unique().tolist()
    selected_career = st.sidebar.selectbox("Filter Career Aspiration:", career_options)
    if selected_career != "Semua":
        df = df[df['career_aspiration'] == selected_career]

st.title("Dashboard Nilai Siswa")
st.write("Dashboard ini dibuat untuk melihat dan menganalisis nilai siswa. Kamu bisa eksplorasi data, lihat distribusi nilai, sampai bandingkan antar mata pelajaran.")

st.write("---")

st.subheader("Data Awal")
st.write("Ini adalah isi dataset yang kita pakai. Scroll ke kanan kalau kolomnya banyak.")
st.dataframe(df.head())

st.write("---")

st.subheader("Missing Values")
st.write("Cek dulu apakah ada data yang kosong. Kalau ada yang kosong, bisa pengaruh ke hasil analisis nanti.")
st.write(df.isnull().sum())

st.write("---")

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

st.subheader("Distribusi Nilai")
st.write("Pilih mata pelajaran yang ingin kamu lihat. Histogram di bawah menunjukkan nilai siswa paling banyak ada di rentang mana.")
selected_col = st.selectbox("Pilih variabel:", numeric_cols)

fig1, ax1 = plt.subplots()
ax1.hist(df[selected_col], bins=10, edgecolor='green')
st.pyplot(fig1)

st.write("---")

st.subheader("Deteksi Outlier")
st.write(f"Di sini kita cek apakah ada nilai ekstrem pada {selected_col}. Caranya pakai metode IQR — nilai yang terlalu jauh dari rata-rata dianggap outlier. Boxplot kiri sebelum dihapus, kanan sesudah.")
Q1 = df[selected_col].quantile(0.25)
Q3 = df[selected_col].quantile(0.75)
IQR = Q3 - Q1
filtered = df[(df[selected_col] >= Q1 - 1.5*IQR) & (df[selected_col] <= Q3 + 1.5*IQR)]
fig2, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10, 5))
sns.boxplot(x=df[selected_col], ax=ax_a)
ax_a.set_title('Sebelum')
sns.boxplot(x=filtered[selected_col], ax=ax_b)
ax_b.set_title('Sesudah')
st.pyplot(fig2)

st.write("---")

st.subheader("Transformasi Log")
st.write(f"Kalau datanya miring ke satu sisi, transformasi log bisa bikin distribusinya lebih simetris. Ini perbandingan {selected_col} sebelum dan sesudah ditransformasi.")
df[selected_col + '_log'] = np.log1p(df[selected_col])
fig3, (ax_c, ax_d) = plt.subplots(1, 2, figsize=(10, 5))
sns.histplot(df[selected_col], kde=True, ax=ax_c)
ax_c.set_title('Sebelum Transformasi')
sns.histplot(df[selected_col + '_log'], kde=True, ax=ax_d)
ax_d.set_title('Sesudah Transformasi')
st.pyplot(fig3)

st.write("---")

st.subheader("Perbandingan Dua Mata Pelajaran")
st.write("Pilih dua mata pelajaran dan lihat perbandingan nilainya lewat boxplot. Bisa keliatan mana yang nilainya lebih tinggi atau lebih merata.")
col_1 = st.selectbox("Pilih mapel pertama:", numeric_cols, key="col1")
col_2 = st.selectbox("Pilih mapel kedua:", numeric_cols, key="col2")
fig4, ax4 = plt.subplots()
sns.boxplot(data=df[[col_1, col_2]], ax=ax4)
st.pyplot(fig4)import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login")
    st.write("Silakan login untuk masuk ke dashboard.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "kelompok 5" and password == "6767":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Username atau password salah")
    st.stop()

df = pd.read_csv('student-scores.csv')

st.sidebar.title("Filter Data")
st.sidebar.write("Filter data sesuai kebutuhan kamu.")

if 'gender' in df.columns:
    gender_options = ["Semua"] + df['gender'].unique().tolist()
    selected_gender = st.sidebar.selectbox("Filter Gender:", gender_options)
    if selected_gender != "Semua":
        df = df[df['gender'] == selected_gender]

if 'career_aspiration' in df.columns:
    career_options = ["Semua"] + df['career_aspiration'].unique().tolist()
    selected_career = st.sidebar.selectbox("Filter Career Aspiration:", career_options)
    if selected_career != "Semua":
        df = df[df['career_aspiration'] == selected_career]

st.title("Dashboard Nilai Siswa")
st.write("Dashboard ini dibuat untuk melihat dan menganalisis nilai siswa. Kamu bisa eksplorasi data, lihat distribusi nilai, sampai bandingkan antar mata pelajaran.")

st.write("---")

st.subheader("Data Awal")
st.write("Ini adalah isi dataset yang kita pakai. Scroll ke kanan kalau kolomnya banyak.")
st.dataframe(df.head())

st.write("---")

st.subheader("Missing Values")
st.write("Cek dulu apakah ada data yang kosong. Kalau ada yang kosong, bisa pengaruh ke hasil analisis nanti.")
st.write(df.isnull().sum())

st.write("---")

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

st.subheader("Distribusi Nilai")
st.write("Pilih mata pelajaran yang ingin kamu lihat. Histogram di bawah menunjukkan nilai siswa paling banyak ada di rentang mana.")
selected_col = st.selectbox("Pilih variabel:", numeric_cols)

fig1, ax1 = plt.subplots()
ax1.hist(df[selected_col], bins=10, edgecolor='green')
st.pyplot(fig1)

st.write("---")

st.subheader("Deteksi Outlier")
st.write(f"Di sini kita cek apakah ada nilai ekstrem pada {selected_col}. Caranya pakai metode IQR — nilai yang terlalu jauh dari rata-rata dianggap outlier. Boxplot kiri sebelum dihapus, kanan sesudah.")
Q1 = df[selected_col].quantile(0.25)
Q3 = df[selected_col].quantile(0.75)
IQR = Q3 - Q1
filtered = df[(df[selected_col] >= Q1 - 1.5*IQR) & (df[selected_col] <= Q3 + 1.5*IQR)]
fig2, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10, 5))
sns.boxplot(x=df[selected_col], ax=ax_a)
ax_a.set_title('Sebelum')
sns.boxplot(x=filtered[selected_col], ax=ax_b)
ax_b.set_title('Sesudah')
st.pyplot(fig2)

st.write("---")

st.subheader("Transformasi Log")
st.write(f"Kalau datanya miring ke satu sisi, transformasi log bisa bikin distribusinya lebih simetris. Ini perbandingan {selected_col} sebelum dan sesudah ditransformasi.")
df[selected_col + '_log'] = np.log1p(df[selected_col])
fig3, (ax_c, ax_d) = plt.subplots(1, 2, figsize=(10, 5))
sns.histplot(df[selected_col], kde=True, ax=ax_c)
ax_c.set_title('Sebelum Transformasi')
sns.histplot(df[selected_col + '_log'], kde=True, ax=ax_d)
ax_d.set_title('Sesudah Transformasi')
st.pyplot(fig3)

st.write("---")

st.subheader("Perbandingan Dua Mata Pelajaran")
st.write("Pilih dua mata pelajaran dan lihat perbandingan nilainya lewat boxplot. Bisa keliatan mana yang nilainya lebih tinggi atau lebih merata.")
col_1 = st.selectbox("Pilih mapel pertama:", numeric_cols, key="col1")
col_2 = st.selectbox("Pilih mapel kedua:", numeric_cols, key="col2")
fig4, ax4 = plt.subplots()
sns.boxplot(data=df[[col_1, col_2]], ax=ax4)
st.pyplot(fig4)
