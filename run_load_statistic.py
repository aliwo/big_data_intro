from pandas import read_csv, options, concat, ExcelWriter
import matplotlib.pyplot as plt

df = read_csv('temp.csv')
df.hist()
plt.show()



