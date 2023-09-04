import streamlit as st
import quiz as q

# Para gerar a lista com 5 perguntas aleatórias sortidas do perguntas.json, se não clicar não vai ter perguntas para serem renderizadas.
# Se clicar de novo um novo quiz com 5 perguntas vai ser escolhido.
def gerar_quiz():
    perguntas = q.quizGenerator()
    st.session_state.perguntas = perguntas
    return


st.title("Quiz")
st.subheader("Vamos treinar os conceitos sobre educação financeira!")


# Chama a função que gera o quiz
gerar_novo_quiz = st.button("Gerar novo Quiz", on_click=gerar_quiz)


# Define o tamanho que os botões de selecionar questão e botões das alternativas vai ocupar.
coluna1, coluna2 = st.columns([1,9])


# Gera os botões para selecionar qual pergunta vai ser renderizada.
# O streamlit vai guardar o estado de cada botão com a variavel nomeada da seguinte forma, ex.: botao1 pro primeiro botao.
with coluna1:
    buttons = [st.button(f'{i+1}', key=f"botao{i+1}") for i in range(5)]


# a função clicou por enquanto tá fazendo nada, o próximo passo seria conseguir validar se
# o botao clicado corresponde a alternativa correta.
def clicou(texto):
    print(alternativa)


# Aqui a ideia é criar os botões com as alternativas, ele também vai renderizar as alternativas de acordo com o estado
# do botão que tiver sido selecionado, veja que no começo ele não renderiza nenhuma questão, porque nenhum botão tá com
# o estado true, assim que clicarmos em um botão ele vai ter o estado true e vai renderizar as alternativas da questão.
with coluna2:
    for n in range(1,6):
        atributo = "botao" + f"{n}"
        if st.session_state[f"{atributo}"] == True:
            st.write(st.session_state.perguntas[int(f"{n-1}")]["pergunta"])
            for alternativa in st.session_state.perguntas[int(f"{n-1}")]["alternativas"]:
                st.button(alternativa, use_container_width=True, key=alternativa, on_click=clicou(alternativa))


# Se quiser ver as variáveis guardadas a cada rerun é só descomentar a próxima linha
# st.session_state