import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
chart_data=pd.DataFrame(np.random.randn(20,2),columns=['line-2','line-3'])
st.line_chart(chart_data)

st.area_chart(chart_data)

st.bar_chart(chart_data)

st.subheader('Distribution Plot ')
data=np.random.randint(0,10,100)
data=pd.DataFrame(data)
fig=plt.figure(figsize=(15,8))
data.value_counts().plot(kind='pie')
st.pyplot(fig)

st.subheader('distribution plot with seaborn ')
fig=plt.figure(figsize=(15,8))
sns.distplot(data)
st.pyplot(fig)

st.subheader('Multiple Graphs in one column')
col1,col2=st.columns(2)
with col1:
    col1.header = 'kde=False'
    fig1=plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(data,kde=False)
    st.pyplot(fig1)

with col2:
    col2.header = 'hist=False'
    sns.set_theme(style='darkgrid',context='poster')
    fig2=plt.figure()
    sns.distplot(data,hist=False)
    st.pyplot(fig2)  
st.subheader('Scatter plot')
fig,ax=plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)