#rao

inputs = list(map(int, input().split(" ")))

sortedInputs = sorted(inputs)


a = pow(sortedInputs[0], 2)
b = pow(sortedInputs[1], 2)
c = pow(sortedInputs[2], 2)


if(a + b == c):
  print("right")
elif(a + b > c):
  print("acute")
else:
  print("obtuse")