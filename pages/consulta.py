import streamlit as st
import pandas as pd

dados = pd.read_csv("clientes.csv")

st.title("Clientes Cadastrados")
st.divider() # cria uma linha na página

st.dataframe(dados)