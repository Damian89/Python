#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:53:09 2020

@author: hquemada
"""


import pandas as pd

data = pd.read_excel('volunteers.xlsx')
data.plot(kind='bar',x='Last Name',y='Days Volunteered',legend=False)