#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 12:45:24 2021

@author: christianbrown
"""

class Time:
    def __inti__(self, hour = 0, minute = 0, seconds = 0):
        self._hour = hour
        self._minute = minute
        self._seconds = seconds
    
    def set_time(self, *time_tupple):
        if (time_tupple[0] < 0 or time_tupple[0] > 24):
            raise ValueError('Invalid hour set')
        elif(time_tupple[1] < 0 or time_tupple[1] > 59):
            raise ValueError('Invalid minute set')
        elif (time_tupple[2] < 0 or time_tupple[2] > 59):
            raise ValueError('Invalid second set')
        else:
            self._minute = time_tupple[1]
            self._hour = time_tupple[0]
            self._seconds = time_tupple[2]
    
    @property
    def hour(self):
        return self._hour
    
    @hour.setter
    def hour(self, hour):
        if (hour < 0 or hour > 23):
            raise ValueError(f'Hour: {hour} must be 0 - 23')
        self._hour = hour
        
    @property
    def minute(self):
        return self._minute
    
    @minute.setter
    def minute(self, minute):
        if (minute < 0 or minute > 59):
            raise ValueError(f'Minute: {minute} must be 0 - 59')
        self._minute = minute

    @property
    def seconds(self):
        return self._seconds
    
    @seconds.setter
    def seconds(self, seconds):
        if (seconds < 0 or seconds > 59):
            raise ValueError(f'Seconds: {seconds} must be 0 - 59')
        self._seconds = seconds

    def __str__(self):
        return ('12' if self.hour in (0, 12) else str(self.hour % 12)) + f':{self.minute:0>2}:{self.seconds:0>2}' + (' AM' if self.hour < 12 else ' PM')
        