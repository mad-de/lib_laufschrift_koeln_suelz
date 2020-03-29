#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import datetime
def return_command_array():
    now = datetime.datetime.now()
    timestamp_kontaktverbot = 1584831600
    beginn_kontaktverbot = datetime.datetime.fromtimestamp(timestamp_kontaktverbot)

    diff_days_kontaktverbot = abs((now - beginn_kontaktverbot).days)
    now = datetime.datetime.now()


    # Ab hier die einzelnen Zeilen ändern. Ticker aktualisiert nach jedem Merge automatisch.
    command_array = [
    'Heute ist der ' + str(now.day) + '.' + str(now.month) + '.' + str(now.year) + ' Es ist ' + str(now.hour) + ' Uhr ' + str(now.minute),
    'Heute ist der ' + str(diff_days_kontaktverbot) + '. Tag des Kontaktverbots in NRW und bundesweit.',     
    'Bleibt zuhause und bleibt gesund!',
    'Wir sitzen alle im selben Boot (zuhause) und aus Langeweile haben wir eine LED Laufschrift gebastelt :).', 
    'Unterstützt eure lokalen Geschäfte in dieser Zeit. Ihr wollt etwas lesen oder braucht eine DVD? Bestellt doch zum Beispiel über der-andere-buchladen-koeln@t-online.de.',
    'Viele Restaurants hier im Viertel bieten einen Lieferdienst oder Abholservice z.B. www.merstonnzesamme.de',
    'Gute Musik ohne Werbung oder Corona-Nachrichten: www.radioparadise.com',
    'Langweilig und Lust auf einen guten Film? Die 10 besten Filme des 21. Jahrhunderts (lt. BBC): 10) No Country for Old Men von Joel Coen and Ethan Coen 9) A Separation von Asghar Farhadi 8) Yi Yi von Edward Yang 7) The Tree of Life von Terrence Malick 6) Eternal Sunshine of the Spotless Mind von Michel Gondry 5) Boyhood von Richard Linklater 4) Spirited Away von Hayao Miyazaki 3) There Will Be Blood von Paul Thomas Anderson 2) In the Mood for Love von Wong Kar-wai 1) Mulholland Drive von David Lynch ... Viel Spass beim Anschauen!',
    'Danke an Alle, die den Laden hier am Laufen halten!', 
    'Eure Nachricht hier anzeigen lassen? https://github.com/mad-de/lib_laufschrift_koeln_suelz/ Oder wollt ihr uns etwas mitteilen? Whatsapp: +44 7537 181802']
    return command_array
