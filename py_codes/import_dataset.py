#https://datahub.io/ to find some datasets
#https://data.nasa.gov/browse?q=stars&sortBy=relevance also
#http://dados.gov.br/
#https://minerandodados.com.br/como-conseguir-datasets-de-projetos-reais-para-usar-no-seu-portfolio/

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("datasets_starwars_planets.csv")

print("\n ---------esse é o nosso dataset--------- \n")
print(dataset)

print("\n ---------essas são as nossas colunas no dataset--------- \n")
print(dataset.columns.values)

#agora vamos filtrar os dados e selecionar dados por nome/terreno/surface_water/gravidade

columns_from_dataset = dataset.columns.values
selected_columns = ['name', 'terrain', 'surface_water','gravity']
filtered_dataset = dataset.filter(items = selected_columns)
print("\n ---------esse é o dataset filtrado com o que nos importa--------- \n")
print(filtered_dataset)

#se vc estiver utilizando muitos dados e seu PC estiver tendo dificuldades para processá-los, 
#para acelerar o processamento vc pode reduzir as linhas tambem. Utilize isso:
# filtered_dataset[0:100] 
#assim vc esta escolhendo quais linhas quer trabalhar

print('printando a coluna de valores de gravidade')
column_gravity = filtered_dataset['gravity']  #escolhendo apenas uma coluna
print(column_gravity)

print('contando os valores de ocorrencias de gravidade')
counting_gravity = column_gravity.value_counts().sort_index() #contando cada ocorrencia de valor da gravidade
print(counting_gravity)

print('printando a coluna de agua na superficie')
column_water = filtered_dataset['surface_water']  #escolhendo apenas uma coluna
print(column_water)

print('contando os valores de ocorrencias de agua na superficie')
counting_water = column_water.value_counts().sort_index() #contando cada ocorrencia de valor da gravidade
print(counting_water)

print("histograma da distribuição de gravidade")
column_gravity.fillna(method='ffill', limit=10000) #preenchendo os NAN 
plt.hist(column_gravity, bins=30)
plt.show()

print("histograma de distribuição de agua na superficie")
column_water.fillna(method='ffill', limit=10000)
plt.hist(column_water, bins=30)
plt.show()