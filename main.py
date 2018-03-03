from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt

def percentage(part, whole):
    return 100* float(part)/float(whole)

consumerKey="kUO8RvKyCsio9kLzUXP5U8Ems"
consumerSecret="qrSWpruuMsxE0waJfUGehi7bUtqkdXHPiRxyhYjessLfY7nm5F"
accessToken="3258489140-GGYwT3gIrnx1TNFpNBmDhAT6Dtk9CwIM0AC4Gsq"
accessTokenSecret="5FCbmqZYx3IPt3BQhySibAs7xGTgi1wxUA8fNpCWCnxNh"

auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter Keyword/hashtag to search about: ")
noOfsearchTerms = int(input("Enter how many tweets to analysis: "))

tweets = tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfsearchTerms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity = polarity+ analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral= neutral + 1;
    elif(analysis.sentiment.polarity < 0.00):
        negative = negative + 1;
    elif(analysis.sentiment.polarity > 0.00):
        positive = positive + 1;
print(positive)
print(negative)
print(neutral)        

positive = percentage(positive, noOfsearchTerms)
negative = percentage(negative, noOfsearchTerms)
neutral = percentage(neutral, noOfsearchTerms)
polarity = percentage(polarity, noOfsearchTerms)
print(positive)
print(negative)
print(neutral)

positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')

print("How people are reacting on "+ searchTerm +"by analyzing " + str(noOfsearchTerms) + " Tweets.")

if(polarity == 0):
    print("Neutral")
elif(polarity < 0):
    print("Negative")
elif(polarity > 0):
    print("Positive")

labels = ['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negative ['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']
patches, text = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches,labels, loc="best")
plt.title("How people are reacting on "+ searchTerm + " by analyzing " + str(noOfsearchTerms) + " Tweets.")
plt.axis('equal')
plt.tight_layout()
plt.show()




















