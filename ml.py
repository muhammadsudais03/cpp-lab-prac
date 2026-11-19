import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

rv=pd.read_csv("sharma-kohli.csv")
df=pd.read_csv("batter.csv")
tip=pd.read_csv("tips.csv")
batrun=pd.read_csv("batsman_season_record.csv")
vk=pd.read_csv("vk.csv")
iris=pd.read_csv("iris.csv")


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

# children=[10,20,40,20,30]
# colors=['red','blue','green','yellow','pink']
# plt.bar(colors,children)
# plt.barh(colors,children)
# plt.show()

# plt.bar(batrun['batsman'],batrun['2016'])
# plt.show()

# plt.bar(np.arange(batrun.shape[0])-0.2,batrun['2015'],width=0.2)
# plt.bar(np.arange(batrun.shape[0]),batrun['2016'],width=0.2)
# plt.bar(np.arange(batrun.shape[0])+0.2,batrun['2017'],width=0.2)
# plt.xticks(np.arange(batrun.shape[0]),batrun['batsman'])
# plt.xticks(rotation='vertical')
# plt.show()

# plt.bar(batrun['batsman'],batrun['2017'],label='2017')
# plt.bar(batrun['batsman'],batrun['2016'],bottom='2017',label='2016')
# plt.bar(batrun['batsman'],batrun['2015'],bottom=(batrun['2016']+batrun['2017']),label='2015')
# plt.legend()
# plt.show()

# plt.hist(vk['batsman_runs'],bins=[0,10,20,30,40,50,60,70,80,90,100,110,120])
# plt.show()

# data=[40,49,100,20,25]
# sub=['eng','science','comp','sst','urdu']
# plt.pie(data,labels=sub,autopct='%0.1f%%',explode=[0.3,0,0,0,0.1],shadow=True)
# plt.show()
# plt.figure(figsize=(15,8))
# iris['Species']=iris['Species'].replace({'Iris-setosa':0,'Iris-versicolor':1,'Iris-vergginica':2})
# plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'],c=iris['Species'],cmap='viridis',alpha=0.7)
# plt.xlabel('SepalLength')
# plt.ylabel('petalLength')
# plt.show()

# plt.scatter(df['avg'],df['strike_rate'])
# plt.show()

# x=[1,2,3,4]
# y=[5,6,7,8]
# plt.scatter(x,y)
# plt.text(1,5,'point 1')
# plt.text(2,6,'point 2')
# plt.text(1+2,5+2,'point 3')
# plt.text(4,8,'point 4',fontdict={'size':12,'color':'yellow'})
# plt.show()

# plt.figure(figsize=(18,10))
# plt.scatter(df["avg"],df['strike_rate'],s=df['runs']/2)
# plt.axhline(130,color='red')
# plt.axvline(30,color='red')
# for i in range(df.shape[0]):
#     plt.text(df['avg'].values[i],df['strike_rate'].values[i],df['batter'].values[i])
#     plt.show()

# fig, ax=plt.subplot(nrows=2,ncols=2,figsize=(10,10))
# ax[0,0]
# ax[0,1].scatter(df['avg'],df['runs'])
# ax[1,0].hist(df['avg'])
# ax[1,1].hist(df['runs'])

# df
# fig=plt.figure()
# ax=plt.subplot(projection='3d')
# ax.scatter3D(df['runs'],df['avg'],df['strike_rate'])
# plt.show()

# x=[0,1,5]
# y=[0,10,13]
# z=[0,13,20]

# fig=plt.figure()
# ax=plt.subplot(projection='3d')
# ax.scatter3D(x,y,z,s=[100,100,100])
# ax.plot3D(x,y,z,color='red')
# plt.show()

# x=np.linspace(-10,10,100)
# y=np.linspace(-10,10,100)

# xx,yy=np.meshgrid(x,y)

# z=xx**2+yy**2 
# z.shape

# fig=plt.figure(figsize=(12,8))
# ax=plt.subplot(projection='3d')
# ax.plot_surface(xx,yy,z,cmap='verdis')
# plt.show()

# fig=plt.figure(figsize=(12,8))
# ax=plt.subplot()
# p=ax.contour(xx,yy,z,cmap='viridis')
# fig.colorbar(p)
# plt.show()

tip.plot(kind='scatter',x='total_bill',y='tip',title='cost analysis',marker='+',figsize=(2.5,1.5),s='size',c='sex',cmap='viridis')
plt.show()