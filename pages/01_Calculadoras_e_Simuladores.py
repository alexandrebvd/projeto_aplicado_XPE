import streamlit as st

st.title("Calculadoras e simuladores")
st.subheader("Essas são algumas calculadoras e simuladores que podem ajudar em seu aprendizado e planejamento financeiro.")
st.header("Calculadora de juros compostos")
        
def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

# Input parameters
principal = st.number_input("Valor inicial", value=1000.0)
rate = st.number_input("Taxa de juros anual (%)", value=10.0)
time = st.number_input("Tempo (anos)", value=10.0)

result = compound_interest(principal, rate, time)

# Display the final amount with larger font size
st.markdown(f"<p style='font-size:36px;'>Total acumulado: ${result:.2f}</p>", unsafe_allow_html=True)