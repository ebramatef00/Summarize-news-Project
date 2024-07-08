import streamlit as st
from newspaper import Article
from textblob import TextBlob
import nltk

nltk.download('punkt')
st.title("News Summarizer Analyzer")
url = st.text_input("Enter the URL of a news article")

if st.button("Summarize"):
    if url:
        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()
            
            # Display article details
            st.subheader("Title")
            st.write(article.title)
            st.subheader("Authors")
            st.write(", ".join(article.authors))
            st.subheader("Publication Date")
            st.write(article.publish_date)
            st.subheader("Summary")
            st.write(article.summary)
            
            # Perform sentiment analysis
            analysis = TextBlob(article.text)
            sentiment = analysis.sentiment.polarity
            sentiment_label = "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral"
            
            st.subheader("Sentiment Analysis")
            st.write(f'Polarity: {sentiment}, Sentiment: {sentiment_label}')
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid URL")

