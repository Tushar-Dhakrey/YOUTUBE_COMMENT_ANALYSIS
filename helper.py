from wordcloud import WordCloud
from collections import Counter
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer
def fetch_stats(df):

    total_comments = df.shape[0]

    unique_users = df['author'].nunique()

    avg_comment_length = df['comment'].apply(len).mean()

    total_likes = df['likes'].sum()

    return (
        total_comments,
        unique_users,
        round(avg_comment_length,2),
        total_likes
    )
def top_commenters(df):

    x = df['author'].value_counts().head(10)

    percent_df = (
        round(
            (df['author'].value_counts()/df.shape[0])*100,2).reset_index()
    )
    return x,percent_df

def create_wordcloud(df):
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc = wc.generate(df['comment'].str.cat(sep=" "))
    return df_wc
from collections import Counter
import pandas as pd
def most_common_words(df):
    words = []
    for comment in df['comment']:
        words.extend(comment.split())
    common_df = pd.DataFrame(Counter(words).most_common(20))
    return common_df
def monthly_timeline(df):

    timeline = (
        df.groupby(['year','month','month_name'])
        .count()['comment']
        .reset_index()
    )

    timeline = timeline.sort_values(
        ['year','month']
    )

    return timeline
def week_activity(df):
    return df['day_name'].value_counts()
def month_activity(df):
    return df['month'].value_counts()
def activity_heatmap(df):
    heatmap = df.pivot_table(index='day_name',columns='period',values='comment',aggfunc='count').fillna(0)
    return heatmap

analyzer = SentimentIntensityAnalyzer()

def sentiment_analysis(df):

    def get_sentiment(text):

        score = analyzer.polarity_scores(text)

        if score['compound'] > 0.05:
            return 'Positive'

        elif score['compound'] < -0.05:
            return 'Negative'

        else:
            return 'Neutral'

    temp_df = df.copy()

    temp_df['sentiment'] = temp_df['comment'].apply(
        get_sentiment
    )

    return temp_df['sentiment'].value_counts()

def most_positive_comments(df):

    temp_df = df.copy()

    temp_df['compound'] = temp_df['comment'].apply(
        lambda x: analyzer.polarity_scores(x)['compound']
    )

    return temp_df.sort_values(
        'compound',
        ascending=False
    )[['author','comment','compound']].head(10)

def most_negative_comments(df):

    temp_df = df.copy()

    temp_df['compound'] = temp_df['comment'].apply(
        lambda x: analyzer.polarity_scores(x)['compound']
    )

    return temp_df.sort_values(
        'compound'
    )[['author','comment','compound']].head(10)

def top_bigrams(df):

    words = []

    for comment in df['comment']:

        words.extend(comment.split())

    bigrams = list(
        ngrams(words,2)
    )

    return pd.DataFrame(
        Counter(bigrams).most_common(20),
        columns=['Bigram','Count']
    )

def top_trigrams(df):

    words = []

    for comment in df['comment']:

        words.extend(comment.split())

    trigrams = list(
        ngrams(words,3)
    )

    return pd.DataFrame(
        Counter(trigrams).most_common(20),
        columns=['Trigram','Count']
    )

def tfidf_keywords(df):

    vectorizer = TfidfVectorizer(
        stop_words='english'
    )

    X = vectorizer.fit_transform(
        df['comment']
    )

    feature_names = (
        vectorizer.get_feature_names_out()
    )

    scores = X.mean(axis=0).A1

    tfidf_df = pd.DataFrame({
        'word': feature_names,
        'score': scores
    })

    tfidf_df = tfidf_df.sort_values(
        'score',
        ascending=False
    )

    return tfidf_df.head(20)



