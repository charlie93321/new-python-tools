import json

import  requests
lines ='''
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cookie: _gcl_au=1.1.1958773265.1600313116; _med=refer; SPC_IA=-1; SPC_EC=-; SPC_F=Ogcp16royJ8MnetDpl32DoiaVm1l27zu; REC_T_ID=671ed3fe-f895-11ea-bd36-b496918692ba; SPC_U=-; language=zhHans; _ga=GA1.3.1122102122.1600313132; SPC_SI=mall.3TFn0tv83kjxqU1Dy3BiUG742C5mJJHR; SPC_R_T_ID="1qy/KwNBD7OqlPVfkEOEKyk2kK+Zi/W6edfnmYMf6oyeaUxf3udzMcBn4td6CAuTb6l5ahMtGDuCeQJvIb4H0u9IY2kpcnKn3lZHecPAIJU="; SPC_T_IV="KtgZN/Pj8Kt85s2HgZj3VA=="; SPC_R_T_IV="KtgZN/Pj8Kt85s2HgZj3VA=="; SPC_T_ID="1qy/KwNBD7OqlPVfkEOEKyk2kK+Zi/W6edfnmYMf6oyeaUxf3udzMcBn4td6CAuTb6l5ahMtGDuCeQJvIb4H0u9IY2kpcnKn3lZHecPAIJU="; AMP_TOKEN=%24ERROR; _gid=GA1.3.118032311.1601459891; _dc_gtm_UA-61915055-6=1
if-none-match-: 55b03-2e5bc3dd0930dbbd734ddbcbec3246f0
referer: https://shopee.com.my/Girls-children's-clothing-children's-rainbow-wings-denim-suspender-i.264854728.7453641936
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
x-api-source: pc
x-requested-with: XMLHttpRequest
x-shopee-language: zh-Hans
'''
headers={}
for line in lines.split("\n"):
    line = line.strip()
    if len(line)>0:
        args = line.split(":")
        if line.startswith(":"):
            headers[":{}".format(args[1].strip())]=args[2].strip()
        else:
            headers[args[0].strip()] = args[1].strip()
print(headers)


resp = requests.get(url='https://shopee.com.my/api/v2/item/get?itemid=7453641936&shopid=264854728',headers=headers)


print(resp.text)