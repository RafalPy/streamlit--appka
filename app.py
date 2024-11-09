import streamlit as st

st.markdown(
    """
    <style>
    .custom-title {
        font-size: 50px;
        font-weight: bold;
        color: #333333;  
        text-align: center;

    }
    </style>
    <h1 class="custom-title">🐸 Hello World to free Złotys spent on Żappsy calculator!</h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* Applies to main content area */
    .stApp {
        background-color: #6AC100;
    }
    </style>
    """,
    unsafe_allow_html=True
)


#st.image("https://www.example.com/image.jpg", caption="This is an online image.", use_column_width=True)


num_żappsy = st.number_input("How many Żappsy you have:", min_value=0, step = 1)



zlotys_spent = num_żappsy/4

if st.button("Submit"):
    st.write(f"<h1 style='font-size: 50px; font-weight: bold;'>You have {num_żappsy} żappsów therefore you have spent at least <h2 style =' font-size: 130px'> {zlotys_spent}  złotys. </h2> </h1>", unsafe_allow_html=True)

st.image("https://pepethefrog.ucoz.com/_nw/9/64629232.jpg", use_container_width=True)

satisfaction = st.slider("App satisfaction level:", 8, 10)
st.markdown("🌟made with Python and Streamlit by Rafal Py🌟")