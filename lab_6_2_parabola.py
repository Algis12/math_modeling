import matplotlib.pyplot as plt
import numpy as np
def parabola_plotter(a=1, b=1, c=0, titler='parabola plotter'):
  x=np.arange(-10, 10, 0.1)
  y=a*x**2+b*x+c
  plt.plot(x, y)
  plt.xlabel ('Coord: x')
  plt.ylabel('Coord: y')
  plt.legend()
  plt.title('Base')
  plt.grid()
  plt.show()
parabola_plotter()