import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page title
st.set_page_config(page_title="🎓 Education Data Explorer", layout="centered")
st.title("🎓 Education Dataset Explorer")
st.markdown("Explore, filter, and visualize the education dataset with ease.")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data/xAPI-Edu-Data.csv")  # Adjust filename if needed

df = load_data()

# Data preview
st.subheader("👀 Preview of the Dataset")
st.dataframe(df.head())

# Dataset shape and column info
st.markdown(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
if st.checkbox("📌 Show column names"):
    st.write(df.columns.tolist())

# Select column to explore
st.subheader("🔍 Column Analysis")
selected_col = st.selectbox("Select a column to analyze:", df.columns)

# Value counts or distribution
if df[selected_col].dtype == "object":
    st.markdown(f"### Value Counts for `{selected_col}`")
    st.write(df[selected_col].value_counts())
    
    fig, ax = plt.subplots()
    sns.countplot(data=df, x=selected_col, order=df[selected_col].value_counts().index, palette="viridis")
    plt.xticks(rotation=45)
    st.pyplot(fig)

else:
    st.markdown(f"### Distribution of `{selected_col}`")
    fig, ax = plt.subplots()
    sns.histplot(df[selected_col], kde=True, color="skyblue", bins=20)
    st.pyplot(fig)

# Summary stats
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# Footer
st.markdown("---")
