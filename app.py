import streamlit as st
st.title('Title -> Abhiram Reddy')
st.header('Header -> Abhiram Reddy')
st.subheader('SubHeader -> Abhiram Reddy')
st.text('Text -> Abhiram Reddy')
st.markdown('Markdown -> Abhiram')
st.markdown('# Markdown1 -> Abhiram')
st.markdown('## Markdown2 -> Abhiram')
st.markdown('### Markdown3 -> Abhiram')
st.markdown('#### Markdown4 -> Abhiram')
st.markdown('##### Markdown5 -> Abhiram')
st.success('Hey , you submitted successfully')
st.info('Information displayed')
st.warning('Warning message')
st.error('There is an error')
st.exception(ZeroDivisionError('Cannot divide '))
st.help(ZeroDivisionError)
st.write('range(0,100)')
st.write(range(0,100))
st.write(1*3+6)
st.code('x=10\n'
         'for i in range(x):\n'
         '\tprint(i)')
if(st.checkbox('Male')):
    st.write('You are a male')
if(st.checkbox('Adult')):
    st.write('You are an adult')
radioButton=st.radio('Select your gender ' ,('Male','Female','Others'))
if(radioButton=='Male'):
    st.write('You are a Male')
elif(radioButton=='Female'):
    st.write('You are a Female')
elif(radioButton=='Others'):
    st.write('You are an other gender')
selectBox=st.selectbox('Data Science ' , ['Data Analysis','Machine Learning','Deep Learning','NLP']) 
st.write('You have selected ',selectBox)
multiSelect=st.multiselect('Data Science ' , ['Data Analysis','Machine Learning','Deep Learning','NLP']) 
st.write('You have selected ' , len(multiSelect), 'courses')
st.subheader('Click here to save ')
if st.button('Click me'):
    st.write('Thanks for clicking ')
st.subheader('Slider')
volume=st.slider('Select the volume ' ,0,50,1)
st.write('The volume is ',volume)
st.subheader('Text input')
name=st.text_input('Name :')
password=st.text_input('Password : ',type='password')
st.text_area('Write something about yourself')
st.subheader('Number input')
st.number_input('Enter your age',10,60)
st.subheader('date input')
st.date_input('date')
st.subheader('Time input')
st.time_input('Time')
df=st.file_uploader('Upload the file : ',type=['csv','xlsx'])
if df is not None:
    st.dataframe(df)