import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # create a dictionary of sentiment scores
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    # read in the raw tweets
    raw_tweet = tweet_file.readlines()

    # capture the tweet scores by state
    state_scores = {}

    # do the sentiment calculation
    for i in range(len(raw_tweet)):
        tweet_json = json.loads(raw_tweet[i])
        # get the text of the tweet
        tweet_txt = tweet_json.get("text", "").encode("UTF-8")
        # break the tweet into words
        tweet_txt_words = tweet_txt.split()
        tweet_score = 0
        # loop over the words looking up the sentiment of each word
        for word in tweet_txt_words:
            tweet_score += scores.get(word, 0)
        # print the sentiment
        print float(tweet_score)
        print tweet_json.get("user",{}).get("location","").encode("UTF-8")


if __name__ == '__main__':
    main()
