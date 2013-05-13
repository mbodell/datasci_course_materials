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

    # get the scores for all the tweets, and all the words
    tweet_texts = []
    tweet_scores = []
    all_words = {}
    for i in range(len(raw_tweet)):
        # get the text of the tweet
        tweet_txt = json.loads(raw_tweet[i]).get("text", "")
        tweet_texts.append(tweet_txt)
        # break the tweet into words
        tweet_txt_words = tweet_txt.split()
        tweet_score = 0
        # loop over the words looking up the sentiment of each word
        for word in tweet_txt_words:
            tweet_score += scores.get(word, 0)
            all_words[word] = 1
        # print the sentiment
        tweet_scores.append(float(tweet_score))

    new_words = {}
    i = -1
    for tweet in tweet_texts:
        i = i + 1
        for word in tweet:
            if (scores.get(word, 6) > 5):
                if(new_words.get(word, "abandon") != "abandon"):
                    new_words[word].append(tweet_scores[i])
                else:
                    new_words[word] = []
                    new_words[word].append(tweet_scores[i])

    for word in new_words:
        print new_words[word]

                        

if __name__ == '__main__':
    main()
