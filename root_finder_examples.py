#! /usr/bin/env python

"""
File: root_finder_examples.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS 227
Assignment: A.4
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Implements different methods for finding a root
"""
import numpy as np
import matplotlib.pyplot as plt

def sin(x):
    return np.sin(x)
def cos(x):
    return np.cos(x)
def num1(x):
    return np.sin(x)
def num2(x):
    return np.sin(x) - x
def num3(x):
    return x **5 - np.sin(x)
def display(f, f_prime, a, b, x_0, x_1):
    n1 = Newton(f,f_prime, x_0)
    b1 = Bisection(f, a, b)
    s1 = Secant(f, x_0, x_1)
    return n1, b1, s1
def run():
    ans1 = display(num1, cos, -1, 1, .5, .4)
    print ans1
def Newton(f, dfdx, x, epsilon=1.0E-7, N=100):
    n = 0
    array = []
    while(abs(f(x)) > epsilon and n <= N):
        array.append(x)
        x = x - f(x)/dfdx(x)
        n += 1
    return array[-1]
def Bisection(f, a, b, eps=1.0E-5):
    fa = f(a)
    i = 0
    array = []
    while b - a > eps:
        i += 1
        m = (a + b) / 2.0
        fm = f(m)
        if fa*fm <= 0:
            b = m
        else:
            a = m
            fa = fm
        array.append([i,a,b])
    return array[-1][1]
def Secant(f, x_0, x_1):
    array = []
    x_n_1 = x_1
    x_n_2 = x_0
    for i in range(5):
        x_n = x_n_1 - (f(x_n_1) * (x_n_1 - x_n_2) / float(f(x_n_1) - f(x_n_2)))
        x_n_2 = x_n_1
        x_n_1 = x_n
        array.append(x_n)
    return array[-1]