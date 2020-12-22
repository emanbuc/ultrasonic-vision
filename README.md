# ultrasonic-vision
Sistema di acquisizione dati in grado di stimare la posizione di un oggetto all'interno di un area delimitata e riconoscere il tipo di oggetto presente utilizzando impulsi ad ultrasuoni ed un sistema di classificazione basato su machine learning

Cose da Realizzare: 

- Report 
- Prototipo (HW+SW) 
- Documentazione utile per proseguire lo sviluppo del sistema 

 

# Descrizione del progetto 

 Realizzare un sistema di misura in grado di stimare la posizione di un oggetto  all'interno di un area delimitata e riconoscere il tipo di oggetto  presente utilizzando impulsi ad ultrasuoni ed un sistema di  classificazione basato su Machine Learning. 

 

## Idea di base 

 Disporre misuratori di distanza sonar intorno ad un area limitata (compatibile  con raggio di azione dei misuratori). Ad esempio un area circolare di  raggio fino a 1.5m oppure un piano di lavoro quadrato o rettangolare con lato 2-3 metri. 

 Gestire i misuratori in modo da inviare un impulso e ricevere eco misturando  tempo di volo del primo eco. Calcolare Intervallo di tempo necessario  tra gli impulsi in modo da evitare sovrapposizione tra i diversi  impulsi. 

 

Raccogliere dati sullo sciame di echi misurati e determinare: 

- Posizione dell'oggetto rispetto ai diversi emettitori 
- Riconoscere l'oggetto utilizzando un modello di classificazione con tecniche di machine learning 

 

Il modello del classificatore può essere deployato come container oppure  come modello standard pre addestrato. Per l'addestramento può esere  usato modello sviluppato ad hoc oppure AutoML per task di  classificazione usando come feaure stime delle distanze. 

In questo caso è facile anche impostare un pipeline e si possono usare  tecniche ML Ops per gestire l'addestramento del modello quando sono  disponibili nuovi dati. 



## Roadmap

- [ ] Realizzare prototipo versione 1
- [ ] Relazione
- [ ] Pubblicare documentazione
- [ ] Progettare versione 2

## Versione 1: sensori HC-SR04 collegati direttamente a Raspberry 

Scopo: 

1. Testare possibilità di riconoscere oggetti sciame di echi provenienti dai diversi sensori 
2. Focus sul software e sull'riconoscimento degli oggetti tramite ML. Utilizzare HW standard, a basso costo e facilmente reperibile. Nessuna scheda  custom: solo moduli già pronti. 

 

Software scritto in python facile da scrivere, matenere e debuggare. Librerie standard tutte disponibili. 

La piattaforma di sviluppo standard su raspberry supporta diverse librerie per machine learning (ecosistema python). 

 

Volendo si può fare i deploy anche di modelli pre-addstrati che utilizzano reti neurali avanzate 

(es. Framework Tensorflow - vedi ad esempio https://blog.paperspace.com/tensorflow-lite-raspberry-pi/) 

 

 

Nota: Ogni sensore richiede GND, VCC + 2 GPIO (Trigger + Echo). Su raspberry 2 ci sono 24 GPIO pin disponibili => questo sistema può supportare  fino a 12 sensori 

 

Sensore standard tipo con interfaccia 4 pin tipo HC-SR04/SR04+ sono più o meno  tutti simili: risoluzione ad 1CM e raggio utile tra 3-4 metri. 

 

I pattern degli echi rilevati devono essere poi usati per il riconoscimento di oggetti. 

 

Velocità propagazione dipende dal mezzo. In aria il parametro fondamentale è la  temperatura che nel caso di applicazioni reali può variare anche in modo significativo. Due possibilità per migliorare l'accuratezza del  sistema: 

1. Misurare la temperatura e applicare compensazione della temperatura nel calcolo della distanza dalla temperatura 
2. Calibrare il sistema (eventualmente anche sensore per sensore) eseguendo delle  misure ripetute su bersagli a distanza nota. --> vedi libreria https://github.com/emanbuc/Bluetin_Python_Echo 

 

Nota: nei Raspberry è presente un sensore di temperatura a bordo della scheda che può essere usato per la calibrazione 

Nota2: esistono versioni industriale dei Raspberry a partire da 130-150€ 

-  es. https://andino.shop/en 
- Oppure piattaforme più evolute con la gestione dei container docker come quella della Hilsher (https://www.hilscher.com/products/product-groups/industrial-internet-industry-40/netiotnetfield-edge/?) 

==> questo sistema può essere trasformato in un prodotto reale utilizzabile in ambiente industriale e portato realmente sul campo con pochissimo  lavoro (qualche giorno) senza modificare il software. 

 

## Versione 2: rete di sensori distribuiti realizzata con moduli WiFi ESP82266 che scambiano dati tramite MQTT 

 1 raspberry utilizzato come broker MQTT e eventualmente anche come gateway/access point wifi 

N noti ESP8266 gestiscono i sensori ed inviano i dati tramite MQTT e rete Wifi 

 

Nota: i moduli ESP8266 espongono fino a 16 GPIO utilizzabili => ogni  modulo può supportare fino a 8 sensori HC-SR04 + sensore di temperatura  su ingresso analogico ADC interno per calibrazione. 

 

In questo modo si può aumentare praticamente all'infinito la risoluzione del sistema in termini di numero di sensori. 

 E si possono estendere le dimensione dell'area di rilevamento fino ai  limiti della copertura delle rete WiFi (In teoria usando dei ripetitori  ed una suddivisione a zone si potrebbe si può coprire anche un intero  palazzo o un area molto grande). 

 ### TODO LIST (versione 1)

- [ ] progetto di massima HW
- [ ] progetto di massima SW
- [ ] progetto sistema ML
- [ ] prototipo HW/SW
- [ ] test acquisizione dati
- [ ] creare dataset per addestramento modello
- [ ] sviluppare un classificatore dimostrativo con un modello di base
- [ ] test deploy del modello su raspberry 
- [ ] creare modello con AutoML
- [ ] ottimizzare modello 
- [ ] sviluppare pipeline per addestramento e miglioramento continuo del modello

 



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

 