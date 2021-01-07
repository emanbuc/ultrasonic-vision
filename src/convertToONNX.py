import pickle


x_test= [[59,87,26,30,35,40,80]]
filename = '../models/rf_classificator_model_pickle_outline_removed.pkl'
load_lr_model =pickle.load(open(filename, 'rb'))
result =load_lr_model.predict(x_test)
print(result)

# Convert into ONNX format
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

initial_type = [('float_input', FloatTensorType([None, 7]))]
onx = convert_sklearn(load_lr_model, initial_types=initial_type)

# Compute the prediction with ONNX Runtime
import onnxruntime as rt
import numpy as np
x_test_array = np.array(x_test, dtype=np.float32)

sess = rt.InferenceSession(onx.SerializeToString())
inputs = sess.get_inputs()[0].name
input_name = sess.get_inputs()[0].name
pred_onx = sess.run(None, {input_name: x_test_array})[0]

print(pred_onx)