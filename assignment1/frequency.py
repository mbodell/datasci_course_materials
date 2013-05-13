import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])

    # read in the raw tweets
    raw_tweet = tweet_file.readlines()

    # get the scores for all the tweets, and all the words
    tweet_texts = []
    all_words = {}
    for i in range(len(raw_tweet)):
        # get the text of the tweet, utf-8
        tweet_txt = json.loads(raw_tweet[i]).get("text", "").encode("UTF-8")
        tweet_texts.append(tweet_txt)
        # break the tweet into words
        tweet_txt_words = tweet_txt.split()
        # loop over the words counting each word
        for word in tweet_txt_words:
            all_words[word] = all_words.get(word, 0.0) + 1.0

    
    # figure out grand total
    total_words = 0.0
    for word in all_words:
        total_words += all_words[word]

    # print out the final result
    for word in all_words:
        print "{0} {1}".format(word,all_words[word]/total_words)

                        

if __name__ == '__main__':
    main()
