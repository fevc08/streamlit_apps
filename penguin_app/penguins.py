import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns

st.title("Palmer's Penguins")
# Import the dataset
penguins_df = pd.read_csv('penguins.csv')
st.write(penguins_df.head())