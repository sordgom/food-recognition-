import streamlit as st
import pandas as pd
import numpy as np
import dill as pickle
from PIL import Image
from backend import nutrition_hybrid_recommender as recommender 

recipeList = pickle.load(open('./models/list.pkl','rb'))

st.title("Welcome to Food recommendation system")
st.write("""## We need some information to give you the recommendation you need""")

st.markdown("""
        <style>
        .css-15zrgzn {display: none}
        .css-eczf16 {display: none}
        .css-jn99sy {display: none}
        </style>
        """, unsafe_allow_html=True)

records = recipeList.to_dict("records")
recipe_data = st.selectbox("Select recipe", options=records, format_func=lambda record: f'{record["recipe_name"]}')
recipe = recipe_data.get('recipe_id')


image = Image.open( "./raw-data-images/" + str(recipe) + ".jpg")
st.image(image)

submit = st.button("Recommend")

if submit:
        nutrition_ar, topN_ar  = recommender(recipe, ['aver_rate'], 3)
        
        image = Image.open( "./raw-data-images/" + str(int(topN_ar.iloc[0][0])) + ".jpg")
        st.image(image)
        
        image = Image.open( "./raw-data-images/" + str(int(topN_ar.iloc[1][0])) + ".jpg")
        st.image(image)
        
        image = Image.open( "./raw-data-images/" + str(int(topN_ar.iloc[2][0])) + ".jpg")
        st.image(image)
        
        st.write("Nutrional facts: ")
        st.write(nutrition_ar)
        
        st.write("Recipe ratings: ")
        st.write(topN_ar)