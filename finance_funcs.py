from numpy_financial import irr

def calculate_simple_interest(principal, rate, time):
    """
    Calcula o juro simples.
    
    Args:
    principal (float): O montante principal.
    rate (float): A taxa de juro (em decimal).
    time (float): O período de tempo (em anos).
    
    Returns:
    float: O montante final após juro simples.
    """
    interest = principal * rate * time
    return principal + interest

def calculate_compound_interest(principal, rate, time, frequency):
    """
    Calcula o juro composto.
    
    Args:
    principal (float): O montante principal.
    rate (float): A taxa de juro (em decimal).
    time (float): O período de tempo (em anos).
    frequency (int): A frequência de capitalização por ano.
    
    Returns:
    float: O montante final após juro composto.
    """
    n = frequency
    amount = principal * (1 + rate / n) ** (n * time)
    return amount

def calculate_annuity_payment(principal, rate, periods):
    """
    Calcula o valor dos pagamentos de uma anuidade (parcelas iguais).
    
    Args:
    principal (float): O montante principal.
    rate (float): A taxa de juro por período (em decimal).
    periods (int): O número de períodos.
    
    Returns:
    float: O valor do pagamento da anuidade.
    """
    payment = (principal * rate) / (1 - (1 + rate) ** -periods)
    return payment


def calculate_future_value_of_annuity(payment, rate, periods):
    """
    Calcula o valor futuro de uma série de pagamentos (anuidade).

    Args:
    payment (float): Valor dos pagamentos periódicos.
    rate (float): Taxa de juros por período (em decimal).
    periods (int): Número de períodos.

    Returns:
    float: O valor futuro da anuidade.
    """
    fv = payment * ((1 + rate) ** periods - 1) / rate
    return fv

def calculate_roi(gains, costs):
    """
    Calcula o Retorno sobre Investimento (ROI).

    Args:
    gains (float): Ganhos provenientes do investimento.
    costs (float): Custos do investimento.

    Returns:
    float: O ROI calculado.
    """
    roi = (gains - costs) * 100 / costs
    return roi

def calculate_break_even_point(fixed_costs, variable_costs, selling_price):
    """
    Calcula o Ponto de Equilíbrio em vendas.

    Args:
    fixed_costs (float): Custos fixos.
    variable_costs (float): Custos variáveis por unidade.
    selling_price (float): Preço de venda por unidade.

    Returns:
    float: O ponto de equilíbrio em unidades.
    """
    bep = fixed_costs / (selling_price - variable_costs)
    return round(bep)

def calculate_net_present_value(cash_flows, rate):
    """
    Calcula o Valor Presente Líquido (VPL) de um conjunto de fluxos de caixa.

    Args:
    cash_flows (list): Lista de fluxos de caixa futuros.
    rate (float): Taxa de desconto por período (em decimal).

    Returns:
    float: O Valor Presente Líquido dos fluxos de caixa.
    """
    npv = sum([cf / (1 + rate) ** idx for idx, cf in enumerate(cash_flows)])
    return npv

def calculate_internal_rate_of_return(cash_flows):
    """
    Calcula a Taxa Interna de Retorno (TIR) de um conjunto de fluxos de caixa.

    Args:
    cash_flows (list): Lista de fluxos de caixa futuros.

    Returns:
    float: A Taxa Interna de Retorno calculada.
    """
    # Implementação da TIR usando métodos numéricos
    return irr(cash_flows)

def calculate_straight_line_depreciation(initial_value, salvage_value, useful_life):
    """
    Calcula a depreciação usando o método de linha reta.

    Args:
    initial_value (float): Valor inicial do ativo.
    salvage_value (float): Valor residual do ativo.
    useful_life (int): Vida útil do ativo em períodos.

    Returns:
    float: A depreciação por período.
    """
    depreciation = (initial_value - salvage_value) / useful_life
    return depreciation

def calculate_loan_payments(principal, rate, periods):
    """
    Calcula os pagamentos de um empréstimo (amortização).

    Args:
    principal (float): Montante principal do empréstimo.
    rate (float): Taxa de juros por período (em decimal).
    periods (int): Número de períodos.

    Returns:
    float: O valor dos pagamentos do empréstimo.
    """
    payment = (principal * rate) / (1 - (1 + rate) ** -periods)
    return payment