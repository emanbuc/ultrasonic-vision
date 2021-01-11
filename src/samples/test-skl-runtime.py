import pickle

x_test= [[59,87,26,30,35,40,80]]
filename = '/home/pi/ultrasonic-vision/models/rf_classificator_model_pickle_outline_removed.pkl'
load_lr_model =pickle.load(open(filename, 'rb'))
result =load_lr_model.predict(x_test)
print(result)
