#!/usr/bin/python3

import webbrowser
import sys
import base64
import os
import json
from urllib.parse import quote


chrome_path = 'open -a /Applications/Google\ Chrome.app %s'



# google drive

url = "https://drive.google.com/drive/search?q=" + sys.argv[1]

webbrowser.get(chrome_path).open(url)



# github

url = "https://github.com/search?q=org%3Agithub+" + sys.argv[1] + "&type=issues"

webbrowser.get(chrome_path).open(url)



# thehub

url = "https://thehub.github.com/search/?query=" + sys.argv[1]

webbrowser.get(chrome_path).open(url)



# slack

query = sys.argv[1]
search_data = json.dumps({
    "d": quote(query),
    "r": quote(query)
})
qhash = base64.b64encode(search_data.encode()).decode()
url = f'https://app.slack.com/client/T0CA8C346/search/search-{qhash}'

os.system(f'open "" {url}')


# email?


# others?

