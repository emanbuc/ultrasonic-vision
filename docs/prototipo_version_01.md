## Il prototipo realizzato (versione 1.0)

### Scopo

Testare possibilità di stimare la posizione di un oggetto e riconoscere il tipo di oggetto utilizzando un numero limitato di sensori

### Requisiti 

1. il sistema deve riuscire a stimare la posizione di un oggetto all'interno di un area delimitata
2. il sistema deve riconoscere il tipo di oggetto presente (classificazione muticlasse)
3. utilizzare HW standard, a basso costo e facilmente reperibile. Possibilmente solo moduli già pronti, senza schede custom.
4. il sistema deve essere documentato e riproducibile. Ad esempio per esercitazioni di laboratorio.  

### Hardware

Prototipo realizzato con Raspberry PI 3 e sensori HC-SR04. Software completamente open source. Costo complessivo  hardaware  inferiore a 50€. Tutti i componenti facilmente reperibili dai rivenditori di elettronica oppure su Amazon eBay e simili.

Nota: Ogni sensore richiede GND, VCC + 2 GPIO (trigger + echo). Su Raspberry 2 ci sono 24 GPIO pin disponibili => questo sistema può supportare  fino a 12 sensori.

Software scritto in Python facile da scrivere, mantenere e debuggare direttamente sul Raspberry senza bisogno di altri ambienti di sviluppo. Include sistema di "simulazione" dei sensori delle libreria GPIO che non è presente nel normali PC in modo da permettere l'esecuzione ed il debug anche senza avere accesso all'hardware. 

### Misuratori ad ultrasuoni

[TBC]

Sensore standard tipo con interfaccia 4 pin tipo HC-SR04/SR04+ sono più o meno  tutti simili: risoluzione ad 1CM e raggio utile tra 3-4 metri. 

### Software

Il software è volutamente scritto in "stile firmware", in modo da essere facilmente portabile verso il linguaggio C utilizzato per lo sviluppo di firmware per maggior parte dei microcontrollori sul mercato.

Software scritto in stile "firmware" da micro Librerie standard tutte disponibili. 

[TBC]