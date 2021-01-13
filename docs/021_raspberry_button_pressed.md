# Gestione eventu "Button Pressed" su Raspberry

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