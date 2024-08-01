import matplotlib.pyplot as plt #Utiliza a biblioteca Matplotlib

fig, gnt = plt.subplots()

gnt.set_ylim(0, 50)  # Define os limites do eixo y
gnt.set_xlim(0, 160)  # Define os limites do eixo x
gnt.set_xlabel('Dias de projeto')
gnt.set_ylabel('Tarefas')  # Define o rótulo do eixo y
gnt.set_yticks([15, 25, 35])
gnt.set_yticklabels(['Tarefa 1', 'Tarefa 2', 'Tarefa 3'])
gnt.grid(True)
gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (30, 9), facecolors=('tab:red'))
gnt.broken_barh([(40, 50)], (20, 9), facecolors=('tab:green'))
gnt.broken_barh([(110, 10), (150, 10)], (10, 9), facecolors=('tab:blue'))

plt.show()