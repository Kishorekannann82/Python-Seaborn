import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
x=[1,2,3,4,5,6,7]
y=[20,40,60,80,90,70,10]
df=pd.DataFrame({"Days":x,"No.of.People":y})
df.head(7)

--Loading from dataset
df=sns.load_dataset("tips")
df.head()
sns.lineplot(x="Days",y="No.of.People",data=df)
plt.show()
--Advanced
sns.lineplot(x="day",y="total_bill",data=df,hue="sex",style="time",palette="flare")
plt.show()
