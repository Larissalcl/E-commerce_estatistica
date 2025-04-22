import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

df=pd.read_csv('ecommerce_estatistica.csv')
print(df.info())

#Passo 1: Gráfico de Histograma
def criar_histograma (df):
    fig1 = px.histogram(df, x='Nota', nbins=30, title='Distribuição de Salários')
    return fig1

#Passo 2: Gráfico de dispersão
def criar_dispersão (df):
    fig2 = px.scatter(df, x='Qtd_Vendidos_Cod', y ='N_Avaliações_MinMax', color='Nota', hover_name='Temporada')
    fig2.update_layout(
        title='Dispersão do N_avaliações por Qtd Vendidos',
        xaxis_title='Qtd Vendidos',
        yaxis_title='N de Avaliações'
    )
    return fig2
#Passo 3: Mapa de calor
def criar_heatmap (df):
    fig3 =px.density_heatmap(df, x='Qtd_Vendidos', y='Preço')
    fig3.update_layout(
        title='Mapa de Calor da Correlação das Variáveis'
    )
    return fig3

#Passo 4: Gráfico de Pizza
def criar_pizza (df):
    fig4 = px.pie(df, names='Gênero', color='Temporada', hole=0.5, color_discrete_sequence=px.colors.sequential.RdBu)
    return fig4

def criar_app(df):
    #Criar App
    app = Dash(__name__) # iniciar o app

    fig1  = criar_histograma(df)
    fig2 = criar_dispersão(df)
    fig3 = criar_heatmap(df)
    fig4 = criar_pizza(df)


    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4)
    ])
    return app

# Executar App
if __name__ == '__main__':
    app=criar_app(df)

    app.run(debug=True, port=8050) #Debug é verifica cada mudança no código e mostra os erros  #Default 8050(padrão)