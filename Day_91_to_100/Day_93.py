# # use news api 

# use  the newsApi and the requests module to fetch the daily news realted to diffrent topics
# got to https://newsapi.org/ and explore the various options and to build you application

import requests

# Your API Key from NewsAPI
API_KEY = 'API_KEY'

# Base URL for the NewsAPI
BASE_URL = "https://newsapi.org/v2/everything"

# Function to fetch news based on a search query (topic)
def fetch_news(query, language='en', page_size=5):
    # Define parameters for the API request
    params = {
        'q': query,  # Search query or topic
        'apiKey': API_KEY,
        'language': language,  # Language of news
        'pageSize': page_size,  # Number of articles per request
        'sortBy': 'publishedAt'  # Sort by newest articles
    }
    
    # Send the GET request to the NewsAPI
    response = requests.get(BASE_URL, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        news_data = response.json()
        return news_data['articles']
    else:
        print("Error:", response.status_code)
        return None

# Example: Fetching news related to "Technology"
topic = "Technology"
news_articles = fetch_news(topic)

# Displaying the news articles
if news_articles:
    print(f"Top {len(news_articles)} news articles on {topic}:")
    for i, article in enumerate(news_articles, 1):
        print(f"{i}. {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"Published at: {article['publishedAt']}")
        print(f"URL: {article['url']}")
        print("=" * 50)

