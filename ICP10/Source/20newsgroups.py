from keras.models import Sequential
from keras import layers
from keras.preprocessing.text import Tokenizer
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
from keras.layers import Embedding,Flatten

#load data
from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset='train',shuffle=True)
#split target and features
data = newsgroups_train['data']
y = newsgroups_train['target']


#tokenizing data
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(data)
#getting the vocabulary of data
X = tokenizer.texts_to_matrix(data)

#split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1000)


#specify input layer size
input_dim = X_train.shape[1]
vocab_size = 1000
model = Sequential()
#adding embedding layer
model.add(Embedding(vocab_size, 50, input_length=input_dim))
model.add(Flatten())
model.add(layers.Dense(300,activation='relu'))
model.add(layers.Dense(20, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['acc'])
history=model.fit(X_train,y_train, epochs=10, verbose=True, validation_data=(X_test,y_test), batch_size=256)

