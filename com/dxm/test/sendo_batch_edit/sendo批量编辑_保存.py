# encoding=utf-8
import json

import requests

url = 'http://localhost:19080/listing/sendo/editBatchSave.json'
product_edit_vo = {
    "id": "1177", "shopId": "843",
    "name": "Headphone J-18 / J18 MACARON CARTOON Stereo Extra Bass - Merah Muda",
    "itemSku": "产品sku",
    "images": "https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/27/47240405/47240405_cd5fd51d-4646-4194-894e-2e482b71d27c_1280_1280,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/24/47240405/47240405_c7337103-ef80-4c13-ad6a-e103f0314dda_700_700,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/24/47240405/47240405_7c017ffc-7627-4818-8563-c8fbcb112add_800_800,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/24/47240405/47240405_e00dfaec-69ae-4227-a491-9e6131c035ad_700_700",
    "price": "",
    "salePrice": "",
    "saleStartDate": "",
    "saleEndDate": "",
    "stock": "",
    "weight": "",
    "length": "12",
    "width": "35",
    "height": "11",
    "unitId": "7",
    "productType": "1",
    "variationEditVos": [
        {
            "variationSku": "产品sku-Nâu-New born",
            "price": "30000",
            "stock": "68",
            "salePrice": "9000",
            "saleStartDate": "2020-09-29",
            "saleEndDate": "2020-09-29"
        },
        {
            "variationSku": "产品sku-Nâu-6 - 8kg",
            "price": "40000",
            "stock": "89",
            "salePrice": "5000",
            "saleStartDate": "2020-09-29",
            "saleEndDate": "2020-10-01"
        }
    ]
}
resp = requests.post(url=url,

                     data=json.dumps(
                         [
                             product_edit_vo
                         ]
                     ),
                     headers={
                         'Content-Type': 'application/json;charset=utf-8',
                         'Cookie': '_ga=GA1.1.1819001414.1599449838; _ati=263102032090; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; _gid=GA1.1.728894743.1602465461; SHAREJSESSIONID=09958ed0-98da-401c-aec6-228437d991ec; rememberMe=axfnqslAVn9r0mKnADLRUxyEj+CVRM2z53VQrvEnQPKE9WvLQnjq28w2UZ4PYiT/5A2nVmRiFnE/phyddeo42SigTL+m8HDH8l/+cXvO4RtK1eLVYIqTXrF/+PKsg4QIW3mnSqkZi4lIY8Xsh1ii/dQ/Cl+wytUI0+T0ZAAJXfXhyTHD4TQWmm0575nxBLvimhscYfE7v3EFtUAfZKL4ga1xXnsU6VWIHftqh2lM0CpnP7YFLV39x4OFRjSVo/M9llZyPIqR1fCnFaiD5HC3ke3chCe1Mcl47iXlxRZRDEyhzYvFF2Co6XDOQ68KflgPq3xtRi/2y3K8hpFV59datX4eQG2F48gvzZw0L12Oo3jbvauXM5dJUNfAWEETVgxHRs6mboknFocq+07JhPGkMqgSjS4ymZ5rDqMWkNwsNOsmojnqkg/hpf7q+VK1J4kXuXIW1defGy74127/k5Gg/LkfBxgSlUX0Q/YFXchSO5JMKKE2t3g9ht9hgwMNEYiV20HfdgTHo1r83uv9UiEpEz04/QYX2NT3EUhvuOQ9XWzF+OZdVrY/rcYYR8sPH2Il'
                     })

print resp.status_code
print resp.headers['Content-Type']
print resp.text
