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

    for i in range(len(raw_tweet)):
        # get the text of the tweet
        tweet_txt = json.loads(raw_tweet[i]).get("text", "")
        # break the tweet into words
        tweet_txt_words = tweet_txt.split()
        tweet_score = 0
        # loop over the words looking up the sentiment of each word
        for word in tweet_txt_words:
            tweet_score += scores.get(word, 0)
        # print the sentiment
        print tweet_score


if __name__ == '__main__':
    main()
