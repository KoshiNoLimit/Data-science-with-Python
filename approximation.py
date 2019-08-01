import numpy
from scipy import linalg
import math
from matplotlib import pylab


def function(x):
    return numpy.sin(x/5)*numpy.exp(x/10) + 5*numpy.exp(-x/2)


def build_system(func, values):
    a = numpy.zeros((len(values), len(values)))
    b = numpy.zeros(len(values))

    for i in numpy.arange(len(values)):
        b[i] = func(values[i])
        ad = numpy.zeros(len(values))

        for deg in numpy.arange(len(values)):
            ad[deg] = math.pow(values[i], deg)
        a[i] = ad
    return a, b


def approx(ox, c_vector):
    oy = numpy.zeros(len(ox))
    for i in numpy.arange(len(ox)):
        for c in numpy.arange(len(c_vector)):
            oy[i] += c_vector[c] * pow(ox[i], c)
    return oy


def polyn_appr(deg):
    x1 = numpy.linspace(0.0, 15, deg + 1)
    a, b = build_system(function, x1)
    y = approx(x1, linalg.solve(a, b))
    pylab.plot(x1, y, label=str('appr' + str(deg)))


polyn_appr(5)
polyn_appr(10)
polyn_appr(20)

#x = numpy.linspace(0.0, 15, 100)
#y1 = function(x)
#pylab.plot(x, y1, label='f(x)')

pylab.legend()
pylab.show()
