import streamlit as st
import pickle
import pandas as pd

# To Add External CSS
with open('css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Application Backend
medicines_dict = pickle.load(open('medicine_dict.pkl','rb'))
medicines = pd.DataFrame(medicines_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(medicine):
    medicine_index = medicines[medicines['Drug_Name'] == medicine].index[0]
    distances = similarity[medicine_index]
    medicines_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_medicines = []
    for i in medicines_list:
        recommended_medicines.append(medicines.iloc[i[0]].Drug_Name)
    return recommended_medicines

# Application Frontend

# Title of the Application
st.title('Search your Medicines')

# Searchbox with default content removed
selected_medicine_name = st.selectbox(
    'Type medicine name for an alternative recommendation.',
    medicines['Drug_Name'].values, index=10000)  # Set index to 0 for an empty default selection

# Recommendation Program
if st.button('Recommend Medicine'):
    recommendations = recommend(selected_medicine_name)
    j = 1
    for i in recommendations:
        st.write(j, i)  # Recommended-drug-name
        st.write("Click here -> "+" https://pharmeasy.in/search/all?name="+i) # Recommended-drug purchase link from pharmeasy
        j += 1

# Image load
from PIL import Image
image = Image.open('images\images.jpeg')
st.image(image, caption='Recommended Medicines')
