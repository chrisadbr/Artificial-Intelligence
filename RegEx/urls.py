# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 02:26:14 2022

@author: chris
"""

import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

#pattern = re.compile(r'https?://(www\.)?[a-z]+\.com')
#pattern =  re.compile(r'https?://(www\.)?\w+\.\w+')

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

#for url in pattern.finditer(urls):
 #   print(url)