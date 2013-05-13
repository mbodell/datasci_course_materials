import sys
import json
import re

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    states = {'AL': 1, 'AK': 1, 'AZ': 1, 'AR': 1, 'CA': 1, 'CO': 1, 'CT': 1, 'DE': 1, 'FL': 1, 'GA': 1, 'HI': 1, 'ID': 1, 'IL': 1, 'IN': 1, 'IA': 1, 'KS': 1, 'KY': 1, 'LA': 1, 'ME': 1, 'MD': 1, 'MA': 1, 'MI': 1, 'MN': 1, 'MS': 1, 'MO': 1, 'MT': 1, 'NE': 1, 'NV': 1, 'NH': 1, 'NJ': 1, 'NM': 1, 'NY': 1, 'NC': 1, 'ND': 1, 'OH': 1, 'OK': 1, 'OR': 1, 'PA': 1, 'RI': 1, 'SC': 1, 'SD': 1, 'TN': 1, 'TX': 1, 'UT': 1, 'VT': 1, 'VA': 1, 'WA': 1, 'WV': 1, 'WI': 1, 'WY': 1}
    # create a dictionary of sentiment scores
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    # read in the raw tweets
    raw_tweet = tweet_file.readlines()

    # capture the tweet scores by state
    state_scores = {}
    for state in states:
        state_scores[state] = []
        # seed it with one 0 value for fun
        state_scores[state].append(0.0)

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
        # get state sentiment
        good = 0
        location = tweet_json.get("user",{}).get("location","").encode("UTF-8")
        m = re.search('^.*,\s*(..)$', location)
        if( m != None):
            state = m.group(1)
            if (states.get(state,0) > 0):
                good = 1
                state_scores[state].append(float(tweet_score))

        place = tweet_json.get("place")
        if (place != None and good != 1):
            fname = place.get("full_name","").encode("UTF-8")
            m = re.search('^.*,\s*(..)$', fname)
            if( m != None):
                state = m.group(1)
                if (states.get(state,0) > 0):
                    state_scores[state].append(float(tweet_score))
            
    max_state = "CA"
    max_value = -55

    for state in states:
        sentiment = sum(state_scores[state])/len(state_scores[state])
        if (sentiment > max_value):
            max_value = sentiment
            max_state = state
        #print "{0} {1}: {2}".format(state, sentiment, state_scores[state])

    print max_state

if __name__ == '__main__':
    main()
