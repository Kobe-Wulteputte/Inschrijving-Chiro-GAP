# InschrijvingsScriptGAP
Een script om snel code te genereren die gebruikt kan worden om gegevens uit excel in te voeren in het 'nieuwe leden' formulier van de GAP

## Data klaarzetten
Vul het 'Vul_in.xslx bestand in met gegevens van de nieuwe leden. Let hierbij zeker op de juiste gegevens op de juiste plaats staan.
Laat de oorspronkelijke eerste rij staan, en vul de gegevens eronder in.

Vul bij de afdeling kolom de naam van de afdeling in, en niets anders. De mogelijke waarden zijn dus: (Sjamfoeter, Speelclub, Rakker, Topper, Kerel, Aspirant)
De telefoonnummer kolom wordt automatisch opgekuist.

## Resultaat in de browser plakken
Met de uitvoer van het 'OUT.txt' bestand kan het formulier voor nieuwe leden toe te voegen sneller ingevuld worden.

Navigeer eerst naar de pagina voor het toevoegen van nieuwe leden. Open nu de console ( druk F12 op chrome en kies in menubalk voor Console ).
Nu zou het mogelijk moeten zijn om tekst in de console te schrijven.

Kopieer per persoon die toegevoegd moet worden een blokje tekst uit het out.txt bestand, en plak het in de console. De blokjes worden gescheiden met enkele witlijnen. 
Nu zouden alle gegevens ingevuld moeten worden van 1 persoon, en wordt deze automatisch doorgevoerd. 

Als alle gegevens correct waren ingegeven in de excel zal er niets mislopen en kan onmiddellijk de volgende persoon toegevoegd worden.
ALs er gegevens niet kloppen, of als de persoon reeds bestaat in de GAP zal er een foutmelding komen. Deze moeten manueel afgehandeld worden.

Zo, als alle blokken uit het out bestand gekopieerd zijn staan de gegevens in de GAP.
