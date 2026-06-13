import streamlit as st
import youtube_api
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("YouTube Comment Analyzer")
url = st.sidebar.text_input("Enter YouTube URL")
if st.sidebar.button("Analyze"):
    if url:
        try:
            video_id = url.split("v=")[1].split("&")[0]
            # Fetch comments
            df = youtube_api.fetch_comments(video_id)
            df = preprocessor.preprocess(df)
            st.subheader("Raw Data")
            st.dataframe(df)
            # Top Statistics
            comments, users, avg_len, likes = helper.fetch_stats(df)
            st.title("Top Statistics")
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.header("Comments")
                st.title(comments)

            with col2:
                st.header("Users")
                st.title(users)

            with col3:
                st.header("Avg Length")
                st.title(round(avg_len, 2))

            with col4:
                st.header("Likes")
                st.title(likes)

            # Monthly Analysis
            st.title("Monthly Analysis")
            timeline = helper.monthly_timeline(df)
            fig, ax = plt.subplots()
            ax.bar(timeline['month_name'],timeline['comment'])
            plt.xticks(rotation=45)
            st.pyplot(fig)
            #weekly analysis
            st.title("Weekly Analysis")
            busy_day = helper.week_activity(df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
            # Top Commenters
            st.title("Top Commenters")
            x, new_df = helper.top_commenters(df)
            fig, ax = plt.subplots()
            ax.bar(x.index,x.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
            st.dataframe(new_df)
            # Word Cloud
            st.title("Word Cloud")
            wc = helper.create_wordcloud(df)
            fig, ax = plt.subplots()
            ax.imshow(wc)
            ax.axis("off")
            st.pyplot(fig)
            
            # Most Common Words
            st.title("Most Common Words")
            common_df = helper.most_common_words(df)
            fig, ax = plt.subplots()
            ax.barh(common_df[0],common_df[1])
            st.pyplot(fig)

            #'''Emoji Analysis
            #st.title("Emoji Analysis")
            #emoji_df = helper.emoji_help(df)
            #col1, col2 = st.columns(2)
            #with col1:
            #    st.dataframe(emoji_df)
            #with col2:
            #    fig, ax = plt.subplots()
            #   ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(),autopct="%0.2f%%")
            #    st.pyplot(fig)'''
            # Heatmap
            st.title("Activity Heatmap")
            heatmap = helper.activity_heatmap(df)
            fig, ax = plt.subplots()
            sns.heatmap(heatmap,ax=ax)
            st.pyplot(fig)
            ##sentiment analysis
            st.title("Sentiment Analysis")
            sentiment_counts = helper.sentiment_analysis(df)
            fig, ax = plt.subplots()
            ax.pie(sentiment_counts.values,labels=sentiment_counts.index,autopct="%0.2f%%")
            st.pyplot(fig)

            st.title("Most Positive Comments")
            positive_df = helper.most_positive_comments(df)
            st.dataframe(positive_df)

            st.title("Most Negative Comments")
            negative_df = helper.most_negative_comments(df)
            st.dataframe(negative_df)

            st.title("📝 Most Common Phrases")
            bigram_df = helper.top_bigrams(df)
            fig, ax = plt.subplots()
            ax.barh(bigram_df['Bigram'].astype(str),bigram_df['Count'])
            st.pyplot(fig)

            st.title("🗣️ Popular Discussion Topics")
            trigram_df = helper.top_trigrams(df)
            fig, ax = plt.subplots()
            ax.barh(trigram_df['Trigram'].astype(str),trigram_df['Count'])
            st.pyplot(fig)

            st.title("🔑 Most Important Keywords")
            tfidf_df = helper.tfidf_keywords(df)
            fig, ax = plt.subplots()
            ax.barh(tfidf_df['word'],tfidf_df['score'])
            st.pyplot(fig)
            st.dataframe(tfidf_df)
        except Exception as e:
            st.exception(e)

    else:
        st.warning("Please enter a YouTube URL")