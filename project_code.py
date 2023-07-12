# IMPORTING LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os

df= pd.read_csv("D:\Sleep_health_and_lifestyle_dataset.csv") # IMPORTING DATASET
df.head()
# output 1

print("Shape of the dataframe is :",df.shape) # TO CHECK SHAPE AND SIZE OF THE DATASET
print("The Size of the dataframe is",df.size)
#output 2

df.dtypes # RETURNS THE DATA TYPES PRESENT ON THE DATASET
#output 3

df.describe() # GIVES BRIEF DESCRIPTION THE DATASET
#output 4

# BAR GRAPH
# compairing no. of individuals with sleep disorder according to gender
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='Gender', hue = 'Sleep Disorder')
plt.title('Number of people with sleep disorder by gender')
plt.xlabel('gender')
plt.ylabel('count')
plt.show()
# output 5


# BOX PLOT
# compairing sleep duration by each gender
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x='Gender', y='Sleep Duration')
plt.title('sleep duration by gender')
plt.xlabel('gender')
plt.ylabel('sleep duration')
plt.show()
# output 6


# VIOLIN PLOT
# compairing sleep quality for each gender 

plt.figure(figsize=(10,6))
sns.violinplot(data=df, x='Gender', y='Quality of Sleep')
plt.title('Quality of sleep for each gender')
plt.xlabel('gender')
plt.ylabel('sleep quality')
plt.show()
# output 7

# SWARM PLOT
# compairing physical activity levels for each gender

plt.figure(figsize=(10,6))
sns.swarmplot(data=df, x='Gender', y='Physical Activity Level')
plt.title('Physical Activity Level for each gender')
plt.xlabel('gender')
plt.ylabel('physical activity level')
plt.show()
# output 8

