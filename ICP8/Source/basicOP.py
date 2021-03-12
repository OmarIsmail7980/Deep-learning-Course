#Question1
import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

dataset = pd.read_csv("diabetes.csv", header=None).values

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,0:8], dataset[:,8],
                                                    test_size=0.25, random_state=87)
np.random.seed(155)
my_first_nn = Sequential() # create model
#added wieght initializer
my_first_nn.add(Dense(50, input_dim=8, activation='relu', kernel_initializer='he_uniform')) # hidden layer
#added 2 more hidden layers with sigmoid and relu activations 
my_first_nn.add(Dense(50, activation='relu', kernel_initializer='he_uniform'))
my_first_nn.add(Dense(50,activation='sigmoid', kernel_initializer = 'GlorotUniform'))
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])
#fit model
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100,
                                     initial_epoch=0)
#summary
print(my_first_nn.summary())
#accuracy
print(my_first_nn.evaluate(X_test, Y_test))
