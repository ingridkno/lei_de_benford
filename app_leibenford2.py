import streamlit as st
import math
import pandas as pd
import plotly.graph_objects as go
import numpy as np

st.set_page_config(layout="wide")



uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
     # can be used wherever a "file-like" object is accepted:
     number = st.number_input('insert a number', value=1, step=1)
     st.write('the current number is ', number)

     header=int(number)
     df = pd.read_excel(uploaded_file, header=header)
     #st.write(df.astype(str))

     st.dataframe(df.astype(str))


coluna_escolhida = st.selectbox(
     'Escolha uma coluna para análise',
     df.columns)

st.write('You selected:', coluna_escolhida)

lei_benford = [math.log10(1 + 1/d) for d in range(1,10)]
#st.dataframe(pd.to_numeric(df[coluna_escolhida].astype(str).str[0], errors='coerce').dropna())
#df.loc[df[coluna_escolhida].astype(str).str.isnumeric(),coluna_escolhida])


lista_primeiros_digitos= pd.to_numeric(df[coluna_escolhida].astype(str).str[0], errors='coerce').dropna()


###figure
x0 = [s for s in lista_primeiros_digitos.tolist() if s != 0]
x1 = lei_benford

fig = go.Figure() 

fig.add_trace(go.Bar(
    x=[i for i in range(1,10)],
    y=x1,
    name='Lei de Benford'
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
    opacity=0.75
))


fig.update_layout(
    title_text='Comparação com Lei de Benford', # title of plot
    xaxis_title_text='Primeiro Dígito', # xaxis label
    yaxis_title_text='Densidade de Probabilidade', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
)

st.plotly_chart(fig, use_container_width=True)