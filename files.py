import streamlit as st
import pandas as pd

st.subheader('Uploading a file : ')
df=st.file_uploader('Upload the csv file : ',type=['csv','xlsx'])
if df is not None:
    st.table(df)

    
st.subheader('Dealing with images')
img_file=st.file_uploader('Upload the image file : ',type=['png','jpg','jpeg'])
if img_file is not None:
    st.image(img_file)

    
st.subheader('Working with videos : ')
vid=st.file_uploader('Upload a video : ',['mkv','mp4'])
if vid is not None:
    st.video(vid,start_time=0)


st.subheader('Working with Audios : ')
aud=st.file_uploader('Upload a Audio : ',['wav','mp3'])
if aud is not None:
    st.audio(aud.read())
