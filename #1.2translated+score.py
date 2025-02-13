import streamlit as st
from translate import Translator
from textblob import TextBlob

# App Title
st.title("🌍 Translation and Context Understanding App")

# Input Text Area
st.header("Enter English Text for Translation:")
input_text = st.text_area("Input Text:", value="""
Today is a very disruptive world, 
but Machine Learning and AI, 
specifically Natural Language Processing, 
is a fascinating field at the intersection of computer science, 
artificial intelligence, and linguistics.
""")

# Translation Section
if st.button("Translate to Urdu"):
    # Translate to Urdu
    translator = Translator(to_lang="ur")
    translated_text = translator.translate(input_text)
    
    # Display Translated Text
    st.subheader("Translated Text (Urdu):")
    st.write(translated_text)
    
    # Sentiment Analysis
    st.header("Sentiment Analysis")
    
    # Analyze Original Sentiment
    original_blob = TextBlob(input_text)
    original_sentiment = original_blob.sentiment
    st.subheader("Original Text Sentiment:")
    st.write(f"Polarity: {original_sentiment.polarity}")
    st.write(f"Subjectivity: {original_sentiment.subjectivity}")
    
    # Analyze Translated Sentiment
    translated_blob = TextBlob(translated_text)
    translated_sentiment = translated_blob.sentiment
    st.subheader("Translated Text Sentiment:")
    st.write(f"Polarity: {translated_sentiment.polarity}")
    st.write(f"Subjectivity: {translated_sentiment.subjectivity}")
