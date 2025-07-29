import streamlit as st
import nltk
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
from textblob import TextBlob
import re

st.title("NLP Sentiment Analysis")
input_text = st.text_area("Enter text for analysis here", height = 100) 
analyze_button = st.button("Analyze")

def cleanText(text):
    #Keeping only Text and digits
    text = re.sub(r"[^A-Za-z0-9]", "", text) 
    #Removes Whitespaces
    text = re.sub(r"\'s", "", text)
    # Removing Links if any
    text = re.sub(r"http\S+", " link ", text)
    # Removes Punctuations and Numbers
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
    # Splitting Text
    text = text.split()
    # Lemmatizer
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
    text = " ".join(lemmatized_words)
    return text

if analyze_button:
    blob = TextBlob(cleanText(input_text)) 
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        custom_emoji = ':blush:' 
        st.success('Happy: {} {}'.format(custom_emoji, sentiment_score)) # Corrected format string
    elif sentiment_score < 0: # Assuming <0 for negative
        custom_emoji = ':disappointed:' 
        st.warning('Sad: {} {}'.format(custom_emoji, sentiment_score)) # Corrected format string
    else:
        custom_emoji = ':confused:'
        st.info('Confused: {} {}'.format(custom_emoji, sentiment_score)) # Corrected format string
    st.success("Polarity Score is: {}".format(sentiment_score))

