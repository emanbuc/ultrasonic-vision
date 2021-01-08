import pickle


x_test= [[59,87,26,30,35,40,80]]
filenameONNX = './models/rf_classificator_model_pickle_outline_removed.onnx'
filename = './models/rf_classificator_model_pickle_outline_removed.pkl'
load_lr_model =pickle.load(open(filename, 'rb'))
result =load_lr_model.predict(x_test)
print(result)

# Compute the prediction with ONNX Runtime
import onnxruntime as rt
import numpy as np
x_test_array = np.array(x_test, dtype=np.float32)

sess = rt.InferenceSession(filenameONNX)
input_name = sess.get_inputs()[0].name
pred_onx = sess.run(None, {input_name: x_test_array})[0]

print(pred_onx)