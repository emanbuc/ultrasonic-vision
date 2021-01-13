# Futuri Sviluppi Ultrasonic - Vision

### Connettività ed invio dati verso storage esterno

Aggiungere sistema per invio dei dati acquisiti verso uno storage esterno. Es. IoT Hub. attraverso protocollo MQTT e rete ethernet/wifi.

### Trigger automatico 

Aggiungere un sistema di trigger per avviare in maniera automatica la misura (es. fotocellula, sensore di prossimità IR, PIR, ...)

### Caratterizzazione dei sensori ad ultrasuoni utilizzati 

Ricavare (dove non disponibile) una caratterizzazione affidabile dei sensori utilizzati.

### Rappresentazione grafica 3D dell'oggetto

Restituire una rappresentazione grafica 3D dell'oggetto a partire dagli echi sonar acquisiti (stima delle distanze )

### Ridurre il tempo necessario ad eseguire una misura

Determinare, in base a caratteristiche dell'hardware e alla configurazione geometrica, l'intervallo di tempo minimo tra due impulsi sonar per evitare interferenze misuratori diversi

### Modello avanzato per riconoscimento oggetti

Sviluppare ed addestrare un modello avanzato per il riconoscimento degli oggetti in un [progetto di ricerca dedicato](https://github.com/emanbuc/ultrasonic-object-recognition).

### Pipeline di miglioramento continuo del classificatore

Progettare, sviluppare e pubblicare pipeline per addestramento e miglioramento continuo del modello ogni volta che sono disponibili nuovi dati per l'addestramento

### Calibrazione del sistema

La velocità propagazione delle onde sonore dipende dal mezzo. In aria il parametro fondamentale è la  temperatura che nel caso di applicazioni reali può variare anche in modo significativo. Due possibilità per migliorare l'accuratezza del  sistema: 

1. Misurare la temperatura e applicare compensazione della temperatura nel calcolo della distanza dalla temperatura 
2. Calibrare il sistema (eventualmente anche sensore per sensore) eseguendo delle  misure ripetute su bersagli a distanza nota. --> vedi libreria https://github.com/emanbuc/Bluetin_Python_Echo 

Nota: nei Raspberry è presente un sensore di temperatura a bordo della scheda che può essere usato per la calibrazione 

### Versione "Industrial grade" del sistema

Utilizzando un gateway per applicazioni IoT industriali compatibile con Raspberry il sistema può essere trasformato in un prodotto reale utilizzabile in ambiente industriale e portato realmente sul campo con pochissimo  lavoro (qualche giorno) senza modificare il software. 

Esempi di prodotti facilmente reperibili a basso costo (130-150€) sono:

-  PLC / PC industriali basati su Raspberry https://andino.shop/en 
-  Industrial gateway della Hilsher (https://www.hilscher.com/products/product-groups/industrial-internet-industry-40/netiotnetfield-edge/?) 

### Versione 2.0: rete di sensori distribuiti realizzata con moduli WiFi ESP82266 che scambiano dati tramite MQTT 

1 raspberry utilizzato come broker MQTT e eventualmente anche come gateway/access point wifi 

N noti ESP8266 gestiscono i sensori ed inviano i dati tramite MQTT e rete Wifi 

Nota: i moduli ESP8266 espongono fino a 16 GPIO utilizzabili => ogni  modulo può supportare fino a 8 sensori HC-SR04 + sensore di temperatura  su ingresso analogico ADC interno per calibrazione. 

In questo modo si può aumentare praticamente all'infinito la risoluzione del sistema in termini di numero di sensori. 

 E si possono estendere le dimensione dell'area di rilevamento fino ai  limiti della copertura delle rete WiFi (In teoria usando dei ripetitori  ed una suddivisione a zone si potrebbe si può coprire anche un intero  palazzo o un area molto grande). 

