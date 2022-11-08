import requests



# 1590969600000 June 1st 00:00:00 2020
# 1609416000000 Dec 31st 12:00:00 2020
# 1609459200000 June 1st 00:00:00 2021
# 1647441900000 March 16th 14:45:00 2022
# 1648609200000 March 30th 03:00:00 2022
# 1665921600000 Oct 16th 12:00:00 2022

# 1607558400000 Dec 10th 00:00:00 2020
# 1620777600000 May 10th 12:00:00 2021
# 1626825600000 Jul 21st 00:00:00 2021
# 1637496000000 Nov 21st 12:00:00 2021

crypto = 'SOL'
market = crypto + 'USDT'
startTime = 1607558400000
lastCandle = 1620777600000
  
complete = ''

x = 1

while startTime <= lastCandle:  
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