import requests

market = 'ETHUSDT'
startTime = 1609459200000 # June 1st 00:00:00 2021
lastCandle = 1647441900000 # March 16th 14:45:00 2022
#1610809200000

complete = ''

x = 1

while startTime <= 1647441900000:  
    url = 'https://fapi.binance.com/fapi/v1/klines?symbol='+market+'&startTime='+str(startTime)+'&limit=1500&interval=15m'

    data = requests.get(url).json()
    print(x)
    x +=1
    complete += str(data)[1:-1] + ','
    startTime += 1350000000

#open text file
text_file = open("./data.txt", "w")
 
#write string to file
text_file.write(complete)
 
#close file
text_file.close()