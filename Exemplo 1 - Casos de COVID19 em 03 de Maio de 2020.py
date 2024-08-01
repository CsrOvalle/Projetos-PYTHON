#Dados de contaminação pela COVID-19 em 03/05/2020
import plotly as py
import plotly.graph_objs as go
data = dict (type = 'choropleth',
    
    #Lista de países
    locations = ['USA','Spain','Italy','UK','France','Germany','Russia','Turkey','Brazil','Iran'], 
    locationmode = 'country names', 
    
    #Indicar uma escala a partir de suas cores ou a partir de escalas pré-determinadas
    colorscale = ['Yellow', 'Orange', 'Red'],
    
    #Lista dos valores 
    z=[1188122,247122,210717,186599,168693,165664,134687,126045,101147,97424])
map = go.Figure(data=[data])  #'Figure' é a estrutura básica para criar gráficos no 'Plotly' 
map.show()                    #'data' é a lista de dados passada como parâmetro para o construtor 'Figure'