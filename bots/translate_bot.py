# Translate Bot - translates input text from one language to another

import string
import sys
from googletrans import Translator


empty_msg = 'Please enter text.'
symbols_msg = 'Translation of words with symbols are not accurate, please enter text without symbols.'
inp = ''

iso_639_choices = dict([('ab', 'Abkhaz'), ('aa', 'Afar'), ('af', 'Afrikaans'), ('ak', 'Akan'), ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('an', 'Aragonese'), ('hy', 'Armenian'), ('as', 'Assamese'),
                    ('av', 'Avaric'), ('ae', 'Avestan'), ('ay', 'Aymara'), ('az', 'Azerbaijani'), ('bm', 'Bambara'), ('ba', 'Bashkir'), ('eu', 'Basque'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('bh', 'Bihari'),
                    ('bi', 'Bislama'), ('bs', 'Bosnian'), ('br', 'Breton'), ('bg', 'Bulgarian'), ('my', 'Burmese'), ('ca', 'Catalan; Valencian'), ('ch', 'Chamorro'), ('ce', 'Chechen'), ('ny', 'Chichewa; Chewa; Nyanja'),
                    ('zh', 'Chinese'), ('cv', 'Chuvash'), ('kw', 'Cornish'), ('co', 'Corsican'), ('cr', 'Cree'), ('hr', 'Croatian'), ('cs', 'Czech'), ('da', 'Danish'), ('dv', 'Divehi; Maldivian;'), ('nl', 'Dutch'),
                    ('dz', 'Dzongkha'), ('en', 'English'), ('eo', 'Esperanto'), ('et', 'Estonian'), ('ee', 'Ewe'), ('fo', 'Faroese'), ('fj', 'Fijian'), ('fi', 'Finnish'), ('fr', 'French'), ('ff', 'Fula'),
                    ('gl', 'Galician'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek, Modern'), ('gn', 'Guaraní'), ('gu', 'Gujarati'), ('ht', 'Haitian'), ('ha', 'Hausa'), ('he', 'Hebrew (modern)'),
                    ('hz', 'Herero'), ('hi', 'Hindi'), ('ho', 'Hiri Motu'), ('hu', 'Hungarian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('ie', 'Interlingue'), ('ga', 'Irish'), ('ig', 'Igbo'), ('ik', 'Inupiaq'),
                    ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('iu', 'Inuktitut'), ('ja', 'Japanese'), ('jv', 'Javanese'), ('kl', 'Kalaallisut'), ('kn', 'Kannada'), ('kr', 'Kanuri'), ('ks', 'Kashmiri'),
                    ('kk', 'Kazakh'), ('km', 'Khmer'), ('ki', 'Kikuyu, Gikuyu'), ('rw', 'Kinyarwanda'), ('ky', 'Kirghiz, Kyrgyz'), ('kv', 'Komi'), ('kg', 'Kongo'), ('ko', 'Korean'), ('ku', 'Kurdish'),
                    ('kj', 'Kwanyama, Kuanyama'), ('la', 'Latin'), ('lb', 'Luxembourgish'), ('lg', 'Luganda'), ('li', 'Limburgish'), ('ln', 'Lingala'), ('lo', 'Lao'), ('lt', 'Lithuanian'), ('lu', 'Luba-Katanga'),
                    ('lv', 'Latvian'), ('gv', 'Manx'), ('mk', 'Macedonian'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mt', 'Maltese'), ('mi', 'Māori'), ('mr', 'Marathi (Marāṭhī)'), ('mh', 'Marshallese'),
                    ('mn', 'Mongolian'), ('na', 'Nauru'), ('nv', 'Navajo, Navaho'), ('nb', 'Norwegian Bokmål'), ('nd', 'North Ndebele'), ('ne', 'Nepali'), ('ng', 'Ndonga'), ('nn', 'Norwegian Nynorsk'),
                    ('no', 'Norwegian'), ('ii', 'Nuosu'), ('nr', 'South Ndebele'), ('oc', 'Occitan'), ('oj', 'Ojibwe, Ojibwa'), ('cu', 'Old Church Slavonic'), ('om', 'Oromo'), ('or', 'Oriya'), ('os', 'Ossetian, Ossetic'),
                    ('pa', 'Panjabi, Punjabi'), ('pi', 'Pāli'), ('fa', 'Persian'), ('pl', 'Polish'), ('ps', 'Pashto, Pushto'), ('pt', 'Portuguese'), ('qu', 'Quechua'), ('rm', 'Romansh'), ('rn', 'Kirundi'),
                    ('ro', 'Romanian, Moldavan'), ('ru', 'Russian'), ('sa', 'Sanskrit (Saṁskṛta)'), ('sc', 'Sardinian'), ('sd', 'Sindhi'), ('se', 'Northern Sami'), ('sm', 'Samoan'), ('sg', 'Sango'), ('sr', 'Serbian'),
                    ('gd', 'Scottish Gaelic'), ('sn', 'Shona'), ('si', 'Sinhala, Sinhalese'), ('sk', 'Slovak'), ('sl', 'Slovene'), ('so', 'Somali'), ('st', 'Southern Sotho'), ('es', 'Spanish; Castilian'),
                    ('su', 'Sundanese'), ('sw', 'Swahili'), ('ss', 'Swati'), ('sv', 'Swedish'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('ti', 'Tigrinya'), ('bo', 'Tibetan'),
                    ('tk', 'Turkmen'), ('tl', 'Tagalog'), ('tn', 'Tswana'), ('to', 'Tonga'), ('tr', 'Turkish'), ('ts', 'Tsonga'), ('tt', 'Tatar'), ('tw', 'Twi'), ('ty', 'Tahitian'), ('ug', 'Uighur, Uyghur'),
                    ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('ve', 'Venda'), ('vi', 'Vietnamese'), ('vo', 'Volapük'), ('wa', 'Walloon'), ('cy', 'Welsh'), ('wo', 'Wolof'), ('fy', 'Western Frisian'),
                    ('xh', 'Xhosa'), ('yi', 'Yiddish'), ('yo', 'Yoruba'), ('za', 'Zhuang, Chuang'), ('zu', 'Zulu')])
lang_codes = dict([(value, key) for key, value in iso_639_choices.items()])

while True:
    inp = input("Translate or exit : ")
    if inp == 'exit':
        sys.exit()
    from_lang = input('Enter language of input text : ').capitalize()
    to_lang = input("Enter language to which text should be translated : ").capitalize()
    translator = Translator()
    text = input('Enter text : ')
    non_letters = set(text) - set(string.ascii_lowercase)
    if non_letters:
        print(symbols_msg)
        continue
    if not text:
        print(empty_msg)
        continue
    print("Translated text : ", translator.translate(text, src=lang_codes[from_lang], dest=lang_codes[to_lang]).text, '\n\n')
