from plotly import figure_factory as ff #Utiliza a biblioteca 'Plotly'

df = [dict(Task='Tarefa A', Start='2020-01-01', Finish='2020-04-28'), #Formato de data YYYY-MM-DD
dict(Task='Tarefa B', Start='2020-02-05',Finish='2020-04-15'),
dict(Task='Tarefa C',Start='2020-02-20', Finish='2020-05-30')]

colors =  ['#FF0000', (0.0, 1.0, 0.0), 'rgb(0, 0, 255)'] #HEXADECIMAL/ NORMALIZADO/ RGB
fig = ff.create_gantt(df,colors)
fig.show()