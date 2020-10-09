import json
import time
import warnings

warnings.filterwarnings("ignore", category=Warning)
import redis
import requests

prefix = 'http://localhost:8080'

cookie = 'Cookie: _ati=9439750950521; _ga=GA1.1.1851909.1599449244; rememberMe=mJ2lXwB3KtdOSBd5zgZZs6MM3mha+Vr63D0ehRHDeWkO71cOjdlrlXLR7jgwtdeiTvMPXx+bQiuYSK3X41hbx7FVEPb2lDsvJ1oMOKB8ZTURlODHDBYUe0GRZ2gRAxlw6ClGaJVQUsxUaeGByztmmkuOtjT9cEMhqRwqVTpzx/MDFsdkvP7LOnJu53CWiryyo1WavK7WO8PKneYFwZn5nhlt8DgiqzHF+uTSNkL+j2nHPDxxogzDlrhFaWRU7dfL6zfMTtZ7rPa7c9CymVkBwmi+JmnBlKZSKhbVHt6jnDhVFXpsSWoIrirEVn2hUBxYkZNQ51UtcTmkr0LeKJ9ZAmoZ68UHoJP2JFx4nw63l8+KPJxHUU8QlJNyLYeqFODUdBcqEUpQHXIxtToYnmYX2i/oaJHdH8+Tk05wJWadM3FFAAROY68ayZnfz+e1EOZkohHBt0vqzL4ZwZWnd0vijdZs4GsfPF0MWHqBQ28L6ZBn60pY5xPeuQa8vBXGLC3cZS2CIL5qnOnSM7n75a/dfHKLrrfrjV6xf8TrLBy2pb9B97X0aVpRdd/7uuaz6kxS; _gid=GA1.1.82248995.1599650536; SHAREJSESSIONID=77cd690b-f561-4798-a657-d718d385ed3e'

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'Cookie': cookie,

    'Content-Type': 'application/json',
    'Host': 'localhost:8080',
    'Referer': 'http://localhost:8080/inventory/inout/list/out/index.json',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest'
}

data = {"id": "1177", "shopId": "843", "categoryId": "6382",
        "name": "Headphone J-18 / J18 MACARON CARTOON Stereo Extra Bass - Merah Muda", "itemSku": "产品sku",
        "optionName1": "Màu sắc", "optionId1": 284, "optionName2": "Kích thước", "optionId2": 1130, "optionName3": "",
        "optionId3": "",
        "images": "https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/27/47240405/47240405_cd5fd51d-4646-4194-894e-2e482b71d27c_1280_1280,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/24/47240405/47240405_c7337103-ef80-4c13-ad6a-e103f0314dda_700_700,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/24/47240405/47240405_7c017ffc-7627-4818-8563-c8fbcb112add_800_800,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/24/47240405/47240405_e00dfaec-69ae-4227-a491-9e6131c035ad_700_700",
        "price": "", "salePrice": "", "saleStartDate": "", "saleEndDate": "", "stock": "",
        "productExtra": {"videoUrl": "", "weight": "450", "length": "12", "width": "35", "height": "11", "unitId": "7",
                         "tags": "关键词", "seoTitle": "", "seoKeyword": "", "seoDescription": "",
                         "sourceUrl": "https://www.tokopedia.com/k2-official/headphone-j-18-j18-macaron-cartoon-stereo-extra-bass-merah-muda",
                         "productType": "1"}, "productText": {
        "description": "J-18 / J18 Headphone Macaron Cartoon Stereo Extra Bass<br />\n<br />\nLEBIH COCOK UTK ANAK2 / WANITA, karena ukuran bando lebih kecil",
        "attributes": "[{\"attribute_id\":284,\"attribute_name\":\"Màu sắc\",\"attribute_is_required\":true,\"attribute_code\":\"\",\"attribute_is_custom\":false,\"attribute_is_checkout\":true,\"attribute_is_image\":false,\"attribute_values\":[{\"id\":602,\"value\":\"Nâu\",\"attribute_img\":\"\",\"is_selected\":true,\"is_custom\":false}]},{\"attribute_id\":1130,\"attribute_name\":\"Kích thước\",\"attribute_is_required\":true,\"attribute_code\":\"\",\"attribute_is_custom\":false,\"attribute_is_checkout\":true,\"attribute_is_image\":false,\"attribute_values\":[{\"id\":19120,\"value\":\"New born\",\"attribute_img\":\"\",\"is_selected\":true,\"is_custom\":false},{\"id\":19049,\"value\":\"6 - 8kg\",\"attribute_img\":\"\",\"is_selected\":true,\"is_custom\":false}]}]"},
        "variationList": [
            {"optionName1": "Nâu", "optionId1": 602, "optionName2": "New born", "optionId2": 19120, "optionName3": "",
             "optionId3": "", "variationSku": "产品sku-Nâu-New born", "price": "30000", "stock": "68",
             "salePrice": "9000", "saleStartDate": "2020-09-29", "saleEndDate": "2020-09-29"},
            {"optionName1": "Nâu", "optionId1": 602, "optionName2": "6 - 8kg", "optionId2": 19049, "optionName3": "",
             "optionId3": "", "variationSku": "产品sku-Nâu-6 - 8kg", "price": "30000", "stock": "89", "salePrice": "7000",
             "saleStartDate": "2020-09-29", "saleEndDate": "2020-10-02"}], "operate": "edit"}

data = {
    "id": "1177",
    "shopId": "843",
    "name": "Headphone J-18 / J18 MACARON CARTOON Stereo Extra Bass - Merah Muda",
    "itemSku": "产品sku",
    "images": "https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/27/47240405/47240405_cd5fd51d-4646-4194-894e-2e482b71d27c_1280_1280,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/24/47240405/47240405_c7337103-ef80-4c13-ad6a-e103f0314dda_700_700,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/24/47240405/47240405_7c017ffc-7627-4818-8563-c8fbcb112add_800_800,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/8/24/47240405/47240405_e00dfaec-69ae-4227-a491-9e6131c035ad_700_700",
    "price": "",
    "salePrice": "",
    "saleStartDate": "",
    "saleEndDate": "",
    "stock": "",
    "weight": "450",
    "length": "12",
    "width": "35",
    "height": "11",
    "unitId": "7",
    "productType": "1"
    , "variationEditVos": [
        {
            "id": 7285,
            "variationSku": "产品sku-Nâu-New born",
            "price": "30000",
            "stock": "68",
            "salePrice": "9000",
            "saleStartDate": "2020-09-29",
            "saleEndDate": "2020-09-29"
        },
        {

            "id": 7286,
            "variationSku": "产品sku-Nâu-6 - 8kg",
            "price": "40000",
            "stock": "89",
            "salePrice": "5000",
            "saleStartDate": "2020-09-29",
            "saleEndDate": "2020-10-01"
        }
    ], "operate": "edit"}
datas = []
datas.append(data)
resp = requests.post(url=prefix + '/listing/sendo/editBatchSave.json', data=json.dumps(datas), headers=headers)

print(resp.text)
r = redis.Redis(host='192.168.1.201', port=8531, password='dxm!123@321#')
reData = json.loads(resp.text)
redisKey = reData['data']
if redisKey is not None:
    while True:
        time.sleep(0.5)
        redata = json.loads(r.get(redisKey), encoding='utf-8')
        print(redata)
        if redata != None:
            if redata['code'] == 1:
                break
