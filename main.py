import streamlit as st  
import numpy as np 
import pandas as pd
import altair as alt

st.set_page_config(page_title="PiJunior")

st.header("PRECIFICAÇÃO PIJUNIOR")   

st.subheader("BASE")

nome_do_projeto = st.text_input("Qual o nome do projeto ?")
st.markdown("<br>", unsafe_allow_html=True)

tipos_de_projetos = ["Automação de Planilhas", "Visualização de Dados", "WebScraping", "Software Empresarial", ""]
projetos_selecionados = st.multiselect("Escolha os tipos de projeto", tipos_de_projetos, default="")

preco_total = 0

for projeto in projetos_selecionados:
    if projeto == "Automação de Planilhas":
        preco_total += 450
    elif projeto == "Visualização de Dados":
        preco_total += 500
    elif projeto == "WebScraping":
        preco_total += 300
    elif projeto == "Software Empresarial":
        preco_total += 700

#st.write(f"Preço total dos projetos selecionados: R${preco_total}") 
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Coeficientes")

with st.form('Coeficientes'):

    numero_de_pessoas = st.number_input("Número de pessoas para realizar o projeto", min_value=1, max_value=100, value=1,step=1)
    semanas_previstas = st.number_input("Semanas previstas", min_value=1.0, max_value=100.0, value=1.0, step=0.5)
    horas_membros = st.number_input("Horas semanais por membros", min_value=1, max_value=100, value=1,step=1)
    dificuldade_do_projeto = st.select_slider("Dificuldade do Projeto", ['Muito Fácil','Fácil', 'Mediano', 'Difícil', 'Muito Difícil'])
    cliente_premium = st.checkbox("O cliente é premium ?")
    if cliente_premium:
        premium = 0.5 
    else:
        premium = 1    
    custo = 18.84
    valor_pela_dificuldade = 0 

    if dificuldade_do_projeto == "Muito Fácil":
        valor_pela_dificuldade = 1
    elif dificuldade_do_projeto == "Fácil":
        valor_pela_dificuldade = 2 
    elif dificuldade_do_projeto == "Mediano":
        valor_pela_dificuldade = 3 
    elif dificuldade_do_projeto == "Difícil":
        valor_pela_dificuldade = 4 
    elif dificuldade_do_projeto == "Muito Difícil":
        valor_pela_dificuldade = 5

    resultado = preco_total + (valor_pela_dificuldade * numero_de_pessoas * semanas_previstas * horas_membros * custo) * premium

    calcular = st.form_submit_button('CALCULAR ')
    if calcular:
        st.write(f"Custo Total do Projeto: R${resultado:.2f}")

