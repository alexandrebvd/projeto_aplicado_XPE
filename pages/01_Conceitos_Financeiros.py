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

st.title("Conceitos Financeiros")
st.subheader("Nesta seção vamos entender mais sobre conceitos e jargões que permeiam esta área!")


with st.expander("Aposentadoria"):
    st.markdown(f"<p style='font-size:20px;'>A aposentadoria é um benefício que a Previdência Social oferece aos trabalhadores segurados que satisfaçam os critérios estabelecidos por lei, como aposentadoria por invalidez, outros critérios específicos, idade mínima e/ou tempo de contribuição. Que envolve economizar e investir ao longo da vida para garantir uma renda estável quando você parar de trabalhar.</p>", unsafe_allow_html=True)

with st.expander("Ações"):
    st.markdown(f"<p style='font-size:20px;'>As ações são ativos negociados na bolsa de valores e representam uma pequena parte de uma empresa. Assim, ao adquirir uma ação, o investidor se torna sócio da empresa que emitiu esse ativo. É um investimento de renda variável, pois os preços e rendimentos das ações se sujeitam às oscilações do mercado.</p>", unsafe_allow_html=True)

with st.expander("Certificado de Depósito Bancário (CDB)"):
    st.markdown(f"<p style='font-size:20px;'>O CDB é um investimento de renda fixa emitido pelos bancos com o objetivo de captar recursos para financiar suas atividades. Assim, ele funciona como um empréstimo do seu dinheiro para uma instituição bancária, em troca de uma taxa de rentabilidade (ou seja, o banco devolve o dinheiro com juros sobre o valor investido).</p>", unsafe_allow_html=True)

with st.expander("Conta Corrente"):
    st.markdown(f"<p style='font-size:20px;'>Uma conta corrente, é uma conta bancária que é usada para transações diárias, como pagar contas, fazer compras com cartões de débito, e transferir dinheiro. Diferentemente da conta poupança, a conta corrente geralmente não gera juros significativos sobre o saldo e é projetada para facilitar transações financeiras.</p>", unsafe_allow_html=True)

with st.expander("Conta Poupança"):
    st.markdown(f"<p style='font-size:20px;'>Uma conta poupança é um tipo de conta bancária que é usada principalmente para guardar dinheiro e economizar. Ela oferece juros sobre o saldo depositado, ajudando a aumentar gradualmente o dinheiro economizado.</p>", unsafe_allow_html=True)

with st.expander("Criptomoeda"):
    st.markdown(f"<p style='font-size:20px;'>Uma criptomoeda ou cibermoeda é um meio de troca, geralmente descentralizado, que se utiliza da tecnologia de blockchain e da criptografia para assegurar a validade das transações e a criação de novas unidades da moeda.</p>", unsafe_allow_html=True)

with st.expander("Deflação"):
    st.markdown(f"<p style='font-size:20px;'>Ao contrário da inflação, a deflação a redução de preços de bens e serviços. Sendo assim, ela representa a redução do custo e vida e a consequente aumento no poder de compra da moeda.</p>", unsafe_allow_html=True)

with st.expander("Educação Financeira"):
    st.markdown(f"<p style='font-size:20px;'>A educação financeira é o processo de aprender a gerenciar suas finanças de forma eficaz e tomar decisões informadas sobre o dinheiro. É sobre se perguntar antes de cada compra se você quer ou precisa daquele produto ou serviço.</p>", unsafe_allow_html=True)

with st.expander("Exchange Traded Fund (ETF)"):
    st.markdown(f"<p style='font-size:20px;'>Um ETF é um fundo negociado na bolsa de valores e que busca refletir um determinado índice - como o Ibovespa. Os recursos aplicados em um ETF, portanto, são investidos em determinados ativos com o objetivo de replicar determinado índice - se o Ibovespa (conjunto de ações mais negociadas na bolsa de valores) sobe, por exemplo, o ETF também deve subir na mesma proporção.</p>", unsafe_allow_html=True)

with st.expander("Fundos imobiliários (FII)"):
    st.markdown(f"<p style='font-size:20px;'>No fundo imobiliário, os recursos aplicados são investidos em empreendimentos imobiliários, como shoppings, hospitais e prédios comerciais. Ao adquirir cotas de FIIs, o investidor passa a receber parte dos aluguéis dos imóveis.</p>", unsafe_allow_html=True)

with st.expander("Fundos de investimento"):
    st.markdown(f"<p style='font-size:20px;'>Os fundos de investimentos são constituídos por valores aplicados por diversas pessoas. Os valores aplicados são administrados por uma gestora, que os investe em algum ativo, como ações, imóveis, títulos públicos, etc.</p>", unsafe_allow_html=True)

with st.expander("Imposto de Renda"):
    st.markdown(f"<p style='font-size:20px;'>Imposto de Renda é um tributo obrigatório que as pessoas e as empresas devem pagar ao governo com base em sua renda ou lucro. Ele é usado para financiar serviços públicos, programas governamentais e infraestrutura.</p>", unsafe_allow_html=True)

with st.expander("Índice Ibovespa"):
    st.markdown(f"<p style='font-size:20px;'>Conhecido como IBOV, o índice funciona como um termômetro do mercado acionário do Brasil e mede, através de um sistema de pontos baseado em reais, o desempenho médio de uma carteira teórica com as ações mais representativas e negociadas em Bolsa.</p>", unsafe_allow_html=True)

with st.expander("Inflação"):
    st.markdown(f"<p style='font-size:20px;'>Inflação é um termo usado para designar o aumento de preços de bens e serviços. Com isso, a inflação representa o aumento do custo e vida e a consequente redução no poder de compra da moeda.</p>", unsafe_allow_html=True)

with st.expander("Investimento"):
    st.markdown(f"<p style='font-size:20px;'>Investimento é uma aplicação de recursos feita com o intuito de obter mais recursos no futuro. Os investimentos financeiros se dividem, basicamente, em duas modalidades: renda fixa e renda variável.</p>", unsafe_allow_html=True)

with st.expander("Juros Compostos"):
    st.markdown(f"<p style='font-size:20px;'>Os juros compostos referem-se à prática de ganhar juros sobre os juros acumulados anteriormente. Isso significa que, com o tempo, seus ganhos financeiros aumentam à medida que seus investimentos ou economias crescem.</p>", unsafe_allow_html=True)

with st.expander("Juros Simples"):
    st.markdown(f"<p style='font-size:20px;'>Juros simples referem-se a um método de cálculo de juros em que os ganhos ou custos financeiros são calculados apenas sobre o valor principal (o montante inicial) durante um determinado período. Os juros simples não levam em consideração os juros acumulados anteriormente. É comumente usado em empréstimos de curto prazo e investimentos de menor complexidade. </p>", unsafe_allow_html=True)

with st.expander("Letra de Crédito Imobiliário (LCI) e Letra de Crédito do Agronegócio (LCA)"):
    st.markdown(f"<p style='font-size:20px;'>As letras de crédito são investimentos de renda fixa emitidos por banco. Ao investir em uma letra de crédito, você está oferecendo um empréstimo ao banco, em troca de uma rentabilidade. Os recursos captados a partir da compra de LCI são direcionados ao financimento de empreendimentos e atividades do setor imobiliário. Os recursos da LCA financiam atividades do agronegócio.</p>", unsafe_allow_html=True)

with st.expander("Moedas Digitais"):
    st.markdown(f"<p style='font-size:20px;'>Moeda digital é qualquer moeda, dinheiro ou ativo semelhante a dinheiro que seja gerenciado, armazenado ou trocado principalmente em sistemas de computador digital, especialmente pela Internet. Os tipos de moedas digitais incluem criptomoeda, moeda virtual e moeda digital do banco central.</p>", unsafe_allow_html=True)

with st.expander("Orçamento Pessoal"):
    st.markdown(f"<p style='font-size:20px;'>O orçamento pessoal é uma ferramenta de controle de gastos, que detalha suas receitas e despesas,ajudando a controlar seus gastos e garantir que você viva dentro de suas possibilidades financeiras. </p>", unsafe_allow_html=True)

with st.expander("Patrimônio Líquido"):
    st.markdown(f"<p style='font-size:20px;'>O patrimônio líquido representa a diferença entre o valor total dos seus ativos (bens, investimentos, dinheiro) e o total das suas dívidas. É uma medida da sua saúde financeira. </p>", unsafe_allow_html=True)

with st.expander("Planejamento financeiro pessoal"):
    st.markdown(f"<p style='font-size:20px;'>Planejar significa definir metas, traçar estratégias e analisar os erros passados para melhorar continuamente o processo.</br> Assim, o planejamento financeiro pessoal é a definição de uma estratégia para tomada de decisões com o seu dinheiro de olho nas suas necessidades e vontades.</p>", unsafe_allow_html=True)

with st.expander("Renda fixa"):
    st.markdown(f"<p style='font-size:20px;'>A renda fixa é a modalidade de investimento em que a rentabilidade é previsível, ou seja, é possível estimar a renda que será gerada pelo investimento. </br> Esses investimentos funcionam basicamente como um empréstimo de dinheiro ao seu emissor (bancos, empresas, governo), que se compromete em devolver o valor, após um período, acrescido de juros. </br> Alguns exemplos dessa modalidade são CDB, Tesouro Direto, LCI e LCA.</p>", unsafe_allow_html=True)

with st.expander("Renda variável"):
    st.markdown(f"<p style='font-size:20px;'>A renda variável não possui previsibilidade nos rendimentos. </br> Esse investimento consiste na compra de parte de uma negócio, como empresa ou empreendimento imobiliário. </br> Alguns exemplos dessa modalidade são ações, ETFs e fundos imobiliários.</p>", unsafe_allow_html=True)

with st.expander("Reserva de Emergência"):
    st.markdown(f"<p style='font-size:20px;'>A reserva de emergência é quando uma pessoa economiza dinheiro ao longo do tempo para lidar com despesas inesperadas, como contas médicas, reparos em casa, compra de remédios, conserto do carro e gastos com educação.</p>", unsafe_allow_html=True)

with st.expander("Seguro"):
    st.markdown(f"<p style='font-size:20px;'>O seguro é um contrato em que a parte contratada deve compensar a outra parte por eventos específicos que ocorreram ou pelos possíveis prejuízos conforme estipulado nas condições contratuais, ou seja, é um contrato que protege contra riscos financeiros, como saúde, vida, propriedade e automóvel e é uma parte importante do planejamento financeiro pessoal.</p>", unsafe_allow_html=True)

with st.expander("Taxa de Câmbio"):
    st.markdown(f"<p style='font-size:20px;'>A taxa de câmbio é o preço relativo entre duas moedas diferentes. É o valor pelo qual uma moeda pode ser trocada por outra. Ela indica quantas unidades de uma moeda são necessárias para comprar uma unidade de outra moeda e vice-versa.</p>", unsafe_allow_html=True)

with st.expander("Taxa de Juros"):
    st.markdown(f"<p style='font-size:20px;'>A taxa de juros é o custo do dinheiro emprestado ou o ganho sobre o dinheiro investido. Ela influencia seus empréstimos, investimentos e economias, afetando sua situação financeira.</p>", unsafe_allow_html=True)

with st.expander("Taxa SELIC"):
    st.markdown(f"<p style='font-size:20px;'>Selic é a taxa básica de juros da economia brasileira. Basicamente, ela influencia todas as demais taxas de juros do Brasil, como as cobradas em empréstimos, financiamentos, e também afeta o retorno de aplicações financeiras.</p>", unsafe_allow_html=True)

with st.expander("Tesouro Direto"):
    st.markdown(f"<p style='font-size:20px;'>O Tesouro Direto é um investimento de renda fixa, que consiste na compra de títulos da dívida pública. Assim, ao comprar esses títulos, você está emprestando dinheiro ao Governo, que se compromete a devolvê-lo acrescido de juros, na data de vencimento.</p>", unsafe_allow_html=True)