import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df=sns.load_dataset("exercise")
df.head()

#scatter plot
mp=sns.FacetGrid(df,col="kind",hue="time")
mp.map(sns.scatterplot,"time","pulse")
mp.add_legend()
plt.show()

#Bar Plot
mp=sns.FacetGrid(df,col="kind",hue="time")
mp.map(sns.barplot,"time","pulse",order=["30 min","1 min","15 min"])
mp.add_legend()
plt.show()

#Kde plot
mp=sns.FacetGrid(df,col="diet")
mp.map(sns.kdeplot,"pulse")

#PairGrid
s=sns.PairGrid(df,hue="time")
s.map_diag(sns.histplot)
s.map_offdiag(sns.scatterplot)
plt.show()
