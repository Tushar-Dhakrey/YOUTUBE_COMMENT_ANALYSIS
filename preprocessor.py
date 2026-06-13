import pandas as pd
import html
import re
import string
from nltk.corpus import stopwords
def preprocess(df):

    # HTML decoding
    df['comment'] = df['comment'].apply(html.unescape)

    # lowercase
    df['comment'] = df['comment'].str.lower()

    # remove urls
    df['comment'] = df['comment'].apply(
        lambda x: re.sub(r'http\S+|www\S+', '', x)
    )

    # remove extra spaces
    df['comment'] = df['comment'].apply(
        lambda x: ' '.join(x.split())
    )

    # datetime conversion
    df['date'] = pd.to_datetime(df['date'])

    # date features
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['day_name'] = df['date'].dt.day_name()

    # comment features
    df['word_count'] = df['comment'].apply(
        lambda x: len(x.split())
    )

    df['char_count'] = df['comment'].apply(len)
    period = []
    for hour in df[['day_name','hour']]['hour']:
        if hour == 23:
            period.append(str(hour)+"-"+str('00'))
        elif hour == 0:
            period.append(str('00')+"-"+str(hour+1))
        else:
            period.append(str(hour)+"-"+str(hour+1))
    df['period'] = period
    df['month_name'] = df['date'].dt.month_name()
    stop_words = set(stopwords.words('english'))
    def clean_text(text):

        text = text.translate(
            str.maketrans('', '', string.punctuation)
        )

        words = []
        for word in text.split():

            if word not in stop_words:

                words.append(word)

        return " ".join(words)
    df['clean_comment'] = df['comment'].apply(clean_text)
    
    return df