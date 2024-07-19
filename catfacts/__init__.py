import streamlit as st
import requests

# Title of the app
st.title("Random Cat Facts")

# Subtitle
st.subheader("Click the button to get a random cat fact!")

# Button to fetch a new cat fact
if st.button("Get a Cat Fact"):
    # Send a request to the Cat Facts API
    response = requests.get('https://catfact.ninja/fact')
    
    # Check the response
    if response.status_code == 200:
        data = response.json()
        cat_fact = data['fact']
        # Display the cat fact
        st.success(cat_fact)
    else:
        st.error("Failed to retrieve data from the API.")

# Footer
st.write("Powered by [Cat Facts API](https://catfact.ninja/)")
