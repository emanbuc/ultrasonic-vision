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





