#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:01:04 2021

@author: christianbrown
"""

import random
from card import Card

class Deck:
    NUMBER_OF_CARDS = 52
    
    def __init__(self):
        self._currentCard = 0
        self._deck = []
        
        for count in range(Deck.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13], Card.SUIT[count // 13]))
            
    def shufle(self):
        self._currentCard = 0
        random.shuffle(self._deck)
    
    def deal_card(self):
        try:
            card = self._deck[self._currentCard]
            self._currentCard += 1
            return card
        except:
            return None
    
    def __str__(self):
        s = ''
        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]}'
            if (index + 1) % 13 == 0:
                s += '\n'
        return s