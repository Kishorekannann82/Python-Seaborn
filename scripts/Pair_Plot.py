import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = sns.load_dataset("ir")

print(df.head())

sns.pairplot(data=df)
plt.show()

#Height
sns.pairplot(data=df,height=1.5)
plt.show()
#Hue and Palette
sns.pairplot(data=df,height=1.5,hue="species",palette="viridis")
plt.show()

#Diagnol Kind
sns.pairplot(data=df,height=1.5,diag_kind="kde")
plt.show()

#Diagnol Histogram
sns.pairplot(data=df,height=1.5,diag_kind="hist")
plt.show()

#Edge Color
sns.pairplot(data=df, height=1.5, plot_kws={"edgecolor": "black"})
plt.show()
