# Dictionary Bot - shows definition, synonyms, antonyms and other features related to the input word

import json
import requests
import sys
import string


API = 'https://dictionaryapi.com/api/v3/references/thesaurus/json/{}?key=b86d6042-e481-4e87-9463-6d804d576778'
error_msg = 'Could not load feature or feature not present for input word.'
empty_msg = 'Please enter a word.'
phrase_msg = 'Definitions for phrases are not available.'
symbols_msg = 'Definitions of words with symbols are not possible.'
inp = ''

while True:
    inp = input("Enter command : ").lower()
    if inp == 'exit':
        sys.exit()
    word = input("\nEnter word : ").lower()
    if len(word.split(' ')) > 1:
        print(phrase_msg)
        continue
    non_letters = set(word) - set(string.ascii_lowercase)
    if non_letters:
        print(symbols_msg)
        continue
    if not word:
        print(empty_msg)
        continue
    response = json.loads(requests.request('GET', API.format(word)).content.decode('utf-8'))
    if inp == 'synonyms':
        syns = response[0]['def'][0]['sseq'][0][0][1]['syn_list'][0]
        if not syns:
            print(error_msg)
            continue
        for syn in syns:
            print(syn['wd'])
    if inp == 'related words':
        rels = response[0]['def'][0]['sseq'][0][0][1]['rel_list']
        if not rels:
            print(error_msg)
            continue
        for rel in rels:
            for r in rel:
                print(r['wd'])
    if inp == 'antonyms':
        ants = response[0]['meta']['ants']
        if not ants:
            print(error_msg)
            continue
        for ant in ants:
            for a in ant:
                print(a)
    if inp == 'example':
        exs = response[0]['def'][0]['sseq']
        if not exs:
            print(error_msg)
            continue
        for ex in exs:
            for e in ex:
                for i in e[1:]:
                    print(i['dt'][1][1][0]['t'])
    if inp == 'define':
        defs = response[0]['def'][0]['sseq'][0][0][1]['dt'][0]
        if not defs:
            print(error_msg)
            continue
        print(defs[1])
