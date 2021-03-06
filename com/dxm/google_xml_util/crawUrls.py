# -*- coding: utf-8 -*-
import copy
from datetime import datetime
from xml.etree import ElementTree as ET

import pytz
import requests
import urllib3
from bs4 import BeautifulSoup
import sys
from urllib3.exceptions import InsecureRequestWarning


class xml_util:
    def __init__(self,dir_path):
        self._zero_zone = 0
        self._tag_prefix = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
        self._loc_tag = 'loc'
        self._lastmod_tag = 'lastmod'
        self._priority_tag = 'priority'
        self.date_str = self.get_utc_time(self._zero_zone)
        self.dir_path=dir_path
        self.tree = None
        self.url_tag = None

    def get_utc_time(self, zone):
        # 创建时区UTC+00:00
        #tz_utc = timezone(timedelta(hours=zone))
        # 获得带时区的UTC时间
        current_time_utc = datetime.utcnow().replace(tzinfo=pytz.timezone('UTC'), microsecond=0)
        timestr = current_time_utc.strftime("%Y-%m-%dT%H:%M:%S%z")
        new_time_str = "{}:{}".format(timestr[0:-2], timestr[-2:])
        return new_time_str

    def parseTemplateXml(self):
        self.tree = ET.parse("{}/template.xml".format(self.dir_path))
        ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
        root = self.tree.getroot()
        for urlTag in list(root):
            urls = list(urlTag)
            for url in urls:
                if self._tag_prefix + self._lastmod_tag == url.tag:
                    url.text = self.date_str
        self.url_tag = urlTag





    def mod_tag(self, tag, locValue, lastmodValue, priority='0.6'):
        for tg in list(tag):
            if self._tag_prefix + 'loc' == tg.tag:
                tg.text = locValue
            elif self._tag_prefix + 'lastmod' == tg.tag:
                tg.text = lastmodValue
            elif self._tag_prefix + 'priority' == tg.tag:
                tg.text = priority

    def write_url_tag(self, locValue):
        if self.url_tag is None:
            raise Exception("url_tag is null, please call reparseXml method first")
        new_tag_url = copy.deepcopy(self.url_tag)
        self.mod_tag(new_tag_url, locValue, self.date_str)
        self.tree.getroot().append(new_tag_url)

    def write_file(self, file_name):
        self.tree.write("{}/{}".format(self.dir_path,file_name), encoding='utf-8', xml_declaration=True)


def crawb(name, page_url):
    page = requests.get(page_url,verify=False).text
    soup = BeautifulSoup(page, 'html.parser')
    links = []
    for link in soup.find_all(name='a'):
        url = link.get("href")
        if str(url).endswith(".htm") and 'faq' in url:
            links.append('https://www.bigseller.com' + link.get('href'))
    return links


def crawMainUrl():
    url = 'https://www.bigseller.com/help/index.htm'
    page = requests.get(url,verify=False).text
    soup = BeautifulSoup(page, 'html.parser')
    languageMap = {}
    for alink in soup.find_all(name="a", attrs={"href": "javascript:"}):
        changLang = alink.get("onclick")
        if changLang is not None:
            lang_symbol = changLang.split('COMMON_FN.navChangeLang')[1]
            lang_symbol = str(lang_symbol).replace("(", "").replace(")", "").replace('\'', '').strip()
            lang_name = alink.text.strip()
            languageMap[lang_name] = lang_symbol
    urls = []
    oldUrl = url
    id = 'faqsLeftNav'
    for langName in languageMap.keys():
        suffix = '?lang=' + languageMap.get(langName)
        url = oldUrl + suffix
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.find(id=id).find_all("li"):
            name = link.find("p").get("name")
            text = link.find("p").text
            urls.append(("{}_".format(langName) + text.strip(),
                         'https://www.bigseller.com/help/faq/{}.htm{}'.format(name, suffix)))
    return urls


if __name__ == "__main__":
    #生成文件的目录
    #dir_path = sys.argv[1]
    dir_path=r'C:\Users\DXM_0093\PycharmProjects\flaskWeb\com\dxm\google_xml_util'
    # 编解码 设置默认编码方式
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # 去除警告
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    urllib3.disable_warnings()

    urls = crawMainUrl()
    util = xml_util(dir_path)
    util.parseTemplateXml()

    size = len(urls)
    index = 0
    for url in urls:
        name = url[0]
        page_url = url[1]
        link_urls = crawb(name, page_url)
        index += 1
        print("进度=======>{}%,name=>{},links_size=>{}".format(round(index * 100 / size),name,len(link_urls)))
        for link_url in link_urls:
            util.write_url_tag(link_url)
    util.write_file('sitemap.xml')
    print("--------------生成文件完毕{}---------------".format(util.date_str))

