from pandas import read_excel, options, concat, ExcelWriter
import matplotlib.pyplot as plt

df = read_excel('temp.xlsx')
df.hist()
plt.show()



