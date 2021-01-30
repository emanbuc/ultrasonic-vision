# Progetto Ultrasonic Vision

Ultrasonic Vision è un sistema di acquisizione dati in grado di rilevare la presenza di un oggetto, determinarne la posizione e riconoscere il tipo oggetto. Il sistema utilizza dei misuratori di distanza ad ultrasuoni e dei modelli di classificazione addestrati con tecniche di machine learning.

L'obiettivo del progetto è quello di realizzare un primo prototipo funzionante al fine di individuare le criticità che dovranno essere affrontate nella progettazione del prodotto finale.

## Sommario

1. [Il sistema Ultrasonic Vision](docs/010_ultrasonic_vision.md)
2. [Il prototipo realizzato](docs/020_prototipo_versione_01.md)
3. [Sintesi dei risultati ottenuti](docs/075_conclusioni_e_risultati.md)
4. [futuri_sviluppi.md](docs\futuri_sviluppi.md)
5. [strumenti e tecnologie utilizzate](docs/095_strumenti_e_tecnologie_utilizzate.md)
6. [Altre Risorse](/docs/090_resources.md)

Relazione finale scaricabile in formato ([ePub](./dist/book.epub) , PDF)

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
- [x] Documentazione utile per proseguire lo sviluppo del sistema

## Contenuto del Repository

Il repository del progetto è ospitato su GitHub  [https://github.com/emanbuc/ultrasonic-vision](https://github.com/emanbuc/ultrasonic-vision). Il contenuto include

- Documentazione del progetto
  - [Diario giornaliero](activity_log.md) con descrizone dettagliata delle attività svolte
  - [Guida alla configurazione dell'Raspberry PI](docs/030_raspberry_setup.md) per la realizzazione del prototipo
  - Istruzioni per la connessione da sessione remota [SSH](docs/031_raspberry_ssh_remote_session.md) o [desktop remoto](docs/034_raspberry_xrdp.md)
  - [Installazione Python 3.8 su Raspberry](docs/032_raspberry_buster_python38_setup.md)
  - [Cablaggio dei moduli HC-SR04](docs/022_raspberry_wiring_HC-SR04.md)
  - Procedura di [verifica del funzionamento](docs/033_distance_meter_test.md) del sistema assemblato
  - Approfondimento sui moduli [HC-SR04](docs/024_ultrasonic-meter_HC-SR04.md)
  - [Gestione evento "pulsante premuto" su Raspberry](docs/021_raspberry_button_pressed.md)
  - Sviluppo del classificatore di oggetti [Azure AutoML](docs/070_azure_autoML.md)
  - Sviluppo del classificatore di oggetti con [SciKit Learn](docs/training_scikit-learn_model.md)
  - Inferenza con modello ML su Raspberry [(Raspberry Edge AI)](docs/050_raspberry_edge_AI.md)
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
  - [Conversione dei modelli addestrati](src/samples/convertToONNX.py) per formato SciKitLearn a formato ONNX
  - [Salvataggio dati su file CSV](src/samples/write-csv-file-test.py)
  - [Salvataggio distanze stimate dai sensori HC-SR04 in file CSV](src/samples/save-sensor-data-to-file.py)
  - [Misuratore di distanza ad ultrasuoni con HC-SR04](src/samples/ultrasonic-meter-test.py)
  - [Test inferenza con modello SciKitLearn](src/samples/test-skl-runtime.py)
  - [Test Inferenza con modello ONNX](src/samples/test-onnx-runtime.py)
