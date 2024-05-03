# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:24:48 2024

@author: dayas
"""

import streamlit as st
import load_data
#import prepare_data
#import pdata
import json
#import topfood
from collections import Counter
#import the file 

def main():
    
    
    
    
    data = load_data.load_data('restaurants.json')

    # Title
    st.title("Cuisine Compass")
    

    # Sidebar
    
    # Dropdown menu in the sidebar
    
    st.sidebar.title("Select City")
     
     # Dropdown menu in the sidebar
        
    # Transform data into a dict with location as key
    locations_data = {restaurant['location']: restaurant for restaurant in data}
    table_data = []
    
    # Sidebar for location selection
    location = st.sidebar.selectbox(
        "", 
        #sorted(list(locations_data.keys())),  # Display sorted list of cities
        sorted([city.title() for city in locations_data.keys()]),
        index=0  # Default selection is the first city in the list
    )
    
    
    
    # Button to show recommendations
    if st.sidebar.button('Show Recommendations'):
       st.write("Click Arrow to expand")
       filtered_data = [restaurant for restaurant in data if restaurant['location'].lower() == location.lower()]
       if filtered_data:
           sorted_data = sorted(filtered_data, key=lambda x: x['rating'], reverse=True)
           for idx,restaurant in enumerate(sorted_data, start=1):
               # Display restaurant data in a table format
               restaurant_name = restaurant['name'].title() 
               top_3_foods = ", ".join([food.title() for food in restaurant['foods'][:3]])
               with st.expander(f"**Rank:** {idx}\n\n**Restaurant Name:** {restaurant_name} \t\n\n**Average Rating:**\n{restaurant['rating']:.2f} Stars \t\n\nTop Foods:\n{top_3_foods}"):
                   st.write("Top Reviews:")
                   for review in restaurant['reviews']:
                       st.text_area("", review, height=100)
                   st.write("Top Dishes to Try:")
                   st.write(", ".join(restaurant['foods']).title())
       else:
           st.write("No recommendations found for this location. Please try a different city.")
    if st.sidebar.button('Results of Comparitive Study'):
        st.write("Results of Comparitive Study")
        
        st.write("Count and Percetange of Sentiments")
        image_path1 = "1.jpeg"
        with open(image_path1, "rb") as f:
            image_bytes = f.read()
            st.image(image_bytes, caption="", width=410)
        st.write("Unique Restaurants per City")
        image_path3 = "5.jpeg"
        with open(image_path3, "rb") as f:
             image_bytes = f.read()
             st.image(image_bytes, caption="", width=410)
        st.write("Average Rating by Location")   
        image_path2 = "2.jpeg"
        with open(image_path2, "rb") as f:
            image_bytes = f.read()
            st.image(image_bytes, caption="", width=410)
        st.write("Accuracy by Model")   
        image_path4 = "accuracy_by_model.png"
        with open(image_path4, "rb") as f:
            image_bytes = f.read()
            st.image(image_bytes, caption="", width=410)
        st.write("F1 Score by Model")
        image_path5 = "f1score.png"
        with open(image_path5, "rb") as f:
            image_bytes = f.read()
            st.image(image_bytes, caption="", width=410)
        st.write("Evaluation of Recommendation System using Confusion Matrix")
        image_path6 = "Confusion_Matrix.png"
        with open(image_path6, "rb") as f:
            image_bytes = f.read()
            st.image(image_bytes, caption="", width=410) 
         
        
        
        

         
    # Display selected option

if __name__ == "__main__":
    main()
