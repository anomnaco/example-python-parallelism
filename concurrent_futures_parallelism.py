import concurrent.futures
import requests
import pickle
from bs4 import BeautifulSoup
import time
    
def get_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.title.string

with open('urls.pickle', 'rb') as f:
    urls = pickle.load(f)

start_time = time.time()

with concurrent.futures.ThreadPoolExecutor() as executor:
    # Download the content and extract the title of each URL using threads
    title_futures = [executor.submit(get_title, url) for url in urls]

titles = {}
for i, url in enumerate(urls):
    title = title_futures[i].result()
    titles[url] = title

end_time = time.time()

print(titles)
print("Elapsed time: ", end_time - start_time)
