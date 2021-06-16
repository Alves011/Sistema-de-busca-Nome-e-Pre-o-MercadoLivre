import pandas as pd
from mercadolivre2 import manda
#lista 
date = []

df = pd.DataFrame(data=date,columns=['NOME PRODUTO','VALOR PRODUTO'])
tupla = manda.manda_infomacao()
#print(tupla[0])

novo = ['ola',f'{i}']
df.loc[len(df)] = novo
print(df)
