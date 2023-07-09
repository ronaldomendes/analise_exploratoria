import pandas as pd

df = pd.read_csv('arquivos/Base Titanic.csv')
titanic = df[['Survived', 'Pclass', 'Age']]

homens = df.query('Sex == "male"')['Sex'].count()
homens_sobreviventes = df.query('Sex == "male" and Survived == 1')['Sex'].count()
mulheres = df.query('Sex == "female"')['Sex'].count()
mulheres_sobreviventes = df.query('Sex == "female" and Survived == 1')['Sex'].count()

prob_pessoa = round((homens_sobreviventes + mulheres_sobreviventes) / (homens + mulheres) * 100, 2)
print(f'A probabilidade de uma pessoa sobreviver é de {prob_pessoa} %')

prob_homem = round(homens_sobreviventes / homens * 100, 2)
print(f'A probabilidade de um homem sobreviver é de {prob_homem} %')

segunda_classe = df.query('Sex == "male" and Pclass == 2')['Pclass'].count()
prob_seg = round(segunda_classe / homens * 100, 2)
print(f'A probabilidade de um homem sobreviver na segunda classe é de {prob_seg} %')

terceira_classe = df.query('Pclass == 3')['Pclass'].count()
prob_mulher = round(mulheres_sobreviventes / mulheres * 100, 2)
print(f'A probabilidade de uma mulher sobreviver é de {prob_mulher} %')

prob_terc = round(terceira_classe / (homens + mulheres) * 100, 2)
print(f'A probabilidade de uma pessoa sobreviver na terceira classe é de {prob_terc} %')
