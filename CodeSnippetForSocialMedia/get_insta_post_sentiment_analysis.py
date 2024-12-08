import requests
from textblob import TextBlob


class InstagramSentimentAnalyzer:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = "https://graph.instagram.com"

    def get_hashtag_id(self, hashtag):
        search_url = f"{self.base_url}/ig_hashtag_search?user_id=YOUR_USER_ID&q={hashtag}&access_token={self.access_token}"
        response = requests.get(search_url).json()
        return response["data"][0]["id"]

    def fetch_posts(self, hashtag_id, count=100):
        posts_url = f"{self.base_url}/{hashtag_id}/recent_media?user_id=YOUR_USER_ID&fields=id,caption&access_token={self.access_token}&limit={count}"
        response = requests.get(posts_url).json()
        return response["data"]

    def analyze_sentiment(self, text):
        analysis = TextBlob(text)
        sentiment = analysis.sentiment.polarity
        return 'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'

    def process_posts(self, posts):
        sentiments = [(post['id'], post['caption'], self.analyze_sentiment(post['caption'])) for post in posts if
                      'caption' in post]
        return sentiments

    def print_post_details(self, sentiments):
        positive_count = sum(1 for _, _, sentiment in sentiments if sentiment == 'Positive')
        negative_count = sum(1 for _, _, sentiment in sentiments if sentiment == 'Negative')
        neutral_count = len(sentiments) - positive_count - negative_count

        for post_id, caption, sentiment in sentiments:
            print(f"Post ID: {post_id}")
            print(f"Caption: {caption}")
            print(f"Sentiment: {sentiment}")
            print("-" * 40)

        total_posts = len(sentiments)
        positive_ratio = positive_count / total_posts if total_posts else 0
        verdict = "Good" if positive_ratio >= 0.7 else "Not Good"

        print(f"Total Posts Analyzed: {total_posts}")
        print(f"Positive Posts: {positive_count}")
        print(f"Negative Posts: {negative_count}")
        print(f"Neutral Posts: {neutral_count}")
        print(f"Overall Verdict: {verdict}")


if __name__ == "__main__":
    # Replace with your own Instagram Graph API access token
    access_token = 'YOUR_ACCESS_TOKEN'

    # Initialize the InstagramSentimentAnalyzer
    analyzer = InstagramSentimentAnalyzer(access_token)

    # Define the search hashtag
    hashtag = "yourhashtag"

    # Get the hashtag ID
    hashtag_id = analyzer.get_hashtag_id(hashtag)

    # Fetch posts
    posts = analyzer.fetch_posts(hashtag_id, count=10000)

    # Process and analyze the fetched posts
    sentiments = analyzer.process_posts(posts)

    # Print post details with sentiment and overall verdict
    analyzer.print_post_details(sentiments)
