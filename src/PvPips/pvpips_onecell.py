#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

import math
import statistics as stats

import sys
import json
import warnings 

print("python info: ", sys.version)
print("pandas version: ", pd.__version__)
print("numpy version: ", np.__version__)


### print statements show version info
### created with following version info:
# python info:  3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]
# pandas version:  1.2.4
# numpy version:  1.20.1


### create error class
class typeError(Exception):
    def __init__(self, message):
        super().__init__(message)


# In[ ]:


### define type error test
def base_test(x, t=int):
    """control type on inputs"""
    if type(x) != t:
        raise typeError("your input %s is the incorrect type.  Try again with type %s" % (x,t))
    else:
        return x


# In[ ]:


### define bootstrapping function

def bootstrap(r=500, **kwargs):
    """simulates PvP matches r number of times
       for each round, when the required pips are achieved, 
       the code will save the results along with the length
       denoted as number of matches n(matches)
       Finally, the code will return the Expected 
       value E[n(matches)] along with its error (confidence interval)"""
    
    match_array = []
    points_array = []

    for rounds in range(r):
        if rounds == 1: print("starting first round")
        cumulative_pips = pips_acquired
        match_count = 0

        while cumulative_pips < pips_needed:
            draw = np.random.choice([lose_pip, win_pip], 1, [1-win_rate, win_rate])
            match_count += 1
            cumulative_pips += draw[0]

        match_array.append(match_count)
        points_array.append(cumulative_pips)
        
        if rounds % 100 == 0: print("round %s " % rounds)
    
    EM = stats.mean(match_array)
    lowerM = round(np.percentile(match_array, 10),2)
    upperM = round(np.percentile(match_array, 90),2)
    
    perDay = round(EM/days_left, 2)
    
    EP = stats.mean(points_array)
    lowerP = round(np.percentile(points_array, 10),2)
    upperP = round(np.percentile(points_array, 90),2)
    
    print("""Based upon your past performance 
             Matches needed to get required pips: %s 
             Match Confidence Interval (alpha =10): (%s, %s)
             Expected final Pips: %s
             Pips Confidence Interval (alpha =10): (%s, %s)
             
             You need to compete in %s PvP matches per day to achieve this in the time alloted.
             Good luck!""" % (EM, lowerM, upperM, EP, lowerP, upperP, perDay))
    
    return 
    


# In[ ]:


### define known parameters
lose_pip =3
win_pip = 10


# In[ ]:


### gather unknown parameters

days_left = int(input("Missy, how many days are left in the season? "))
pips_acquired = int(input("Missy, how many pips do you have? "))
pips_needed = int(input("Missy, how many pips are needed to loot up? "))
win_rate = float(input("Missy, what is your current win ratio? \n\t(please represent as a percentage, such as 50%= 0.50): "))


# In[ ]:


### cleaner

days_left = base_test(days_left)
pips_acquired = base_test(pips_acquired)
pips_needed = base_test(pips_needed)
win_rate = base_test(win_rate, float)


# In[ ]:


pips_remaining = pips_needed - pips_acquired


# In[ ]:


bootstrap(r=500, lose_pip=lose_pip, 
          win_pip=win_pip, 
          win_rate=win_rate, 
          pips_acquired=pips_acquired, 
          days_left =days_left)


# In[ ]:




