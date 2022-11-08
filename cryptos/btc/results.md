Without AI:

Start                     2021-07-21 14:45:00
End                       2021-11-22 23:45:00
Duration                    124 days 09:00:00
Equity Final [$]                   111337.684
Equity Peak [$]                     114444.78
Return [%]                          11.337684
Buy & Hold Return [%]               77.008216
Return (Ann.) [%]                   36.834363
Max. Drawdown [%]                    -3.27221
Avg. Drawdown [%]                   -0.627549
Max. Drawdown Duration       35 days 23:15:00
Avg. Drawdown Duration        2 days 20:37:00
# Trades                                  163
Win Rate [%]                         38.03681
Best Trade [%]                       2.502973
Worst Trade [%]                     -1.564644
Avg. Trade [%]                       0.107639
Max. Trade Duration           0 days 08:15:00
Avg. Trade Duration           0 days 00:54:00
Profit Factor                         1.56499

=============================================
With AI: 

Equity Final [$]                   108545.828
Equity Peak [$]                    110257.644
Return [%]                           8.545828
Buy & Hold Return [%]               77.008216
Return (Ann.) [%]                   27.054589
Max. Drawdown [%]                    -4.45665
Avg. Drawdown [%]                   -0.658476
Max. Drawdown Duration       59 days 07:15:00
Avg. Drawdown Duration        4 days 06:24:00
# Trades                                  145
Win Rate [%]                        37.241379
Best Trade [%]                       2.502973
Worst Trade [%]                     -1.564644
Avg. Trade [%]                       0.090248
Max. Trade Duration           0 days 08:15:00
Avg. Trade Duration           0 days 00:48:00
Profit Factor                        1.464468

=============================================
With labels by bot:

Equity Final [$]                    119348.65
Equity Peak [$]                     121143.22
Return [%]                           19.34865
Buy & Hold Return [%]               77.008216
Return (Ann.) [%]                   67.612781
Max. Drawdown [%]                   -2.767493
Avg. Drawdown [%]                   -0.475448
Max. Drawdown Duration       18 days 16:00:00
Avg. Drawdown Duration        1 days 16:37:00
# Trades                                  148
Win Rate [%]                        41.891892
Best Trade [%]                       2.502973
Worst Trade [%]                     -1.564644
Avg. Trade [%]                       0.151984
Max. Trade Duration           0 days 08:15:00
Avg. Trade Duration           0 days 00:57:00
Profit Factor                        1.853741

=============================================

Training:

- batch_size=32,epochs=100

Epoch 1/100
210/210 [==============================] - 2s 6ms/step - loss: 0.4233 - accuracy: 0.8953  
Epoch 2/100
210/210 [==============================] - 1s 6ms/step - loss: 0.2960 - accuracy: 0.9138
Epoch 3/100
210/210 [==============================] - 1s 6ms/step - loss: 0.2940 - accuracy: 0.9138

Epoch 98/100
210/210 [==============================] - 1s 5ms/step - loss: 0.1763 - accuracy: 0.9312
Epoch 99/100
210/210 [==============================] - 1s 6ms/step - loss: 0.1788 - accuracy: 0.9306
Epoch 100/100
210/210 [==============================] - 1s 5ms/step - loss: 0.1760 - accuracy: 0.9314

37/37 - 0s - loss: 0.3988 - accuracy: 0.8405 - 218ms/epoch - 6ms/step

Confusion Matrix:
   predictions
    0     1
0 [  40   57]
1 [ 414 5446]

Accuracy:
0.9209

Precision TP/(TP+FP):
0.9896

Recall TP/(TP+FN):
0.9294

F1 2*(Precision*Recall/(Precision+Recall)):
0.9584