
import numpy as np
def f(key=0, h=0, l=0, R=0, a=0, b=0):
  if key==0:
    S=h*l/2
  if key==1:
    S=np.pi*R**2
  if key==2:
    S=a*b
  print(S)
f(key=0, h=2, l=4)