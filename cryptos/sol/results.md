Without AI:

Start                     2021-07-21 14:45:00
End                       2021-11-22 23:45:00
Duration                    124 days 09:00:00
Exposure Time [%]                    8.910477
Equity Final [$]                   115022.738
Equity Peak [$]                   117819.4904
Return [%]                          15.022738
Buy & Hold Return [%]              714.667876
Return (Ann.) [%]                   53.798178
Volatility (Ann.) [%]                53.97001
Sharpe Ratio                         0.996816
Sortino Ratio                        2.495767
Calmar Ratio                         3.120995
Max. Drawdown [%]                   -17.23751
Avg. Drawdown [%]                   -4.129658
Max. Drawdown Duration       69 days 13:15:00
Avg. Drawdown Duration        8 days 14:24:00
# Trades                                  259
Win Rate [%]                         39.76834
Best Trade [%]                       4.797277
Worst Trade [%]                     -2.698554
Avg. Trade [%]                       0.054096
Max. Trade Duration           0 days 17:00:00
Avg. Trade Duration           0 days 00:47:00
Profit Factor                        1.127062

=============================================
With AI: 

Equity Final [$]                  112860.3814
Equity Peak [$]                   113697.5304
Return [%]                          12.860381
Buy & Hold Return [%]              714.667876
Return (Ann.) [%]                   45.507039
Volatility (Ann.) [%]               48.965932
Sharpe Ratio                         0.929361
Sortino Ratio                        2.291299
Calmar Ratio                         2.659473
Max. Drawdown [%]                  -17.111296
Avg. Drawdown [%]                    -3.73416
Max. Drawdown Duration       68 days 19:30:00
Avg. Drawdown Duration       10 days 01:33:00
# Trades                                  242
Win Rate [%]                        39.669421
Best Trade [%]                       4.797277
Worst Trade [%]                     -2.698554
Avg. Trade [%]                       0.050041
Max. Trade Duration           0 days 17:00:00
Avg. Trade Duration           0 days 00:47:00
Profit Factor                        1.118977

=============================================
With labels by bot:

Equity Final [$]                  143313.6314
Equity Peak [$]                   144359.5916
Return [%]                          43.313631
Buy & Hold Return [%]              714.667876
Return (Ann.) [%]                  192.295605
Max. Drawdown [%]                  -12.272004
Avg. Drawdown [%]                   -2.156649
Max. Drawdown Duration       43 days 19:00:00
Avg. Drawdown Duration        3 days 04:11:00
# Trades                                  197
Win Rate [%]                        47.715736
Best Trade [%]                       4.797277
Worst Trade [%]                     -2.698554
Avg. Trade [%]                       0.183007
Max. Trade Duration           0 days 17:00:00
Avg. Trade Duration           0 days 00:57:00
Profit Factor                        1.416099

=============================================
Training:

- batch_size=32,epochs=100

Epoch 1/100
210/210 [==============================] - 2s 6ms/step - loss: 0.4287 - accuracy: 0.8782  
Epoch 2/100
210/210 [==============================] - 1s 6ms/step - loss: 0.2806 - accuracy: 0.9215
Epoch 3/100
210/210 [==============================] - 1s 6ms/step - loss: 0.2779 - accuracy: 0.9215

Epoch 98/100
210/210 [==============================] - 1s 5ms/step - loss: 0.1577 - accuracy: 0.9416
Epoch 99/100
210/210 [==============================] - 1s 5ms/step - loss: 0.1603 - accuracy: 0.9409
Epoch 100/100
210/210 [==============================] - 1s 5ms/step - loss: 0.1589 - accuracy: 0.9407

37/37 - 0s - loss: 0.2568 - accuracy: 0.9081 - 227ms/epoch - 6ms/step


[TN FP]
[FN TP]

Confusion Matrix:
   predictions
    0     1
0 [ 139  350]
1 [ 292 5176]

Accuracy:
0.8922

Precision TP/(TP+FP):

0.9367

Recall TP/(TP+FN):

0.9466

F1 2*(Precision*Recall/(Precision+Recall)):

0.9416


