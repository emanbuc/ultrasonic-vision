### Test stima posizione del bersaglio con telaio supporto pannello superiore montato

Dopo aver montato il pannello superiore è stato eseguito un test del funzionamento del sistema a vuoto e con oggetti presenti nella zona di rilevazione. Nel caso non siano presenti oggetti che producono echi sonar ben definiti entro 2-3 metri di distanza i sensori HC-SR-04 producono dei risultati instabili tipici del funzionamento fuori scala.

Per evitare questo problema l'area di rilevamento è stata delimitata montando una barriera sul lato opposto a quello dei sensori. In un primo momento la barriera di delimitazione risultava essere inclinata di circa 45° rispetto al piano frontale dei sensori. In queste condizioni la distanza stimata dai sensori non era corretta. (vedi acquisizione dati "WALL")

Il pannello originale è stato poi sostituito da due pannelli separati, paralleli ai sensori (vedi acquisizione dat "WALL_45_DEGREE"). In questa configurazione tutti i sensori riescono a stimare la distanza con un errore massimo di qualche centimetro (accuratezza 5-10%) che è ragionevole ai fine dell'esperimento corrente.

I test effettuati hanno evidenziato che:

-  i sensori sono sensibili rispetto alle condizioni dell'ambiente circostante e in alcuni casi hanno restituito delle letture anomale
- La forma ed il materiale degli oggetti ha un effetto importante nell'accuratezza della stima della distanza. 
  - Per la riflessione delle onde sonore vale la legge si Snell quindi se l'onda sonora colpisce una superficie non parallela al piano frontale del sensore è possibile che l'onda riflessa non raggiunga direttamente il ricevitore (distanza stimata superiode a quella reale, o non lo raggiunga affatto)
  - L'impednza acustica dell'interfaccia tra l'aria (gas) ed un corpo solido bersaglio è solitamente molto elevata e questo in generale genera una buona riflessione. In presenza di superfici  fonoassorbenti l'energi ariflessa può essere molto minore e a volte l'eco putrebbe non essere rilevato dal ricevitore
  - 

Sistemi di acquisizione con molti sensori e legge di Murphy

	- con solo 7 sensori la legge di Murphy non vale: solo sporadicamente si sono verificati errori docuti al collegamento dei sensori .

Diversi problemi invece docuti alle breadboard di pessima qualità ... con tutti questi collegamenti meglio andare usare una millefori per ottenere un sistema ben più affidabile usando alla fine solo poco tempo in più nell'assemblaggio.



## 2021-01-02

### Configurazione a sette sensori

L'hardware utilizzato consente di utilizzare fino a 12 sensori. Al momento in laboratorio sono disponibili 5 sensori HCSR04+ e 5 sensori HCSR04 . Per l'addestramento del classificatore è stata utilizzata una configurazione con sette sensori in modo da lasciare alcuni sensori disponibili per testare l'utilizzo di moduli remoti con microcontrollore ESP8266, mantenendo invariata la configurazione dei sistema principale.