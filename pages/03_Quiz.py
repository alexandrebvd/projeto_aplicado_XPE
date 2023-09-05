import streamlit as st
import quiz as q


sst = st.session_state

# Inicializa as variáveis que vamos compartilhar a cada rerun.
if 'corretas' not in sst:
    sst.corretas = 0

if 'perguntas' not in sst:
    sst.perguntas = []

if 'questao_atual' not in sst:
    sst.questao_atual = 1

if 'quiz' not in sst:
    sst.quiz = False


# Define função que gera o quiz com 5 perguntas escolhidas aleatórias do arquivo json.
def gerar_quiz():
    perguntas = q.quizGenerator()
    sst.perguntas = perguntas
    sst.corretas = 0
    sst.quiz = True
    return


def verifica_alternativa():
    for item in sst.items():
        if item[1] and item[0] == sst.perguntas[int(sst.questao_atual) - 1]["resposta_correta"]:
            sst.corretas += 1


def renderiza_questao(n):
    st.subheader(sst.perguntas[int(f"{n-1}")]["pergunta"])
    for alternativa in sst.perguntas[int(f"{n-1}")]["alternativas"]:
        st.button(alternativa, use_container_width=True, key=alternativa, on_click=verifica_alternativa)


st.subheader("Vamos treinar os conceitos sobre educação financeira!")
col1, col2, col3 = st.columns(3)
with col1:
    st.title("Quiz")
with col2:
    st.write('Questões corretas: ', sst.corretas)
with col3:
    gerar_novo_quiz = st.button("Gerar novo Quiz", on_click=gerar_quiz)


if sst.quiz:
    botoes = st.columns(5)
    for indice_botao in range(len(botoes)):
        with botoes[indice_botao]:
            st.button(f'{indice_botao+1}', key=f"botao{indice_botao+1}", use_container_width=True)


    for numero_questao in range(1,6):
        atributo = "botao" + f"{numero_questao}"
        if sst[f"{atributo}"] == True:
            sst.questao_atual = numero_questao

if sst.quiz:
    renderiza_questao(sst.questao_atual)

# Se quiser ver as variáveis guardadas a cada rerun é só descomentar a próxima linha
# sst
