#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 23:28:18 2021

@author: christianbrown
"""
from decimal import Decimal

class Account:
    
    def __init__(self, name, amount):
        if (amount < 0):
            raise ValueError('Amount must be greater than zero')
        self.name = name
        self.balance = amount
        
    def deposit(self, amount):
        if (amount < 0):
            raise ValueError('Amount must be greater than zero')
        self.balance += amount
        
    def withDraw(self, amount):
        if (amount > self.balance):
            raise ValueError('Insufficient funds')
        elif (amount < Decimal('0.00')):
            raise ValueError('Amount must be greater than zero')
        else:
            self.balance -= amount
            
    def getName(self):
        return self.name
    
    def getBalance(self):
        return self.balance
    
   