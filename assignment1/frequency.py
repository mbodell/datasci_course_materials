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
    defaultTerm = "foo"
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
        defaultTerm = term

    # read in the raw tweets
    raw_tweet = tweet_file.readlines()

    # get the scores for all the tweets, and all the words
    tweet_texts = []
    tweet_scores = []
    all_words = {}
    for i in range(len(raw_tweet)):
        # get the text of the tweet, utf-8
        tweet_txt = json.loads(raw_tweet[i]).get("text", "").encode("UTF-8")
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

    
    # figure out the new words
    new_words = {}
    for i in range(len(tweet_texts)):
        tweet = tweet_texts[i]
        tweet_word = tweet.split()
        for word in tweet_word:
            # only do it if it wasn't in the sentiment term
            if (scores.get(word, 6) > 5):
                if(new_words.get(word, defaultTerm) != defaultTerm):
                    new_words[word].append(tweet_scores[i])
                else:
                    new_words[word] = []
                    new_words[word].append(tweet_scores[i])

    # print out the final result
    for word in new_words:
        print "{0} {1}".format(word,sum(new_words[word])/len(new_words[word]))

                        

if __name__ == '__main__':
    main()
