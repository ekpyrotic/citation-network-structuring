from bs4 import BeautifulSoup
import requests as rq
#testing different webscrapers:
#using beautiful soup
r = rq.get("http://genomebiology.biomedcentral.com/articles/10.1186/gb-2009-10-3-r25")
soup = BeautifulSoup(r.text,"html.parser")
print(soup.title)