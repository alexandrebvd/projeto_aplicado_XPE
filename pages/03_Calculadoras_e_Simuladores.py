import streamlit as st
import finance_funcs as ff
import re
import numpy as np
import plotly.graph_objects as go
from PIL import Image
from styles import dark, light

img = Image.open('fm-favicon.png')
st.set_page_config(page_title="FinanceiraMente", page_icon = img)

st.markdown(light, unsafe_allow_html=True)

with st.sidebar:
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

st.title("Calculadoras e simuladores")
st.subheader("Essas são algumas calculadoras e simuladores que podem ajudar em seu aprendizado e planejamento financeiro.")
        
def text_to_list(text):
    """
    Extract positive and negative decimal numbers from a string containing several numbers
    """
    numbers_list = "".join(text.split())
    numbers_list = numbers_list.split(",")
    try:
        numbers_list = [float(i) for i in numbers_list]
    except:
        st.error("Erro: insira apenas números separados por vírgula.")
        numbers_list = []
    return numbers_list

# Juros simples
with  st.expander("Calculadora de juros simples"):
    # Input parameters
    principal = st.number_input("Valor inicial (R$)", min_value=0.0, value=500.0)
    rate = st.number_input("Taxa de juros (%)", value=10.0)
    rate = rate / 100
    time = st.number_input("Tempo (anos)", min_value=1, value=10)

    result = ff.calculate_simple_interest(principal, rate, time)

    # Display the final amount with larger font size
    st.markdown(f"<p style='font-size:24px;'>Total acumulado: R$ {result:.2f}</p>", unsafe_allow_html=True)
    
    x_values = np.arange(time + 1)
    y_values = [ff.calculate_simple_interest(principal, rate, t) for t in x_values]
    fig = go.Figure()
    fig.add_trace(
            go.Scatter(
                x=x_values, 
                y=y_values,
                name="Juros simples"
            )
        )
    fig.update_layout(title='Gráfico de juros simples',
                   xaxis_title='Anos',
                   yaxis_title='Valor (R$)')
    st.plotly_chart(fig, use_container_width=True)


# Juros compostos
with st.expander("Calculadora de juros compostos"):
    # Input parameters
    principal = st.number_input("Valor inicial (R$)", min_value=0.0, value=1000.0)
    rate = st.number_input("Taxa de juros anual (%)", value=10.0)
    rate = rate / 100
    time = st.number_input("Tempo (anos)", min_value=1, value=30)
    frequency = st.number_input("Frequência de capitalização", min_value=1, value=1)

    result = ff.calculate_compound_interest(principal, rate, time, frequency)

    # Display the final amount with larger font size
    st.markdown(f"<p style='font-size:24px;'>Total acumulado: R$ {result:.2f}</p>", unsafe_allow_html=True)
    
    x_values = np.arange(time + 1)
    y_values = [ff.calculate_compound_interest(principal, rate, t, frequency) for t in x_values]
    fig = go.Figure()
    fig.add_trace(
            go.Scatter(
                x=x_values, 
                y=y_values,
                name="Juros compostos"
            )
        )
    fig.update_layout(title='Gráfico de juros compostos',
                   xaxis_title='Anos',
                   yaxis_title='Valor (R$)')
    st.plotly_chart(fig, use_container_width=True)


# Pagamento de anuidade
with st.expander("Calculadora de pagamento de anuidade"):
    # Input parameters
    principal = st.number_input("Valor inicial (R$)", min_value=0.0, value=900.0)
    rate = st.number_input("Taxa de juros por período (%)", value=10.0)
    rate = rate / 100
    periods = st.number_input("Número de períodos", min_value=1, value=12)

    result = ff.calculate_annuity_payment(principal, rate, periods)

    st.markdown(f"<p style='font-size:24px;'>Valor do pagamento da anuidade: R$ {result:.2f}</p>", unsafe_allow_html=True)


# Valor futuro da anuidade
with st.expander("Calculadora de valor futuro da anuidade"):
    # Input parameters
    payment = st.number_input("Valor dos pagamentos periódicos", min_value=0.0, value=150.0)
    rate = st.number_input("Taxa de juros por período (%)", value=5.0)
    rate = rate / 100
    periods = st.number_input("Número de períodos", min_value=1, value=5)
    
    result = ff.calculate_future_value_of_annuity(payment, rate, periods)

    st.markdown(f"<p style='font-size:24px;'>Valor futuro da anuidade: R$ {result:.2f}</p>", unsafe_allow_html=True)

# ROI
with st.expander("Calculadora do ROI (Retorno sobre o investimento)"):
    # Input parameters
    gains = st.number_input("Ganhos provenientes do investimento", min_value=0.0, value=3000.0)
    costs = st.number_input("Custos do investimento", min_value=0.01, value=2500.0)

    result = ff.calculate_roi(gains, costs)

    st.markdown(f"<p style='font-size:24px;'>Valor do ROI: {result:.2f}%</p>", unsafe_allow_html=True)
    

# Ponto de Break Even
with st.expander("Calculadora de ponto de Break Even"):
    # Input parameters
    fixed_costs = st.number_input("Custos fixos", min_value=0.0, value=500.0)
    variable_costs = st.number_input("Custos variáveis por unidade", min_value=0.0, value=2.50)
    selling_price = st.number_input("Preço de venda por unidade", min_value=0.0, value=10.0)
    try:
        result = ff.calculate_break_even_point(fixed_costs, variable_costs, selling_price)
    except:
        st.error("Erro: Custos variáveis não podem ter o mesmo valor do preço de venda.")
        result = 0
    if variable_costs > selling_price:
        st.error("Erro: Custos variáveis não podem ser maiores que o preço de venda.")
        result = 0
    st.markdown(f"<p style='font-size:24px;'>O ponto de break even ocorre em {result:.0f} unidades</p>", unsafe_allow_html=True)
    

# Valor presente líquido
with st.expander("Calculadora do valor presente líquido"):
    # Input parameters
    str_cash_flows = st.text_input("Lista de fluxos de caixa futuros", value="273.80, 579.90, 1030.50")
    cash_flows = text_to_list(str_cash_flows)
    rate = st.number_input("Taxa de desconto por período (%)", value=15.0)
    rate = rate / 100

    result = ff.calculate_net_present_value(cash_flows, rate)

    st.markdown(f"<p style='font-size:24px;'>Valor Presente Líquido dos fluxos de caixa: {result:.2f}</p>", unsafe_allow_html=True)

# Taxa interna de retorno
with st.expander("Calculadora da taxa interna de retorno"):
    st.write("A taxa interna de retorno é a taxa de desconto que torna o valor presente líquido igual a zero.\
            Para calcular a TIR, basta inserir os fluxos de caixa futuros. Lembrando que o primeiro fluxo de caixa\
            deve ser negativo, pois representa o investimento inicial.", )
    str_cash_flows = st.text_input("Lista de fluxos de caixa futuros", value="-100, 39, 59, 55, 20")
    cash_flows = np.array(text_to_list(str_cash_flows))
    result = ff.calculate_internal_rate_of_return(cash_flows)
    
    st.markdown(f"<p style='font-size:24px;'>A taxa interna de retorno é {result*100:.2f}%.</p>", unsafe_allow_html=True)
    

# Depreciação linear
with st.expander("Calculadora de depreciação linear"):
    # Input parameters
    initial_value = st.number_input("Valor inicial do ativo", value=33000.00)
    salvage_value = st.number_input("Valor residual do ativo", max_value=initial_value, value=15000.00)
    useful_life = st.number_input("Vida útil do ativo em períodos", value=7)

    result = ff.calculate_straight_line_depreciation(initial_value, salvage_value, useful_life)

    st.markdown(f"<p style='font-size:24px;'>A depreciação por período: R$ {result:.2f}</p>", unsafe_allow_html=True)
    
    x_values = np.arange(useful_life + 1)
    y_values = [initial_value - result * x for x in x_values]
    fig = go.Figure()
    fig.add_trace(
            go.Scatter(
                x=x_values, 
                y=y_values,
                name="Depreciação linear"
            )
        )
    fig.update_layout(title='Gráfico de depreciação linear',
                   xaxis_title='Anos',
                   yaxis_title='Valor(R$)')
    st.plotly_chart(fig, use_container_width=True)
    

# Pagamentos de empréstimos
with st.expander("Calculadora de pagamentos de empréstimos"):
    # Input parameters
    principal = st.number_input("Montante principal do empréstimo", min_value=0.0, value=7000.0)
    rate = st.number_input("Taxa de juros por período (%)", value=8.0)
    rate = rate / 100
    periods = st.number_input("Número de períodos", min_value=1, value=7)

    result = ff.calculate_loan_payments(principal, rate, periods)

    st.markdown(f"<p style='font-size:24px;'>Valor dos pagamentos do empréstimo: R$ {result:.2f} por período</p>", unsafe_allow_html=True)
