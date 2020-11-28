# Search Bot - displays web search of input

import json
import requests
import sys

API = 'http://api.serpstack.com/search?access_key=a62765649ce08acb89966a11fa8c2df0&query={}'
empty_msg = 'Please enter text.'
inp = ''

while True:
    do = input("Search or exit : ")
    if do == 'exit' :
        sys.exit()
    inp = input("\nEnter word/phrase : ").lower()
    if inp == 'exit':
        sys.exit()
    print('\n')
    if inp.split(' ') is not None:
        inp = inp.replace(' ', '-')
    response = requests.request('GET', API.format(inp))
    response = json.loads(response.content.decode('utf-8'))
    if 'knowledge_graph' in response:
        print("Description : ", response['knowledge_graph']['description'], '\n\n')
    print("Found Results/Links : ", len(response['organic_results']))
    for results in response['organic_results']:
        print('\nTitle : ', results['title'], '\nSnippet : ', results['snippet'], '\nURL : ', results['url'])