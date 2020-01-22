#fill

s, w, p = map(float, input().split(" " ))

sample = [["Wide Receiver", 4.5, 150, 200], ["Lineman", 6.0, 300, 500], ["Quarterback", 5.0, 200, 300]]
myPositions = []

for i in range(len(sample)):
  pos = sample[i]
  if(s <= pos[1] and w >=pos[2] and p >= pos[3]):
    myPositions.append(pos[0])

if len(myPositions) > 0:
  print(' '.join(myPositions))
else:
  print('No positions')