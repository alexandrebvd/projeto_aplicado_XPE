import streamlit as st
from PIL import Image
from styles import dark, light

img = Image.open('fm-favicon.png')
st.set_page_config(page_title="FinanceiraMente", page_icon = img)

st.markdown(light, unsafe_allow_html=True)

with st.sidebar:
    # Create a toggle button
    toggle = st.button("Modo :sun_with_face:/ :new_moon_with_face:")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('financeiraMente__1_-removebg-preview.png')

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

st.title("Sobre")
st.subheader("FinanceiraMente é um projeto aplicado da Faculdade XPE desenvolvido pelo Squad 1")
st.write("O aplicativo surgiu a partir da necessidade de promover o ensino de educação financeira para o público que não possui a capacitação necessária para atuação no mercado de trabalho nem conhecimentos de educação financeira. Dessa forma, nosso objetivo é que através da educação nosso público atinja uma melhor qualidade de vida a partir do planejamento financeiro e relização de suas metas.")
st.write("**Integrantes:**")
st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](http://www.linkedin.com/in/adrianohcs) [![GitHub](https://img.icons8.com/fluency/48/github.png)](https://github.com/adrianohcs) Adriano Henrique Cavalcante Silva" )
st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](https://www.linkedin.com/in/adriel-alexs/) [![GitHub](https://img.icons8.com/fluency/48/github.png)](https://github.com/AdrielProg) Adriel Alexander De Sousa" )
st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](https://www.linkedin.com/in/alan-lisboa-25173123b) [![GitHub](https://img.icons8.com/fluency/48/github.png)](https://github.com/alanblisboa) Alan Barros Lisboa" )
st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](https://www.linkedin.com/in/alessandramariana) [![GitHub](https://img.icons8.com/fluency/48/github.png)](https://github.com/AlessandraMariana) Alessandra Mariana De Souza" )
st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](https://www.linkedin.com/in/alexandredaltro/) [![GitHub](https://img.icons8.com/fluency/48/github.png)](https://github.com/alexandrebvd) Alexandre Brandão Veras Daltro" )
st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](https://www.linkedin.com/in/andr%C3%A9-baena-drugovich-365399214/) [![GitHub](https://img.icons8.com/fluency/48/github.png)](https://github.com/AndreBDrugovich) André Baena Drugovich" )
st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](https://www.linkedin.com/in/acrafilho-undefined-130937249/) [![GitHub](https://img.icons8.com/fluency/48/github.png)](https://github.com/ocarlosaragao) Antônio Carlos Rodrigues Aragão Filho" )
st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](https://www.linkedin.com/in/david-aguina-85a11925b/) [![GitHub](https://img.icons8.com/fluency/48/github.png)](https://github.com/DavidSatAg) David Satoshi Aguina" )
st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](http://www.linkedin.com/in/gabriel-andrade-6029ba252) [![GitHub](https://img.icons8.com/fluency/48/github.png)](https://github.com/gabriel-andradec) Gabriel Andrade Da Cunha" )

st.write("**Orientador:**")
st.write("[![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png)](https://www.linkedin.com/in/pauloobasilio/)Paulo Basílio")