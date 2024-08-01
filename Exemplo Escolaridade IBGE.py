import matplotlib.pyplot as plt 

#Dados do gráfico
labels = ('Nenhum','Fundamental','Médio','Superior')
sizes = [86026, 28525, 57394, 25286]
colors = ['gold','yellowgreen','coral','lightskyblue']

#Cria o gráfico em pizza
patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct ='%1.1f%%', startangle=90) #Plt.pie cria um gráfico do tipo pizza                                                              
plt.legend(patches, labels, loc= "lower right")                                              #Adiciona uma legenda para o gráfico
plt.axis('equal')                                                                            #Escala dos eixos X e Y                                                       
plt.show()                                                                   
