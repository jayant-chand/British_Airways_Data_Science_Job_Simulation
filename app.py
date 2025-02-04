import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from src.analysis import analyze_sentiment

def main():
    st.title("British Airways Reviews Analysis")
    
    # Load data
    df = pd.read_csv("data/BA_reviews.csv")
    
    # Show sentiment distribution
    st.subheader("Sentiment Distribution")
    fig, ax = plt.subplots()
    df['Analysis'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    st.pyplot(fig)
    
    # Show wordcloud
    st.subheader("Common Terms in Reviews")
    wordcloud = WordCloud().generate(' '.join(df['Lemma']))
    fig, ax = plt.subplots()
    plt.imshow(wordcloud)
    plt.axis('off')
    st.pyplot(fig)

if __name__ == "__main__":
    main() 