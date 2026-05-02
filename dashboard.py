import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('student-scores.csv')

st.title("Dashboard Nilai Siswa")

st.write("Data Awal:")
st.dataframe(df.head())

st.write("Missing Values:")
st.write(df.isnull().sum())

st.write("Distribusi Nilai English:")
fig1, ax1 = plt.subplots()
ax1.hist(df['english_score'], bins=10, edgecolor='green')
st.pyplot(fig1)

st.write("Boxplot Sebelum vs Sesudah Filter Outlier:")
Q1 = df['english_score'].quantile(0.25)
Q3 = df['english_score'].quantile(0.75)
IQR = Q3 - Q1
filtered = df[(df['english_score'] >= Q1 - 1.5*IQR) & (df['english_score'] <= Q3 + 1.5*IQR)]

fig2, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(10, 5))
sns.boxplot(x=df['english_score'], ax=ax_a)
ax_a.set_title('Sebelum')
sns.boxplot(x=filtered['english_score'], ax=ax_b)
ax_b.set_title('Sesudah')
st.pyplot(fig2)

st.write("Transformasi Log:")
df['english_score_log'] = np.log1p(df['english_score'])
fig3, (ax_c, ax_d) = plt.subplots(1, 2, figsize=(10, 5))
sns.histplot(df['english_score'], kde=True, ax=ax_c)
sns.histplot(df['english_score_log'], kde=True, ax=ax_d)
st.pyplot(fig3)

st.write("Perbandingan Nilai:")
fig4, ax4 = plt.subplots()
sns.boxplot(data=df[['english_score', 'math_score']], ax=ax4)
st.pyplot(fig4)
