#!/usr/bin/env python

def smallest(a,b,c):
    if(a<b) and (a<c):
       smallest_num=a
    elif (b<a) and (b<c):
       smallest_num=b
    else:
       smallest_num=c
    print("the smallest number is :", smallest_num)

smallest(7,6,9)
