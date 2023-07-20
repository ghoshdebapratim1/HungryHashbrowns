#import libraries
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff


#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
st.title("Attributes of Songs on Spotify")

st.header('Intro About our Project ')
st.write("Our project is on the attributes of spotify songs. The goal of out project is to answer different questions about the dataset and make visualizations to go with it. We looked at the different categories in the dataset and started forming questions to answer in our project. We made visualizations to go with the questions to see different relations and correlations among the dataset. The visualizations make it easier to understand the data and the different correlations and relations we found while doing this project.")

st.header('Team Members Intro ')

st.markdown("- Riana: Hi my name is Riana Abdulle. I am 15 years old and I live in Arizona. In the last week I have been learning about the basics of Python and how to make visualizations using a dataset. I have learned how to take questions about a dataset and turn it into something I can look at.")
st.markdown("- Elayeh: Hi my name is Elayeh Thorpe. I'm currently 15 years old. I'm from Georgia. Over the last few days I've been learning more and more about data science and how to code in Python. Specifically, I've learned how to create data visualizations and how to analyze datasets. I'm now able to use this new information to turn datasets into something that is easier to look at." )



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

st.write("From this we can see that alt z is is genre with the most hours played, and that pop genres are the more popular genres with more hours played than other genres.")

st.subheader("Question 2 : Which genre has more danceability than other?")

df_plot=pd.DataFrame(df.groupby('genre')['danceability'].mean().sort_values(ascending=False).head(20)).reset_index()

df_plot.columns=['genre','avg_danceability']

fig = px.bar(df_plot,x='genre',y='avg_danceability',color='genre',title='Genre vs Average Danceability')

st.plotly_chart(fig)

st.write("From this chart we can see that canadian old school hip hop has the most danceability than the others followed by trap queen and russian drill.")

st.subheader("Question 3 : Is the loudness realted to the genre?")

df_plot=pd.DataFrame(df.groupby('genre')['loudness'].mean().sort_values(ascending=False).head(20)).reset_index()

df_plot.columns=['genre','avg_loudness']


fig = px.bar(df_plot,x='genre',y='avg_loudness',color='genre',title='Genre vs Average Loudness')

st.plotly_chart(fig)

st.write("From this chart we can see that the loudest genre is j-idol followed by aggresive phonk and modern dream pop.")

st.subheader("Question 4 : What are the top soundtracks in terms of hours played?")

df_plot=df[["trackName", "hrPlayed"]].sort_values(by="hrPlayed", ascending=False).head(20)

fig=px.bar(df_plot, x="trackName", y="hrPlayed")

st.plotly_chart(fig)

st.write("From this we can see that the top soundtracks are Sparkle - movie ver. and there is a huge gap between this soundtrack and the others.")

st.subheader("Question 5 : What is the correlation between each categorie?")

numerical_df = df[['msPlayed', 'danceability', 'energy','loudness','speechiness','acousticness','instrumentalness','liveness','valence','tempo','duration_ms']]

df_corr = numerical_df.corr() # Generate correlation matrix
x = list(df_corr.columns)
y = list(df_corr.index)
z = np.array(df_corr)

figSix = ff.create_annotated_heatmap(
    z,
    x = x,
    y = y ,
    annotation_text = np.around(z, decimals=2),
    hoverinfo='z',
    colorscale='Blues',
    showscale=True,
    )
figSix.update_xaxes(side="bottom")
figSix.update_layout(
    title_text='Correlation Heatmap',
    title_x=0.5,
    width=1000,
    height=1000,
    yaxis_autorange='reversed',
    template='plotly_dark'
)

st.plotly_chart(figSix)

st.write("This heatmap shows the correlation between each categorie in the dataset. The darker colors shows a strong relationship while the lighter colors shows a weaker relationship.")
##############################################################################################

st.header('Elayeh - Viz')

st.subheader(' Question 1 : What genre has the higher instrumentalness ') ## Elayeh 

df_plot=pd.DataFrame(df.groupby('genre')['instrumentalness'].mean().sort_values(ascending=False)).head(10).reset_index()

df_plot.columns=['genre','avg_intrumentalness']


fig = px.bar(df_plot,x='genre',y='avg_intrumentalness', color= 'genre', title='Genre vs Average Instrumentalness')
st.plotly_chart(fig)
st.write("From this chart we can gather that Chiptune has the highest instrumentalness out of all of the genres. We can also understand that most of the genres with higher instrumentalness are the ones that typically have less speech in it such as classical and lo-fi music.")

st.subheader(' Question 2 : What genre has more valence?')
df_plot=pd.DataFrame(df.groupby('genre')['valence'].mean().sort_values(ascending=False)).head(10).reset_index()

df_plot.columns=['genre','avg_valence']


fig = px.bar(df_plot,x='genre',y='avg_valence', color= 'genre', title='Genre vs Average Valence')
st.plotly_chart(fig)
st.write("From this chart we can understand that the blues genre has the highest average valence.")

st.subheader(' Question 3 : Is there a relation between speechiness and duration?')
fig=px.scatter(df,x='speechiness', y='duration_ms', title='Speechiness vs Duration')
st.plotly_chart(fig)

st.write("From this chart we can understand that the lower the speechiness is the higher the duration of the track is.")

st.subheader(' Question 4: Who are the Top Artists')
df_plot=pd.DataFrame(df.groupby('artistName')['hrPlayed'].sum().sort_values(ascending=False).head()).reset_index()

df_plot.columns=['artistName','TotalhrPlayed']

fig=px.bar(df_plot,x='artistName',y='TotalhrPlayed',color='artistName',title='Top Artists')
st.plotly_chart(fig) 

st.write("This chart helps us  understand who are the top artists.")

st.subheader(' Question 5: Which genres are major or minor?')
df_plot=pd.DataFrame(df.groupby(['genre','mode']).size()).reset_index()

df_plot.columns=['genre','mode','count']
fig = px.sunburst(df_plot, path=['mode', 'genre'], values='count', color='mode')
st.plotly_chart(fig)
st.write("This chart tells us that there are more major than minor tracks and that Alt Z and Pop have more tracks in the major area.")

st.subheader(" Question 6: How does the distribution of tempos vary among different genres?")
df_plot=pd.DataFrame(df.groupby('genre')['hrPlayed'].sum().sort_values(ascending=False).head(10)).reset_index()

df_plot.columns=['genre','tempo']

df_plot_new=df[df['genre'].isin(df_plot['genre'])]

fig=px.box(df_plot_new,x='genre',y='tempo',color='genre',title='Tempo Distribution by Genre')
st.plotly_chart(fig)
st.write("From this chart we can understand that singer-songwriter pop has one of the widest ranges of tempo and that Japanese teen pop has the shortest range of tempo.")

st.header('Conclusion')
st.write("In conclusion, we have used our newfound data visualization skills to find correlations between various bits of data within our dataset. Every chart shown has made it easier to process and understand this information. We have come to understand from our charts that Alt z and Pop seem to be the popular genres within gour dataset. We have also learned that the canadian old hip hop genre has the most danceability. It can be found in our data that the blues genre has the most average valence. There is much information that can be found within our data visualisations.")
