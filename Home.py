import streamlit as st
from PIL import Image

img = Image.open('fm-favicon.png')
st.set_page_config(page_title="FinanceiraMente", page_icon = img)


def main():
    st.title("Bem-vindo(a) ao FinanceiraMente")
    st.write("Projeto Aplicado - Faculdade XPE")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('financeiraMente__1_-removebg-preview.png', width=380)
    st.subheader("Nosso objetivo é facilitar o seu aprendizado sobre educação financeira.")

    col4, col5 = st.columns(2)
    col4.button("Entrar", use_container_width=True)
    col5.button("Criar nova conta", use_container_width=True)
    st.markdown(f"<p style='color:#ff0000;font-size:24px;'>Funcionalidade de login em construção.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()