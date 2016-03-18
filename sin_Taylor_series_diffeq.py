#! /usr/bin/env python

"""
File: sin_Taylor_series_diffeq.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: A.14
Date: March 18
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Finding difference equations for computing sin(x)
"""
import numpy as np

def sin_Taylor(x, n):
    count = 1
    s_prev = 0
    a_prev = x
    sum = 0
    while(count < n):
        a = (-1 * (x ** 2) / ((2*count + 1) * 2*count)) * a_prev
        sum += a
        a_prev = a
        count += 1
    return sum, np.abs(a_prev)
def test_Taylor():
    ans = sin_Taylor(0, 2)
    assert(ans - 0 < 1e-5)
def output():
    x = np.linspace(0,1,10)
    print "x | n | s_n"
    for elem_n, elem_x in enumerate(x):
        ans = sin_Taylor(elem_x, elem_n)
        print str(elem_x) + " | " + str(elem_n) + " | " + str(ans[0])