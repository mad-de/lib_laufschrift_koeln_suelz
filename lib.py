#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import random
import json
from urllib import urlopen


def return_command_array():
	
    # GREETINGS

    greeting = 'Guten Morgen!'
    if datetime.datetime.now().hour > 11 and datetime.datetime.now().hour < 14:
        greeting = 'Mahlzeit!'
    if datetime.datetime.now().hour > 13 and datetime.datetime.now().hour < 19:
        greeting = 'Schönen Nachmittag!'	
    if datetime.datetime.now().hour > 18 and datetime.datetime.now().hour < 22:
        greeting = 'Guten Abend!'
    if datetime.datetime.now().hour > 21 and datetime.datetime.now().hour < 25:
        greeting = 'Gute Nacht!'	
	
    # DATES

    now = datetime.datetime.now()
    timestamp_kontaktverbot = 1584831600
    beginn_kontaktverbot = \
        datetime.datetime.fromtimestamp(timestamp_kontaktverbot)

    diff_days_kontaktverbot = abs((now - beginn_kontaktverbot).days)
    now = datetime.datetime.now()

    # WEATHER

    json_weather_url = \
        urlopen('http://api.openweathermap.org/data/2.5/weather?q=cologne&appid=0425f15e65bc996e74e9f9d0583cda12&units=metric&lang=de'
                )
    json_weather = json.loads(json_weather_url.read())

    # NEWS

    json_news_url = \
        urlopen('http://newsapi.org/v2/top-headlines?country=de&apiKey=2d9859f0514247a596b6eb020e0a81fe'
                )
    json_news = json.loads(json_news_url.read())
    newsticker = \
        'Der Coronavirus-freie Newsfeed mit Material von newsapi.org: '

    corona_free_int = 0
    for news_i in range(0, 20):
        if not json_news[u'articles'][news_i][u'source'][u'name'] \
            == None:
            get_ticker = ' +++ ' + json_news[u'articles'
                    ][news_i][u'source'][u'name'] + ': '
        if not json_news[u'articles'][news_i][u'title'] == None:
            get_ticker = get_ticker + json_news[u'articles'
                    ][news_i][u'title'] + '. '
        if not json_news[u'articles'][news_i][u'description'] == None:
            get_ticker = get_ticker + json_news[u'articles'
                    ][news_i][u'description']

	#if not (json_news[u'articles'][news_i][u'content'] == None):
	#    get_ticker = get_ticker + json_news[u'articles'][news_i][u'content']

        if not ('CORONA' in get_ticker.upper() or 'COVID'
                in get_ticker.upper() or 'DER WESTEN'
                in get_ticker.upper() or 'AUSGANGSBESCHR'
		in get_ticker.upper() or 'VIP'
	       	in get_ticker.upper() or 'BUNTE'
	       	in get_ticker.upper()):
            corona_free_int = corona_free_int + 1
            if corona_free_int < 4:
                newsticker = newsticker + get_ticker.encode('utf-8')

    # Recipe

    rezept_url = \
        urlopen('https://www.rezepteplan.de/SpeisePlan/Zuf%C3%A4lligerSpeisePlan.aspx?34=1'
                )
    rezept_html = rezept_url.read()
    temp_html = rezept_html.split('<br /><a RecipeId=', 1)[1]
    rezept_id = temp_html.split(' NiceTitle=', 1)[0].rstrip('"')[1:]
    temp_html = temp_html.split(' NiceTitle=', 1)[1]
    rezept_name = temp_html.split(' onmouseover', 1)[0].rstrip('"')[1:]

    # TEXTE
    # Ab hier die einzelnen Zeilen Ã€ndern / oder über "]" eine neue hinzufügen. Der Ticker aktualisiert sich nach jedem Merge automatisch.
    # Beispiel:
    #
    # 'Meine Nachricht'
    #,
    #

    command_array = [
        greeting + ' Heute ist der ' + str(datetime.datetime.now().day) + '.'
            + str(datetime.datetime.now().month) + '.'
            + str(datetime.datetime.now().year) + '. Es ist '
            + str(datetime.datetime.now().hour) + ' Uhr '
            + str(datetime.datetime.now().minute) + '.'
            ,
        'Heute ist der ' + str(diff_days_kontaktverbot)
            + '. Tag des Kontaktverbots in NRW und bundesweit.'
            ,
        'Bleibt zuhause und bleibt gesund!',
        newsticker,
        'Das Wetter: ' + str(json_weather[u'weather'][0][u'description'
                             ].encode('utf-8'))
            + '. Aktuelle Temperatur: ' + str(json_weather[u'main'
                ][u'temp']).replace('-', u'\u2212').encode('utf-8')
            + '\xc2\xb0C. Gef\xc3\xbchlte Temperatur: '
            + str(json_weather[u'main'][u'feels_like']).replace('-',
                u'\u2212').encode('utf-8') + '\xc2\xb0C.'
            ,
        'Unterst\xc3\xbctzt eure lokalen Gesch\xc3\xa4fte in dieser Zeit. Ihr wollt etwas lesen oder braucht eine DVD? Bestellt doch zum Beispiel \xc3\xbcber der-andere-buchladen-koeln@t-online.de.'
            ,
        'Viele Restaurants hier im Viertel bieten einen Lieferdienst oder Abholservice z.B. abs1.de, merstonnzesamme.de oder palanta.de. Auf bringsl.com gibt es auch einen Fahrradlieferdienst für Feinkost.'
            ,
        'Auf der Suche nach guter Musik ohne Werbung oder Corona-Nachrichten: www.radioparadise.com'
            ,
        #'Langweilig und Lust auf einen guten Film? Die 10 besten Filme des 21. Jahrhunderts (lt. BBC): 10) No Country for Old Men von Joel Coen and Ethan Coen 9) A Separation von Asghar Farhadi 8) Yi Yi von Edward Yang 7) The Tree of Life von Terrence Malick 6) Eternal Sunshine of the Spotless Mind von Michel Gondry 5) Boyhood von Richard Linklater 4) Spirited Away von Hayao Miyazaki 3) There Will Be Blood von Paul Thomas Anderson 2) In the Mood for Love von Wong Kar-wai 1) Mulholland Drive von David Lynch ... Viel Spass beim Anschauen!'
        #    ,
        'Was soll man nur kochen? Wie w\xc3\xa4re es mit '
            + rezept_name
            + '? Rezept unter: https://www.rezepteplan.de/Rezepte/.rezept?0='
             + rezept_id + ' Guten Appetit!'
            ,
        #'Wie w\xc3\xa4re es mit einer neuen Serie? Die 10 besten Serien aller Zeiten (lt. Cinemablend): 10) The Simpsons 9) Mad Men 8) I love Lucy 7) Saturday Night Live 6) The Sopranos 5) Seinfeld 4) Game of Thrones 3) The X-Files 2) Breaking bad 1) Friends ... Viel Spass beim Suchten!'
        #    ,
        'Danke an Alle, die den Laden hier am Laufen halten!'
            ,
	'ABS verteilt jeden Tag kostenlos Essen an Bedürftige im Gottesweg 135 ab 17 Uhr. '
            ,
	'Habt ihr noch medizinisches Material wie Einmalhandschuhe oder Atemschutzmasken übrig? Spendet sie doch an Gesundheitsdienstleister auf remedymatch.io'
            ,
	'Von uns getestete, kostenlose Spiele f\xc3\xbcr einen Remote-Spieleabend mit (ebenfalls isolierten) Freunden: Trickster (App), Drawful 2 (Steam). Viel Spass beim Ausprobieren!'
            ,
        'Ihr braucht aktuell jemanden, der f\xc3\xbcr euch einkauft? Ihr wollt Hilfe anbieten? Freiwillige Helfer findet man unter anderem auf machbarschaft.jetzt & colivery.de & nebenan.de/corona & die-einkaufshelden.de oder auch telefonisch: 040 299960980. Oder ihr schreibt uns per Whatsapp: +44 7537 1818 02. Wir helfen auch gerne!'
            ,
	'Eure Nachricht hier anzeigen lassen? https://github.com/mad-de/lib_laufschrift_koeln_suelz/ Oder wollt ihr uns etwas mitteilen? Whatsapp: +44 7537 181802'
            ,
        ]

  #  random.shuffle(command_array)

    return command_array
