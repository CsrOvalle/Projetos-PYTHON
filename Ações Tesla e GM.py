import quandl
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da chave da API Quandl
quandl.ApiConfig.api_key = 'gbfyz8FHhdc3Y_8q4Btf'

# Obtenção dos dados das ações da Tesla e da GM
tesla = quandl.get('WIKI/TSLA')
gm = quandl.get('WIKI/GM')

# Visualização dos preços das ações
plt.plot(gm.index, gm['Adj. Close'], label='GM')
plt.plot(tesla.index, tesla['Adj. Close'], 'r', label='Tesla')
plt.title('Stock Prices')
plt.ylabel('Price ($)')
plt.legend()
plt.show()

# Definição do número de ações em circulação para Tesla e GM
tesla_shares = {2018: 168e6, 2017: 162e6, 2016: 144e6, 2015: 128e6, 2014: 125e6, 2013: 119e6, 2012: 107e6, 2011: 100e6, 2010: 51e6}
gm_shares = {2018: 1.42e9, 2017: 1.50e9, 2016: 1.54e9, 2015: 1.59e9, 2014: 1.61e9, 2013: 1.39e9, 2012: 1.57e9, 2011: 1.54e9, 2010: 1.50e9}

# Cálculo da capitalização de mercado para Tesla e GM
tesla['Year'] = tesla.index.year
tesla['Tesla_Cap'] = tesla['Year'].map(tesla_shares) * tesla['Adj. Close']

gm['Year'] = gm.index.year
gm['GM_Cap'] = gm['Year'].map(gm_shares) * gm['Adj. Close']

# Visualização da capitalização de mercado
plt.plot(gm.index, gm['GM_Cap'] / 1e9, label='GM')
plt.plot(tesla.index, tesla['Tesla_Cap'] / 1e9, 'r', label='Tesla')
plt.title('Market Cap of GM and Tesla')
plt.xlabel('Date')
plt.ylabel('Market Cap (Billions $)')
plt.legend()
plt.show()