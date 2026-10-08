import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

rv=pd.read_csv("sharma-kohli.csv")
df=pd.read_csv("batter.csv")
tip=pd.read_csv("tips.csv")
# price=[48000,59000,32000,45000,50000,52000,4355663444]
# year=[2015,2016,2017,2018,2019,2020,2021]

# plt.plot(year,price)
# plt.ylim(30000,60000)
# plt.grid()
# plt.show()
# print(np.mean(price))

# plt.plot(rv['index'],rv['V Kohli'],color="#9DFF00",linestyle='dashed',linewidth='4',marker='D',markersize=4,label='Virat')
# plt.plot(rv['index'],rv['RG Sharma'],color="#062D32",linestyle='dashdot',marker='.',label='Rohit')
# plt.title("Rohit Sharma Vs Virat Kohli IPL Carrier Comparison")
# plt.xlabel("Season")
# plt.ylabel("Run Scored")
# plt.legend(loc='best')
# plt.legend()
# plt.show()
# plt.show()

# print(rv['RG Sharma'].sum())
# df=df.head(50)
# plt.scatter(df['avg'],df['strike_rate'])
# plt.show()

# plt.scatter(tip['total_bill'],tip['tip'],s=tip['size']*10)
# plt.show()

# plt.plot(tip['total_bill'],tip['tip'],'o')
# plt.show()