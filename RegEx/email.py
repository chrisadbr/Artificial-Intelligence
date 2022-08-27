# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 02:07:54 2022

@author: chris
"""

import re

emails = '''
    CoreyMSchafer@gmail.com
    corey.schafer@university.edu
    corey-321-schafer@my-work.net
'''

pattern =  re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')

for match in pattern.finditer(emails):
    print(match)