
import requests



def get_news(category):
    # Define the API endpoint and parameters
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": "API_KEY",  #API
        "category": category
    }

    try:
        # Send GET request to the API
        response = requests.get(url, params=params)
        # Parse JSON response
        news_data = response.json()

        # Check if the response is successful
        if response.status_code == 200:
            # Extract and return the relevant news articles
            articles = news_data.get("articles", [])
            return articles
        else:
            print("Failed to fetch news:", news_data.get("message"))
            return None
    except Exception as e:
        print("An error occurred while fetching news:", e)
        return None
