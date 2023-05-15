import dask.bag as db
import requests
import pickle
from bs4 import BeautifulSoup
import time
    
def download_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string.strip()
    except:
        title = "Error: Unable to retrieve title"
    return url, title

def download_urls_dask(urls):
    start_time = time.time()
    bag = db.from_sequence(urls)
    results = bag.map(download_url).compute()
    end_time = time.time()
    return results, end_time - start_time

if __name__ == "__main__":
    with open("urls.pickle", "rb") as f:
        urls = pickle.load(f)
        
    results, elapsed_time = download_urls_dask(urls)
    print(f"Results: {results}")
    print(f"Elapsed time: {elapsed_time}")
