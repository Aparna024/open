import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt 
from plotly import graph_objs as go 
st.title("Salary_Predictor")
nav= st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])
from PIL import Image
data=pd.read_csv("C:/Users/Aparna/Downloads/Salary_Data.csv")
# Load image from file or URL
image = Image.open("C:/Users/Aparna/Downloads/C,C++/data/emp.png")

# Display the image

if nav=='Home':
    
         st.image(image, use_column_width=True)
         if st.checkbox("Show Table"): #to disp a table
                st.table(data)
         
         graph=st.selectbox('Which Graph?',["Non-Interactive","Interactive"])  
         
         if graph=="Non-Interactive":
             plt.figure(figsize= (10,5))
             plt.scatter(data["YearsExperience"],data["Salary"])
             plt.ylim(0)
             plt.xlabel("Years OF Experience")
             plt.ylabel("Salary") 
             plt.tight_layout()
             st.pyplot( )
         
         if graph=="Interactive":
              layout =go.Layout(xaxis=dict(range=[0,16]),yaxis=dict(range=[0,2100000]))
              import plotly.graph_objects as go

              fig = go.Figure(data=go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode='markers'))

              st.plotly_chart(fig)
if nav=='Prediction':
         st.write('pred')

if nav=='Contribute':
         st.write('contri')      
 