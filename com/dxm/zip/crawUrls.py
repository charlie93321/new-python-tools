import json
import re
import requests
from bs4 import BeautifulSoup


map={}

def crawb(name,url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    links=[]
    for link in soup.find_all(name='a'):
        url = link.get("href")
        if str(url).endswith(".htm") and 'faq' in url:
            links.append('https://www.bigseller.com'+link.get('href'))
    if len(links)>0:
        map[name]=links



def crawMainUrl():
    url = 'https://www.bigseller.com/help/index.htm'
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    languageMap = {}
    for alink in soup.find_all(name="a",attrs={"href":"javascript:"}):
        changLang = alink.get("onclick")
        if changLang is not None :
            lang_symbol = changLang.split('COMMON_FN.navChangeLang')[1]
            lang_symbol=str(lang_symbol).replace("(","").replace(")","").replace('\'','').strip()
            lang_name = alink.text.strip()
            languageMap[lang_name]=lang_symbol
    print(languageMap)
    urls = []
    oldUrl = url
    id ='faqsLeftNav'
    for langName in languageMap.keys():
        suffix = '?lang='+languageMap.get(langName)
        url = oldUrl+suffix
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.find(id=id).find_all("li"):
            name =link.find("p").get("name")
            text = link.find("p").text
            urls.append(("{}_".format(langName)+text.strip(), 'https://www.bigseller.com/help/faq/{}.htm{}'.format(name,suffix)))
    return urls

if __name__=="__main__":
    urls = crawMainUrl()
    for url in urls:
        crawb(url[0],url[1])
    print(json.dumps(map,ensure_ascii=False))