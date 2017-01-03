from bs4 import BeautifulSoup,SoupStrainer
import requests 
import scrapy 
import re

#testing different webscrapers:
#using beautiful soup
r = requests.get("http://genomebiology.biomedcentral.com/articles/10.1186/gb-2009-10-3-r25")
soup = BeautifulSoup(r.text,"html.parser")
print(soup.title)

# testing a scrapy webscrawler base class

def cool_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://genomebiology.biomedcentral.com/articles/10.1186/gb-2009-10-3-r25' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        Soup = BeautifulSoup(plain_text)
      
        for link in Soup.findAll('a', {'class': ''}):
            href = link.get('href')
            print(href)
        page += 1

cool_spider(5)
