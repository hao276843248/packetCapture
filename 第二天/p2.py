import json

import requests

cookies = {

}

headers = {

}

json_data = {
    'format_type': 'format_json',
    'input_str': open("../data/急性腹膜炎.txt","r",encoding="utf-8").read(),
}

response = requests.post('https://spidertools.cn/spidertools/format_json', cookies=cookies, headers=headers, json=json_data)
print(json.loads(response.text))