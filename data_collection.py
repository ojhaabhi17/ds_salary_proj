# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 01:09:44 2020

@author: Abhishek
"""

import glass_scrapper as gs
import pandas as pd

path = "C:/Users/Abhishek/Desktop/PGDDS - IIITB/DS Project - Youtube/ds_salary_proj/chromedriver.exe"

df = gs.get_jobs('data scientist',15, False,path,20)
