# Activity Log

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








