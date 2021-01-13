# Progetto Ultrasonic Vision
Ultrasonic Vision è un sistema di acquisizione dati in grado di rilevare la presenza di un oggetto, determinarne la posizione e riconoscere il tipo oggetto. Il sistema utilizza dei misuratori di distanza ad ultrasuoni dei modelli di classificazione addestrati con tecniche di machine learning.

L'obiettivo del progetto è quello di progettare e realizzare un primo prototipo funzionante del sistema con lo scopo di valutare la fattibilità del progetto ed individuare le criticità che dovranno essere affrontate nelle realizzazione delle successive versioni del sistema.

## Sommario
- [Progetto Ultrasonic Vision](#progetto-ultrasonic-vision)
  - [Sommario](#sommario)
  - [Il sistema Ultrasonic Vision](#il-sistema-ultrasonic-vision)
  - [Il prototipo realizzato](#il-prototipo-realizzato)
  - [Contenuto del Repository](#contenuto-del-repository)
  - [Roardmap del progetto](#roardmap-del-progetto)
  - [Futuri Sviluppi](#futuri-sviluppi)

## Il sistema Ultrasonic Vision
[sistema Ultrasonic Vision](docs/010_ultrasonic_vision.md)

## Il prototipo realizzato

 [Prototipo del sistema di misura Ultrasocin Vision - versione 1.0](docs\020_prototipo_versione_01.md) 



## Contenuto del Repository

Il repository ufficile del progetto è un repository pubblico ospitato su GitHub  https://github.com/emanbuc/ultrasonic-vision. Il contenuto comprende:

- Documentazione del progetto 
  - [Diario giornaliero](activity_log.md) con descrizone dettagliata delle attività svolte
  - [Guida alla configurazione dell'Raspberry PI](docs/raspberry_setup.md) per lo sviluppo e l'utilizzo del sistema
  - [Guida utilizzo desktop remoto da Windows a Raspian](docs/raspbery_xrdp.md)
  - [Installazione Python 3.8 su Raspberry]()
  - [Cablaggio dei moduli HC-SR04](docs/raspberry_wiring_HC-SR04.md)
  - [Gestione evento "pulsante premuto" su Raspberry](docs/raspberry_button_pressed.md)
  - [Classificatore con Azure AutoML](docs/azure_autoML.md)
  - [Classificatore con SciKit Learn](docs/training_scikit-learn_model.md)
  - [Edge AI]()
- [Dataset](datasets/) per l'addestramento dei classificatori
- [Modelli ML addestrati](models/) e pronti all'uso per la classificaizone degli oggetti
- Notebook Jupyter per l'analisi dei dati, feature engineering e addestramento dei classificatori
  - [Analsi dati acquisiti dai sensori](notebooks/analisi_dati_sensori.ipynb)
  - [Conversione modelli in formato ONNX](notebooks/convertoToONNX.ipynb)
  - [Preparazione dataset per addestramento](notebooks/create_training_dataset.ipynb)
  - [Scikit-Leanr Model Training](notebooks/model_training.ipynb)
  - [Azure AutoML Model Training](notebooks/ultrasonic-vision-train-automl.ipynb)
  - [Rimozione Outliear](notebooks/remove_outlier.ipynb)
- [Alcuni esempi di dati prodotti](sample_acquisitions/) dal sistema nelle diverse configurazioni geometriche
- Software Python3:
  - [Modulo FakeRPi](src/FakeRPi) per eseguire il software senza l'hardware di acquisizione dati
  - [Applicazione console ultrasonic-vision](src/ultrasonic-vision.py)
- Vari script sviluppati durante il progetto
  - [Conversione dei modelli addestrati ](src/samples/convertToONNX.py) per formato SciKitLearn a formato ONNX
  - [Salvataggio dati su file CSV](src/samples/write-csv-file-test.py)
  - [Salvataggio distanze stimate dai sensori HC-SR04 in file CSV](src/samples/save-sensor-data-to-file.py)
  - [Misuratore di distanza ad ultrasuoni con HC-SR04](src/samples/ultrasonic-meter-test.py)
  - [Test inferenza con modello SciKitLearn](src/samples/test-skl-runtime.py)
  - [Test Inferenza con modello ONNX](src/samples/test-onnx-runtime.py)


## Roardmap del progetto

_Nota: Una descrizione dettagliata delle attività svolte è riportata in [activity_log.md](activity_log.md)_

- [x] progetto di massima HW
- [x] progetto di massima SW
- [x] progetto sistema ML
- [x] prototipo HW/SW
- [x] test acquisizione dati
- [x] analisi dei dati acquisiti
- [x] definire configurazione geometrica riproducibile del sistema
- [x] creare dataset per addestramento modello
- [x] sviluppare un classificatore dimostrativo con un modello semplice
- [x] deploy del modello su Raspberry 
- [x] deploy del modello su cloud come web service
- [x] valutazione performance del modello
- [x] ottimizzare classificatore
- [ ] Relazione sul lavoro svolto e risultati ottenuti
- [ ] Documentazione utile per proseguire lo sviluppo del sistema 

## Futuri Sviluppi 

 [futuri_sviluppi.md](docs\futuri_sviluppi.md) 


