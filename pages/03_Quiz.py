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


# Define função que gera o quiz com n perguntas escolhidas aleatórias do arquivo json.
def gerar_quiz(n_perguntas=5):
    perguntas = q.quizGenerator(n_perguntas)
    sst.perguntas = perguntas
    sst.corretas = 0
    sst.quiz = True
    return


def resetar_quiz():
    sst.quiz = False
    sst.corretas = 0


def verifica_alternativa():
    for item in sst.items():
        if item[1] and item[0] == sst.perguntas[int(sst.questao_atual) - 1]["resposta_correta"]:
            sst.corretas += 1


def renderiza_questao(n):
    st.subheader(sst.perguntas[int(f"{n-1}")]["pergunta"])
    for alternativa in sst.perguntas[int(f"{n-1}")]["alternativas"]:
        st.button(alternativa, use_container_width=True, key=alternativa, on_click=verifica_alternativa)


st.title("Vamos treinar os conceitos sobre educação financeira!")
col1, col2 = st.columns(2)
with col1:
    n_perguntas = st.number_input('Número de questões (Máx. 10)', 1, 10, on_change=resetar_quiz)
    gerar_novo_quiz = st.button("Gerar novo Quiz", on_click=gerar_quiz, args=(n_perguntas,), use_container_width=True)
with col2:
    st.write(f'Questões corretas: {sst.corretas}')


if sst.quiz:
    botoes = st.columns(n_perguntas)
    for indice_botao in range(len(botoes)):
        with botoes[indice_botao]:
            st.button(f'{indice_botao+1}', key=f"botao{indice_botao+1}", use_container_width=True)


    for numero_questao in range(1,len(botoes)+1):
        atributo = "botao" + f"{numero_questao}"
        if sst[f"{atributo}"] == True:
            sst.questao_atual = numero_questao

if sst.quiz:
    renderiza_questao(sst.questao_atual)

# Se quiser ver as variáveis guardadas a cada rerun é só descomentar a próxima linha
# sst
