import pickle


x_test= [59,87,26,30,35,40,80]
x_test2= [60,87,25,40,80,90]
filename = 'C:/gitrepos/ultrasonic-vision/models/linearSVC_classificator_model_pickle_outline_removed.pkl'
load_lr_model =pickle.load(open(filename, 'rb'))
result =load_lr_model.predict([x_test])
print(result)

# Convert into ONNX format
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

initial_type = [('float_input', FloatTensorType([None, 5]))]
onx = convert_sklearn(load_lr_model, initial_types=initial_type)
with open(filename+".onnx", "wb") as f:
    f.write(onx.SerializeToString())

# Compute the prediction with ONNX Runtime
import onnxruntime as rt
import numpy

x_test_array = numpy.array([20,30,40,50,20,30,40,50,10], dtype=numpy.float32)
sess = rt.InferenceSession(filename+".onnx")
input_name = sess.get_inputs()[0].name
label_name = sess.get_outputs()[0].name
pred_onx = sess.run([label_name], {input_name: x_test_array})[0]
print(pred_onx)