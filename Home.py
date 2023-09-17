import streamlit as st
from PIL import Image

img = Image.open('fm-favicon.png')
st.set_page_config(page_title="FinanceiraMente", page_icon = img)


def main():
    st.title("Bem-vindo(a) ao FinanceiraMente")
    st.write("Projeto Aplicado - Faculdade XPE")
    st.image('logo - bing.jpg', use_column_width='auto')
    st.subheader("Nosso objetivo é facilitar o seu aprendizado sobre educação financeira.")

    col1, col2 = st.columns(2)
    col1.button("Entrar", use_container_width=True)
    col2.button("Criar nova conta", use_container_width=True)

if __name__ == "__main__":
    main()