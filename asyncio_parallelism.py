import asyncio
import aiohttp
import requests
import pickle
from bs4 import BeautifulSoup
import time
    
async def fetch_title(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        return soup.title.string

async def main():
    urls = pickle.load(open('urls.pickle', 'rb'))
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_title(session, url))
            tasks.append(task)
        titles = await asyncio.gather(*tasks)
    end_time = time.time()
    result = dict(zip(urls, titles))
    print(result)
    print("Elapsed time:", end_time - start_time)

asyncio.run(main())
