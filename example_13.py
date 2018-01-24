#!/usr/bin/env python


def largest(a):
    max=0
    for i in a:
        if i>max:
            max=i
    return max


print (largest([3,5,8,6,14]))
