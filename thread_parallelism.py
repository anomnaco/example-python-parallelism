import threading
import requests
import pickle
from bs4 import BeautifulSoup
import time
    
# Define a function to download url content and extract title
def process_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else ''
    return url, title

with open('urls.pickle', 'rb') as f:
    urls = pickle.load(f)

start_time = time.time()

# Create threads to process each url
results = {}
threads = []
for url in urls:
    t = threading.Thread(target=lambda r, u: r.update({u: process_url(u)}), args=(results, url))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Combine results into a dictionary
output = {}
for k, v in results.items():
    output[k] = v
    
end_time = time.time()
    
print(output)
print("Elapsed time:", end_time - start_time)
