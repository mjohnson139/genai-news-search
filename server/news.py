# news.py

from configs import NEWS_API_KEY

from newsdataapi import NewsDataApiClient

# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey=f'{NEWS_API_KEY}')

# api = NewsDataApiClient(apikey="pub_43275eac554de1ddd3f2af3ac2ba5dd738104")

async def getNews(query: str, max_size: int = 8):
    
    response = api.news_api( q=query)
    return response