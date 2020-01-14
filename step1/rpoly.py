#rpoly
import math
r,n = map(float , input().split())

angle = 360 / n 

print("%0.3f" % (r * r / 2 * math.sin(angle * math.pi / 180) * n))