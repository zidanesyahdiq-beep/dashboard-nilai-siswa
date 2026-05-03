import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("")
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

st.write("Data Awal:")
st.dataframe(df.head())

st.write("Missing Values:")
st.write(df.isnull().sum())

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
selected_col = st.selectbox("Pilih variabel:", numeric_cols)

st.write(f"Distribusi Nilai {selected_col}:")
fig1, ax1 = plt.subplots()
ax1.hist(df[selected_col], bins=10, edgecolor='green')
st.pyplot(fig1)

st.write("Boxplot Sebelum vs Sesudah Filter Outlier:")
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

st.write("Transformasi Log:")
df[selected_col + '_log'] = np.log1p(df[selected_col])
fig3, (ax_c, ax_d) = plt.subplots(1, 2, figsize=(10, 5))
sns.histplot(df[selected_col], kde=True, ax=ax_c)
sns.histplot(df[selected_col + '_log'], kde=True, ax=ax_d)
st.pyplot(fig3)

st.write("Perbandingan Nilai:")
col_1 = st.selectbox("Pilih mapel pertama:", numeric_cols, key="col1")
col_2 = st.selectbox("Pilih mapel kedua:", numeric_cols, key="col2")
fig4, ax4 = plt.subplots()
sns.boxplot(data=df[[col_1, col_2]], ax=ax4)
st.pyplot(fig4)
