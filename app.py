import base64
from random import Random

from flask import Flask, send_from_directory
app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/static")
@app.route('/')
def hello_world():
      return "hello"


@app.route('/lazada/label')
def lazada_label():
    import requests
    url = 'https://manage.bigseller.com/search/print.htm?platform=lazada&orderId=262364007317143'
    resp = requests.get(url=url, headers={
        'Cookie': '_ga=GA1.2.783650283.1599030915; _ati=2883770674564; _gid=GA1.2.2089958532.1600651172; rememberMe_BG=bQ7DaG295EadXkyV38LYQ+yoqP9matLiKrZKtaAxNQp6Z9LJAbJNpXWUHXImWwau0oHoVDRZNEZhyC9sYmpjvWf++LI2KD46kAdt3HZCzNbhi/pqnatctZbh9gaxV0hnnUJLhJ7vJG1+NETgn6EAdmKOIZVX4GFjLOQkRfAXedQJvMwX78Xk8Df5B7Wp+1sxRJiRYxPRF7zuzCJS7nyLq/E7QvnFOBj9lxG2l00ymL4Qvx17PM3hKQUvG3sPqcN9tN9SWCMyXCMwZrHhYjkwXhetxrk6zBGXWOE630Qb8SzLkYJ8BYyiiKGh5hta6LV/3xrgpUcH5uGpPDlvh/m1KsGC+WaK4lLCwtSQrSn00uMOw+LJaanchToAnDnmnMhubk2qotPL01aB29PNu9YZ7fosTJr54xr7rESVKBlh706u1SUKpoovvxOv87b0KBrtHtvDky9gV2dc3BqtUA82X3GujIfR1qY702P2hHm8OyEOHZtRhMXKYbLvZH12qQ00eOINR8yIwwvoiYbNRWy95hRxovPS9l5ZeZ6BQRQgfaP86xmSQ+hMCg811GuHku7u; Hm_lvt_d97abf6d61c21d773f97835defbdef4e=1600680591; Hm_lpvt_d97abf6d61c21d773f97835defbdef4e=1600680591; SHAREJSESSIONID_BG=f77f22c9-dd36-4f5e-9807-ea3c968cf130'})
    print(resp.status_code)
    str64 = base64.b64encode(resp.content)
    return str(str64, encoding='utf-8')





@app.route('/lazada/poslaju/label')
def lazada_poslaju_label():
    import requests
    i = Random().randint(1,10000000000000)
    #   262025268373081
    id = '262364007317143'
    if i % 2 == 0:
        id = '262364007317143'
    else:
        id = '262025268373081'

    url = 'https://manage.bigseller.com/search/print.htm?platform=lazada&orderId={}'.format(id)
    resp = requests.get(url=url, headers={
        'Cookie': '_ga=GA1.2.783650283.1599030915; _ati=2883770674564; _gid=GA1.2.2089958532.1600651172; rememberMe_BG=bQ7DaG295EadXkyV38LYQ+yoqP9matLiKrZKtaAxNQp6Z9LJAbJNpXWUHXImWwau0oHoVDRZNEZhyC9sYmpjvWf++LI2KD46kAdt3HZCzNbhi/pqnatctZbh9gaxV0hnnUJLhJ7vJG1+NETgn6EAdmKOIZVX4GFjLOQkRfAXedQJvMwX78Xk8Df5B7Wp+1sxRJiRYxPRF7zuzCJS7nyLq/E7QvnFOBj9lxG2l00ymL4Qvx17PM3hKQUvG3sPqcN9tN9SWCMyXCMwZrHhYjkwXhetxrk6zBGXWOE630Qb8SzLkYJ8BYyiiKGh5hta6LV/3xrgpUcH5uGpPDlvh/m1KsGC+WaK4lLCwtSQrSn00uMOw+LJaanchToAnDnmnMhubk2qotPL01aB29PNu9YZ7fosTJr54xr7rESVKBlh706u1SUKpoovvxOv87b0KBrtHtvDky9gV2dc3BqtUA82X3GujIfR1qY702P2hHm8OyEOHZtRhMXKYbLvZH12qQ00eOINR8yIwwvoiYbNRWy95hRxovPS9l5ZeZ6BQRQgfaP86xmSQ+hMCg811GuHku7u; Hm_lvt_d97abf6d61c21d773f97835defbdef4e=1600680591; Hm_lpvt_d97abf6d61c21d773f97835defbdef4e=1600680591; SHAREJSESSIONID_BG=f77f22c9-dd36-4f5e-9807-ea3c968cf130'})

    print(resp.status_code)
    str64 = base64.b64encode(resp.content)
    return str(str64, encoding='utf-8')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
