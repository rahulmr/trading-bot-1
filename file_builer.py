import numpy as np
from feature_builder import *

features,labels = buildFeature(get_sol())
feature_data = np.array(features)
feature_data = feature_data.astype('float32')

x_min = feature_data.min(axis=(1, 2), keepdims=True)
x_max = feature_data.max(axis=(1, 2), keepdims=True)
feature_data = (feature_data - x_min)/(x_max-x_min)

with open('feature.txt', 'w') as outfile:
    outfile.write('# Array shape: {0}\n'.format(feature_data.shape))
    for data_slice in feature_data:
        np.savetxt(outfile, data_slice, fmt='%-7.6f')
        outfile.write('# New slice\n')

labels = np.savetxt("labels.txt",labels,fmt='%s')


test_features,test_labels = buildFeature(get_eth_test())
test_features = np.array(test_features)
test_features = test_features.astype('float32')

test_labels = np.savetxt("test_lbl_bot.txt",test_labels,fmt='%s')

x_min = test_features.min(axis=(1, 2), keepdims=True)
x_max = test_features.max(axis=(1, 2), keepdims=True)
test_features = (test_features - x_min)/(x_max-x_min)

with open('test_feature.txt', 'w') as outfile:
    outfile.write('# Array shape: {0}\n'.format(test_features.shape))
    for data_slice in test_features:
        np.savetxt(outfile, data_slice, fmt='%-7.6f')
        outfile.write('# New slice\n')
