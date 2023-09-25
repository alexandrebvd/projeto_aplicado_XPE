import streamlit as st
import quiz as q
from PIL import Image
from styles import dark, light

img = Image.open('fm-favicon.png')
st.set_page_config(page_title="FinanceiraMente", page_icon = img)

st.markdown(light, unsafe_allow_html=True)

with st.sidebar:
    # Create a toggle button
    toggle = st.button("Modo :sun_with_face:/ :new_moon_with_face:")
    col1, col2, col3 = st.columns(3)
    

# Use a global variable to store the current theme
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Change the theme based on the button state
if toggle:
    if st.session_state.theme == "light":
        st.session_state.theme = "dark"
    else:
        st.session_state.theme = "light"

# Apply the theme to the app
if st.session_state.theme == "dark":
    st.markdown(dark, unsafe_allow_html=True)
else:
    st.markdown(light, unsafe_allow_html=True)


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
col1, col2, col3 = st.columns(3)
with col2:
    st.image('logo - bing.jpg', use_column_width=True)

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
            porcentagem_acertos = sst.corretas / sst.n_perguntas
            st.success(f"Você acertou {sst.corretas} de {sst.n_perguntas}.")
            with st.expander("**Feedback:**"):
                if 0 <= porcentagem_acertos <= 0.25:
                    st.error(f'''**Sua porcentagem de acertos foi de {porcentagem_acertos*100:.0f}%**  
                            **Você está iniciando**  
                            Parabéns por mostrar interesse em melhorar seus conhecimentos em finanças! Seu nível atual de conhecimento é relativamente baixo, mas não se preocupe, muitas pessoas começam a partir desse ponto. Para melhorar, você pode começar lendo livros, participando de cursos online ou consultando um profissional de finanças. Com dedicação e esforço, você pode aumentar seu conhecimento e tomar decisões financeiras mais informadas.''',
                            icon = "🚨")
                    st.write("Independentemente da faixa em que você se encontra, lembre-se de que a educação financeira é uma jornada contínua. Nunca é tarde para melhorar seus conhecimentos financeiros e tomar decisões mais sólidas em relação ao seu dinheiro. Continue investindo em seu aprendizado e colherá os benefícios ao longo do tempo.")
                if 0.25 < porcentagem_acertos <= 0.5:
                    st.warning(f'''**Sua porcentagem de acertos foi {porcentagem_acertos*100:.0f}%**  
                            **Você já tem algum conhecimento**  
                            Você já tem um conhecimento básico em finanças, o que é um bom começo. No entanto, ainda há espaço para melhorias. Considere aprofundar seus conhecimentos em áreas específicas, como investimentos, orçamento pessoal ou planejamento para o futuro. A educação financeira é uma jornada contínua, e com mais esforço, você pode tomar decisões financeiras mais sólidas e alcançar seus objetivos.''',
                            icon = "📈")
                    st.write("Independentemente da faixa em que você se encontra, lembre-se de que a educação financeira é uma jornada contínua. Nunca é tarde para melhorar seus conhecimentos financeiros e tomar decisões mais sólidas em relação ao seu dinheiro. Continue investindo em seu aprendizado e colherá os benefícios ao longo do tempo.")
                if 0.5 < porcentagem_acertos <= 0.75:
                    st.info(f'''**Sua porcentagem de acertos foi {porcentagem_acertos*100:.0f}%**  
                            **Você possui uma base sólida**  
                            Seu conhecimento em finanças está em um bom nível! Você demonstrou uma compreensão sólida de conceitos financeiros essenciais. Continue aprimorando suas habilidades, explorando estratégias de investimento mais avançadas e aprofundando sua compreensão de planejamento financeiro. Com esse nível de conhecimento, você está bem encaminhado para tomar decisões financeiras mais eficazes.''',
                            icon = "✅")
                    st.write("Independentemente da faixa em que você se encontra, lembre-se de que a educação financeira é uma jornada contínua. Nunca é tarde para melhorar seus conhecimentos financeiros e tomar decisões mais sólidas em relação ao seu dinheiro. Continue investindo em seu aprendizado e colherá os benefícios ao longo do tempo.")
                if 0.75 < porcentagem_acertos <= 1:
                    st.success(f'''**Sua porcentagem de acertos foi {porcentagem_acertos*100:.0f}%**  
                            **Você tem bastante conhecimento**  
                            Parabéns! Seu conhecimento em finanças é impressionante e você está bem informado sobre os princípios financeiros. Você provavelmente já alcançou muitos sucessos financeiros em sua vida. Continue se mantendo atualizado e considere compartilhar seus conhecimentos com os outros. Lembre-se de que sempre há mais a aprender, especialmente em um campo tão dinâmico como as finanças.''',
                            icon = "✨")
                    st.write("Independentemente da faixa em que você se encontra, lembre-se de que a educação financeira é uma jornada contínua. Nunca é tarde para melhorar seus conhecimentos financeiros e tomar decisões mais sólidas em relação ao seu dinheiro. Continue investindo em seu aprendizado e colherá os benefícios ao longo do tempo.")

# Se quiser ver as variáveis guardadas a cada rerun é só descomentar a próxima linha
# sst

