# Test del prototipo nella configurazione a sette sensori

Dopo aver i tre pannelli con i sensori è stato eseguito un test del funzionamento del sistema a vuoto e con oggetti presenti nella zona di rilevazione.

Nel caso di funzionamento a vuoto, senza oggetti presenti si sono state osservati diversi episodi di funzionamento instabile dei moduli HC-SR04 riconducibili alla ricezione di echi da parte di superfi riflettenti dell'ambiente circostante.

Per evitare questo problema l'area di rilevamento è stata delimitata montando una barriera sul lato opposto a quello dei sensori. 

In un primo momento la barriera di delimitazione risultava essere inclinata di circa 45° rispetto al piano frontale dei sensori. In queste condizioni la distanza stimata dai sensori non era corretta. (vedi acquisizione dati "WALL")

Il pannello originale è stato poi sostituito da due pannelli separati, paralleli ai sensori (vedi acquisizione dat "WALL_45_DEGREE"). In questa configurazione tutti i sensori riescono a stimare la distanza con un errore massimo di qualche centimetro (accuratezza 5-10%) che è ragionevole ai fine dell'esperimento corrente.

## Numero di sensori utilizzati

L'hardware utilizzato consente di utilizzare fino a 12 sensori. Al momento in laboratorio sono disponibili 5 sensori HC-SR04+ e 5 sensori HC-SR04 . Per l'addestramento del classificatore è stata utilizzata una configurazione con sette sensori in modo da lasciare alcuni sensori disponibili per testare l'utilizzo di moduli remoti con microcontrollore ESP8266, mantenendo invariata la configurazione dei sistema principale.

## Risultati del test
I test effettuati hanno evidenziato che:

-  LA stima della distanza restituita dai moduli HC-SR04 è influenzata da fari fattori ambientali (variazioni di temperatura, correnti d'aria, sorgenti di rumore o vibrazione significative ...)
- La forma ed il materiale degli oggetti ha un effetto importante nell'accuratezza della stima della distanza. 
  - Per la riflessione delle onde sonore vale la legge si Snell quindi se l'onda sonora colpisce una superficie non parallela al piano frontale del sensore è possibile che l'onda riflessa non raggiunga direttamente il ricevitore (distanza stimata superiode a quella reale, o non lo raggiunga affatto)
  - L'impednza acustica dell'interfaccia tra l'aria (gas) ed un corpo solido bersaglio è solitamente molto elevata e questo in generale genera una buona riflessione. In presenza di superfici  fonoassorbenti e l'energi ariflessa può essere molto minore e a volte l'eco putrebbe non essere rilevato dal ricevitore
  - Nel caso di superci irregolari l'onda riflessa può essere molto attenuta a causa fi fenomeni di diffrazione

