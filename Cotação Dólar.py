from pandas import  read_csv
from matplotlib import pyplot
series = read_csv(r"d:\Projetos PYTHON\Visualização Da Informação\Unidade II\Dataset - USD_BRL_hist.csv", header=0, index_col = 0, parse_dates=True)
series.plot()
pyplot.show()