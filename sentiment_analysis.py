# Small program to show sentiment analysis
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob


# nltk.download('vader_lexicon')


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
        print("Please enter a sentence or a word fragment: ")
    else:
        text_blob(text)
        text_nltk(text)
    text = input("Please enter a sentence or a word fragment: ")

print("Bye, program terminated!")
