a = int(input())

change = 1000 - a

coin100 = change / 100
change = change % 100
coin50 = change / 50
change = change % 50
coin10 = change / 10

print("%d %d %d" % (coin100, coin50, coin10))