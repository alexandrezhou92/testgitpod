import pandas as pd  
import seaborn as sns
import matplotlib.pyplot as plt

ser = pd.Series([0, 1, 2, 3, 4, 5, 6])
ser.cumsum()
plt.show()