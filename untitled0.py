# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:28:51 2022

@author: Krist
"""

import pandas as pd
import os


os.chdir("C:/Users/Krist/Desktop/PiB/Variants and mutation rate in SARS-cov2")


df = pd.read_csv("forlooped test.csv")

# Dictionary to hold counts of positions
position_dict = dict()

for i, row in df.iterrows():
    pos = row['position']
    if pos in position_dict:
        position_dict[pos] += 1
    else:
        position_dict[pos] = 1

print(position_dict)

df['mutation_overlap'] = df.apply(lambda row: position_dict[row.position] > 1, axis=1)

df.to_csv("C:/Users/Krist/Desktop/PiB/Variants and mutation rate in SARS-cov2/mutation_overlap.csv")









df2 = pd.read_csv("dk_merged_wuhan.csv")




#group by position and base


df2.groupby(["position","base","variant_base","Variant"]).size()
df3 = pd.DataFrame({'count' : df2.groupby(["position","base","variant_base","Variant"]).size()}).reset_index()



df3.to_csv("C:/Users/Krist/Desktop/PiB/Variants and mutation rate in SARS-cov2/dk_wuhan_statcount_with_Variant.csv")

















            

