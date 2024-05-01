import news  
import asyncio  
import json # Import json for potential parsing attempt

async def main():
    news_results = await news.getNews(query="technology", max_size=5)
    print(json.dumps(news_results, indent=4))

if __name__ == "__main__":
    asyncio.run(main())