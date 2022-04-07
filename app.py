import matplotlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from predict_page import show_predict_page

datframe=pd.read_csv('survey_results_public.csv')
st.sidebar.title('Choose any option:')
st.sidebar.image('https://roshnihealthcarepvtltd.com/wp-content/uploads/2019/11/Medical-billing-software.png')


user_menu=st.sidebar.radio(
    ' ',
    ('Predict','Explore')
)

# Predict=show_predict_page()
# Explore=print('chal')


if user_menu =='Predict':
    show_predict_page()

if user_menu=='Explore':
    
    st.header('Most Demanding Technologies in repective domain')
    datframe=datframe[['DevType','WebframeHaveWorkedWith','DatabaseHaveWorkedWith','MiscTechHaveWorkedWith','ToolsTechHaveWorkedWith']]
    datframe=datframe.dropna()
    st.subheader('Post')
    typeWork=datframe['DevType'].value_counts()
    typeWork=typeWork[:4]
    typeWork


    st.subheader('Framework')
    Framework=datframe['WebframeHaveWorkedWith'].value_counts()
    Framework=Framework[:4]
    Framework


    st.subheader('Databases')
    Database=datframe['DatabaseHaveWorkedWith'].value_counts()
    Database=Database[:4]
    Database
    

    st.subheader('Technology')
    Tech=datframe['MiscTechHaveWorkedWith'].value_counts()
    Tech=Tech[:4]
    Tech


    st.subheader('Tools ')
    Tools=datframe['ToolsTechHaveWorkedWith'].value_counts()
    Tools=Tools[:4]
    Tools


    # data = datframe["Country"].value_counts()

    # fig1, ax1 = plt.subplots()
    # ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    # ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    # st.write("""#### Number of Data from different countries""")

    # st.pyplot(fig1)
    
    # st.write(
    #     """
    # #### Mean Salary Based On Country
    # """
    # )



    # st.write(
    #     """
    # #### Mean Salary Based On Experience
    # """
    # )

    # data = datframe.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    # st.line_chart(data)




