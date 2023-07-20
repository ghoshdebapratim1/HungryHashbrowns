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

## Removed Irrelevant Columns 

## Removing Missing Values 

## Removed duplicated 




