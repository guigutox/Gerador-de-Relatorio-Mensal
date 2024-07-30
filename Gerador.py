import pandas as pd



# Função para processar os dados
def processar_atendimentos(file_path):
    # Ler o arquivo Excel
    df = pd.read_excel(file_path)

    # Exibir os dados lidos (para verificação)
    print("Dados lidos:")

    teste = df.sort_values(by=['Data', 'Valor Estab.'])

    print(teste)




file_path = "atendimentos.xlsx"

processar_atendimentos(file_path)