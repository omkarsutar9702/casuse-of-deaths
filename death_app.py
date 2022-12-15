### import libraries-------------------------------------------------------------------------------
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

## import dataset----------------------------------------------------------------------------------
df = pd.read_csv("death_cause.csv")

# create a app-------------------------------------------------------------------------------------
st.set_page_config(layout="wide" , page_title="Cause of death")
st.markdown("<h1 style='text-align: center;'>Cause of deaths</h1>", unsafe_allow_html=True)
### diseses graph-----------------------------------------------------------------------------------
st.markdown("<h3 style='text-align: center;'>Cause of death by different reasons in a single year</h3>", unsafe_allow_html=True)
option = df['year'].unique()
option = sorted(option , reverse=True)
options = st.selectbox('Select the year' , option)
df1 = df[df['year'] == options]
pivot = pd.pivot_table(df1 , values=df1.columns[3:-1] , index='country' , aggfunc=np.sum)
dieses = pivot.columns
option_dis = st.multiselect('Select disease' , dieses , "terrorism")
pivot = pivot.nlargest(20 , option_dis)
fig = px.bar(
    pivot , x = pivot.index , y =  option_dis
            , barmode = 'group' 
            ,labels={
                "country":'Countries',
                "value":"Total Deaths" 
                }
            )
st.plotly_chart(fig ,use_container_width=True)

## country graph-----------------------------------------------------------------------------------
st.markdown("<h3 style='text-align: center;'>Cause of death by different reasons in a single country</h3>", unsafe_allow_html=True)

sel1 = st.selectbox("Select the country you want to analyze" , df['country'].unique())
opt = df['year'].unique()
opt = sorted(opt , reverse=True)
sel2 = st.multiselect("Select the year" , opt, 1991)
country_name= df[(df['country']== sel1) & (df['year'].isin(sel2))]
fig1 = px.bar(country_name , x = 'year', y=country_name.columns[2:], barmode='group',
              labels={
                  "value":"Total Deaths" 
              })
st.plotly_chart(fig1 ,use_container_width=True)
