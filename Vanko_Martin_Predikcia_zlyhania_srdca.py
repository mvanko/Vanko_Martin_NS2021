# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:42:42 2021

@author: Kylly
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn

data = pd.read_csv("heart_failure_clinical_records_dataset.csv" , sep=",")

print(data.head())
print(data.info())
print("Number of duplicates: ", data.duplicated().sum())
print(data.describe())
