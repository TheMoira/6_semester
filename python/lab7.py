
# import matplotlib
# matplotlib.use('ps')
import matplotlib.pyplot as plt
import random

data1 = ((0,0,0,0,0.16,0), (0.2,-0.26,0,0.23,0.22,1.6), (-0.15,0.28,0,0.26,0.24,0.44), (0.85,0.04,0,-0.04,0.85,1.6))

def fun1(wsp):
    x = 1
    y = 1
    probability = (0.01,0.07,0.07,0.85)
    for t in range(1000):
        plt.plot(x,y,'go')
        factors = random.choices(wsp,probability)
        a,b,c,d,e,f = factors[0]
        x = a*x + b*y + c
        y = d*x + e*y + f
    plt.show()ch

fun1(data1)