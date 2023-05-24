import random
import math
import matplotlib.pyplot as plt
from samila import Marker
from samila import GenerativeImage, Projection
def f1(x,y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**3) + abs(y-x)
    return result

def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.sin(x**4) + 2*x
    return result

g = GenerativeImage(f1,f2)

g.generate()

g.seed

g.plot(projection = Projection.POLAR, color = 'blue', bgcolor = 'white')


plt.show()