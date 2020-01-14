#x_length
import math
a, b = map(float , input().split())

lengthA = 2 * a * 3.14159 / 2
lengthB = 2 * b * 3.14159 / 2

print("%0.3f" % (math.sqrt(2) * a + math.sqrt(2) * b + lengthA + lengthB))

