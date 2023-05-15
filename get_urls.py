import requests
from bs4 import BeautifulSoup
import pickle

wiki_main_page = requests.get("https://en.wikipedia.org/wiki/Main_Page")
wiki_main_page_soup = BeautifulSoup(wiki_main_page.text, features="lxml")
link_list = [ link.get('href') for link in wiki_main_page_soup.find_all('a') ]

def wiki_check(link):
    return link.startswith("/wiki/")

filtered_link_list = list(filter(wiki_check, link_list))

completed_link_list = [ "https://en.wikipedia.org"+link for link in filtered_link_list ]
urls = completed_link_list[0:50]

with open('urls.pickle', 'wb') as f:
    pickle.dump(urls, f)
