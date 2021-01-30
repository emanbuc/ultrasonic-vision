# Risultati ottenuti

L'analisi dei dati dimostra che il vettore dei tempi di volo (_TOF_) stimanti dai sensori dipende dalla posizione del bersaglio all'interno dell'area di rilevamento e dalle caratteristiche fisiche (geometria, materiale e tipo di superfice) dell'oggetto. Il sistema è quindi potenzialmente in grado di stimare la posizione dell'oggetto all'interno dell'area di rilevamento e di dicriminare tra diversi tipi di oggetti.

I test eseguiti con ilprototipo del sistema hanno però evidenziato anche alcune importanti criticità:

- Il pattern delle distanze stimate dipende in maniera non facilmente separabile sia dal tipo di oggetto presente nell'area di rilevamento che dalla posizione dell'oggetto rispetto ai sensori. Il problema può essere mitigato scgliendo una opportuna configurazione geometrica (numero e posizione dei sensori).

- L'impossibilità di separare gli effetti della posizione dell'bersaglio da quelli della geometria e delle caratteristiche fisiche dell'oggetto rendono particolarmente complesso il compito di sviluppare un sistema di classificazione degli oggetti indipendente dalla posizione. 
  
I modelli di classificazione addestrati e testati si sono invece rivelati molto precisi se gli oggetti da identificare vengono posizionati in maniera precisa, riucreando una condizione molto vicina a quella in cui sono stati prodotti i dati di addestramento.

- I classificatori addestrati nell'ambito di queso progetto hanno performance molto elevate se gli oggetti vengono posizionati esattamente come durante la fase di training, ma non riescono ad riconoscere l'oggetto in maniera indipendente dalla posizione. Questo problema è affrontato nel progetto [Ultrasonic Object Recognition](https://github.com/emanbuc/ultrasonic-object-recognition) che ha come obiettivo la realizzazione di un sistema di riconoscimento degli oggetti basato sui misuratori ad ultrasuoni utilizzando tecniche di machine learning e deep learning più avanzare avanzate.

- La relazione tra la distanza stimata e quella reale non è sempre lineare. Nel caso di posizionemento dell'oggetto non ideale la misura è affetta da errori annche molto ampi e difficimente compensabili perchè dipendenti dalle carateristiche fisiche e geometriche del bersaglio.
  - La forma ed il materiale degli oggetti ha un effetto importante nell'accuratezza della stima della distanza.
  - Per la riflessione delle onde sonore vale la legge si Snell quindi se l'onda sonora colpisce una superficie non parallela al piano frontale del sensore è possibile che l'onda riflessa non raggiunga direttamente il ricevitore (distanza stimata superiode a quella reale, o non lo raggiunga affatto)
  - L'impedenza acustica dell'interfaccia tra l'aria (gas) ed un corpo solido bersaglio è solitamente molto elevata e questo in generale genera una buona riflessione. In presenza di superfici  fonoassorbenti e l'energi ariflessa può essere molto minore e a volte l'eco putrebbe non essere rilevato dal ricevitore
  - Nel caso di superfici irregolari l'onda riflessa può essere molto attenuta a causa fi fenomeni di diffrazione)