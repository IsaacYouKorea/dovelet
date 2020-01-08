#empty_bottle
a = int(input())
sum = a

firstRewardBottle = int(a / 4)
sum = sum + firstRewardBottle
firstLastBottle = a % 4

a = firstRewardBottle + firstLastBottle
secondRewardBottle = int(a / 4)
sum = sum + secondRewardBottle
secondLastBottle = a % 4

print("%d %d" % (sum, secondLastBottle))
