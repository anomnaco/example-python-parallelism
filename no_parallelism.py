import pickle
import requests
from bs4 import BeautifulSoup
import time

# Load urls from a pickle file
with open('urls.pickle', 'rb') as f:
    urls = pickle.load(f)

# Start the timer
start_time = time.time()

# Download and extract titles
html_results = []
for url in urls:
    response = requests.get(url)
    html_results.append(response.content)

results = [ BeautifulSoup(content, 'html.parser').title.string for content in html_results ]
title_dict = dict(zip(urls, results))

# End the timer
end_time = time.time()

# Print the resulting dictionary and elapsed time
print(title_dict)
print(f"Elapsed time: {end_time - start_time} seconds")

