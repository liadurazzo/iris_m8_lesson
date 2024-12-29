import streamlit as st
import pandas as pd
import plotly.express as px
import os

   
# ---------------------------
# 📊 MULTI-PAGE NAVIGATION 📊
# ---------------------------
page = st.sidebar.selectbox("Select a Page", ["Practice", "Home", "Data Dashboard", "About"])


if page == "Practice":
    st.title("My First Streamlit App")
    st.write("Welcome to my first Streamlit app!")

    number = st.slider("Pick a number", 1, 10)
    st.write(f"You selected: {number}")

    st.title("Simple Data Dashboard")
    st.write("Here’s the sample data:")

    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 23, 45, 15]
    })
    st.dataframe(data)

    fig = px.bar(data, x='Category', y='Values', title='Category Values',
                 labels={'Category': 'Category', 'Values': 'Values'})
    st.plotly_chart(fig, key="practice_chart")

    st.title("Interactive Category Adjustments")
    value_a = st.slider("Value for Category A", 0, 100, 47)
    value_b = st.slider("Value for Category B", 0, 100, 41)
    value_c = st.slider("Value for Category C", 0, 100, 64)
    value_d = st.slider("Value for Category D", 0, 100, 50)

    updated_data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [value_a, value_b, value_c, value_d]
    })

    fig = px.bar(updated_data, x='Category', y='Values', title='Updated Category Values',
                 labels={'Category': 'Category', 'Values': 'Values'})
    st.plotly_chart(fig, key="practice_updated_chart")


elif page == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the home page of your multi-page app.")

elif page == "Data Dashboard":
    st.title("📊 Data Dashboard")
    st.write("Here’s the sample data:")

    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [10, 23, 45, 15]
    })

    st.dataframe(data)

    # Create and display a bar chart using Plotly
    fig = px.bar(data, x='Category', y='Values', title='Category Values',
                 labels={'Category': 'Category', 'Values': 'Values'})

    # Display the Plotly chart in Streamlit
    st.plotly_chart(fig, key="dashboard_chart")

# ---------------------------
# 📚 ABOUT PAGE 📚
# ---------------------------
elif page == "About":
    st.title("About")
    st.write("This is an example of a multi-page Streamlit app.")



