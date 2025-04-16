import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
df=sns.load_dataset("tips")
df.head()
#Darker Background
sns.set_style("dark")
sns.countplot(x="day",data=df)

#Whitegrid
sns.set_style("whitegrid")
sns.countplot(x="day",data=df)

#ticks
sns.set_style("ticks")
sns.countplot(x="day",data=df)

#Plaette
sns.palplot(sns.color_palette("viridis"))
plt.show()

#DEEp
sns.palplot(sns.color_palette("deep",10))
plt.show()
#Muted
sns.palplot(sns.color_palette("muted"))
plt.show()
sns.palplot(sns.color_palette("dark"))
plt.show()
