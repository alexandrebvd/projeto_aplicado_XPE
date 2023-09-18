import streamlit as st

def calculate_INSS(grossSalary):
    """
    Calcula o desconto da Contribuição Previdenciária.
    
    Arg:
    grossSalary (float): Salário bruto.
    
    Returns:
    float: O valor do desconto da Contribuição Previdenciária.
    """
    inss = 0

    if grossSalary <= 1320.00:
        inss = grossSalary * 0.075
    elif grossSalary > 1320.00 and grossSalary < 2571.30:
        inss = 1320.00 * 0.075 + (grossSalary - 1320.00) * 0.09
    elif grossSalary >= 2571.30 and grossSalary < 3856.95:
        inss = 1320.00 * 0.075 + (2571.29 - 1320.00) * 0.09 + (grossSalary - 2571.29)* 0.12
    elif grossSalary >= 3856.95 and grossSalary < 7507.50:
        inss = 1320.00 * 0.075 + (2571.29 - 1320.00) * 0.09 + (3856.94 - 2571.29) * 0.12 + (grossSalary - 3856.94) * 0.14
    else:
        inss = 1320.00 * 0.075 + (2571.29 - 1320.00) * 0.09 + (3856.94 - 2571.29) * 0.12 + (7507.49 - 3856.94) * 0.14

    return inss


def calculate_IRPF(grossSalary, dependents):
    """
    Calcula desconto de Imposto de Renda Pessoa Física.
    
    Args:
    grossSalary (float): Salário bruto.
    dependents (integer): Número de dependentes.
    
    Returns:
    float: O montante final após desconto do Imposto de Renda.
    """
    calculationBasis = grossSalary - (calculate_INSS(grossSalary) + (dependents * 189.59))
    irpf = 0

    if calculationBasis <= 2112.00:
        irpf = 0
    elif calculationBasis > 2112.00 and calculationBasis <= 2826.65:
        irpf = (calculationBasis - 2112.00) * 0.075
    elif calculationBasis > 2826.65 and calculationBasis <= 3751.05:
        irpf = (2826.65 - 2112.00) * 0.075 + (calculationBasis - 2826.65) * 0.15
    elif calculationBasis > 3751.05 and calculationBasis <= 4664.68:
        irpf = (2826.65 - 2112.00) * 0.075 + (3751.05 - 2826.65) * 0.15 + (calculationBasis - 3751.05) * 0.225
    else:
        irpf = (2826.65 - 2112.00) * 0.075 + (3751.05 - 2826.65) * 0.15 + (4664.68 - 3751.05) * 0.225 + (calculationBasis - 4664.68) * 0.275

    return irpf
    

st.title("Salário Líquido")  

with st.expander("Salário Líquido e IR", expanded=True):
    # Input parameters
    grossSalary = st.number_input("Salário Bruto", value=1320.0) 
    dependents = st.number_input("Número de dependentes", value=0)
    otherDiscounts = st.number_input("Outros descontos", value=0.0)

    # Calculations
    resultINSS = calculate_INSS(grossSalary)
    resultIRPF = calculate_IRPF(grossSalary, dependents)
    finalResult = grossSalary - (resultINSS + resultIRPF + otherDiscounts)

    # Display the final amount with larger font size
    st.markdown(f"<p style='font-size:24px;'>Contribuição Previdenciária (INSS): R$ {resultINSS:.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:24px;'>Imposto de Renda: R$ {resultIRPF:.2f}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:24px;'>Salário Líquido: R$ {finalResult:.2f}</p>", unsafe_allow_html=True)