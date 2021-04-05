#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 23:45:56 2021

@author: christianbrown
"""
from decimal import Decimal
from account import Account

def main():
    acc = Account('Rukia Rajab', Decimal('560.46'))
    acc.deposit(Decimal('782.25'))
    print(f'Customer name: {acc.getName()}\nBalance: ${acc.getBalance()}')
    
    acc2 = Account('Gregory Jumanne', Decimal('975.98'))
    acc2.withDraw(Decimal('100'))
    print(f'Customer name: {acc2.getName()}\nBalance: ${acc2.getBalance()}')
    
if __name__ == '__main__':
    main()