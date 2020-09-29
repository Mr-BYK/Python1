
#Web Scraping

from bs4 import BeautifulSoup
import requests
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
html=requests.get(url).content
soup=BeautifulSoup(html, "html.parser")
list=soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=50)
count=1
for tr in list:
    title=tr.find("td",{"class":"titleColumn"}).find("a").text
    year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    strong = tr.find("td", {"class": "ratingColumn imdbRating"}).find("strong").text
    print(f"{count}-Film: {title.ljust(60)} yıl:{year} değerlendirme: {strong}")
    count+=1
#print(list)