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

```Bash
cat /etc/os-release
```

La versione corrente (dicembre 2020 è "Buster". Un elenco delle versioni è mantentuo sulla [pagina Wikipedia](https://en.wikipedia.org/wiki/Raspberry_Pi_OS) dedicata al prodotto.

Per la procedura di aggiornamento seguire la [guida nella documentazione](https://www.raspberrypi.org/documentation/raspbian/updating.md) ufficiale.  **Dopo l'aggironamento eseguire un riavvio del sistema**.

## Pulsante di avvio della misurazione

Il progetto prevede un pulsante/interuttore per abilitare l'acquisizione collegato ad uno dei pin GPIO.

### gestione  software I/O digitale

Dal punto di vista software La chisura dell La gestione evento "button press" in un sistema embedded tipicamente può essere fatta può essere realizzata in tre modi:

1. associando una _callback function_ all'evento "Input Up/Down" esposto nell'ambiente di programmazione ad alto livello
2. definendo una _Interrupt Service Routine (ISR)_ associata al fronte di salita/discesa sel segnale sul pin  
3. andando a leggere lo stato dell'input all0interno di un pooling loop ed eseguire una azione in diversa in base allo stato rilevato.

Nel caso di Raspberry l'SDK in python non espone gli interrupt HW del micro, quindi il controllo dello stato del pin connesso all'interruttore è stato fatto con la tecnica del _pooling_ all'interno del _main loop_.

Main loop:

 ```Python
    while True:

        mainTriggerState= GPIO.input(MAIN_TRIGGER_GPIO)

        if(mainTriggerState):
            distances,sampleTimestamp = doMeasure()

        else:
            time.sleep(0.1) 
            print(".")
 ```

#### La gestione degli interrupt in Python

L'ambiente di programmazione Python una implementazione "software" simile a quella degli interrup hardware attraverso la funzione GPIO.wait_for_edge(), ma si tratta di una sovrastruttura che non sfrutta realmente le interrupt service routine hardware del micro.

Alcuni esempi disponibili in rete:

- [https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/](https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/)
- [https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/](https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/)

### Pull Up /Pull down su input digitali

Raspberry PI dispone di resistenze Pull-Up / Pull-Down onboard configurabili via software. Si possono usare le resistenze interne e semplificare il circuito eliminando resistenze esterne.

```Python
#pull down for trigger button   
GPIO.setup(MAIN_TRIGGER_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    
```

Alcuni esempi disponibili in rete sulla gestione di input digitali

- [https://kalitut.com/raspberrypi-gpio-pull-up-pull-down-resistor/](https://kalitut.com/raspberrypi-gpio-pull-up-pull-down-resistor/)
- [https://raspi.tv/2013/rpi-gpio-basics-6-using-inputs-and-outputs-together-with-rpi-gpio-pull-ups-and-pull-downs](https://raspi.tv/2013/rpi-gpio-basics-6-using-inputs-and-outputs-together-with-rpi-gpio-pull-ups-and-pull-downs)
- [https://www.programcreek.com/python/example/98874/RPi.GPIO.add_event_detect](https://www.programcreek.com/python/example/98874/RPi.GPIO.add_event_detect)

## Sessione remota su Raspberry da PC di sviluppo

Connettendo alla rete locale il raspberry è possibile aprire una sessione remota sul raspberry montato all'interno del sistema di misura.

Raspian OS supporta sessioni [remote di terminale SSH](./031_raspberry_ssh_remote_session.md) oppure sessioni [desktop](./034_raspberry_xrdp.md) verso il raspberry.

Da Windows è consigliabile  usare _Putty_ come client per le sessioni SSH e _Connesione a Desktop Remoto_ (RDP) per le sessioni grafiche.

_Nota: Per l'utilizzo del raspberry montato all'interno del sistema di misura conviene configurare la rete WiFi._
