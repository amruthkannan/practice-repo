import streamlit as st 
from demo import area_of_circle

st.title("Hello World")
st.write("This is a simple Streamlit app.")

radius = st.number_input("Enter the radius of the circle:", min_value=0.0)
if st.button("Calculate Area"):
    area = area_of_circle(radius)
    st.write(f"The area of the circle with radius {radius} is {area}.")
st.write("Thank you for using this app!")