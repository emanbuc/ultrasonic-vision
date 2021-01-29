# Addestramento manuale dei modelli di classificazione con libreria SciKit Learn

L'addestramento è atato eseguito dal notebook [model traiining](062_training_scikit-learn_model.md)

Sono stati testati diversi algoritmi comunemente usati per problemi di calssificazione:

- Support Vector Machine (SVM)
- Linear SVC
- KNN

Una gamma molto più ampia di algoritimi è stata testata in maniera effiente usando il [servizio Azure AutoML](070_azure_autoML.md).
  
Per i dettagli sulle implmentazioni dei modelli si rimanda alla [documentazione della libreria](https://scikit-learn.org/stable/user_guide.html)

Per il training sono stati utilizzati dati ripuliti dagli outliars e normalizzati.

```Py
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline,Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
clf = make_pipeline(StandardScaler(), RandomForestClassifier())
clf.fit(x_train_all, np.ravel(y_train_all))
```

Il modello addestrato è stato poi serializzato salvato in un file nel formato nativo SciKit Learn e nel formato ONNX per garantire una migliore portabilità nei diversi ambienti di runtime.

```Py
import pickle
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

filename='../models/rf_classificator_model_pickle_outline_removed.pkl'
filenameONNX='../models/rf_classificator_model_pickle_outline_removed.onnx'

pickle.dump(clf, open(filename, 'wb'))


initial_type = [('distances', FloatTensorType([None, 7]))]
onx = convert_sklearn(clf, initial_types=initial_type)
with open(filenameONNX, "wb") as f:
    f.write(onx.SerializeToString())
```
