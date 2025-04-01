import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('fbi.csv')
# Crime trend over years
df.groupby('Year')['Murder'].sum().plot(kind='line')
plt.show()