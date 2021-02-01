import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pl


df = pd.read_csv("train.csv")
df



mean_mrs = int(df[df.Name.str.match(r'(^.*Mrs\..*)') == True].Age.mean()) 
mean_mr = int(df[df.Name.str.match(r'(^.*Mr\..*)') == True].Age.mean())
mean_miss = int(df[df.Name.str.match(r'(^.*Miss\..*)') == True].Age.mean())
mean_master = int(df[df.Name.str.match(r'(^.*Master\..*)') == True].Age.mean())

df.apply(lambda x  : mean_master if ((x.Name.str.match(r'(^.*Master\..*)') == True) & pd.isna(x.Age)) else x.Age )