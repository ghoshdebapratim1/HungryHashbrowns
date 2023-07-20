#import libraries
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
import plotly.express as px

#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
st.title("Attributes of Songs on Spotify")

st.header('Intro About our Project ')


st.header('Team Members Intro ')

st.markdown("Riana: Hi my name is Riana Abdulle. I am 15 years old and I live in Arizona. In the last week I have been learning about the basics of Python and how to make visualizations using a dataset. I have learned how to take questions about a dataset and turn it into something I can look at.")
st.markdown("Elayeh: Hi my name is Elayeh Thorpe. I'm currently 15 years old. I'm from Georgia. Over the last few days I've been learning more and more about data science and how to code in Python. Specifically, I've learned how to create data visualizations and how to analyze datasets. I'm now able to use this new information to turn datasets into something that is easier to look at." )



st.header('Dataset Description and Pre-Processing')

st.subheader('Sneak-peek into the dataset ')
# Loading our Dataset 
df=pd.read_csv('Spotify_Song_Attributes.csv')

st.write(df.head())  


## Removed Irrelevant Columns - Elayeh
st.subheader('Dropping Irrelevant Columns ')
st.write('All the columns present in the dataset ')
st.write(df.columns)
columns_to_drop = ['id', 'uri','track_href', 'analysis_url']
df.drop(columns_to_drop, axis=1, inplace=True)
st.write(' After dropping the irrelevant columns, the new columns are displayed below ')
st.write(df.columns)

## Removing Missing Values - Riana 
st.subheader('Treating Missing Values')
st.write('Missing Values in the dataset')
st.write(df.isnull().sum())
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
st.write('After dropping missing values  in the dataset')
st.write(df.isnull().sum())

map={1:'Major',0:'Minor'}

df['mode']=df['mode'].map(map)
df['mode'].value_counts()

df['minPlayed']=df['msPlayed']/(1000*60)

df['hrPlayed']=df['msPlayed']/(1000*60*60)

## Removed duplicated 
st.subheader('Dropping Duplicate Values ')
st.write('Number of Rows before dropping duplicates ')
st.write(df.shape[0])
df.drop_duplicates(inplace=True)
st.write('Number of Rows after dropping duplicates ')
st.write(df.shape[0])

st.header('Data Exploration - Answering Questions relevant to our analysis ')

## Riana 
st.header('Riana- Viz')
st.subheader(' Question 1 : What are the top genres in terms of hours played?')

df_plot=pd.DataFrame(df.groupby('genre')['hrPlayed'].sum().sort_values(ascending=False).head(20)).reset_index()

df_plot.columns=['genre','TotalhrPlayed']

fig=px.bar(df_plot,x='genre',y='TotalhrPlayed',color='genre',title='Top Genres')

st.plotly_chart(fig)

st.subheader("Question 2 : Which genre has more danceability than other?")

df_plot=pd.DataFrame(df.groupby('genre')['danceability'].mean().sort_values(ascending=False).head(20)).reset_index()

df_plot.columns=['genre','avg_danceability']


fig = px.bar(df_plot,x='genre',y='avg_danceability',color='genre',title='Genre vs Average Danceability')

st.plotly_chart(fig)

st.subheader("Question 3 : Is the loudness realted tot he genre?")

df_plot=pd.DataFrame(df.groupby('genre')['loudness'].mean().sort_values(ascending=False).head(20)).reset_index()

df_plot.columns=['genre','avg_loudness']


fig = px.bar(df_plot,x='genre',y='avg_loudness',color='genre',title='Genre vs Average Loudness')

st.plotly_chart(fig)

st.subheader("Question 4 : What are the top soundtracks in terms of hours played?")

df_plot=df[["trackName", "hrPlayed"]].sort_values(by="hrPlayed", ascending=False).head(20)

fig=px.bar(df_plot, x="trackName", y="hrPlayed")

st.plotly_chart(fig)

##############################################################################################

st.header('Elayeh - Viz')

st.subheader(' Question 1 : What genre has the higher instrumentalness ') ## Elayeh 

df_plot=pd.DataFrame(df.groupby('genre')['instrumentalness'].mean().sort_values(ascending=False)).head(10).reset_index()

df_plot.columns=['genre','avg_intrumentalness']


fig = px.bar(df_plot,x='genre',y='avg_intrumentalness', color= 'genre', title='Genre vs Average Instrumentalness')
st.plotly_chart(fig)

st.subheader(' Question 2 : What genre has more valence?')
df_plot=pd.DataFrame(df.groupby('genre')['valence'].mean().sort_values(ascending=False)).head(10).reset_index()

df_plot.columns=['genre','avg_valence']


fig = px.bar(df_plot,x='genre',y='avg_valence', color= 'genre', title='Genre vs Average Valence')
st.plotly_chart(fig)

st.subheader(' Question 3 : Is there a relation between speechiness and duration?')
fig=px.scatter(df,x='speechiness', y='duration_ms', title='Speechiness vs Duration')
st.plotly_chart(fig)

st.subheader(' Question 4: Who are the Top Artists')
df_plot=pd.DataFrame(df.groupby('artistName')['hrPlayed'].sum().sort_values(ascending=False).head()).reset_index()

df_plot.columns=['artistName','TotalhrPlayed']

fig=px.bar(df_plot,x='artistName',y='TotalhrPlayed',color='artistName',title='Top Artists')
st.plotly_chart(fig)
