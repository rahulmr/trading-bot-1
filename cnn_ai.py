import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from feeder import *
from pre_processor import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPool2D, Flatten

# features,labels = buildFeature(get_btc(),4)

# feature_data = np.array(features)
# feature_data = feature_data.astype('float32')

# x_min = feature_data.min(axis=(1, 2), keepdims=True)
# x_max = feature_data.max(axis=(1, 2), keepdims=True)

# feature_data = (feature_data - x_min)/(x_max-x_min)

# labels = np.savetxt("labels.txt",labels,fmt='%s')
# # Write the array to disk
# with open('feature.txt', 'w') as outfile:
#     outfile.write('# Array shape: {0}\n'.format(feature_data.shape))
#     for data_slice in feature_data:
#         np.savetxt(outfile, data_slice, fmt='%-7.6f')
#         outfile.write('# New slice\n')

# import sys; sys.exit()

feature_data = np.loadtxt('feature.txt')
feature_data = feature_data.reshape((-1,8,6))

labels = np.loadtxt("labels.txt",dtype ='int32')

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

loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer = tf.keras.optimizers.Adam(lr=0.001)
metrics = ['accuracy']

model.compile(loss=loss, optimizer=optimizer, metrics=metrics)

train_features = np.array(feature_data[:-2300])
train_labels = np.array(labels[:-2300])
test_features = np.array(feature_data[-2300:])
test_labels = np.array(labels[-2300:])

history = model.fit(train_features,train_labels,batch_size=20,epochs=15,validation_data=(test_features,test_labels))

# print(model.summary())

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')