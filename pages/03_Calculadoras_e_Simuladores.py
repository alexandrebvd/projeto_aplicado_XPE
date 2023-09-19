import streamlit as st
import finance_funcs as ff
import re

st.title("Calculadoras e simuladores")
st.subheader("Essas são algumas calculadoras e simuladores que podem ajudar em seu aprendizado e planejamento financeiro.")
        
def text_to_list(text):
    numbers_list = [int(i) for i in re.split("[^0-9]", text) if i != ""]
    return numbers_list

# Juros simples
with  st.expander("Calculadora de juros simples"):
    # Input parameters
    principal = st.number_input("Valor inicial", value=500.0)
    rate = st.number_input("Taxa de juros em decimal (Ex.:0.10)", value=0.10)
    time = st.number_input("Tempo (anos)", value=5)

    result = ff.calculate_simple_interest(principal, rate, time)

    # Display the final amount with larger font size
    st.markdown(f"<p style='font-size:24px;'>Total acumulado: R$ {result:.2f}</p>", unsafe_allow_html=True)


# Juros compostos
with st.expander("Calculadora de juros compostos"):
    # Input parameters
    principal = st.number_input("Valor inicial", value=1000.0)
    rate = st.number_input("Taxa de juros anual (%)", value=10.0)
    time = st.number_input("Tempo (anos)", value=10)
    frequency = st.number_input("Frequência de capitalização por ano (meses)", value=12)

    result = ff.calculate_compound_interest(principal, rate, time, frequency)

    # Display the final amount with larger font size
    st.markdown(f"<p style='font-size:24px;'>Total acumulado: R$ {result:.2f}</p>", unsafe_allow_html=True)


# Pagamento de anuidade
with st.expander("Calculadora de pagamento de anuidade"):
    # Input parameters
    principal = st.number_input("Valor inicial", value=900.0)
    rate = st.number_input("Taxa de juros por período em decimal (Ex.: 0,10)", value=0.3)
    periods = st.number_input("O número de períodos.", value=12)

    result = ff.calculate_annuity_payment(principal, rate, periods)

    st.markdown(f"<p style='font-size:24px;'>Valor do pagamento da anuidade: R$ {result:.2f}</p>", unsafe_allow_html=True)

# Valor do fluxo de caixa
with st.expander("Calculadora de valor presente de fluxos de caixa futuros"):
    # Input parameters
    str_cash_flows = st.text_input("Lista de fluxos de caixa futuros", value="1023.4, 784.5, 987.53")
    cash_flows = text_to_list(str_cash_flows)
    rate = st.number_input("A taxa de desconto por período (em decimal)", value=0.03)

    result = ff.present_value_of_cash_flows(cash_flows, rate)

    st.markdown(f"<p style='font-size:24px;'>Valor presente líquido dos fluxos de caixa: R$ {result:.2f}</p>", unsafe_allow_html=True)


# Valor futuro da anuidade
with st.expander("Calculadora de valor futuro da anuidade"):
    # Input parameters
    payment = st.number_input("Valor dos pagamentos periódicos", value=150.00)
    rate = st.number_input("Taxa de juros por período (em decimal)", value=0.05)
    periods = st.number_input("Número de períodos", value=5)
    
    result = ff.calculate_future_value_of_annuity(payment, rate, periods)

    st.markdown(f"<p style='font-size:24px;'>Valor futuro da anuidade: R$ {result:.2f}</p>", unsafe_allow_html=True)

# ROI
with st.expander("Calculadora do ROI (Retorno sobre o investimento)"):
    # Input parameters
    gains = st.number_input("Ganhos provenientes do investimento", value=3000.00)
    costs = st.number_input("Custos do investimento", value=2500.00)

    result = ff.calculate_roi(gains, costs)

    st.markdown(f"<p style='font-size:24px;'>Valor do ROI: {result:.2f}%</p>", unsafe_allow_html=True)
    

# Ponto de Break Even
with st.expander("Calculadora de ponto de Break Even"):
    # Input parameters
    fixed_costs = st.number_input("Custos fixos", value=500.00)
    variable_costs = st.number_input("Custos variáveis por unidade", value=2.50)
    selling_price = st.number_input("Preço de venda por unidade", value=10.00)

    result = ff.calculate_break_even_point(fixed_costs, variable_costs, selling_price)

    st.markdown(f"<p style='font-size:24px;'>O ponto de equilíbrio em unidades: {result:.0f}</p>", unsafe_allow_html=True)
    

# Valor presente líquido
with st.expander("Calculadora do valor presente líquido"):
    # Input parameters
    str_cash_flows = st.text_input("Lista de fluxos de caixa futuros", value="273.80, 579.90, 1030.50")
    cash_flows = text_to_list(str_cash_flows)
    rate = st.number_input("Taxa de desconto por período (em decimal)", value=0.15)

    result = ff.calculate_net_present_value(cash_flows, rate)

    st.markdown(f"<p style='font-size:24px;'>Valor Presente Líquido dos fluxos de caixa: {result:.2f}</p>", unsafe_allow_html=True)

# Taxa interna de retorno
with st.expander("Calculadora da taxa interna de retorno"):
    st.markdown("Calculadora em construção")
    

# Depreciação linear
with st.expander("Calculadora de depreciação linear"):
    # Input parameters
    initial_value = st.number_input("Valor inicial do ativo", value=33000.00)
    salvage_value = st.number_input("Valor residual do ativo", max_value=initial_value, value=15000.00)
    useful_life = st.number_input("Vida útil do ativo em períodos", value=7)

    result = ff.calculate_straight_line_depreciation(initial_value, salvage_value, useful_life)

    st.markdown(f"<p style='font-size:24px;'>A depreciação por período: R$ {result:.2f}</p>", unsafe_allow_html=True)
    

# Pagamentos de empréstimos
with st.expander("Calculadora de pagamentos de empréstimos"):
    # Input parameters
    principal = st.number_input("Montante principal do empréstimo", value=7000)
    rate = st.number_input("Taxa de juros por período (em decimal)", value=0.08)
    periods = st.number_input("Número de períodos", value=7)

    result = ff.calculate_loan_payments(principal, rate, periods)

    st.markdown(f"<p style='font-size:24px;'>Valor dos pagamentos do empréstimo: R$ {result:.2f}</p>", unsafe_allow_html=True)