#tri

inputs = list(map(int, input().split(" ")))

sortedInputs = sorted(inputs)


print("yes" if sortedInputs[2] < sortedInputs[0] + sortedInputs[1] else "no")