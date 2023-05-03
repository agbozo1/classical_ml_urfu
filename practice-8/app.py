#build streamlit app
from numpy import double
import streamlit as st
import pickle

#load model

model = pickle.load(open("D:\codehub\classical_ml_urfu\models\iris-flower-model.pkl",'rb'))

#print(model.predict([[2,2,1,2]]))

st.set_page_config(layout='wide')
st.title('Iris Flower Predictor')


with st.container():
    st.text('This app is going to predict Iris Flower types based on the: sepal and petal lengnth & width')

    with st.form(key='iris_form'):
        st.text('Enter the Details Below')

        sepL = st.text_input(label='Sepal Length')
        sepW = st.text_input(label='Sepal Width')
        petL = st.text_input(label='Petal Length')
        petW = st.text_input(label='Petal Width')

        submit = st.form_submit_button()

        if submit:
            #st.write('Input: '+sepL + ', '+ sepW + ', '+ petL + ', '+ petW)

            #type casting - convert input variables from string to integer
            #place input into model
            
            output = model.predict([[float(sepL), float(sepW), float(petL), float(petW)]])

            st.text('The predicted flower is: '+str(output))

            if output == 'Iris-setosa':
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/413px-Irissetosa1.jpg")

            elif output =='Iris-versicolor':
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Iris_versicolor_3.jpg/800px-Iris_versicolor_3.jpg")

            else: #iris virginica
                st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/330px-Iris_virginica_2.jpg")

