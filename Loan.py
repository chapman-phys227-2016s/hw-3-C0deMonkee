#! /usr/bin/env python

"""
File: Loan.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: A.4
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Implementing equations A.16 and A.17
"""

def equations(L, n, p):
    """
    Implementing equations A.16 and A.17
    """
    x_prev = L
    for i in range(n):
        y = ( p / 1200 * x_prev ) + ( L / float(n) )
        x_temp = x_prev + ( p / 1200 * x_prev ) - y
        print y
        print x_temp
        x_prev = x_temp