import cloudscraper
import re

scraper=cloudscraper.create_scraper()
trc=scraper.get("https://www.dizibox.pw").text
result=open("trc.txt","w",encoding='utf-8')
result.write(trc)
with open ("trc.txt",'r',encoding="utf-8") as dosya:
    for satir in dosya:
        sonuc = re.findall("<a href=(.*?) class",satir)
        if sonuc:
            print(sonuc)










