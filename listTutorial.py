#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:33:43 2021

@author: christianbrown
"""

odd_numbers = [number for number in range(1, 20) if number % 5 == 1]
print(odd_numbers)

#List comprehension
cities = [towns.title() for towns in (['arusha', 'tanga', 'kilimanjaro'])]
cities.extend(towns.title() for towns in(['morogoro', 'mbeya', 'kigoma']))
print(cities)

numbers = [number for number in range(1, 30)]
#def get_even(num):
 #   return num % 2 != 1
#print(list(filter(get_even, numbers)))
print(list(filter(lambda x: x % 2 != 1, numbers)))

#print(list(map(lambda x: x % 2 != 1, numbers)))
#combining filter and map all together
print(list(map(lambda x: x ** 2, 
               filter(lambda x : x % 2 != 1, numbers))))
#Conversions using lambda
kilometer = [km for km in range(5, 50, 5)]
miles = list(map(lambda x : (x, x * 1.6), kilometer))
#print(f'Kilometer: {kilometer}')
print(f'Kilometer to miles: {miles}')
# Conversions using lambda
fareinheit = [farh for farh in range(30, 70, 5)]
print(list(map(lambda farein: (farein, (farein - 32) * 5 / 9), fareinheit)))
#