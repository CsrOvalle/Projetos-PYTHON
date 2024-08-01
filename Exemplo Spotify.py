import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

#Dados do gráfico
musicas = ('Liberdade Provisória','Sentadao','Combatchy','Surtada','Cheirosa')
indice = np.arange(len(musicas))
acessos = [1068254, 866216,849895,763652,758198]

#Definindo cores e transparência para cada barra 
cores = [
    (1.0, 0.0, 0.0, 0.7),  # Vermelho com 70% de transparência
    (0.0, 1.0, 0.0, 0.7),  # Verde com 70% de transparência
    (0.0, 0.0, 1.0, 0.7),  # Azul com 70% de transparência
    (1.0, 1.0, 0.0, 0.7),  # Amarelo com 70% de transparência
    (1.0, 0.5, 0.0, 0.7)   # Laranja com 70% de transparência
]

#Criando o Gráfico
plt.barh(indice, acessos, color=cores)
plt.yticks(indice, musicas)
plt.ylabel('Acessos')
plt.title('Ranking do Spotify 31 Dez. 2019')
plt.ticklabel_format(style = 'plain', axis = 'y')
plt.show()