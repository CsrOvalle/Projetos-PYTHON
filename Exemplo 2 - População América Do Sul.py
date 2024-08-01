import plotly.graph_objects as go
import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/ismarfrango/visualizacaoCS/master/southAmerica-pop.csv')

fig = go.Figure(data=go.Choropleth(locations=df['name'], #Nome do país
    z = df['pop'].astype(int),                           #Dados para o Choropleth
    locationmode = 'country names',                      #Tipo de identificação geográfica
    colorscale = 'Reds',                                 #Escala contínua em tons de vermelho       
    colorbar_title ='População'))                        #Título da escala de cores

fig.update_layout(title = 'População da América Do Sul - 2019',
    geo_scope='south america')                           #Limita o escopo do gráfico para a América Do Sul
fig.show()