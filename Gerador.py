import pandas as pd

def processar_atendimentos(file_path):

    df = pd.read_excel(file_path)

    df_desejado = df[colunas_desejadas]


    if 'Cliente' in df_desejado.columns:
        df_desejado.loc[:, 'Cliente'] = df_desejado['Cliente'].str.replace(r'^\d+-', '', regex=True).str.strip()

    if 'Serviço' in df_desejado.columns:
        df_desejado.loc[:, 'Serviço'] = df_desejado['Serviço'].str.replace(r'^\d+-', '', regex=True).str.strip()

    print("Dados lidos:")

    agrupado = df_desejado.groupby('Data')

    for data, group in agrupado:
        print(f"\nAtendimentos de {data}:")
        print(group.drop(columns=['Data']).sort_values(by=['Parte', 'Serviço']).to_string(index=False))

        contagem_servicos = group['Serviço'].value_counts().reset_index()
        contagem_servicos.columns = ['Serviço', 'Quantidade']


        print("\nContagem de serviços:")
        print(contagem_servicos.to_string(index=False))

        x = group['Parte'].sum()
        print("Ganhos do dia: "+str(x))
        print("\n----------------------------------------------------\n")


colunas_desejadas = ['Data', 'Cliente', 'Serviço', 'Parte']


file_path = "atendimentos.xlsx"

processar_atendimentos(file_path)