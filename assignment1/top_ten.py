import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])

    # read in the raw tweets
    raw_tweet = tweet_file.readlines()

    # hashtags are what we want
    hashtags = {}

    # do the sentiment calculation
    for i in range(len(raw_tweet)):
        tweet_json = json.loads(raw_tweet[i])
        # get the entities of the tweet
        tweet_entities = tweet_json.get("entities")

        if(tweet_entities != None):
            tweet_hash = tweet_entities.get("hashtags")
            for i in range(len(tweet_hash)):
                tag = tweet_hash[i].get("text","").encode("UTF-8")
                hashtags[tag] = hashtags.get(tag, 0.0) + 1.0

    i = 0
    # sort the hashtag
    for w in sorted(hashtags, key=hashtags.get, reverse=True):
        # print only the top 10
        if( i < 10 ):
            print w, hashtags[w]
        i = i + 1
           

if __name__ == '__main__':
    main()
