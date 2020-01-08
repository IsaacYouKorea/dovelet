#
orgPrice, sellPrice, fakeMoney, changes = map(int , input().split())


print("%d" % ( -sellPrice + ( orgPrice + fakeMoney )))
