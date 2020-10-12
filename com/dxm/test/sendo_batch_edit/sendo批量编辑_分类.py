# encoding=utf-8
import requests

url = 'http://localhost:19080'
#1:草稿,2:发布中,3:发布失败,4:在线
resp = requests.post(url=url,

                    data={
                        'platform': 'sendo', 'batchEditIds': '1153,1177','bsStatus':'xx','ids': '1153,1177'
                    },
                    headers={
                        'Cookie': '_ga=GA1.1.1819001414.1599449838; _ati=263102032090; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; _gid=GA1.1.728894743.1602465461; SHAREJSESSIONID=09958ed0-98da-401c-aec6-228437d991ec; rememberMe=axfnqslAVn9r0mKnADLRUxyEj+CVRM2z53VQrvEnQPKE9WvLQnjq28w2UZ4PYiT/5A2nVmRiFnE/phyddeo42SigTL+m8HDH8l/+cXvO4RtK1eLVYIqTXrF/+PKsg4QIW3mnSqkZi4lIY8Xsh1ii/dQ/Cl+wytUI0+T0ZAAJXfXhyTHD4TQWmm0575nxBLvimhscYfE7v3EFtUAfZKL4ga1xXnsU6VWIHftqh2lM0CpnP7YFLV39x4OFRjSVo/M9llZyPIqR1fCnFaiD5HC3ke3chCe1Mcl47iXlxRZRDEyhzYvFF2Co6XDOQ68KflgPq3xtRi/2y3K8hpFV59datX4eQG2F48gvzZw0L12Oo3jbvauXM5dJUNfAWEETVgxHRs6mboknFocq+07JhPGkMqgSjS4ymZ5rDqMWkNwsNOsmojnqkg/hpf7q+VK1J4kXuXIW1defGy74127/k5Gg/LkfBxgSlUX0Q/YFXchSO5JMKKE2t3g9ht9hgwMNEYiV20HfdgTHo1r83uv9UiEpEz04/QYX2NT3EUhvuOQ9XWzF+OZdVrY/rcYYR8sPH2Il'
                    })

print resp.status_code
print resp.headers['Content-Type']
print resp.text
