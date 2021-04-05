#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:58:01 2021

@author: christianbrown
"""
#from card import Card
from deck import Deck

def main():
    player1 = Deck()
    player1.shufle()
    player1.deal_card()
    print(player1)

if __name__ == '__main__':
    main()