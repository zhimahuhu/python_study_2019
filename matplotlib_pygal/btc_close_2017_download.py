from __future__ import (absolute_import, division, print_function, unicode_literals)
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import json
import requests

if __name__ == '__main__':
    json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
    # response = urlopen(json_url)
    # req = response.read()
    req = requests.get(json_url)
    with open('btc_close_2017.json', 'w') as f:
        f.write(req.text)
    # file_urllib = json.loads(req)
    # print(file_urllib)
    file_requests = req.json()
    print(file_requests)
