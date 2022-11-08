Without AI:

Start                     2021-07-21 14:45:00
End                       2021-11-22 23:45:00
Duration                    124 days 09:00:00
Exposure Time [%]                    5.644418
Equity Final [$]                   116261.714
Equity Peak [$]                    116986.108
Return [%]                          16.261714
Buy & Hold Return [%]               93.913676
Return (Ann.) [%]                   57.321659
Max. Drawdown [%]                   -8.661575
Avg. Drawdown [%]                   -1.143386
Max. Drawdown Duration       51 days 21:30:00
Avg. Drawdown Duration        3 days 13:11:00
# Trades                                  184
Win Rate [%]                        38.586957
Best Trade [%]                       2.911336
Worst Trade [%]                     -1.499622
Avg. Trade [%]                       0.082107
Max. Trade Duration           0 days 06:30:00
Avg. Trade Duration           0 days 00:40:00
Profit Factor                        1.298395

=============================================
With AI:
 
Equity Final [$]                    111624.08
Equity Peak [$]                    113639.474
Return [%]                           11.62408
Buy & Hold Return [%]               93.913676
Return (Ann.) [%]                   39.690328
Volatility (Ann.) [%]               23.893855
Sharpe Ratio                          1.66111
Sortino Ratio                        4.365193
Calmar Ratio                         4.141948
Max. Drawdown [%]                   -9.582528
Avg. Drawdown [%]                   -1.270431
Max. Drawdown Duration       67 days 10:15:00
Avg. Drawdown Duration        4 days 16:34:00
# Trades                                  176
Win Rate [%]                        36.931818
Best Trade [%]                       2.911336
Worst Trade [%]                     -1.499622
Avg. Trade [%]                       0.062552
Max. Trade Duration           0 days 06:30:00
Avg. Trade Duration           0 days 00:41:00
Profit Factor                        1.225577

=============================================
With labels by bot:

Equity Final [$]                   119579.064
Equity Peak [$]                    121416.914
Return [%]                          19.579064
Buy & Hold Return [%]               93.913676
Return (Ann.) [%]                    70.79153
Max. Drawdown [%]                    -5.56544
Avg. Drawdown [%]                   -1.011224
Max. Drawdown Duration       28 days 21:15:00
Avg. Drawdown Duration        2 days 17:43:00
# Trades                                  147
Win Rate [%]                        42.176871
Best Trade [%]                       2.911336
Worst Trade [%]                     -1.499622
Max. Trade Duration           0 days 06:30:00
Avg. Trade Duration           0 days 00:43:00
Profit Factor                        1.457416

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


Confusion Matrix:
   predictions
    0     1
0 [  71  269]
1 [ 225 5392]

Accuracy:
0.9170

Precision TP/(TP+FP):
.9525

Recall TP/(TP+FN):
.9599

F1 2*(Precision*Recall/(Precision+Recall)):
.9562