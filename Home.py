import streamlit as st
from PIL import Image

img = Image.open('fm-favicon.png')
st.set_page_config(page_title="FinanceiraMente", page_icon = img)

dark = '''
<style>
    .stApp {
    background-color: #0E1117;
    color: #FAFAFA;
    }
    #stSidebar {
    background-color: #0E1117;
    color: #FAFAFA;
    }
    li {
    color: #FAFAFA;
    }
    h1, span {
    color: #FAFAFA;
    }
    .element-container {
    color: #FAFAFA;
    }
    .stButton {
    color: #31333F;
    }
</style>
'''

light = '''
<style>
    .stApp {
    background-color: #FFFFFF;
    color: #31333F
    }
</style>
'''
st.markdown(light, unsafe_allow_html=True)

# Create a toggle button
toggle = st.button("Modo :sun_with_face:/ :new_moon_with_face:")

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