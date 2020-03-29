#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import datetime
import random

def return_command_array():
    now = datetime.datetime.now()
    timestamp_kontaktverbot = 1584831600
    beginn_kontaktverbot = datetime.datetime.fromtimestamp(timestamp_kontaktverbot)

    diff_days_kontaktverbot = abs((now - beginn_kontaktverbot).days)
    now = datetime.datetime.now()


    # Ab hier die einzelnen Zeilen ändern / oder oben unter "command_array = [" eine neue hinzufügen. Ticker aktualisiert nach jedem Merge automatisch.
    # Beispiel:
    # 'Meine Nachricht',
    
    command_array = [
    'Heute ist der ' + str(now.day) + '.' + str(now.month) + '.' + str(now.year) + ' Es ist ' + str(now.hour) + ' Uhr ' + str(now.minute),
    'Heute ist der ' + str(diff_days_kontaktverbot) + '. Tag des Kontaktverbots in NRW und bundesweit.',     
    'Bleibt zuhause und bleibt gesund!',
    'Wir sitzen alle im selben Boot (zuhause) und aus Langeweile haben wir eine LED Laufschrift gebastelt :).', 
    'Unterstützt eure lokalen Geschäfte in dieser Zeit. Ihr wollt etwas lesen oder braucht eine DVD? Bestellt doch zum Beispiel über der-andere-buchladen-koeln@t-online.de.',
    'Viele Restaurants hier im Viertel bieten einen Lieferdienst oder Abholservice z.B. www.merstonnzesamme.de',
    'Auf der Suche nach guter Musik ohne Werbung oder Corona-Nachrichten: www.radioparadise.com',
    'Langweilig und Lust auf einen guten Film? Die 10 besten Filme des 21. Jahrhunderts (lt. BBC): 10) No Country for Old Men von Joel Coen and Ethan Coen 9) A Separation von Asghar Farhadi 8) Yi Yi von Edward Yang 7) The Tree of Life von Terrence Malick 6) Eternal Sunshine of the Spotless Mind von Michel Gondry 5) Boyhood von Richard Linklater 4) Spirited Away von Hayao Miyazaki 3) There Will Be Blood von Paul Thomas Anderson 2) In the Mood for Love von Wong Kar-wai 1) Mulholland Drive von David Lynch ... Viel Spass beim Anschauen!',
    'Wie wäre es mit einer neuen Serie? Die 10 besten Serien aller Zeiten (lt. Cinemablend): 10) The Simpsons 9) Mad Men 8) I love Lucy 7) Saturday Night Live 6) The Sopranos 5) Seinfeld 4) Game of Thrones 3) The X-Files 2) Breaking bad 1) Friends ... Viel Spass beim Suchten!',
    'Danke an Alle, die den Laden hier am Laufen halten!', 
    'Tolle von uns getestete, kostenlose Spiele für einen Remote-Spieleabend mit (ebenfalls isolierten) Freunden: Trickster (App), Drawful 2 (Steam). Viel Spass beim Ausprobieren!',
    'Ihr braucht aktuell jemanden, der für euch einkauft? Ihr wollt Hilfe anbieten? Freiwillige Helfer findet man unter anderem auf https://nebenan.de/corona oder www.die-einkaufshelden.de Oder ihr schreibt uns per Whatsapp: +44 7537 1818 02 Wir helfen auch gerne!',
    'Eure Nachricht hier anzeigen lassen? https://github.com/mad-de/lib_laufschrift_koeln_suelz/ Oder wollt ihr uns etwas mitteilen? Whatsapp: +44 7537 181802']
    random.shuffle(command_array)
    return command_array
