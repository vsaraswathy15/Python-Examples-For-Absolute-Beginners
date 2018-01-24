#!/usr/bin/env python 


def largest(a,b):
    if a == b:
        print("a and b are equal")
        return b
    elif a > b:
        print("a is greaterthan b")
        return a
    else:
        print("a is lessthan b")
        return b


print (largest(6,9))
