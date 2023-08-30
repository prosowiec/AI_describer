import streamlit as st
from scraper import Scraper
import streamlit_scrollable_textbox as stx
import chat

st.set_page_config(layout="wide")

st.header('Amazon webscraper')
asin = st.text_input(label = "ASIN", max_chars = 10)
images = st.checkbox("Save images")

if st.button('Start scraping') and asin:
    
    with st.spinner():
        web_scraper = Scraper(asin)
        descriptions = web_scraper.get_every_description()
    
    if images:
        with st.spinner():
            web_scraper.save_images()
            
        new_title = '<p style="font-family:sans-serif; color:Green; font-size: 25px;">Images has been saved</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        
    c1, c2 = st.columns([1,1])
    
    with c1:
        stx.scrollableTextbox(descriptions["pl"], height = 700)
        
    with c2:
        stx.scrollableTextbox(descriptions["de"], height = 700)
        
    st.divider()
    
    c3, c4 = st.columns([1,1])
    with c3:
        stx.scrollableTextbox(descriptions["fr"], height = 700)
    
response = ''
with st.form(key="input_parameters"):
    promt = st.text_area(label = "Opis do gpt", height=500)
    if st.form_submit_button("Wyślij promt"):
        st.session_state.keep_graphics = True
        
        response = chat.get_gpt_summary(promt, xxx)
        
        st.write("Chat response")
        stx.scrollableTextbox(response, height = 700)
