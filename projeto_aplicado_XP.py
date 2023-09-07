import streamlit as st
from finance_funcs import *

def main():
    st.title("Nome do aplicativo")

    # Sidebar navigation
    menu = ["Calculadora de Juros Simples", "Calculadora de Juros Compostos", "Calculadora de Anuidade", 
            "Calculadora de ROI", "Calculadora de Ponto de Equilíbrio", "Calculadora de VPL",
            "Calculadora de TIR", "Calculadora de Depreciação", "Calculadora de Pagamentos de Empréstimo"]
    choice = st.sidebar.selectbox("Selecionar opção", menu)
    
    if choice == "Calculadora de Juros Simples":
        st.header("Calculadora de juros simples")
        # Input parameters
        principal_simple = st.number_input("Valor inicial", value=1000.0)
        rate_simple = st.number_input("Taxa de juros anual (%)", value=10.0) / 100  # Convert to decimal
        time_simple = st.number_input("Tempo (anos)", value=10.0)
        # Calling the function to calculate simple interest
        result_simple = calculate_simple_interest(principal_simple, rate_simple, time_simple)
        # Display the final amount with larger font size
        st.markdown(f"<p style='font-size:36px;'>Total acumulado: ${result_simple:.2f}</p>", unsafe_allow_html=True)


    elif choice == "Calculadora de Juros Compostos":
        st.header("Calculadora de juros compostos") 
        # Input parameters
        principal = st.number_input("Valor inicial", value=1000.0)
        rate = st.number_input("Taxa de juros anual (%)", value=10.0) / 100  # Convert to decimal
        time = st.number_input("Tempo (anos)", value=10.0)
        frequency = st.number_input("Frequência de capitalização (meses)", value=12.0)
        # Calling the function to calculate compound interest
        result = calculate_compound_interest(principal, rate, time, frequency)
        # Display the final amount with larger font size
        st.markdown(f"<p style='font-size:36px;'>Total acumulado: ${result:.2f}</p>", unsafe_allow_html=True)

    
    elif choice == "Calculadora de Anuidade":
        st.header("Calculadora de pagamentos de anuidade") 
        # Input parameters
        principal_annuity = st.number_input("Valor principal", value=1000.0)
        rate_annuity = st.number_input("Taxa de juros por período (%)", value=10.0) / 100  # Convert to decimal
        periods = st.number_input("Número de períodos", value=10)
        # Calling the function to calculate annuity payment
        payment_annuity = calculate_annuity_payment(principal_annuity, rate_annuity, periods)
        # Display the annuity payment with larger font size
        st.markdown(f"<p style='font-size:36px;'>Pagamento da anuidade: ${payment_annuity:.2f}</p>", unsafe_allow_html=True)
    
    elif choice == "Calculadora de ROI":
        pass

    elif choice == "Calculadora de Ponto de Equilíbrio":
        pass

    elif choice == "Calculadora de VPL":
        pass
        
    elif choice == "Calculadora de TIR":
        pass
        
    elif choice == "Calculadora de Depreciação":
        pass
        
    elif choice == "Calculadora de Pagamentos de Empréstimo":
        pass        
        
    elif choice == "Conceitos":
        st.title("Educação financeira")
        st.write("Página em construção.")


if __name__ == "__main__":
    main()
