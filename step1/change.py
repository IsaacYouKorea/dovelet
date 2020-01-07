a = int(input())



change = 1000 - a
coinType = [100, 50, 10]
coinCounter = list(range(len(coinType)))
for i in range(len(coinType)):
  coinCounter[i] = int(change / coinType[i])
  change = change % coinType[i]

print(coinCounter)


# coin100 = change / 100
# change = change % 100
# coin50 = change / 50
# change = change % 50
# coin10 = change / 10

# print("%d %d %d" % (coin100, coin50, coin10))