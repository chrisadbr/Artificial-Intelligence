#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:25:49 2021

@author: christianbrown
"""

class Card: 
    FACES = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Qeen', 'King']
    SUIT = ['Heart', 'Spade', 'Club', 'Diamond']
    
    def __init__(self, face, suit):
        self._face = face
        self._suit = suit
    
    @property
    def suit(self):
        return self._suit
    
    @property
    def face(self):
        return self._face
    
    def __str__(self):
        return f'{self.face} of {self.suit}\n'