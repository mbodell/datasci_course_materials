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

    # create a list of tweet text
    tweet_txt = []
    for i in range(len(raw_tweet)):
        tweet_txt.append(json.loads(raw_tweet[i])["text"])


if __name__ == '__main__':
    main()
