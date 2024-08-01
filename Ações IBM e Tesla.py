import quandl
import pandas as pd
import matplotlib.pyplot as plt

# Define a chave de API
quandl.ApiConfig.api_key = 'gbfyz8FHhdc3Y_8q4Btf'

# Obtém os dados das ações da IBM e da Tesla
ibm = quandl.get('WIKI/IBM')
tesla = quandl.get('WIKI/TSLA')

# Cria uma nova figura com 1 linha e 2 colunas para os gráficos
plt.figure(figsize=(15, 5))

# Plota o gráfico das ações da IBM
plt.subplot(1, 2, 1)
plt.plot(ibm.index, ibm['Adj. Close'])
plt.title('Ações da IBM')
plt.ylabel('Preço ($)')

# Plota o gráfico das ações da Tesla
plt.subplot(1, 2, 2)
plt.plot(tesla.index, tesla['Adj. Close'], 'r')
plt.title('Ações da Tesla')
plt.ylabel('Preço ($)')
plt.show()
