#!/usr/bin/env python3
import mmh3
import requests
import codecs

response = requests.get('https://m.forzza.co/Content/images/app-snapshot.ico')
favicon = codecs.encode(response.content,"base64")
hash = mmh3.hash(favicon)
print(hash)

