#https://datahub.io/ to find some datasets
#https://data.nasa.gov/browse?q=stars&sortBy=relevance also
#http://dados.gov.br/

import pandas as pd
import matplotlib

dataset = pd.read_csv("datasets_starwars_planets.csv")

print("\n ---------esse é o nosso dataset--------- \n")
print(dataset)

print("\n ---------essas são as nossas colunas no dataset--------- \n")
print(dataset.columns.values)

#agora vamos filtrar os dados e selecionar dados por nome/terreno/surface_water

columns_from_dataset = dataset.columns.values
selected_columns = ['name', 'terrain', 'surface_water']
filtered_dataset = dataset.filter(items = selected_columns)
print("\n ---------esse é o dataset filtrado com o que nos importa--------- \n")
print(filtered_dataset)

#se vc estiver utilizando muitos dados e seu PC estiver tendo dificuldades para processá-los, 
#para acelerar o processamento vc pode reduzir as linhas tambem. Utilize isso:
# filtered_dataset[0:100] 
#assim vc esta escolhendo quais linhas quer trabalhar



