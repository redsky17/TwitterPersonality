TwitterPersonality
==================

Provides a look at a user's polarity and subjectivity on twitter using the TextBlob library

Prerequisites
-------------
1. Install the Natural Language Toolkit from [its website](http://nltk.org)
 * Make sure you install all of NLTK's prerequisites
2. Install TextBlob from [its website](http://textblob.readthedocs.org/en/latest/)

Using
-----
1. Make sure you have a consumer key and secret generated by registering for a new api key on [Twitter's developer page](https://dev.twitter.com/)
2. From the terminal, type `python [path/to/twitter-persona.py] [key] [secret] [user_to_analyze] [tweet_count] [include_retweets]`
 * Make sure you replace the objects in brackets with valid values
 * Twitter's API will return at most 800 tweets.
