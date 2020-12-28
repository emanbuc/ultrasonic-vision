# Ultrasonic-Vision
Sistema di acquisizione dati in grado di stimare la posizione di un oggetto all'interno di un area delimitata e riconoscere il tipo di oggetto presente utilizzando impulsi ad ultrasuoni ed un sistema di classificazione basato su machine learning.

## Scopo del progetto 

Realizzare un sistema di misura in grado di stimare la posizione di un oggetto  all'interno di un area delimitata e riconoscere il tipo di oggetto presente utilizzando impulsi ad ultrasuoni ed un sistema di classificazione basato su _machine learning_. 

L'obiettivo del progetto è quello di progettare e realizzare un primo prototipo funzionante del sistema con lo scopo di valutare la fattibilità del progetto ed individuare le eventuali criticità che dovranno essere affrontate nelle realizzazione delle successive versioni del sistema.

### Attività previste

- [ ] Progettare e realizzare un prototipo del sistema di acquisizione dati (hardware e software)
- [ ] Progettare e realizzare un prototipo sistema di classificazione (modello addestrato e  webservice consumabile con endpoint pubblico)
- [ ] Relazione sul lavoro svolto e risultati ottenuti
- [ ] Documentazione utile per proseguire lo sviluppo del sistema 

### Architettura

Architettura Industrial IoT standard a tre livelli field, edge/fog, cloud (oppure on-premeses).

[diagramma]

[Edge vs Fog computing]

## Funzionamento del sistema

La componete di campo utilizza dei misuratori di distanza ad ultrasuoni. Ogni misuratore è indipendente ed è composto da un emettitore di impulsi ad ultrasuoni e da un ricevitore. La distanza del bersaglio viene stimanta misurando il tempo (_Time Of Flight - TOF_) trascorso tra l'emissione dell'impulso e la ricezione del primo eco riflesso dal beraglio.

I misuratori sono sono fissi ed in posizioni note. L'insieme delle sistanze stimate rispetto ai diversi misuratori, conbinato con le informazioni sulla configurazione geometrica del sistema,  viene utilizzato per stimare la posizione del bersaglio ed riconoscere  il tipo di oggetto. L'aggregazione e la prima elaborazione dei dati provenienti dai sensori viene eseguita localmente a livello di _edge_ (_edge computing_). A questo livello viene elaborata la stima della posizione e può essere eseguita anche la classificazione del oggetto. I dati acquisiti vengono poi inviati alla componente _cloud_ per elaborazioni di secondo livello, miglioramento del modello di classificazione e memorizzazione a lungo termine (_cloud computing_).

Il riconoscimento dell'oggetto viene eseguito utilizzando un classificatore muticlasse addestrato con dati ottenuti da misurazioni precedentemente eseguite con il sistema nella stessa configurazione (numero e posizione dei sensori) su oggetti noti a priori. Il classificatore può essere eseguito localmente sul disposivo di campo che gestisce i sensori, come web server su rete locale oppure come web server remoto.

In generale la configurazione geometrica del sistema ed il numero di sensori devono essere scelta in base ai requisiti di simmetria e risoluzione che si vogliono soddisfare. Nel caso del prototipo realizzato per questo progetto non erano stati posti  particolari vincoli e quindi sono stati utilizzati i sensori che erano disponibili in laboratorio, sperimentando diverse configurazioni geometriche. 

### Limitazioni note

**Il numero dei sensori utilizzabili** (e quindi la risoluzione spaziale del sistema) è limitato dal numero di linee di input/output digitale (_GPIO_)  del microcontrollore utilizzato e dal tempo disponibile per effettuare la misura (i misuratori vengono accesi singolarmente in sequenza). Solitamente i sensori ad ultrasuoni richiedono 2 linee (anche se alcuni modelli ne richiedono solo una). Nel caso del prototipo sonostati utilizzati dei sensori HC-SR04 che richiedono 2 GPIO e un Raspberry PI 3 mette nativamente a disposizone 24 GPIO quindi il prototipo, senza circuiteria aggiuntiva per multiplexing, può gestire fino a 12 sensori.

**Il raggio d'azione** del sistema dipende dalla configurazione geometrica del sistema e dalle caratteristiche dei misuratori utilizzati. Molti misuratori commerciali a bassa costo hanno una portata operativa di 2-3 metri anche se ne esistono alcuni con portata fino 7 metri.  Ad esempio disponendo i misuratori ai vertici e lungo i lati di un quadrato di potrebbe agevolmente coprire un area di almeno 2 mq anche con misuratori di fascia economica. Un altra possibilità è quella di disporre i misuratori lungo un circonferenza di diametro minore o uguale alla portata massima dei dispositivi.









## Il prototipo realizzato (versione 1.0)

### Scopo

Testare possibilità di stimare la posizione di un oggetto e riconoscere il tipo di oggetto utilizzando un numero limtato di sensori

### Requisiti 

1. il sistema deve riuscire a stimare la posizione di un oggetto all'interno di un area delimitata
2. il sistema deve riconoscere il tipo di oggetto presente (classificazione muticlasse)
3.  utilizzare HW standard, a basso costo e facilmente reperibile. Possibilmente solo moduli già pronti, senza schede custom.
4. il sistema deve essere documentato e riproducibile. Ad esempio per esercitazioni di laboratorio.  

 ### Roadmap versione 1.0

- [x] progetto di massima HW
- [x] progetto di massima SW
- [x] progetto sistema ML
- [x] prototipo HW/SW
- [x] test acquisizione dati
- [ ] definire configurazione geometrica riproducibile del sistema
- [ ] creare dataset per addestramento modello
- [ ] sviluppare un classificatore dimostrativo con un modello semplice
- [ ] deploy del modello su raspberry 
- [ ] deploy del modello come web service
- [ ] valutazione performance del modello
- [ ] ottimizzare modello 

### Hardware

Prototipo realizzato con Raspberry PI 3 e sensori HC-SR04. Software completamente open source. Costo complessivo  hardaware  inferiore a 50€. Tutti i componenti facimente reperibili dai rivenditori di elettronica oppure su Amazon eBay e simili.

Nota: Ogni sensore richiede GND, VCC + 2 GPIO (Trigger + Echo). Su raspberry 2 ci sono 24 GPIO pin disponibili => questo sistema può supportare  fino a 12 sensori.

Software scritto in python facile da scrivere, matenere e debuggare direttamente sul Raspberry senza bisogno di altri ambienti di sviluppo. Include sistema di "simulazione" dei sensori delle libreria GPIO che non è presente nel normali PC in modo da permettere l'esecuzione ed il debug anche senza avere accesso all'hardware. 

### Misuratori ad ultrasuoni

[TBC]

Sensore standard tipo con interfaccia 4 pin tipo HC-SR04/SR04+ sono più o meno  tutti simili: risoluzione ad 1CM e raggio utile tra 3-4 metri. 

### Software

Il software è volutamente scritto in "stile firmware", in modo da essere facilmente portabile verso il linguaggio C utilizzato per lo sviluppo di firmware per maggior parte dei microcontrollori sul mercato.

Software scritto in stile "firmware" da micro Librerie standard tutte disponibili. 

[TBC]

 ### Classificatore e Machine Learning

Il modello del classificatore può essere deployato come container oppure  come modello standard pre addestrato. Per l'addestramento può esere  usato modello sviluppato ad hoc oppure AutoML per task di  classificazione usando come feaure stime delle distanze. 

In questo caso è facile anche impostare un pipeline e si possono usare  tecniche ML Ops per gestire l'addestramento del modello quando sono  disponibili nuovi dati. 

La piattaforma di sviluppo standard su raspberry supporta diverse librerie per machine learning (ecosistema python). 

Volendo si può fare i deploy anche di modelli pre-addstrati che utilizzano reti neurali avanzate 

(es. Framework Tensorflow - vedi ad esempio https://blog.paperspace.com/tensorflow-lite-raspberry-pi/) 

### Industrializzazione 

Esistono versioni industriale dei Raspberry a partire da 130-150€ 

-  es. https://andino.shop/en 
-  Oppure piattaforme più evolute con la gestione dei container docker come quella della Hilsher (https://www.hilscher.com/products/product-groups/industrial-internet-industry-40/netiotnetfield-edge/?) 

==> questo sistema può essere trasformato in un prodotto reale utilizzabile in ambiente industriale e portato realmente sul campo con pochissimo  lavoro (qualche giorno) senza modificare il software.

## Futuri Sviluppi 

### Connettività ed invio dati verso storage esterno

Aggiungere sistema per invio dei dati acquisiti verso uno storage esterno. Es. IoT Hub. attraverso protocollo MQTT e rete ethernet/wifi.

### Trigger automatico 

Aggiungere un sistema di trigger per avviare in maniera automatica la misura (es. fotocellula, sensore di prossimità IR, PIR, ...)

### Caratterizzazione dei sensori ad ultrasuoni utilizzati 

Ricavare (dove non disponibile) una caratterizzazione affidabile dei sensori utilizzati.

### Rappresentazione grafica 3D dell'oggetto

Restituire una rappresentazione grafica 3D dell'oggetto a partire dagli echi sonar acquisiti (stima delle distanze )

### Ridurre il tempo necessario ad eseguire una misura

Dterminare, in base a caratteristiche dell'hardware e alla configurazione geometrica, l'intervallo di tempo minimo tra due impulsi sonar per evitare interverenze misuratori diversi

### Modello avanzato per riconoscimento oggetti

Sviluppare ed addestrare un modello avanzato per il riconoscimento degli oggetti in un [progetto di ricerca dedicato](https://github.com/emanbuc/ultrasonic-object-recognition).

### Pipeline di miglioramento continuo del classificatore

Progettare, sviluppare e pubblicare pipeline per addestramento e miglioramento continuo del modello ogni volta che sono disponibili nuovi dati per l'addestramento

### Calibrazione del sistema

La velocità propagazione delle onde sonore dipende dal mezzo. In aria il parametro fondamentale è la  temperatura che nel caso di applicazioni reali può variare anche in modo significativo. Due possibilità per migliorare l'accuratezza del  sistema: 

1. Misurare la temperatura e applicare compensazione della temperatura nel calcolo della distanza dalla temperatura 
2. Calibrare il sistema (eventualmente anche sensore per sensore) eseguendo delle  misure ripetute su bersagli a distanza nota. --> vedi libreria https://github.com/emanbuc/Bluetin_Python_Echo 

Nota: nei Raspberry è presente un sensore di temperatura a bordo della scheda che può essere usato per la calibrazione 

### Versione 2.0: rete di sensori distribuiti realizzata con moduli WiFi ESP82266 che scambiano dati tramite MQTT 

1 raspberry utilizzato come broker MQTT e eventualmente anche come gateway/access point wifi 

N noti ESP8266 gestiscono i sensori ed inviano i dati tramite MQTT e rete Wifi 

Nota: i moduli ESP8266 espongono fino a 16 GPIO utilizzabili => ogni  modulo può supportare fino a 8 sensori HC-SR04 + sensore di temperatura  su ingresso analogico ADC interno per calibrazione. 

In questo modo si può aumentare praticamente all'infinito la risoluzione del sistema in termini di numero di sensori. 

 E si possono estendere le dimensione dell'area di rilevamento fino ai  limiti della copertura delle rete WiFi (In teoria usando dei ripetitori  ed una suddivisione a zone si potrebbe si può coprire anche un intero  palazzo o un area molto grande). 



# Risorse Utili

 

## Utrasonic Range Sensors 

https://www.seeedstudio.com/blog/2019/11/04/hc-sr04-features-arduino-raspberrypi-guide/ 

https://www.instructables.com/HC-SR04-Ultrasonic-Sensor-With-Raspberry-Pi-2/ 

https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi 

http://codelectron.com/measure-distance-ultrasonic-sensor-pi-hc-sr04/ 

https://www.bluetin.io/sensors/python-library-ultrasonic-hc-sr04/ 

 

https://emanuelebuchicchio.wordpress.com/2016/07/18/misurare-la-distanza-di-un-oggetto/ 

https://emanuelebuchicchio.wordpress.com/2016/08/04/sensore-ad-ultrasuoni-hc-sr04-un-sonar-integrato-compatibile-con-esp8266-arduino-e-raspberry-per-3e/ 

 

## ESP8266 

https://arduino-esp8266.readthedocs.io/en/latest/index.html 

http://espcopter.com/ 

https://github.com/esp8266/Arduino 

 

## MQTT 

https://www.instructables.com/How-to-Use-MQTT-With-the-Raspberry-Pi-and-ESP8266/ 

https://everythingesp.com/arduino-tutorial-protocol-buffers-messages-with-strings/ 

 

## ML 

https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/teach-your-raspberry-pi-multi-gesture/single-page 

 