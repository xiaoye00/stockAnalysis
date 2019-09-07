'''
this file simulates a stock tend and analyze buying index one by one 

version : python 3.7.3   64bit
'''
import numpy as np
import matplotlib.pyplot as plt



#variables to adjust the parameter

initialMoney = 3000
baseMoney = 2000
stepEsclatingMoney = 0
lastTimeMoney = 0

startedSteps = 12
flattingSteps = 5
risingSteps = 7
fallingSteps = 5

#how many times you sell stocks
soldStockTimes = 4
#sale time to peak value
SaleOffsetToPeakPoint = -2
#stop buying time to peak value
stopBuyingOffsetToPeakPoint = -4

#make simulated stock data tend
totalCycle = startedSteps + flattingSteps + risingSteps + fallingSteps
peakValuePoint = startedSteps + flattingSteps + risingSteps 
beginToSellPoint = peakValuePoint + SaleOffsetToPeakPoint
stopBuyingPoint = peakValuePoint + stopBuyingOffsetToPeakPoint

leadTime = np.linspace(1,totalCycle,num=totalCycle)
stockValue = np.linspace(3200,2000,num=startedSteps)
stockValueFlating = np.linspace(2000,2000,num=flattingSteps)
stockValueRising = np.linspace(2000,4500,num=risingSteps)
stockValueFalling = np.linspace(4520,2800,num=fallingSteps)

stockValue = stockValue.tolist()
stockValue.extend(stockValueFlating)
stockValue.extend(stockValueRising)
stockValue.extend(stockValueFalling)
boughtStocks = stockValue[0:stopBuyingPoint]

#caculate one piece stock and add into list
stockVolumList = []
sumBoughtStock = initialMoney/stockValue[0]
sumPaidMoney = initialMoney

#simulating process
stockVolumList.append(sumBoughtStock)
paidMoneyTrendList = []
for perStock in boughtStocks:
    money = baseMoney + lastTimeMoney
    stockVolumList.append(money/perStock)
    sumBoughtStock += money/perStock
    sumPaidMoney += money
    paidMoneyTrendList.append(sumPaidMoney)
    lastTimeMoney += stepEsclatingMoney

averageValue = sumPaidMoney/sumBoughtStock

totalSoldMoney = 0

soldStockValue = stockValue[beginToSellPoint:beginToSellPoint+soldStockTimes]

for value in soldStockValue:
    totalSoldMoney += sumBoughtStock * (1/soldStockTimes) * value

profit = totalSoldMoney - sumPaidMoney

profitRate = (profit/sumPaidMoney)*100

profit = int(profit)
sumPaidMoney = int(sumPaidMoney)
profitRate = int(profitRate)

#draw the entire cycle line
plt.plot(leadTime,stockValue)

#draw stop buying dot
plt.scatter(stopBuyingPoint, stockValue[stopBuyingPoint-1], s=100,label='stop buying point',facecolor='blue',alpha=0.5)

#draw sale dot
salePointList = leadTime[beginToSellPoint:beginToSellPoint+soldStockTimes]
plt.scatter(salePointList, soldStockValue, s=200,label='sale point',facecolor='green',alpha=0.5)

#draw start buying dot
plt.scatter(1, stockValue[0], s=200,label='start buying point',facecolor='purple',alpha=0.5)


plt.plot(leadTime,stockValue)
plt.legend(loc='up left')

profit = "profit is " + str(profit) + "RMB"
sumPaidMoney = "total paid money " + str(sumPaidMoney) + "RMB"
profitRate = "total profit rate " + str(profitRate) + "%"
plt.text(0,3800,profit)
plt.text(0,3700,sumPaidMoney)
plt.text(0,3600,profitRate)
plt.show()