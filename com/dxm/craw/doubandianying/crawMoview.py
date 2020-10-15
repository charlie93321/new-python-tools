# -- encoding=utf-8

import requests
from bs4 import BeautifulSoup

url='http://localhost:8080/listing/sendo/index.htm'
headers={
    'Cookie': '_ga=GA1.1.1819001414.1599449838; _ati=263102032090; _gid=GA1.1.728894743.1602465461; rememberMe=61rZilsKKlxLI9RI4Psz/36l0aLbGzPxxzJpknLKCQKPP8Z8iVd2j5Zk2aUC5tO9E9vs+uNhwtPN+D/v64vtnqevxtO8vpxNZE/An2BR3pIIdgtRbEBaHhSCw7842Mc8AJZIxLsJXTViukE6PP31Lmb3/13topojhRNuxaERThz+Vg1jTKFaDm6Ork0w12hD5aED46Dw94yek1SL5K5z2Qe2vveYl3Th/H41qilDeW8bcvOO5RaHOu2GoMRu6QPDPi/ePvhFoREr8QZ4CEluKE4zZ7EUlzvugSDs19IwM+jbvG41UGr18FT1T+nDevA8xN0NCqKpoSKPsP3XpnUwD82Y3CZIqQf7+1t977lOm4dSxsi/pnROSpKMG4h5/CBdG39hwyI4oGRE65fJysENgz/DJArJDdV6NHl2kp1DdY5reL6N/siV+LIoG9LpcnJqhDlVqyJgBkmIyomKtTXRhY9wMu9ahjTnOGZBGH86fOvG740scRy+f/Viwq/qvyRe9Mq0wRjTHzmaaNvLepDaSyesvPm5JOmfm7TS3gJ8BdVMoimQtp8w0ZsQ76JndOYa; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; JSESSIONID=B9648F5527782817A0BB064992A0DA91; SHAREJSESSIONID=54734a34-fa8a-4b3a-8c7b-77f1aad13f80'
}
resp = requests.get(url=url,headers=headers)


print BeautifulSoup(resp.text.strip(),"html.parser")
