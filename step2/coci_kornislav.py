#coci_kornislav

inputList = list(map(int, input().split(" ")))

sortedList = sorted(inputList)
area = sortedList[0] * sortedList[2]
print("%d" % area)
