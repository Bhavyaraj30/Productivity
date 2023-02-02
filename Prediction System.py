import numpy as np
import pickle

# loading the saved model
loaded_model1 = pickle.load(open('C:\Users\bhavya raj\Desktop\Bhavya\Prediction System.py', 'rb'))


## Building a Predictive System 
input_data = (22,2,13,111,90.58,18,2518,4,54,160,90.73,5,0,9.05,14.9,0,3.6)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1) 

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not productive')
else:
  print('The person is productive')