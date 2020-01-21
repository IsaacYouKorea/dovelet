#fourth 
inputs = []

inputs.append(list(map(int, input().split(" "))))
inputs.append(list(map(int, input().split(" "))))
inputs.append(list(map(int, input().split(" "))))

x = []
y = []
for i in range(3):
  newInput = inputs[i]

  if newInput[0] in x:
    x.remove(newInput[0])
  else:
    x.append(newInput[0])

  if newInput[1] in y:
      y.remove(newInput[1])
  else:
    y.append(newInput[1])

print(x[0], y[0])