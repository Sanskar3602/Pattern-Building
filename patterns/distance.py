x1, x2, x3 = 1, 2, 3
y1, y2, y3 = 1, 2, 3

m = (y2-y1)/(x2-x1)
c = y1 - m*x1

ch = y3 - m*x3 - c
d = pow(1 + m*m, 0.5)
print(abs(ch/d))
