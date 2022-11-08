Without AI:

Start                     2021-07-21 14:45:00
End                       2021-11-22 23:45:00
Duration                    124 days 09:00:00
Exposure Time [%]                    7.436563
Equity Final [$]                   112307.012
Equity Peak [$]                     120162.23
Return [%]                          12.307012
Buy & Hold Return [%]              111.387795
Return (Ann.) [%]                   43.089645
Volatility (Ann.) [%]               24.496094
Sharpe Ratio                         1.759041
Sortino Ratio                        4.493638
Calmar Ratio                         6.591476
Max. Drawdown [%]                   -6.537177
Avg. Drawdown [%]                   -1.245851
Max. Drawdown Duration       54 days 02:45:00
Avg. Drawdown Duration        3 days 18:15:00
# Trades                                  205
Win Rate [%]                        36.097561
Best Trade [%]                       4.162684
Worst Trade [%]                     -1.912286
Avg. Trade [%]                       0.057661
Max. Trade Duration           1 days 00:00:00
Avg. Trade Duration           0 days 00:50:00
Profit Factor                        1.215794

=============================================
With AI: 

Equity Final [$]                   115175.738
Equity Peak [$]                    122033.892
Return [%]                          15.175738
Buy & Hold Return [%]              111.387795
Return (Ann.) [%]                   54.026082
Volatility (Ann.) [%]               26.342457
Sharpe Ratio                         2.050913
Sortino Ratio                        5.846504
Calmar Ratio                         9.613393
Max. Drawdown [%]                   -5.619876
Avg. Drawdown [%]                   -1.163397
Max. Drawdown Duration       54 days 02:45:00
Avg. Drawdown Duration        3 days 17:33:00
# Trades                                  201
Win Rate [%]                         36.81592
Best Trade [%]                       4.162684
Worst Trade [%]                     -1.912286
Avg. Trade [%]                       0.070738
Max. Trade Duration           1 days 00:00:00
Avg. Trade Duration           0 days 00:50:00
Profit Factor                        1.268305

=============================================
With labels by bot:

Equity Final [$]                    115606.57
Equity Peak [$]                    121196.302
Return [%]                           15.60657
Buy & Hold Return [%]              111.387795
Return (Ann.) [%]                    55.71451
Max. Drawdown [%]                   -4.612131
Avg. Drawdown [%]                   -1.157836
Max. Drawdown Duration       50 days 22:15:00
Avg. Drawdown Duration        4 days 02:38:00
# Trades                                  174
Win Rate [%]                         39.08046
Best Trade [%]                       4.162684
Worst Trade [%]                     -1.912286
Avg. Trade [%]                       0.084765
Max. Trade Duration           1 days 00:00:00
Avg. Trade Duration           0 days 00:53:00
Profit Factor                        1.330797

=============================================

Training:

- batch_size=32,epochs=100

Epoch 1/100
210/210 [==============================] - 2s 6ms/step - loss: 0.4358 - accuracy: 0.8752  
Epoch 2/100
210/210 [==============================] - 1s 6ms/step - loss: 0.2935 - accuracy: 0.9162
Epoch 3/100
210/210 [==============================] - 2s 7ms/step - loss: 0.2913 - accuracy: 0.9162

Epoch 98/100
210/210 [==============================] - 1s 6ms/step - loss: 0.1979 - accuracy: 0.9272
Epoch 99/100
210/210 [==============================] - 1s 6ms/step - loss: 0.1967 - accuracy: 0.9278
Epoch 100/100
210/210 [==============================] - 1s 6ms/step - loss: 0.1957 - accuracy: 0.9260

37/37 - 0s - loss: 0.2325 - accuracy: 0.9365 - 240ms/epoch - 6ms/step


Confusion Matrix:
   predictions
    0     1
0 [  25  285]
1 [  75 5572]

Accuracy:
0.9396

Precision TP/(TP+FP):
0.9513

Recall TP/(TP+FN):
0.9876

F1 2*(Precision*Recall/(Precision+Recall)):
0.9691