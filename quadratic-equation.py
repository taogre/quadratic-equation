import math

a = eval(input("Choose parameter a."))
b = eval(input("Choose parameter b."))
c = eval(input("Choose parameter c."))

d = (b**2)-4*a*c

if d>0:
  print("No solution!")
elif d==0: 
  z = math.sqrt(d**2)
  x = (-b+math.sqrt(z))/2*a
  print(x)
else:
  z = math.sqrt(d**2)
  x1 = (-b+math.sqrt(z))/2*a
  x2 = (-b-math.sqrt(z))/2*a
  print(x1,x2)
