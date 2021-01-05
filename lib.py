#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import random
import json
from urllib import urlopen
from requests import Request, Session
import requests
import pandas as pd

# Crypto

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':'LTC,BTC,XLM,ETH,EURS',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'ea1255b1-ccb2-49a2-9043-3a84fa9bc62e',
}

session = Session()
session.headers.update(headers)
response = session.get(url, params=parameters)
data = json.loads(response.text)

ethUSD = str("{:,.2f}".format(data[u'data'][u'ETH'][u'quote'][u'USD'][u'price']))
ethEUR = str("{:,.2f}".format(data[u'data'][u'ETH'][u'quote'][u'USD'][u'price'] /  data[u'data'][u'EURS'][u'quote'][u'USD'][u'price']))
if data[u'data'][u'ETH'][u'quote'][u'USD'][u'percent_change_24h'] > 0:
 eth24h = "+" + str("{:.2f}".format(data[u'data'][u'ETH'][u'quote'][u'USD'][u'percent_change_24h']))
else:
  eth24h = str("{:.2f}".format(data[u'data'][u'ETH'][u'quote'][u'USD'][u'percent_change_24h'])).replace('-', '- ').encode('utf-8')

btcUSD = str("{:,.2f}".format(data[u'data'][u'BTC'][u'quote'][u'USD'][u'price']))
btcEUR = str("{:,.2f}".format(data[u'data'][u'BTC'][u'quote'][u'USD'][u'price'] /  data[u'data'][u'EURS'][u'quote'][u'USD'][u'price']))
if data[u'data'][u'BTC'][u'quote'][u'USD'][u'percent_change_24h'] > 0:
 btc24h = "+" + str("{:.2f}".format(data[u'data'][u'BTC'][u'quote'][u'USD'][u'percent_change_24h']))
else:
  btc24h = str("{:.2f}".format(data[u'data'][u'BTC'][u'quote'][u'USD'][u'percent_change_24h'])).replace('-', '- ').encode('utf-8')

ltcUSD = str("{:,.2f}".format(data[u'data'][u'LTC'][u'quote'][u'USD'][u'price']))
ltcEUR = str("{:,.2f}".format(data[u'data'][u'LTC'][u'quote'][u'USD'][u'price'] /  data[u'data'][u'EURS'][u'quote'][u'USD'][u'price']))
if data[u'data'][u'LTC'][u'quote'][u'USD'][u'percent_change_24h'] > 0:
 ltc24h = "+" + str("{:.2f}".format(data[u'data'][u'LTC'][u'quote'][u'USD'][u'percent_change_24h']))
else:
  ltc24h = str("{:.2f}".format(data[u'data'][u'LTC'][u'quote'][u'USD'][u'percent_change_24h'])).replace('-', '- ').encode('utf-8')

xlmUSD = str("{:,.3f}".format(data[u'data'][u'XLM'][u'quote'][u'USD'][u'price']))
xlmEUR = str("{:,.3f}".format(data[u'data'][u'XLM'][u'quote'][u'USD'][u'price'] /  data[u'data'][u'EURS'][u'quote'][u'USD'][u'price']))
if data[u'data'][u'XLM'][u'quote'][u'USD'][u'percent_change_24h'] > 0:
 xlm24h = "+" + str("{:.2f}".format(data[u'data'][u'XLM'][u'quote'][u'USD'][u'percent_change_24h']))
else:
  xlm24h = str("{:.2f}".format(data[u'data'][u'XLM'][u'quote'][u'USD'][u'percent_change_24h'])).replace('-', '- ').encode('utf-8')

crypto_ticker = "Die aktuellen Cryptokurse: Bitcoin: " + btcUSD + " $ (" + btcEUR + " €); " + btc24h + " % || Ethereum: " + ethUSD + " $ (" + ethEUR + " €); " + eth24h + " % || Stellar: " + xlmUSD + " $ (" + xlmEUR + " €); " + xlm24h + " % || Litecoin: " + ltcUSD + " $ (" + ltcEUR + " €); " + ltc24h + " %"

# Vaccinations

url_vaccinations = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Impfquotenmonitoring.xlsx?__blob=publicationFile'
vacc_request = requests.get(url_vaccinations)

with open('Impfquotenmonitoring.xlsx', 'wb') as f:
    f.write(vacc_request.content)

vaccinations_table = pd.read_excel('Impfquotenmonitoring.xlsx', sheet_name=1)
vaccinations_date = pd.read_excel('Impfquotenmonitoring.xlsx', sheet_name=0)

vaccination_ger_num = vaccinations_table.values.tolist()[16][1]
vaccination_ger_perc = vaccination_ger_num / 83002000 * 100
vaccination_ger_diff = vaccinations_table.values.tolist()[16][2]
vaccination_date = str(vaccinations_date.values.tolist()[1])
vaccination_date = vaccination_date.split('Impfungen_bis_einschl_', 1)[1]
vaccination_date = vaccination_date.split(')', 1)[0]

vaccinations_diff = pd.read_excel('~/rpi-rgb-led-matrix/examples-api-use/Impfquotenmonitoring.xlsx', sheet_name=2).values.tolist()
vaccinations_diff_dates = len(vaccinations_diff)
vaccinations_diff = (float(vaccinations_diff[vaccinations_diff_dates-1][1]) - float(vaccinations_diff[vaccinations_diff_dates-2][1])) / float(vaccinations_diff[vaccinations_diff_dates-1][1]) * 100
if vaccinations_diff > 0:
   vaccinations_diff_vorz = "+"

# Old format (until 04-01-2021)
#vaccination_date_time = vaccinations_date.values.tolist()[1][2]
#vaccination_date = vaccination_date.strftime("%m.%d.%Y")

vaccinations = "Aktuelle COVID-19-Impfungen in Deutschland: Es wurden " + str("{:,.0f}".format(vaccination_ger_num)) + " Personen (" + str("{:.2f}".format(vaccination_ger_perc)) + " % der Bevölkerung) bis zum " + str(format(vaccination_date)) + " geimpft. An diesem Tag wurden " + str("{:,.0f}".format(vaccination_ger_diff)) + " Personen geimpft (" + vaccinations_diff_vorz + str("{:.2f}".format(vaccinations_diff)) + " % im Vergleich zum Vortag)"

# CATFACTS

def return_return_random_cat_facts():
	cat_facts_array = [
	'Viele Tierheime weigern sich um Halloween herum, ihre schwarzen Katzen wegzugeben - aus Angst vor Satanisten, die die Katzen opfern oder foltern.'
	,
	'In Belgien wurden Katzen 1879 kurz als "Postboten" benutzt - sie trugen in einem Radius von 30 Kilometern Briefe aus. Allerdings scheiterte der Versuch nach kurzer Zeit, denn die Katzen wollten einfach nicht gehorchen.'
	,
	'Die Siamkatze "F. D. C. Willard" ist bis heute die einzige Katze, die physikalische Arbeiten in Fachzeitschriften veröffentlichte. Der eigentliche Autor, Jack H. Hetherington, hatte immer in der "Wir"-Form geschrieben, und holte dafür seinen Kater als Ko-Autor hinzu und ließ ihn sogar die ersten Druckexemplare mit Pfotenabdrücken "signieren".'
	,
	'Guinness World Records verleiht offiziell keine Preise mehr an die "fetteste Katze der Welt" (bzw. an irgendein fettestes Tier der Welt), um absichtliche Überfütterung zu stoppen.'
	,
	'Freddie Mercury, der Sänger der Band Queen, widmete sein Solo-Album seiner Katze Jerry mit den Worten: "Für meine Katze Jerry, sowie für Tom, Oscar und Tiffany und alle Katzen-Liebhaber dieser Welt - alle anderen kann man vergessen."'
	,
	'Nachts gehört das Disneyland in Kalifornienden Katzen. Etwa 200 wilde Katzen leben in dem Themenpark und werden dort nicht nur toleriert, sondern wie Haustiere behandelt: Sie werden kastriert und geimpft. Nur gefüttert werden sie nicht, denn es ist ihre Funktion, den Park von Mäusen zu säubern.'
	,
	'Der Kater "Oscar", der in einem Altersheim in den USA lebt, gilt als "Hellseher" - wann immer er sich zum Schlafen neben einen der Heimbewohner lebt, stirbt dieser wenige Stunden darauf. So hat "Oscar" schon über 100 Tode vorhergesagt. Die Mitarbeiter rufen inzwischen schon die Angehörigen, sobald sie "Oscar" neben dem Patienten liegen sehen.'
	,
	'Erwachsene Katzen kommunizieren nicht durch Miauen miteinander. Sie miauen dann nur noch, um mit uns Menschen zu "sprechen".'
	,
	'"Creme Puff" und sein Bruder "Granpa" waren die beiden ältesten Katzen der Welt. "Creme Puff" starb mit 38, "Granpa" mit 34 Jahren. Sie lebten im selben Haushalt und wurden mit Speck, Eiern, Brokkoli, Spargel sowie Kaffee mit Sahne ernährt.'
	,
	'Die Katze "Emmy" war Schiffskatze auf der RMS Empress of Ireland und auf jeder Reise dabei. Eines Tages weigerte sie sich jedoch, an Bord zu gehen - und das Schiff sank am nächsten Tag. '
	,
	'"Merlin" ist die lauteste Katze der Welt - sein Schnurren hält den Weltrekord mit fast 70 Dezibel. Das ist so laut wie ein Staubsauger!'
	,
	'Katzen sind für gewöhnlich "rechtshändig", während Kater die linke Pfote bevorzugen.'
	,
	'Katzen dürfen nicht vegetarisch ernährt werden, da sie Taurin benötigen, das nur in Fleisch enthalten ist. Eine vegetarische Ernährung kann zu Blindheit und schließlich zum Tod führen.'
	,
	'65-85% aller Katzen, die zwei blaue Augen haben, sind taub.'
	,
	'Katzen können von Thunfisch abhängig werden und sich weigern, etwas anderes zu essen.'
	,
	'Der Herzschlag einer Katze ist doppelt so schnell wie der eines Menschen. 110 – 140 Mal schlägt das kleine Herz Ihres Abenteurers in der Minute.'
	,
	'Es stimmt! Katzen landen wirklich (fast) immer auf ihren Beinen. Der sogenannte Stellreflex sorgt dafür, dass eine Katze ihren Körper im freien Fall blitzschnell drehen kann. Diese lebensnotwendige Technik beherrschen Katzenkinder ab dem 39sten Lebenstag. Ausnahmen bestätigen allerdings auch hier die Regel: Ist die Fallhöhe zu niedrig, kann sich die Katze eventuell nicht vollständig drehen. Ist die Fallhöhe dagegen zu hoch, könnte sie sich trotz der Landung auf ihren Pfoten ernsthaft verletzen. '
	,
	'Im Alten Ägypten war es nicht erlaubt eine Katze zu töten. Die Tiere hielten die große Getreidespeicher des Landes frei von Nagetieren und sorgten so für das Überleben der ganzen Bevölkerung. Nahm man einer Katze das Leben, musste man um sein eigenes fürchten!'
	,
	'\"Gott schuf die Katze, damit der Mensch einen Tiger zum Streicheln hat.\" (Victor Hugo)'
	,
	'Katzen können nichts Süßes schmecken. Ihre Zungen haben dafür keine Geschmacksrezeptoren.'
	,
	'Katzen lieben mit ihren Augen! Wenn Sie Ihre Katze langsam anblinzelt, ist das ein Zeichen dafür, dass Sie ihr Freund sind.'
	,
	'Sir Isaac Newton ist nicht nur der Entdecker der Schwerkraft, er hat auch die Katzenklappe erfunden!'
	,
	'In Deutschland leben über 11 Millionen Katzen. Die Katze ist also mit Abstand das beliebteste Haustier der Deutschen.'
	,
	'Es gibt 70 verschiedene anerkannte Katzenrassen. Auf sogenannten Katzenausstellungen werden die schönsten ihrer Art prämiert.'
	,
	'1983 hat Frankreich die erste Katze ins All geschickt. Sie hieß Felicette und landete nach ihrem Abenteuer wieder putzmunter auf der Erde.'
	,
	'Katzen sind unglaublich gute Springer! Sie können das bis zu 5 fache ihrer Schwanzlänge springen.'
	,
	'Der Rücken einer Katze ist extrem flexibel. Er hat insgesamt 43 Rückenwirbel. Ein Mensch hat im Vergleich dazu nur 34.'
	,
	'Katzen haben kein Schlüsselbein! Ihre „lose“ sitzenden Schultern machen ihr Skelett besonders wendig und flexibel. So gilt die Katzen-Faustregel: Passt der Kopf durch, ist der Körper kein Problem!'
	,
	'Erwachsene Katzen haben eine Normaltemperatur von 38,3 bis 39 °C. Da sie am Körper keine Schweißdrüsen haben, schwitzen sie ausschließlich über ihre Pfoten.'
	,
	'Weibliche Katzen sind meistens Rechtshänder, ihre männlichen Kollegen dagegen meistens Linkshänder.'
	,
	'Das Gehirn einer Katze ist einem Menschengehirn ähnlicher als einem Hundegehirn. Menschen und Katzen haben die identischen Regionen für Emotionen.'
	,
	'Wildkatzen sind Einzelgänger. Sie beanspruchen ihr Gebiet für sich allein und verteidigen ihr Revier erbittert.'
	,
	'Katzen sind überaus reinliche Tiere. Da sie ihr Fell gerne mit ihrer rauen Zunge putzen und dabei viele Haare schlucken, müssen sie von Zeit zu Zeit einen Haarballen herauswürgen. Der Fachbegriff für diesen Haarballen ist \"Bezoar\".'
	,
	'Das Gehör einer Katze ist besser als das eines Hundes. Sie können zwei Oktaven höher hören als Menschen.'
	,
	'Katzen verschlafen im Durchschnitt 70% ihres Lebens. Anders gesagt: Katzen verschlafen zwei Drittel ihres Lebens! Na dann, gute Nacht.'
	]
	return random.choice(cat_facts_array)


def return_command_array():
	
    # GREETINGS

    greeting = 'Guten Morgen!'
    if datetime.datetime.now().hour > 11 and datetime.datetime.now().hour < 14:
        greeting = 'Mahlzeit!'
    if datetime.datetime.now().hour > 13 and datetime.datetime.now().hour < 18:
        greeting = 'Schönen Nachmittag!'	
    if datetime.datetime.now().hour > 17 and datetime.datetime.now().hour < 20:
        greeting = 'Guten Abend!'
#    if datetime.datetime.now().hour > 20 and datetime.datetime.now().hour < 22:
#        greeting = 'Es unser Veedel, Denn he hält m`r zosamme, Ejal wat och passeet, En uns`rem Veedel.'	
    if datetime.datetime.now().hour > 19 and datetime.datetime.now().hour < 25:
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

    # Radioparadise
    rp_json_url = \
        urlopen('https://api.radioparadise.com/api/now_playing?chan=0'
                )
    json_rp = json.loads(rp_json_url.read())
       
    # NEWS

    json_news_url = \
        urlopen('https://newsapi.org/v2/top-headlines?sources=spiegel-online&apiKey=2d9859f0514247a596b6eb020e0a81fe'
                )
    json_news = json.loads(json_news_url.read())
    if json_news[u'status'] == "error":
	newsticker = ""
    else:
    	newsticker = \
        	'Spiegel News (via newsapi.org): '
    	news_array = []
	
    	for news_i in range(0, 10):
        	if not json_news[u'articles'][news_i][u'title'] == None:
            		news_array.append(json_news[u'articles'
                    	][news_i][u'title'] + '. ' + json_news[u'articles'
                    	][news_i][u'description'])

    	newsticker = newsticker + random.choice(news_array).encode('utf-8')

    # Recipe
    rezept_url = \
        urlopen('https://www.rezepteplan.de/SpeisePlan/Zuf%C3%A4lligerSpeisePlan.aspx?34=1')
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
#        'Heute ist der ' + str(diff_days_kontaktverbot)
#            + '. Tag der Kontakteinschränkungen in NRW und bundesweit.'
#            ,
        'Gerade läuft: ' + str(json_rp[u'title'].encode('utf-8')) 
	    + ' von ' +  str(json_rp[u'artist'].encode('utf-8')) 
	    + ' aus dem Album ' +  str(json_rp[u'album'].encode('utf-8')) 
	    + ' (' +  str(json_rp[u'year'].encode('utf-8')) + ')' 
	    ,	    
        'Das Wetter: ' + str(json_weather[u'weather'][0][u'description'
                             ].encode('utf-8'))
            + '. Aktuelle Temperatur: ' + str("{:.1f}".format(json_weather[u'main'
                ][u'temp'])).replace('-', u'\u2212').encode('utf-8')
            + '\xc2\xb0C. Gef\xc3\xbchlte Temperatur: '
            + str("{:.1f}".format(json_weather[u'main'][u'feels_like'])).replace('-',
                u'\u2212').encode('utf-8') + '\xc2\xb0C.'
	    ,
	    crypto_ticker
            ,
	    vaccinations
	    ,
	    newsticker,
	'Zufälliger Katzenfakt: ' + return_return_random_cat_facts(),
        'Zufälliges Rezept: '
            + rezept_name
            + ' auf: https://www.rezepteplan.de/Rezepte/.rezept?0='
             + rezept_id + '. Guten Appetit!'
            ,        ]

  #  random.shuffle(command_array)

    return command_array
