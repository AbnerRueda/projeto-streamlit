import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, dt_nasc, tipo):
    if nome and dt_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{dt_nasc},{tipo}\n")
        st.session_state["Sucesso"] = True
    else:
        st.session_state["Sucesso"] = False

st.set_page_config(
    page_title="Cadastrado de Clientes",
    page_icon="💳"
)

st.title("Cadastrado de Clientes")
st.divider()

nome = st.text_input("Digite o Nome do Cliente",
                     key ="nome_cliente")

dt_nasc = st.date_input("Data de Nascimento", format="DD/MM/YYYY")

tipo = st.selectbox("Tipo de Cliente", 
                    ["Pessoa Física", "Pessoa Jurídica"])

btn_cadastrar = st.button("Cadastrar", 
                          on_click=gravar_dados(nome, dt_nasc, tipo))

if btn_cadastrar:
    if st.session_state["Sucesso"]:
        st.success("Cliente cadastrado com sucesso", 
                   icon="✅")
    else:
        st.error("Erro ao cadastrar cliente", 
                 icon="❌")
