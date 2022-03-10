# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:54:05 2021

@author: Zoey Leo
"""

import numpy as np
def add_interest(initial, rate):
    return (rate*initial)/100+initial
    
    


def f(x):
    match x:
        case 'a':
            return 1
        case 'b':
            return 2
        case _:        
            return 0   # 0 is the default case if x is not found