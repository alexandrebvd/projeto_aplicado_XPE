import streamlit as st

def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def main():
    st.title("Nome do aplicativo")

    # Sidebar navigation
    menu = ["Calculadora", "Conceitos"]
    choice = st.sidebar.selectbox("Selecionar opção", menu)

    if choice == "Calculadora":
        st.header("Calculadora de juros compostos")
        
        # Input parameters
        principal = st.number_input("Valor inicial", value=1000.0)
        rate = st.number_input("Taxa de juros anual (%)", value=10.0)
        time = st.number_input("Tempo (anos)", value=10.0)

        result = compound_interest(principal, rate, time)

        # Display the final amount with larger font size
        st.markdown(f"<p style='font-size:36px;'>Total acumulado: ${result:.2f}</p>", unsafe_allow_html=True)
    
    elif choice == "Conceitos":
        st.title("Educação financeira")
        st.write("Página em construção.")

if __name__ == "__main__":
    main()
