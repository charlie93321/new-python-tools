

import  requests
url = 'http://localhost:19080/sitemap.xml'
url ='https://test.bigseller.com/sitemap.xml'
resp = requests.get(url)


print resp.headers['Content-Type']



