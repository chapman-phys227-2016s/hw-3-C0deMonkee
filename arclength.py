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
    return x, f

def integral_function(f, dfdx):
    return np.sqrt(1 + dfdx**2)

def arclength(f, a, b, n):
    x_lin = np.linspace(a,b,n+1)
    s = []
    for(elem_x in x_lin):
        ans = integral(f, a, elem_x, integral_function)
        s.append(ans)

def test_arclength():