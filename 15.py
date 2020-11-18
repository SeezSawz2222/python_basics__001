import math
i = list(map(float, input().split()))
j = list(map(float, input().split()))
D=((j[0]-i[0])**2)+((j[1]-i[1])**2)
D=math.sqrt(D)
print("{0:.4f}".format(D))

