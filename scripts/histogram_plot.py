sns.histplot(x="total_bill",data=df)
plt.show()

--With accurate data
sns.histplot(x="total_bill",data=df,discrete="false")
plt.show()

--with hue
sns.histplot(x="total_bill",data=df,hue="sex",palette="spring")
plt.show()

--with kernel density estimation
sns.histplot(x="total_bill",data=df,kde=True)
plt.show()

--With edge color
sns.histplot(x="total_bill",data=df,edgecolor="red",linestyle="--")
plt.show()

--With bar color
sns.histplot(x="total_bill",data=df,kde=True,color="hotpink")
plt.show()
