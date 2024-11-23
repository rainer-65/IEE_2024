# Small program to show sentiment analysis
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob


# Option 1: Using TextBlob
def text_blob(text):
    blob = TextBlob(text)
    sentiment_textblob = blob.sentiment.polarity
    print(f"Sentiment analysis with TextBlob: {sentiment_textblob:.2f}")


# Option 2: Using NLTK’s Pre-Trained Sentiment Analyzer (Vader)
def text_nltk(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_nltk = sia.polarity_scores(text)
    print(f"Sentiment analysis with NLTK: {sentiment_nltk}")


# Asking for input
text = input("Please enter a sentence or a word fragment: ")
while text.lower() != "stop":
    if text == "":
        pass
    else:
        text_blob(text)
        text_nltk(text)
    text = input("Please enter a sentence or a word fragment: ")

print("Bye, program terminated!")
