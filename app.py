import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px 
from PIL import Image



df=pd.read_csv(r"fitness_exercises.csv")

df.drop('id',axis=1,inplace=True)

df.rename({'bodyPart':"Body_Part", 'target':'Target_Muscle','name':'Exercise_Name','gifUrl':'Exercise_gif','equipment':"Equipment"},axis=1,inplace=True)


## Side Bar
html_sidebar_heading="""
<div style='background-color:#0b2038;'>
<h1 style="color: white; text-align: center">Analytics</h1>
</div>
"""

st.sidebar.markdown(html_sidebar_heading,unsafe_allow_html=True)



a=st.sidebar.selectbox("Select a Feature",df.columns)
b=st.sidebar.selectbox("Select Feature to compare",df.columns[1:])

if st.sidebar.button('Go'):
    bb=df.groupby(b).apply(lambda df:df[a].value_counts().sum()).sort_values(ascending=False).head(15)
    bb_px=px.bar(bb,title=f'Top 15 Most Used {b} by {a}')
    bb_px



## Main Page 

def main():
    html_sidebar_heading="""
    <div style='background-color:#010101;'>
    <h1 style="color: yellow; text-align: center; font-size:50px">Fitness</h1>
    </div>
    """

    st.markdown(html_sidebar_heading,unsafe_allow_html=True)



    body_part=st.selectbox('Body Part',df['Body_Part'].unique())



    target_muscle=st.selectbox('Muscle',df[df['Body_Part']==body_part]['Target_Muscle'].unique())


    if st.button('Find'):
        #ex=(
        #    df[(df['Body_Part']==body_part) & (df['Target_Muscle']==target_muscle)]['Exercise_Name'].values
     #)

    #ex_bar=px.bar(ex,width=800,height=700,title="<b>Exercise Name for Your Muscle Group<b>")
    #st.plotly_chart(ex_bar)
    #st.write(ex)
        gif_url=(
            df[(df['Body_Part']==body_part) & (df['Target_Muscle']==target_muscle)]['Exercise_gif'].values
        )
        for i in gif_url:
            ex=df[df['Exercise_gif']==i]['Exercise_Name'].values[0]
            st.subheader(ex)
            st.image(i)


if __name__=="__main__":
    main()
