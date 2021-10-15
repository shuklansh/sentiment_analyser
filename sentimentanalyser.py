######## sentiment analysis for given statement #######
from textblob import TextBlob
# enter the statement of your choice #
y = input("enter statement:")
edu = TextBlob(y)
x = edu.sentiment.polarity
#### if the statement polarity is less than zero -> the statement is negative #####
if x < 0:
    print("Negative")
#### if the statement polarity is equal to zero -> the statement is neutral #####
elif x == 0:
    print("Neutral")
#### if the statement polarity is greater than zero but also less than or equal to 1 -> the statement is positive #####
elif 0 < x <= 1:
    print("Positive")
