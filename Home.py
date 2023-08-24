import streamlit as st

def main():
    st.title("[Nome do app]")
    st.subheader("Nosso objetivo é facilitar o seu aprendizado sobre educação financeira.")

    col1, col2 = st.columns(2)
    col1.button("Entrar")
    col2.button("Criar nova conta")

if __name__ == "__main__":
    main()