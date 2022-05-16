import pandas as pd

#Lê o arquivo csv e remove a coluna de ID
data = pd.read_csv('data2.csv').drop(columns = 'ID')


#Pega as estatisticas de cada posição
def estatisticas(elemento):
    media   = elemento.mean(numeric_only = True)
    moda    = elemento.mode(numeric_only = True) 
    mediana = elemento.median(numeric_only = True)
    desvio  = elemento.std(numeric_only = True)

    #Cria um dicionario de listas contendo os dados do DataFrame
    dados = {"Stats": data.drop(columns = 'Position').columns.values, #Uma lista feita com os valores das colunas('Position' e 'ID' removidas)
             "Media": media.values,
             "Moda": moda.iloc[0].values,
             "Mediana": mediana.values,
             "Desvio": desvio.values}

    #Cria o DataFrame
    return pd.DataFrame(dados)


def save_files():
    nomes = data.Position.drop_duplicates().values #Cria uma lista com os valores das posições e remove as duplicatas
    nomes.sort() #Organiza a lista

    #Loop para criar um aqruivo CSV de cada posição com seu respectivo nome
    for i in range(len(nomes)):
        position = data.loc[data['Position'] == nomes[i]] #Cria um DataFrame com todos os valores que pertencem a posição atual
        
        df = estatisticas(position)
        df.to_csv("_" + nomes[i] + ".csv", index = False)

save_files()
