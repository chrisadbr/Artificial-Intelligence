#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:58:22 2021

@author: christianbrown
"""
from timewithproperties import Time

def main():
    time1 = Time()
    time1.set_time(13, 50, 56)
    print(time1)
    
    #Object II
    time2 = Time()
    time2.hour = 23
    time2.minute = 36
    time2.seconds = 7
    print(time2)
    
if __name__ == '__main__':
    main()