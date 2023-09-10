import streamlit as st
import quiz as q
import json


sst = st.session_state

# Inicializa as variáveis que vamos compartilhar a cada rerun.
if 'corretas' not in sst:
    sst.corretas = 0

if 'perguntas' not in sst:
    sst.perguntas = []

if 'quiz' not in sst:
    sst.quiz = False

if 'preenchido' not in sst:
    sst.preenchido = False


# Define função que gera o quiz com n perguntas escolhidas aleatórias do arquivo json.
def gerar_quiz(n_perguntas=5):
    perguntas = q.quizGenerator(n_perguntas)
    sst.perguntas = perguntas
    sst.corretas = 0
    sst.quiz = True
    sst.preenchido = False


def resetar_quiz():
    sst.quiz = False
    sst.preenchido = False
    sst.corretas = 0


def verifica_alternativas():
    sst.corretas = 0
    for key in sst.keys():
        if "questao" in key:
            numero_questão = int(key.split("_")[1])
            if sst[key] == sst.perguntas[numero_questão - 1]["resposta_correta"]:
                sst.corretas += 1


def verifica_preenchimento():
    sst.questoes_preenchidas = 0
    sst.preenchido = False
    for key in sst.keys():
        if "questao" in key and sst[key] != "":
            sst.questoes_preenchidas += 1
    if sst.questoes_preenchidas == sst.n_perguntas:
        sst.preenchido = True
        verifica_alternativas()
    else:
        st.warning("Preencha todas as questões antes de submeter o quiz.")


st.title("Vamos treinar os conceitos sobre educação financeira!")
n_perguntas = st.number_input('Número de questões (Máx. 10)', 1, 10, value=5, on_change=resetar_quiz, key="n_perguntas")
gerar_novo_quiz = st.button("Gerar novo Quiz", on_click=gerar_quiz, args=(n_perguntas,), use_container_width=True)


if sst.quiz:
    ans = []
    mark = 0
    with st.form(key = "quiz_form"):
        for i, questao in enumerate(sst.perguntas):
            # Tonar a primeira label invisível para que o radio button não fique selecionado
            st.markdown(
                        """
                    <style>
                        div[role=radiogroup] label:first-of-type {
                            visibility: hidden;
                            height: 0px;
                        }
                    </style>
                    """,
                        unsafe_allow_html=True,
                    )
            st.radio(f'Q{i+1}: {questao["pergunta"]}', options=[""]+questao["alternativas"], key=f'questao_{i+1}')
        submitted = st.form_submit_button(label='Submit', on_click=verifica_preenchimento)
        if sst.preenchido:
            st.success(f"Você acertou {sst.corretas} de {sst.n_perguntas}.")

# Se quiser ver as variáveis guardadas a cada rerun é só descomentar a próxima linha
# sst
