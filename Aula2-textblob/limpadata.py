import re

def cleanData(tweets):
        tweets['tweetos'] = ''
        # add tweetos first part
        for i in range(len(tweets['text'])):
            try:
                tweets['tweetos'][i] = tweets['text'].str.split(' ')[i][0]
            except AttributeError:
                tweets['tweetos'][i] = 'other'

        # Preprocessing tweetos. select tweetos contains 'RT @'
        for i in range(len(tweets['text'])):
            if tweets['tweetos'].str.contains('@')[i] == False:
                tweets['tweetos'][i] = 'other'

        # remove URLs, RTs, and twitter handles
        for i in range(len(tweets['text'])):
            tweets['text'][i] = " ".join([word for word in tweets['text'][i].split()
                                          if 'http' not in word and '@' not in word and '<' not in word])

        # remove ponctuations, put text in lower case and delete double space
        tweets['text'] = tweets['text'].apply(
            lambda x: re.sub('[!@#$:).;,?&]', '', x.lower()))
        tweets['text'] = tweets['text'].apply(lambda x: re.sub('  ', ' ', x))
        tweets['text'][1]
        return tweets