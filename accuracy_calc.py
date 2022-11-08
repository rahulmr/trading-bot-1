import numpy as np
import tensorflow as tf     

CRYPTO = 'eth'

labels = np.loadtxt('cryptos/'+CRYPTO+'/test_lbl.txt',dtype ='int32')
labels_bot = np.loadtxt('cryptos/'+CRYPTO+'/test_lbl_bot.txt',dtype ='int32')

# correct predictions / total
sum = np.sum(labels == labels_bot)
total = len(labels)

con = tf.math.confusion_matrix(labels=labels_bot, predictions=labels,num_classes=2)

print(con)
print("Accuracy:")
print(sum/total)

