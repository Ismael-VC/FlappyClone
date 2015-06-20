#! /usr/bin/python
#encoding: utf-8

__author__ = "Dj_System"
__date__ = "$05/11/2014 01:30:39 AM$"

from utilities import *

def main():

    clrscr()
    
    # input

    x = []
    y = []

    for i in range(1, 4):
        x.append(float(raw_input('x' + str(i) + '=')))
        y.append(float(raw_input('y' + str(i) + '=')))

    # process
	
    l1 = ((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2) ** 0.5
    l2 = ((x[1] - x[2]) ** 2 + (y[1] - y[2]) ** 2) ** 0.5
    l3 = ((x[0] - x[2]) ** 2 + (y[0] - y[2]) ** 2) ** 0.5

    p = (l1 + l2 + l3) / 2

    S = (p * (p - l1) * (p - l2) * (p - l3)) ** 0.5

    # output

    print 'El área del triángulo es ' + str(S)

if __name__ == "__main__":
    main()
