import pandas
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

web_stats = {'Day' : [1, 2, 3, 4, 5, 6],
             'Visitors' : [43, 34, 65, 56, 29, 76],
             'Bounce Rate' : [65, 67, 78, 65, 45, 52]}

df = pandas.DataFrame(web_stats)

df.set_index('Day', inplace=True)  # to set date as index

# print(df.head()) to print first 5 lines
# print(df.tail())  to print last 5 lines
# print(df.tail(2))   # to print 2 last lines

print(df['Visitors'])  # or print(df.Visitors) as there are no spaces in name
df[['Visitors', 'Bounce Rate']].plot()
plt.show()

