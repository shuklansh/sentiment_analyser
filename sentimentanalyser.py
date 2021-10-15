from textblob import TextBlob
y = input("enter statement:")
edu = TextBlob(y)
x = edu.sentiment.polarity
if x < 0:
    print("Negative")
elif x == 0:
    print("Neutral")
elif x > 0 & x <= 1:
    print("Positive")
