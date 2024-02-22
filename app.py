import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from PIL import Image
# Title
st.title("Web app using streamlit")
#Image
st.image("download.png")


st.title("Case study on diamond Dataset")
st.image("dimoand image.jpg")
data=pd.read_csv("diamonds.csv")
data
st.write("shape of a dataset", data.shape)
menu=st.sidebar.radio("Menu",["Home","prediction price"])
if menu== "Home":
    st.header("Tabular data of diamond")
    if st.checkbox("Tabular Data"):
        st.table(data.head(150))
        st.header("Statistical summary of a dataframe")
        if st.checkbox("Statistics"):
            st.table(data.describe())
            st.title("Graphs")
            graph=st.selectbox("Different types of graphs",["Scatter plot","Bar Graph","Histogram"])
            if graph=="Scatter plot":
                value=st.slider("Filter data using carat",0,6)
                data=data.loc[data["carat"]>=value]
                fig,ax=plt.subplots(figsize=(10,5))
                sns.scatterplot(data=data,x="carat",y="price",hue="cut")
                st.pyplot(fig)
            if graph=="Bar Graph":
                fig,ax=plt.subplots(figsize=(3.5,2))
                sns.barplot(x="cut",y=data.cut.index,data=data)
                st.pyplot(fig)
            if graph=="Histogram":
                fig,ax=plt.subplots(figsize=(5,3))
                sns.distplot(data.price,kde=True)
                st.pyplot(fig)
if menu=="prediction price":
     st.title("prediction price of a diamond")
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
x=np.array(data["carat"]).reshape(-1,1)
y=np.array(data["price"]).reshape(-1,1)
lr.fit(x,y)
value=st.number_input("carat",0.20,5.01,step=0.15)
value=np.array(value).reshape(1,-1)
prediction=lr.predict(value)[0]
if st.button("price prediction ($)"):
    st.write(f"{prediction}")