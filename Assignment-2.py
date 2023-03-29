# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 12:55:53 2023

@author: neham
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import stats


def data_frame(file):
    
    if ".xlsx" in file:
        df = pd.read_excel(file, na_values="..", index_col=0)
    elif ".csv" in file:
        df = pd.read_csv(file, na_values="..", index_col=0)
    else:
        print("invalid filetype")
        
    df_clean = df.dropna(axis=1, how="all").dropna()
    
    df_t = df_clean.transpose()
    
    return df_clean, df_t







    
    