import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(layout='wide')
import altair as alt
import pandas as pd
import numpy as np
import os
import wikipedia

def show_wiki_content(suggestion):
    option = st.sidebar.selectbox('Plaese Select Company ?', options=suggestion)
    st.write('You selected:', option)
    st.subheader(option)
    try:
        st.subheader("Summary")
        content = wikipedia.summary(option)
        st.markdown(content)
        st.subheader("Content")
        ril = wikipedia.page(option)
        st.markdown(ril.content)
    except:
       st.markdown("Article Not Found")


# This is the main app app itself, which appears when the user selects "Run the app".
def run_the_app(company_name):
    
       
    suggestion = wikipedia.search(company_name)
    show_wiki_content(suggestion)

    

# Streamlit encourages well-structured code, like starting execution in a main() function.
def main():
    

    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("What to do")
    

    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["Run the app"])
    if app_mode == "Run the app":
        company_name = st.text_input("Search : ", value= "food companies", key = "Search Company wiki info")
        run_the_app(company_name)


if __name__ == "__main__":
    main()        
