# Progetto Ultrasonic Vision

Ultrasonic Vision è un sistema di acquisizione dati in grado di rilevare la presenza di un oggetto, determinarne la posizione e riconoscere il tipo oggetto. Il sistema utilizza dei misuratori di distanza ad ultrasuoni dei modelli di classificazione addestrati con tecniche di machine learning.

L'obiettivo del progetto è quello di progettare e realizzare un primo prototipo funzionante del sistema con lo scopo di valutare la fattibilità del progetto ed individuare le criticità che dovranno essere affrontate nelle realizzazione delle successive versioni del sistema.

## Sommario

- [Progetto Ultrasonic Vision](#progetto-ultrasonic-vision)
  - [Sommario](#sommario)
  - [Il sistema Ultrasonic Vision](#il-sistema-ultrasonic-vision)
  - [Il prototipo realizzato](#il-prototipo-realizzato)
  - [Risultati ottenuti](#risultati-ottenuti)
  - [Roardmap del progetto](#roardmap-del-progetto)
  - [Futuri Sviluppi](#futuri-sviluppi)
  - [Repository del progetto](#repository-del-progetto)

## Il sistema Ultrasonic Vision

[sistema Ultrasonic Vision](docs/010_ultrasonic_vision.md)

## Il prototipo realizzato

 [Prototipo del sistema di misura Ultrasocin Vision - versione 1.0](docs/020_prototipo_versione_01.md)

## Risultati ottenuti

L'analisi dei dati dimostra che il vettore dei tempi di volo (_TOF_) stimanti dai sensori dipende dalla posizione del bersaglio all'interno dell'area di rilevamento e dalle caratteristiche fisiche (geometria, materiale e tipo di superfice) dell'oggetto. Il sistema è quindi potenzialmente in grado di stimare la posizione dell'oggetto all'interno dell'area di rilevamento e di dicriminare tra diversi tipi di oggetti.

I test eseguiti con ilprototipo del sistema hanno però evidenziato anche alcune importanti criticità:

- Il pattern delle distanze stimate dipende in maniera non facilmente separabile sia dal tipo di oggetto presente nell'area di rilevamento che dalla posizione dell'oggetto rispetto ai sensori. Il problema può essere mitigato scgliendo una opportuna configurazione geometrica (numero e posizione dei sensori).

- L'impossibilità di separare gli effetti della posizione dell'bersaglio da quelli della geometria e delle caratteristiche fisiche dell'oggetto rendono particolarmente complesso il compito di sviluppare un sistema di classificazione degli oggetti indipendente dalla posizione. 
  
I modelli di classificazione addestrati e testati si sono invece rivelati molto precisi se gli oggetti da identificare vengono posizionati in maniera precisa, riucreando una condizione molto vicina a quella in cui sono stati prodotti i dati di addestramento.

- I classificatori addestrati nell'ambito di queso progetto hanno performance molto elevate se gli oggetti vengono posizionati esattamente come durante la fase di training, ma non riescono ad riconoscere l'oggetto in maniera indipendente dalla posizione. Questo problema è affrontato nel progetto [Ultrasonic Object Recognition](https://github.com/emanbuc/ultrasonic-object-recognition) che ha come obiettivo la realizzazione di un sistema di riconoscimento degli oggetti basato sui misuratori ad ultrasuoni utilizzando tecniche di machine learning e deep learning più avanzare avanzate.

- La relazione tra la distanza stimata e quella reale non è sempre lineare. Nel caso di posizionemento dell'oggetto non ideale la misura è affetta da errori annche molto ampi e difficimente compensabili perchè dipendenti dalle carateristiche fisiche e geometriche del bersaglio.
  - La forma ed il materiale degli oggetti ha un effetto importante nell'accuratezza della stima della distanza.
  - Per la riflessione delle onde sonore vale la legge si Snell quindi se l'onda sonora colpisce una superficie non parallela al piano frontale del sensore è possibile che l'onda riflessa non raggiunga direttamente il ricevitore (distanza stimata superiode a quella reale, o non lo raggiunga affatto)
  - L'impedenza acustica dell'interfaccia tra l'aria (gas) ed un corpo solido bersaglio è solitamente molto elevata e questo in generale genera una buona riflessione. In presenza di superfici  fonoassorbenti e l'energi ariflessa può essere molto minore e a volte l'eco putrebbe non essere rilevato dal ricevitore
  - Nel caso di superfici irregolari l'onda riflessa può essere molto attenuta a causa fi fenomeni di diffrazione)


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
- [] Relazione sul lavoro svolto e risultati ottenuti
- [x] Documentazione utile per proseguire lo sviluppo del sistema

## Futuri Sviluppi

 [futuri_sviluppi.md](docs\futuri_sviluppi.md)

 
## Repository del progetto

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

