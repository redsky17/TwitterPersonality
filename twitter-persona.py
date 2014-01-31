import nltk
import tweepy
from textblob import TextBlob
import argparse
import sys

class TwitterPersona:
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        
    def getApi(self):
        auth = tweepy.auth.OAuthHandler(self.key, self.secret)
        return tweepy.API(auth)
        
    def getUserTimeline(self, user, count, retweets):
        return self.getApi().user_timeline(count=count, screen_name=user, include_rts=retweets)
        
    def getSentimentForTweet(self, tweet):
        return TextBlob(tweet).sentiment
        
    def getSentimentForAllTweets(self, tweets):
        return map(lambda x: (x.text, self.getSentimentForTweet(x.text)), tweets)
        
    def getSortedSentimentByPolarity(self, tweets):
        return sorted(self.getSentimentForAllTweets(tweets), key=lambda x: x[1].polarity)
    
    def getSortedSentimentBySubjectivity(self, tweets):
        return sorted(self.getSentimentForAllTweets(tweets), key=lambda x: x[1].subjectivity)
    
if __name__ == "__main__":
    twitPersona = TwitterPersona(sys.argv[1], sys.argv[2])
    user = sys.argv[3]
    count = sys.argv[4]
    include_rts = sys.argv[5]
    tweets = twitPersona.getUserTimeline(user, count, include_rts)
    sortedByPolarity = twitPersona.getSortedSentimentByPolarity(tweets)
    sortedBySubjectivity = twitPersona.getSortedSentimentBySubjectivity(tweets)
    averagePolarity = 0.0
    averageSubjectivity = 0.0
    for tweet in sortedByPolarity:
        averagePolarity += tweet[1].polarity
        averageSubjectivity += tweet[1].subjectivity
        
    averagePolarity = averagePolarity / len(sortedByPolarity)
    averageSubjectivity = averageSubjectivity / len(sortedByPolarity)
    
    print "Average Polarity of Tweets: " + str(averagePolarity) + "\nAverage Subjectivity of Tweets: " + str(averageSubjectivity) + "\nMost Negative Tweet: " + str(sortedByPolarity[0][0].encode('utf-8')) + "\nMost Positive Tweet: " + str(sortedByPolarity[-1][0].encode('utf-8')) + "\nMost Objective Tweet: " + str(sortedBySubjectivity[0][0].encode('utf-8')) + "\nMost Subjective Tweet: " + str(sortedBySubjectivity[-1][0].encode('utf-8'))