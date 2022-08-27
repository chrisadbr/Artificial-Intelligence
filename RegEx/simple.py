# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 00:07:13 2022

@author: chris
"""

import re

text_to_search = '''
    abcdefghijklmnopqurtuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    1234567890
    Ha HaHa
    MetaCharacters (Need to be escaped):
    . ^ $ * + ? { } [ ] \ | ( )
    coreyms.com
    321-555-4321
    123.555.1234
    123*555*1234
    800-555-1234
    900-555-1234
    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson
    Mr. T
    
    cat
    mat
    bat
    pat
'''

sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print("#Link Patterns")
link_pattern =  re.compile(r'coreyms\.com')
link_matches =  link_pattern.finditer(text_to_search)

for link in link_matches:
    print(link) 

# Word boundary {space or start of a sentence}
pattern2 = re.compile(r'\bHa')
matches2 = pattern2.finditer(text_to_search)

for match in matches2:
    print(match)
    
# Start and end of a string
pattern3 = re.compile(r'^Start')
matches3 = pattern3.finditer(sentence)

for match in matches3:
    print(match)

pattern4 =  re.compile(r'end$')
matches4 = pattern4.finditer(sentence)

for match in matches4:
    print(match)

# Phone number patterns
#pattern5 = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
pattern5 = re.compile(r'[89]00[-.]\d{3}[-.]\d{4}')
matches5 = pattern5.finditer(text_to_search)

for match in matches5:
    print(match)
    
#with open('./data.txt', 'r') as f:
 #    data =  f.read()

#for match in pattern5.finditer(data):
 #   print(match)

pattern6 = re.compile(r'[^b]at')

for match in pattern6.findall(text_to_search):
    print(match)
    
pattern7 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
for match in pattern7.finditer(text_to_search):
    print(match)
    
pattern8 = re.compile(r'start', re.I) # ignore case
for match in pattern8.findall(sentence):
    print(match)