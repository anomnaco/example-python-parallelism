import multiprocessing as mp
import pickle
import requests
import time
from bs4 import BeautifulSoup

def extract_html(url):
    response = requests.get(url)
    return response.content

if __name__ == '__main__':
    urls = pickle.load(open('urls.pickle', 'rb'))
    start_time = time.time()
    
    pool = mp.Pool(processes=mp.cpu_count())
    html_results = pool.map(extract_html, urls)
    pool.close()
    pool.join()
    
    results = [ BeautifulSoup(content, 'html.parser').title.string for content in html_results ]
    title_dict = dict(zip(urls, results))

    end_time = time.time()
    
    print(title_dict)
    print("Elapsed time: {} seconds".format(end_time - start_time))
