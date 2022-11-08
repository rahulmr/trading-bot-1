import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from pre_processor import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPool2D, Flatten, Softmax
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.optimizers import Adam

CRYPTO = 'eth'

feature_data = np.loadtxt('cryptos/'+CRYPTO+'/feature.txt')
feature_data = feature_data.reshape((-1,8,6))

labels = np.loadtxt('cryptos/'+CRYPTO+'/labels.txt',dtype ='int32')

test_features = np.loadtxt('cryptos/'+CRYPTO+'/test_feature.txt')
test_features = test_features.reshape((-1,8,6))

model = Sequential()
model.add(Conv2D(64, (2,2), input_shape = (8,6,1)))
model.add(Activation("relu"))
model.add(MaxPool2D(pool_size=(2,2), padding="same"))

model.add(Conv2D(64, (2,2)))
model.add(Activation("relu"))
model.add(MaxPool2D(pool_size=(2,2), padding="same"))

model.add(Flatten())
model.add(Dense(64, activation="sigmoid"))

model.add(Dense(10))

loss = SparseCategoricalCrossentropy(from_logits=True)
optimizer = Adam(lr=0.001)
metrics = ['accuracy']

model.compile(loss=loss, optimizer=optimizer, metrics=metrics)

train_features = np.array(feature_data[:-740])
train_labels = np.array(labels[:-740])
validation_features = np.array(feature_data[-740:])
validation_labels = np.array(labels[-740:])

model.fit(train_features,train_labels,batch_size=32,epochs=100)

model.evaluate(validation_features,validation_labels, batch_size=20, verbose=2)

probability_model = Sequential([
    model,
    Softmax()
])

predictions = probability_model(test_features)
pred = predictions
lbl = np.argmax(pred,axis=1)
lbl = np.savetxt('cryptos/'+CRYPTO+'/test_lbl3.txt',lbl,fmt='%s')