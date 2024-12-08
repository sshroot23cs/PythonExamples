import tweepy
from textblob import TextBlob
import time


class TwitterSentimentAnalyzer:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def fetch_tweets(self, hashtag, count=10000, batch_size=100):
        all_tweets = []
        for tweet in tweepy.Cursor(self.api.search_tweets, q=hashtag, lang="en").items(count):
            all_tweets.append(tweet)
            if len(all_tweets) % batch_size == 0:
                print(f"Fetched {len(all_tweets)} tweets so far...")
            time.sleep(0.1)  # Short sleep to prevent hitting rate limits excessively
        return all_tweets

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(tweet.text)
        sentiment = analysis.sentiment.polarity
        return 'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'

    def process_tweets(self, tweets):
        sentiments = [(tweet.user.screen_name, tweet.text, self.analyze_sentiment(tweet)) for tweet in tweets]
        return sentiments

    def print_tweet_details(self, sentiments):
        positive_count = sum(1 for _, _, sentiment in sentiments if sentiment == 'Positive')
        negative_count = sum(1 for _, _, sentiment in sentiments if sentiment == 'Negative')
        neutral_count = len(sentiments) - positive_count - negative_count

        for user, text, sentiment in sentiments:
            print(f"User: {user}")
            print(f"Tweet: {text}")
            print(f"Sentiment: {sentiment}")
            print("-" * 40)

        total_tweets = len(sentiments)
        positive_ratio = positive_count / total_tweets if total_tweets else 0
        verdict = "Good" if positive_ratio >= 0.7 else "Not Good"

        print(f"Total Tweets Analyzed: {total_tweets}")
        print(f"Positive Tweets: {positive_count}")
        print(f"Negative Tweets: {negative_count}")
        print(f"Neutral Tweets: {neutral_count}")
        print(f"Overall Verdict: {verdict}")


if __name__ == "__main__":
    # Replace with your own credentials obtained from your Twitter Developer account
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

    # Initialize the TwitterSentimentAnalyzer
    analyzer = TwitterSentimentAnalyzer(consumer_key, consumer_secret, access_token, access_token_secret)

    # Define the search hashtag
    hashtag = "#yourhashtag"

    # Fetch tweets
    tweets = analyzer.fetch_tweets(hashtag, count=10000)

    # Process and analyze the fetched tweets
    sentiments = analyzer.process_tweets(tweets)

    # Print tweet details with sentiment and overall verdict
    analyzer.print_tweet_details(sentiments)
