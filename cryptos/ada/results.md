Withou AI:

Start                     2021-07-21 14:45:00
End                       2021-11-22 23:45:00
Duration                    124 days 09:00:00
Equity Final [$]                 117246.64554
Equity Peak [$]                    119680.653
Return [%]                          17.246646
Buy & Hold Return [%]               51.375053
Return (Ann.) [%]                   55.898086
Max. Drawdown [%]                  -11.959354
Avg. Drawdown [%]                   -1.565628
Max. Drawdown Duration       74 days 00:45:00
Avg. Drawdown Duration        4 days 03:29:00
# Trades                                  223
Win Rate [%]                        38.565022
Best Trade [%]                       3.268456
Worst Trade [%]                     -3.085152
Avg. Trade [%]                       0.071376
Max. Trade Duration           1 days 21:00:00
Avg. Trade Duration           0 days 01:02:00
Profit Factor                        1.227258

=============================================
With AI:

Equity Final [$]                  118214.2149
Equity Peak [$]                  120558.00336
Return [%]                          18.214215
Buy & Hold Return [%]               51.375053
Return (Ann.) [%]                   59.684613
Max. Drawdown [%]                  -10.947789
Avg. Drawdown [%]                   -1.466711
Max. Drawdown Duration       48 days 12:45:00
Avg. Drawdown Duration        3 days 03:00:00
# Trades                                  210
Win Rate [%]                        39.047619
Best Trade [%]                       3.268456
Worst Trade [%]                     -3.085152
Avg. Trade [%]                       0.079713
Max. Trade Duration           1 days 21:00:00
Avg. Trade Duration           0 days 01:01:00
Profit Factor                         1.25577

=============================================
With labels by bot:

Equity Final [$]                 125072.51134
Equity Peak [$]                  126639.81962
Return [%]                          25.072511
Buy & Hold Return [%]               51.375053
Return (Ann.) [%]                     88.2696
Max. Drawdown [%]                   -6.336728
Avg. Drawdown [%]                   -1.423233
Max. Drawdown Duration       24 days 21:45:00
Avg. Drawdown Duration        3 days 00:18:00
# Trades                                  184
Win Rate [%]                        41.847826
Best Trade [%]                       3.268456
Worst Trade [%]                     -3.085152
Avg. Trade [%]                       0.121665
Max. Trade Duration           1 days 21:00:00
Avg. Trade Duration           0 days 01:06:00
Profit Factor                         1.40978

=============================================

Training:

- batch_size=32,epochs=100

Epoch 1/100
210/210 [==============================] - 2s 6ms/step - loss: 0.4199 - accuracy: 0.8706  
Epoch 2/100
210/210 [==============================] - 1s 6ms/step - loss: 0.3004 - accuracy: 0.9129
Epoch 3/100
210/210 [==============================] - 1s 6ms/step - loss: 0.2987 - accuracy: 0.9129

Epoch 97/100
210/210 [==============================] - 1s 7ms/step - loss: 0.1824 - accuracy: 0.9279
Epoch 98/100
210/210 [==============================] - 1s 6ms/step - loss: 0.1835 - accuracy: 0.9285
Epoch 99/100
210/210 [==============================] - 1s 7ms/step - loss: 0.1827 - accuracy: 0.9299
Epoch 100/100
210/210 [==============================] - 2s 8ms/step - loss: 0.1807 - accuracy: 0.9306

37/37 - 0s - loss: 0.3193 - accuracy: 0.9000 - 246ms/epoch - 7ms/step


Confusion Matrix:
   predictions
    0     1
0 [  71  251]
1 [ 298 5337]

Accuracy:
0.9078

Precision TP/(TP+FP):
0.9551

Recall TP/(TP+FN):
0.9471

F1 2*(Precision*Recall/(Precision+Recall)):
0.9511