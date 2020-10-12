#encoding=utf-8
'''
#写入的文件编码格式为utf-8
with open("robots.txt","w")as f:
 f.write("User-agent: *".encode("utf-8"))
 f.write("\n")
 f.write("Sitemap: https://www.bigseller.com/sitemap.xml".encode("utf-8"))'''
import requests

resp = requests.get('https://test.bigseller.com/robots.txt')

print resp.headers['Content-Type']

print resp.text