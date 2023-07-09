import numpy as np
import pandas as pd

AMPLITUDE = 9
COLUNA = 'IDADE'

df = pd.read_excel('arquivos/Base Cobrança.xlsx', sheet_name='Case_cobranca')
df['TEMP_RECUPERACAO'].fillna(0, inplace=True)
print(df.head(15))

limite_min = int(np.floor(df[COLUNA].min()))
limite_max = df[COLUNA].max()

classes = []
while True:
    classes.append([limite_min, limite_min + AMPLITUDE])
    limite_min = limite_min + AMPLITUDE
    if limite_min > limite_max:
        break

valores_classes = []
for classe in classes:
    filtro = df[(classe[0] <= df[COLUNA]) & (df[COLUNA] < classe[1])][COLUNA]
    valores_classes.append(list(filtro))

num_elementos = []
for i in range(len(valores_classes)):
    num_elementos.append(len(valores_classes[i]))

tabela = pd.DataFrame({'Classes': classes, 'Frequencia': num_elementos})
print(tabela)

percentil_35 = 35 * (tabela['Frequencia'].sum() + 1) / 100
print(percentil_35)

media = tabela['Frequencia'].mean()
print(media)

mediana = tabela['Frequencia'].median()
print(mediana)
