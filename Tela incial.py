import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Funções para cada opção do menu
def oque_e_blockchain():
    return ("Blockchain é uma tecnologia que permite o registro seguro e transparente de informações.\n"
            "Imagine um livro de registro digital que é compartilhado entre várias pessoas, onde cada\n"
            "página é um bloco de informações. Esses blocos estão ligados entre si, formando uma cadeia\n"
            "(daí o nome blockchain). Por exemplo, a tecnologia é usada em criptomoedas como o Bitcoin.")

def criptomoedas_sao_seguras():
    return ("As criptomoedas são consideradas seguras devido à tecnologia blockchain, que utiliza\n"
            "criptografia para proteger as transações. Isso significa que cada transação é registrada\n"
            "de forma imutável e pode ser verificada por qualquer pessoa, o que dificulta fraudes.")

def sistema_mercado_p2p():
    return ("A blockchain possibilita a criação de mercados de energia peer-to-peer (P2P), onde\n"
            "indivíduos e pequenas empresas podem comprar e vender energia diretamente entre si,\n"
            "sem a necessidade de uma autoridade central. Por exemplo, imagine um bairro onde os\n"
            "moradores possuem painéis solares e vendem o excedente de energia para vizinhos.")

def contratos_inteligentes():
    return ("Contratos inteligentes na blockchain permitem que transações de energia sejam automatizadas\n"
            "de acordo com regras predefinidas, sem a necessidade de intervenção humana. Por exemplo,\n"
            "uma casa com excedente de energia solar pode automaticamente vendê-la a um vizinho a um\n"
            "preço predefinido.")

def criacao_tokens_energia():
    return ("A blockchain permite a criação de tokens de energia, onde a energia produzida é convertida\n"
            "em tokens digitais que representam uma unidade de energia. Esses tokens podem ser trocados,\n"
            "vendidos ou armazenados, promovendo a descentralização.")

def transparencia_rastreabilidade():
    return ("A blockchain permite rastrear a origem e o tipo de energia consumida, garantindo que os\n"
            "consumidores estão comprando energia de fontes renováveis e sustentáveis.")

def reducao_custos():
    return ("Tradicionalmente, a venda e compra de energia dependem de intermediários, como concessionárias.\n"
            "Com blockchain, consumidores e pequenos geradores podem negociar diretamente, eliminando custos\n"
            "desnecessários.")

def micro_redes_autonomas():
    return ("A blockchain pode apoiar a criação de micro-redes descentralizadas, permitindo que comunidades\n"
            "locais operem de forma autônoma e independente das grandes redes energéticas.")

def gerar_grafico_efetividade():
    # Dados para o gráfico
    data = {
        "Tipo de Energia": ["Solar", "Eólica", "Hidrelétrica", "Carvão", "Gás Natural"],
        "Geração em kWh": [1200, 1000, 800, 600, 500],  # # Exemplo de geração mensal
        "Custo Mensal Médio": [120, 80, 40, 90, 60]  # Exemplo de custo mensal
    }
    df = pd.DataFrame(data)

    # Criando o gráfico
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Gráfico de barras para Geração em kWh
    color = 'tab:blue'
    ax1.set_xlabel('Tipo de Energia')
    ax1.set_ylabel('Geração em kWh', color=color)
    ax1.bar(df['Tipo de Energia'], df['Geração em kWh'], color=color, alpha=0.6, label='Geração em kWh')
    ax1.tick_params(axis='y', labelcolor=color)

    # Criando um segundo eixo para o custo
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Custo Mensal Médio (R$)', color=color)
    ax2.plot(df['Tipo de Energia'], df['Custo Mensal Médio'], color=color, marker='o', label='Custo Mensal Médio')
    ax2.tick_params(axis='y', labelcolor=color)

    # Adicionando título e legendas
    plt.title('Comparação de Efetividade entre Tipos de Energia')
    fig.tight_layout()  # Para evitar sobreposição de eixos
    plt.show()

def custo_energia():
    # Lista de informações sobre tipos de energia
    energia_info = [
        {
            "Tipo": "Solar",
            "Custo de Implementação": "R$ 5.000,00 por kW",
            "País que mais usa": "Alemanha",
            "Efetividade": "Alta",
            "Produção em kWh": 1200
        },
        {
            "Tipo": "Eólica",
            "Custo de Implementação": "R$ 4.000,00 por kW",
            "País que mais usa": "Estados Unidos",
            "Efetividade": "Alta",
            "Produção em kWh": 1000
        },
        {
            "Tipo": "Hidrelétrica",
            "Custo de Implementação": "R$ 3.000,00 por kW",
            "País que mais usa": "Brasil",
            "Efetividade": "Muito Alta",
            "Produção em kWh": 800
        },
        {
            "Tipo": "Carvão",
            "Custo de Implementação": "R$ 2.500,00 por kW",
            "País que mais usa": "China",
            "Efetividade": "Média",
            "Produção em kWh": 600
        },
        {
            "Tipo": "Gás Natural",
            "Custo de Implementação": "R$ 3.500,00 por kW",
            "País que mais usa": "Estados Unidos",
            "Efetividade": "Média",
            "Produção em kWh": 500
        }
    ]

    print("Tipo de Energia | Custo de Implementação | País que mais usa | Efetividade | Produção em kWh")
    print("-" * 90)
    for info in energia_info:
        print(f"{info['Tipo']: <15} | {info['Custo de Implementação']: <22} | {info['País que mais usa']: <18} | {info['Efetividade']: <12} | {info['Produção em kWh']}")

def gerar_mapa_3d():
    # Dados fictícios para os países e suas principais fontes de energia
    data = {
        "País": ["Brasil", "Alemanha", "Estados Unidos", "China", "Índia"],
        "Fonte de Energia": ["Hidrelétrica", "Eólica", "Gás Natural", "Carvão", "Solar"],
        "Latitude": [-14.2350, 51.1657, 37.0902, 35.8617, 20.5937],
        "Longitude": [-51.9253, 10.4515, -95.7129, 104.1954, 78.9629]
    }
    df = pd.DataFrame(data)

    # Criando o mapa 3D
    fig = px.scatter_geo(df,
                         lat='Latitude',
                         lon='Longitude',
                         text='País',
                         hover_name='País',
                         hover_data={'Fonte de Energia': True},
                         title='Mapa 3D das Principais Fontes de Energia por País',
                         projection='natural earth')

    fig.update_traces(marker=dict(size=10, opacity =0.8, line=dict(width=0.5, color='white')))
    fig.show()

def menu():
    print("Escolha uma opção:")
    print("1. Informações sobre nosso projeto")
    print("2. Criar mapa 3D das principais fontes de energia")
    print("0. Sair")

    opcao = input("Digite sua opção: ")
    return opcao

def menu_informacoes():
    print("Escolha uma opção:")
    print("1. O que é blockchain?")
    print("2. Criptomoedas são seguras?")
    print("3. Como a blockchain ajuda no mercado P2P?")
    print("4. O que são contratos inteligentes?")
    print("5. Como criar tokens de energia?")
    print("6. Transparência e rastreabilidade na energia")
    print("7. Redução de custos com blockchain")
    print("8. Micro-redes autônomas")
    print("9. Gerar gráfico de efetividade")
    print("10. Custo da energia")
    print("0. Voltar")

    while True:
        opcao = input("Digite sua opção: ")
        if opcao in [str(i) for i in range(11)]:
            return opcao
        else:
            print("Opção inválida. Tente novamente.")

def boas_vindas():
    nome = input("Digite seu nome: ")
    print(f"Bem-vindo(a), {nome}! Vamos explorar as informações sobre nosso projeto.")

if __name__ == "__main__":
    boas_vindas()
    while True:
        opcao = menu()
        if opcao == "1":
            while True:
                sub_opcao = menu_informacoes()
                if sub_opcao == "1":
                    print(oque_e_blockchain())
                elif sub_opcao == "2":
                    print(criptomoedas_sao_seguras())
                elif sub_opcao == "3":
                    print(sistema_mercado_p2p())
                elif sub_opcao == "4":
                    print(contratos_inteligentes())
                elif sub_opcao == "5":
                    print(criacao_tokens_energia())
                elif sub_opcao == "6":
                    print(transparencia_rastreabilidade())
                elif sub_opcao == "7":
                    print(reducao_custos())
                elif sub_opcao == "8":
                    print(micro_redes_autonomas())
                elif sub_opcao == "9":
                    gerar_grafico_efetividade()
                elif sub_opcao == "10":
                    custo_energia()
                elif sub_opcao == "0":
                    break
        elif opcao == "2":
            gerar_mapa_3d()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")