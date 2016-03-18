#! /usr/bin/env python

"""
File: arclength.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS 227
Assignment: A.13
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Calculates the arc length of a curve
"""

import numpy as np
import matplotlib.pyplot as plt

def integral(g, a, x, func, N=20):
    index_set = range(N+1)
    x = np.linspace(a, x, N+1)
    g_ = np.zeros_like(x)
    f = np.zeros_like(x)
    g_[0] = g(x[0])
    f[0] = 0
    for n in index_set[1:]:
        g_[n] = g(x[n])
        f[n] = f[n-1] + 0.5*(x[n] - x[n-1])*(g_[n-1] + g_[n])
    return f[-1]

def diff(f, h=1e-6):
    return lambda input: (f(input+h) - f(input-h)/(2*h)) 
    #assumes most functions will be relatively smooth

def integral_function(f, dfdx):
    return np.sqrt(1 + dfdx**2)

def linear_func(x):
    return 2*x + 1
def part_3_func(x):
    return (1/(np.sqrt(2 * np.pi)))*np.exp(-4*(x ** 2))

def arclength(f, a, b, n):
    x_lin = np.linspace(a,b,n+1)
    y_lin = f(x_lin)
    s = []
    for elem_x in x_lin:
        ans = integral(f, a, elem_x, integral_function)
        s.append(ans)
    return s, y_lin
def test_integral():
    ans = integral(linear_func, 0, 5, integral_function)
    assert(ans - 30.0 < 1e-2)
def part_3():
    ans = arclength(part_3_func, -2, 2, 1000)
    y_array = ans[1]
    s_array = ans[0]
    plt.plot(y_array, s_array)