import matplotlib.pyplot as plt
import numpy as np

def giperbola_plotter(k=2):
  x=np.arange(0.1, 10, 0.1)
  y=k/x
  plt.plot(x, y)
  plt.xlabel ('Coord: x')
  plt.ylabel('Coord: y')
  plt.legend()
  plt.title('Base')
  plt.grid()
  plt.show()
giperbola_plotter()