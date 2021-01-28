# Basic Raspberry setup

_Per la configurazione inziale, fino a quando non viene abilitato l'accesso remoto, è necessario utilizzare tastiera, mouse e schermo collegati al raspberry. Successivamente sarà possibile eseguire una sessione remota._

## Hardware per confiugrazione iniziale
- Raspberri Pi 3 Model B
- tastiera USB
- alimentatore
- accesso ad internet tramite rete locale ethernet (cablata o WiFi)

## Raspian Install/Ugrade Rasperry OS (Raspian)
Per il prototipo è necessario installare una versione recente di Raspberry OS (Raspian). Si tratta di una distribuzione Linux drivata dalla Debian, ottimizzata per l'utilizzo su Raspberry.

Per l'installazione di Rspberry OS fare riferimento alla [guida](https://www.raspberrypi.org/documentation/installation) nella documentazione ufficiale. 

Se si dispone di un Raspberry con Raspina già installata è invece consigliato eseguire un upgrade del software alla versione corrente.

### Upgrade Raspberry OS

Per prima cosa verificare la versione installata del sistema operativo. Da terminale:
```
cat /etc/os-release
```
La versione corrente (dicembre 2020 è "Buster". Un elenco delle versioni è mantentuo sulla [pagina Wikipedia](https://en.wikipedia.org/wiki/Raspberry_Pi_OS) dedicata al prodotto.

Per la procedura di aggiornamento seguire la [guida nella documentazione](https://www.raspberrypi.org/documentation/raspbian/updating.md) ufficiale

Raspian upgrade


- Raspian version history [Raspberry Pi OS - Wikipedia]()
- Raspian upgrade  [Updating and upgrading Raspberry Pi OS - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/raspbian/updating.md)
- Reboot


## Pulsante di avvio della misurazione
Il progetto prevede un pulsante/interuttore per abilitare l'acquisizione. LA chisura dell

La gestione evento "button press" in un sistema embeded può essere fatta in stile "eventi e callback" (interrupt service routine nel mondo dei micrcontrollori) oppure andando in pooling all'interno di un main loop 
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

## Sessione remota su Raspberry da PC di sviluppo

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

