# Activity Log

## 2020-12-21

project kickoff

## 2020-12-22

creato repository di progetto

studio di fattibilità

roadmap di progetto

ipotesi architettura HW e SW

## 2020-12-25

Creato progetto e repository separato per modello riconoscimento oggetti avanzato



## 2020-12-26

### Basic Raspberry setup

keybord, power supply, nework cable

Raspian upgrade

- check raspian version [How to check the Raspbian Version - Pi My Life Up](https://pimylifeup.com/raspbian-version/)
- Raspian version history [Raspberry Pi OS - Wikipedia](https://en.wikipedia.org/wiki/Raspberry_Pi_OS)
- Raspian upgrade  [Updating and upgrading Raspberry Pi OS - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/raspbian/updating.md)
- Reboot

### Ultrasonic sensors test

Hardware:

- Raspberry PI 3 model B [Buy a Raspberry Pi 3 Model B – Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
  - getting started [Setting up your Raspberry Pi - Introduction | Raspberry Pi Projects](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up) 

- HC-SR04+

test code and wiring from [HC-SR04 Ultrasonic Sensor With Raspberry Pi : 6 Steps - Instructables](https://www.instructables.com/HC-SR04-Ultrasonic-Sensor-With-Raspberry-Pi-2/) 

- HC-SR04+ funzionano a 3.3V  e non a 5V! Non serve il partitore di tensione. => CONNESSIONE DIRETTA
- Spegnere Raspberry e stacare  alimentazione quando di modifica il circuito elettrico
- check model specific pinout [GPIO - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/usage/gpio/)![GPIO pins](media\GPIO-Pinout-Diagram-2.png)

clonato repository su rasberry 

fix syntax for python 3

config git user info on raspberry

run  [ultrasonic-sensor-test.py](src\ultrasonic-sensor-test.py) 

test OK funziona. (foto scattate da cellulare)

Test salvataggio dati acquisiti su file per future elaborazioni



test lettura distanza e salvataggio dati in file CSV [save-sensor-data-to-file.py](src/save-sensor-data-to-file.py)

testOK

definito schema file dati
- dati per riga con ID sensore in modo da poter aggiungere sensori a piacere senza dover modificare lo schema
- valore in colonna "generica"*value" in modo da poter supportare anche alri tipi di dato

refactoring del codice:

- funzioni principali estratte dal main
- predisposizione per:
  - modalità sensore simulato
  - gestione array di sensori
- Mockup GPIO per sviluppo su windows
- Inserita modalità FAKE_HW per eseguire software senza hardware (distanza random)

## 2020-12-27 

Gestione sensori multipli 

Test acquisizione dati con sensori multipli 

- test OK. Foto setup scattata da smartphone
- aggiunto a repository esempio di acquisizione  con due sensori

Attivato Azure for students  con account  emanuele.buchicchio@studenti.unipg.it 

Attivato Workspace Azure Machine Learning 



## 2020-12-28

GPIO.cleanup() see [RPi.GPIO basics 3 – How to Exit GPIO programs cleanly, avoid warnings and protect your Pi – RasPi.TV](http://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi)

### Use digital input to trigger measurement process startup

Gestione evento "button press" come trigger per avviare la misura

-  la gestione può essere fatta in stile "eventi e callback" (interrupt service routine nel mondo dei micrcontrollori) oppure andando in pooling all'interno di un main loop 
- 
- Nota:  nel caso di Raspberry l'SDK in python non espone gli interrupt HW del micro, quindi lo faccio nel main loop
  - esiste una gestione software delle callbak  simile agli interrupt https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/ per fare "edge detection sugli input digitali"
    - https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
    - https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/

Raspberry PI dispone di resistenze Pull-Up / Pull-Down onboard configurabili via software

- si possono usare le resistenze interne e semplificare il circuito eliminando resistenze esterne
- https://kalitut.com/raspberrypi-gpio-pull-up-pull-down-resistor/ 
- https://raspi.tv/2013/rpi-gpio-basics-6-using-inputs-and-outputs-together-with-rpi-gpio-pull-ups-and-pull-downs
- https://www.programcreek.com/python/example/98874/RPi.GPIO.add_event_detect

### Open a remote session to Raspberry

Raspberry collegato a rete WiFi. Host name "raspberrypi"

- ora è possibile eseguire sessioni remote con sistema di acquisizione montato

- per aprire una sessione remota è necessario conoscere hostaname oppure indirizzo IP del raspberry

  - il raspberry è configurato per connetersi alle reti wifi ed ottenre l'indiirzzo IP tramite DHCP quindi è meglio utilizzare l'hostname

  - da Raspian:

    `hostname` per avere il nome host

    `hostname -I` per avere l'indirizzo IP

- Da PC windows ping -a raspberrypi` per ottenere indirizzo ip

Sessione remota verso Raspberry

è  possibile utilizzare sessioni SSH oppure sessioni desktop verso il raspberry.

Nota: l'utente root di defualt di Raspian è username: pi password: raspberry

Nota2: nelle versioni recenti il server SSH su Raspian è disabilitato per defaut e deve essere abilitato  vedi [SSH (Secure Shell) - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/remote-access/ssh/) 

- server abilitato da pannello Preferenze-> configurazioni

- da windows conviene usare Putty per le sessioni SSH o Desktop remoto (RDP) per le sessioni grafiche 
  - su Raspian `sudo apt-get install xrdp`

Xrdp is an open-source implementation of Microsoft’s proprietary RDP Server, the same protocol that most installations of Windows can connect to and be connected from.

The xrdp software replicates Microsoft’s RDP protocol so that other remote desktop clients can connect to your device. The software package even works with Microsoft’s own remote desktop client built into Windows.

Nota3: in Raspian Buster (ad oggi 28-dic-2020) c'è un bug nella configurazione di XRDP che ne impedisce la corretta esecuzione dopo il rebbot. In pratica c'è un problema con i diritti di scrittura del file di log. Le soluzioni sono due: 

- modificare i permessi del file

Disable automatic start at boot time (`systemctl disable xrdp`)

```
touch /var/log/xrdp.log

chown xrdp:adm /var/log/xrdp.log

chmod 640 /var/log/xrdp.log

systemctl start xrdp

systemctl status xrdp
```

You may wish to add this to `/etc/crontab @reboot`

- modificare il percorso dle file di log nel file di configurazione /etc/xrdp/xrdp.ini

  ```
  LogFile=/tmp/xrdp.log
  ```

Nota4: c'è anche ul altro problema di configurazione di xRDP:

vedi [RDP on Raspberry Pi | I.T. Plays Well With Flavors](https://it.playswellwithflavors.com/2020/04/24/rdp-on-raspberry-pi/)

By default Xrdp uses the `/etc/ssl/private/ssl-cert-snakeoil.key` file which is readable only by users that are members of the “ssl-cert” group. You’ll need to add the user that runs the Xrdp server to the `ssl-cert` group.

```bash
sudo adduser xrdp ssl-cert 
```

![image-20201228150623568](media\rdp_raspberry.png)



![image-20201228150825761](media\remote_desktop_session_python.png)



Ora è possibile utilizzare l'ambiente desktop per sviluppo e debug remoto anche dopo il riavvio del Raspberry

Nota5: dalla sessione remota desktop sembra non funzionare l'arresto ed il riavvio del sistema. è necessario eseguire da terminale (o da sessione ssh) i comandi `sudo halt` e `sudo reboot`



## 2020-12-29

### configurazione a quattro sensori

wiring e firmware configuration for four sensors configuration

### Data format for machine learning training

Per rendere facimente utilizzabili i dati ho modificato lo schame del file prodotto dal sistema:

```yaml
Time:  'timestamp unix epoch time (precision to seconds)' #long

HCSR04_001: 'distanza stimata da sensore 1' #: float

HCSR04_002: 'distanza stimata da sensore 2' #: float

HCSR04_003: 'distanza stimata da sensore 3' #: float

HCSR04_004: 'distanza stimata da sensore 4' #: float

ObjectClass: 'tipo di oggetto (classe) presente'  #: string 
```

## Traning dataset 

creato dataset (con dati simulati) per iniare a sperimentare l'addestramento ed il deploy del classificatore

![image-20201229120842143](media\image-20201229120842143.png)



## Training Pipeline with AutoML

Creato Notebook per creazione Pipeline che produce e pubblica classificatore usando i dataset pubblicato in github

Work in progress.... 



## 2020-12-30

AutoML training notebook

Test pubblicazione webservice

Test creazione pipeline per retrain automatico

## 2020-12-31

Assemblato prototipo nella configurazione a 4 sensori

Test acquisizione tadi di training con vari oggetti

Arrivati oggi altri 4  sensori (da montare appena possibile)



## 2021-01-01

## Wiring

I moduli HCSC04 sono predisposit per collegamento con cavi Dupont a 4 poli. In laboratorio ho disponibili solo cavi corti (10-20cm), metre per collegare i sensori sul tetto sono necessari cavi a circa 1 metro.  Cavi lunghi sono più difficili da trovare disponibili sul mercato, ma sono costosi [Amazon.it : cavi dupont](https://www.amazon.it/s?k=cavi+dupont).  Per il prototipo ho individuato due possibili soluzioni economincamente sostenibili:

- cavo ethernet (xx coppie di cavi)
- cavo per sensori impianto di allarme a 4 poli (Vcc, GND, signal01, signal02) + schermatura + anima i nylon per restistenza meccanica

Avevo disponibili degli spezzoni da circa due metri di cavo per sistemi di allarme già tagliati  ed li ho utilizzati per realizzare i cavi dupont.

![Visualizza immagine di origine](media/cavo_allarme.jpg)

[Cavo antifurto 2 x 0,50 mm² + 2 x 0,22 mm² GR2 - MESSI & PAOLONI 5222-CCA - Spagnuolo S.R.L.](https://www.spagnuolosrl.it/prodotto/cavo-antifurto-2-x-050-mm-2-x-022-mm-gr2-messi-paoloni-5222-cca/)

 Dopo aver intestato i cavi con i connettori dupont maschio/femmina ho così ottenuto dei a quattrofili ottimi per il collegamento dei moduli HCSR04

[Immagine cavo realizzato]



collegamento per gruppo sensori 3D

Sistemi di acquisizione con molti sensori e legge di Murphy

	- con solo 7 sensori la legge di Murphy non vale: solo sporadicamente si sono verificati errori docuti al collegamento dei sensori .

Diversi problemi invece docuti alle breadboard di pessima qualità ... con tutti questi collegamenti meglio andare usare una millefori per ottenere un sistema ben più affidabile usando alla fine solo poco tempo in più nell'assemblaggio.

Montaggio telaio per gruppo sensori superiori e test acquisiszione a vuoto con i sensori delle pareti

problemi di interferezenza del telaio sui sensori

geometria e materiale degli oggetti ha un effetto rilevante nella stima della distanza a parità di posizione dell'oggetto e configurazione geometrica dei sensori.

Esperimento con barriera parallela al piano dei sensori (label: WALL_45_DEGREE) e telaio sensori soffitto montato

- ora la distanza della barriera e coerente su tutti i sensori. Errore di qualche centimetro (approssimativamente entro 10%)



## 2021-01-02

### Configurazione a sette sensori

L'hardware utilizzato consente di utilizzare fino a 12 sensori. Al momento in laboratorio sono disponibili 5 sensori HCSR04+ e 5 sensori HCSR04 . Per l'addestramento del classificatore è stata utilizzata una configurazione con sette sensori in modo da lasciare alcuni sensori disponibili per testare l'utilizzo di moduli remoti con microcontrollore ESP8266, mantenendo invariata la configurazione dei sistema principale.

### Interfacciamento con moduli HC-SR-04 / HC-SR-04+ 

I moduli HC-SR-04 in commercio sono più o meno tutti uguali e derivano da uno stesso progetto di base. La versione "+" è stata modificata per avere tensioni di ingresso/uscita a 3.3V al posto dei 5V dell'originale.  

I moduli HC-SR-04+ possono essere collegati direttamente ai GPIO del Raspberry.

I moduli HC-SR-04 non possono essere collegati direttamente ai GPIO di Raspberry, ma serve un adattatore di livello da 5V a 3.3V. In questo caso è sufficiente un partitore di tensione.

Tra resistenze disponibili in laboratorio sono stati scelti valori 18K e 10K per realizzare il partitore.

 => v_out = 5 * 18K / (18K+10K)=3.2V 

 - ![V_2 = V_{out} = V_{in} \frac{R_2}{R_1 + R_2}](media/Voltage_divider_formula.svg)

 - ![voltage divider](media/Voltage_divider.svg)

 - image source: [Voltage divider - Partitore di tensione - Wikipedia](https://it.wikipedia.org/wiki/Partitore_di_tensione#/media/File:Voltage_divider.svg)


Nota: *Usare il rosso per Vcc 5V e Vcc 3.3 non è una buona idea*!

Test della configurazione a sette sensori (file "EMPTY_SEVEN")

- misure instabili e fuori range da parte di alcuni sensori: credo dipenda dalla geometria dell'oggetto 
  - vengono prodotte misure fuori range che probabilmente non portano informazione utile per la classificazione.
  - ragionare su come gestire i fuori range
- Dal sensore 007 non riesco ad ottenere una lettura corretta.  Ho provato a sostituire il sensore, ma il risultato non migliora.  La lettura però presenta un errore sistematico approssimativamente costante, quindi posso procedere lo stesso all'acquisizione dei dati di training.

  - problema di cablatura?
  - disturbo ambientale?
  - 

### ESD Protection

Solitamente per maneggiare i moduli destinati ai makers non servono procedure ed accortezze di protezione da scariche elettrostatiche. Questa volta però ho esagerato: durante il posizionamento dei sensori indossavo abiti sintetici e scarpe di gomma ed ho avuto modo di testare la robustrezza dai sensori a due scariche di notevole intensità. Fortuantamente funzionano ancora!  Non serve il canonico kit scarpe, camice e braccialetto per questi componenti, ma ho iniziato a toccare un termosifone prima di toccare componenti del sistema!



## Dati training 3D

Ogni oggetto è stato posto approssimativamente al centro dell'altra di acquisizione dati, senza utilizzare riferimenti precisi per la posizione con lo scopo di rendere più robusto il riconoscimento da parte del classificatore. Per ogni oggetto acquisizione dati è stata ripetuta più volte dopo aver tolto e posizionato nuovamente l'oggetto con variazioni casuali di posizionamento. 

### Posizionamento oggetti

Sono stati sperimentati diversi posizionamenti degli oggetti all'interno del range dei sensori.  I dati di training del classificatore sono stati acquisiti posizionando gli oggetti nella zona centrale on modo da avere potenzialmente letture significative da tutti sensori presenti (compresi quelli ora non presenti nella configurazione a sette sensori)

![posizionamento_oggetto](C:\gitrepos\ultrasonic-vision\media\object_postion03.jpg)



Acquisizione second dataset di training con configurazione  a sette sensori e barriere parallele ai piani dei sensori

- SQUARE_MILK_90 ![SQUARE_MILK_90](media/SQUARE_MILK_90.jpg)
- SQUARE_MILK_45 ![SQUARE_MILK_45](media/SQUARE_MILK_45.jpg)

- BEAN_CAN ![BEAN_CAN](media/BEAN_CAN.jpg)
- SOAP_BOTTLE_FRONT ![SOAP_BOTTLE_FRONT](media/SOAP_BOTTLE_FRONT.jpg)
- SOAP_BOTTLE_SIDE ![SOAP_BOTTLE_SIDE](media/SOAP_BOTTLE_SIDE.jpg)
- GLASS ![GLASS](media/GLASS.jpg)
- RECTANGULAR_BOX  ![RECTANGULAR_BOX](media/RECTANGULAR_BOX.jpg)
- RECTANGULAR_BOX_SIDE ![RECTANGULAR_BOX_SIDE](media/RECTANGULAR_BOX_SIDE.jpg)
- WALL_BALL ![BALL_WALL](media/BALL_WALL.jpg)
- BALL_CENTER ![BALL_CENTER](media/BALL_CENTER.jpg)
- BEER_BOTTLE ![BEER_BOTTLE](media/BEER_BOTTLE.jpg)

Ogni oggetto è stato posto approssimativamente al centro dell'altra di acquisizione dati, senza utilizzare riferimenti precisi per la posizione con lo scopo di rendere più robusto il riconoscimento da parte del classificatore. Per ogni oggetto l'acquisizione dati è stata ripetuta più volte dopo aver tolto e posizionato nuovamente l'oggetto con variazioni casuali di posizionamento. 



