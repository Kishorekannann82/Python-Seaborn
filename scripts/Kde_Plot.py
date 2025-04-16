import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x=np.random.randn(100)
y=np.random.randn(100)
sns.kdeplot(x)

#Shading
sns.kdeplot(y,shade=True,color="violet")

sns.kdeplot(x,y,shade=True,cmap="GnBu")

#With dataframe
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
x = np.random.normal(size=100)
y = np.random.normal(size=100)
sns.kdeplot(x=x, y=y, fill=True, cmap="spring")
plt.show()
