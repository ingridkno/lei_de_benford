import streamlit as st
import math
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from PIL import Image

st.set_page_config(layout="wide")

lei_benford = [math.log10(1 + 1/d) for d in range(1,10)]
x1 = lei_benford

st.title('Lei de Benford')

uploaded_file = st.file_uploader("Insira uma planilha")

if uploaded_file is not None:
     # can be used wherever a "file-like" object is accepted:
     number = st.number_input('Insira o número da linha representante da coluna', value=0, step=1)
     st.write('Número da linha para representar colunas:', number)

     header=int(number)
     df = pd.read_excel(uploaded_file, header=header)
     #st.write(df.astype(str))

     st.dataframe(df.astype(str))


     coluna_escolhida = st.selectbox(
          'Escolha uma coluna para análise',
          df.columns)

     st.write('Coluna selecionada:', coluna_escolhida)
     
     lista_primeiros_digitos= pd.to_numeric(df[coluna_escolhida].astype(str).str[0], errors='coerce').dropna()


     ###figure
     x0 = [s for s in lista_primeiros_digitos.tolist() if s != 0]
    
     fig = go.Figure() 

     fig.add_trace(go.Bar(
         x=[i for i in range(1,10)],
         y=x1,
         name='Lei de Benford',
         text=y,
         textposition='auto'
         ))

     fig.add_trace(go.Histogram(
         x=x0,
         histnorm='probability density',
         name='checagem', # name used in legend and hover labels
         # xbins=dict( # bins used for histogram
         #     start=0,
         #     end=9,
         #     size=0.5
         # ),
         marker_color='#EB89B5',
         opacity=0.75,
         texttemplate="%{x}"
     ))


     fig.update_layout(
         title_text='Comparação com Lei de Benford', # title of plot
         xaxis_title_text='Primeiro Dígito', # xaxis label
         yaxis_title_text='Densidade de Probabilidade', # yaxis label
         bargap=0.2, # gap between bars of adjacent location coordinates
         bargroupgap=0.1, # gap between bars of the same location coordinates
         font=dict(size=18)
     )

     st.plotly_chart(fig, use_container_width=True)
else:
     st.header('Compare um conjunto de valores para indícios de fraude com a Lei de Benford')
     st.write('A Lei de Benford, ou lei do primeiro dígito, refere-se à distribuição de dígitos.') 
     st.write('Ao contrário do que se pensa, a distribuição dos primeiros números não é homogênea e, sim, heterogênea com o primeiro dígito tendo maior probablidade de ser pequeno.') 
     
     fig = go.Figure()
     fig.add_trace(go.Bar(
         x=[i for i in range(1,10)],
         y=x1,
         name='Lei de Benford',
         text=y,
         textposition='auto'
         ))
     fig.update_layout(
         title_text='Lei de Benford', # title of plot
         xaxis_title_text='Primeiro Dígito', # xaxis label
         yaxis_title_text='Densidade de Probabilidade', # yaxis label
         bargap=0.2, # gap between bars of adjacent location coordinates
         bargroupgap=0.1, # gap between bars of the same location coordinates
         font=dict(size=18)
     )
     
     st.plotly_chart(fig, use_container_width=True)

 
image = Image.open('DataIN_logo_estreito.png')
st.image(image, width=500, caption='Produzido por DataIN')
