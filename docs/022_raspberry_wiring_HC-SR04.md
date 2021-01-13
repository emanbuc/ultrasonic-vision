# Interfacciamento moduli HC-SR-04 / HC-SR-04+ 

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

## Cablaggio pannello sensori superiore

I moduli HCSC04 sono predisposit per collegamento con cavi Dupont a 4 poli. In laboratorio ho disponibili solo cavi corti (10-20cm), metre per collegare i sensori sul tetto sono necessari cavi a circa 1 metro.  

Cavi lunghi sono più difficili da trovare disponibili sul mercato, ma sono costosi [Amazon.it : cavi dupont](https://www.amazon.it/s?k=cavi+dupont).  Per il prototipo ho individuato due possibili soluzioni economincamente sostenibili:

- cavo ethernet (xx coppie di cavi)
- cavo per sensori impianto di allarme a 4 poli (Vcc, GND, signal01, signal02) + schermatura + anima i nylon per restistenza meccanica

Avevo disponibili degli spezzoni da circa due metri di cavo per sistemi di allarme già tagliati  ed li ho utilizzati per realizzare i cavi dupont.

![Visualizza immagine di origine](media/cavo_allarme.jpg)

[Cavo antifurto 2 x 0,50 mm² + 2 x 0,22 mm² GR2 - MESSI & PAOLONI 5222-CCA - Spagnuolo S.R.L.](https://www.spagnuolosrl.it/prodotto/cavo-antifurto-2-x-050-mm-2-x-022-mm-gr2-messi-paoloni-5222-cca/)

 Dopo aver intestato i cavi con i connettori dupont maschio/femmina ho così ottenuto dei a quattrofili ottimi per il collegamento dei moduli HCSR04

![cavo sensori](media/sensor_cable02.jpg)

Dopo aver realizzato i tre cavi di lunghezza sufficiente e stato possibile montare il pannello superiore con i sensori ed il relativo telaio di sostegno. Per minimizzare i disturbi il telaio di supporto è stato realizzato filo di ferro plastificato a sezione circolare.

![roof sensor panel](media/roof_panel_wiring.jpg)

