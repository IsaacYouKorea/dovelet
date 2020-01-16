#coci_note
notes = list(map(int, input().split(" ")))

isDirection = 0
result = 'mixed'

if (notes[0] != 1 and notes[0] != len(notes)):
    result = 'mixed'
else :
  for i in range(len(notes) - 1):
    if (notes[i] > notes[i+1]):
      if (isDirection == -1):
        result = 'mixed'
        break
      isDirection = 1 #Asc
      result = 'descending'
    else:
      if (isDirection == 1):
        result = 'mixed'
        break
      isDirection = -1 #Desc
      result = 'ascending'

print(result)