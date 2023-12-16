import pandas as pd
import numpy as np
import torch

dataFrame = pd.read_csv('data\\traffic.csv')
# print(dataFrame.head())

new_dataFrame = dataFrame[['Junction','Vehicles']]
new_dataFrame.to_csv('data\\new_traffic.csv', index=False)
# print(new_dataFrame.head())

max_no_of_vehciles = new_dataFrame['Vehicles'].idxmax()
print(max_no_of_vehciles)
new_dataFrame['Vehicles'].iloc[40723]




