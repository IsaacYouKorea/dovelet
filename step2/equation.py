# equation

a, b, c, d = map(int, input().strip().split(" "))

left = a - c
right = d - b

if(left == 0):
  if(right == 0):
    print("many")
  else:
    print("none")

else:
  x = right / left
  print("%0.3f" % x)

# if left / right:
#   print("many")
# elif left ==