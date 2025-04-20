import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head().to_string())
print(df.info())

# Objetivo: analisar as avaliações dos produtos com a quantidade vendida.

#Passo 1: Gráfico de Histograma
plt.figure(figsize=(10,6))
plt.hist(df['Nota'], bins=20, color='#1091ba', alpha=0.8)
plt.title('Histograma - Distribuição das Notas')
plt.xlabel('Notas')
plt.ylabel('Frequência')
plt.grid(True)
#plt.show()

#Passo 2: Gráfico de dispersão
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
sns.scatterplot(x='Qtd_Vendidos_Cod', y ='N_Avaliações_MinMax', data=df)
plt.title('Dispersão do N_avaliações por Qtd Vendidos')

plt.subplot(1,2,2)
sns.scatterplot(x='Desconto_MinMax', y ='N_Avaliações_MinMax', data=df)
plt.title('Dispersão do N_avaliações pelo Desconto')

plt.tight_layout()
#plt.show()

#Passo 3: Mapa de calor
df_corr = df[['Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto_MinMax', 'Preço_MinMax', 'Marca_Cod', 'Material_Cod', 'Temporada_Cod', 'Qtd_Vendidos_Cod']].corr()
plt.figure(figsize=(10,7))
sns.heatmap(df_corr, annot=True, fmt='.2f')
plt.title('Mapa de Calor da Correlação das Variáveis')
#plt.show()

#Passo 4: Gráfico de barra
x = df['Temporada'].value_counts().index
y = df['Temporada'].value_counts().values
plt.figure(figsize=(10,6))
plt.bar( x, y,color='#60aa65')
plt.title('Divisão por Temporada')
plt.xlabel('Temporadas')
plt.ylabel('Quantidade')
plt.xticks(rotation=10)
#plt.show()

#Passo 5: Gráfico de pizza
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values
plt.figure(figsize=(10,6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=180, textprops={'fontsize': 7})
plt.title('Porcentagem dos Gêneros')
plt.tight_layout()
#plt.show()

#Passo 6: Gráfico de densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['Nota'], fill=True, color='#1091ba')
plt.title('Densidade das Notas')
plt.xlabel('Notas')
#plt.show()


#Passo 7: Gráfico de Regressão
plt.figure(figsize=(10,6))
sns.regplot(x='Nota', y='Preço', data=df, color='#278f65', scatter_kws={'alpha':0.5, 'color': '#34c289'})
plt.title('Regressão do Preço por Nota')

plt.tight_layout()
plt.show()