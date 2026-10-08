import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

mov=pd.read_csv("movies.csv")
ipl=pd.read_csv("ipl-matches.csv")
mov2=pd.read_csv("imdb-top-1000.csv")
ipl2=pd.read_csv("deliveries.csv")
crs=pd.read_csv("courses.csv")
mchs=pd.read_csv("matches.csv")
reg1=pd.read_csv("reg-month1.csv")
reg2=pd.read_csv("reg-month2.csv")
stdt=pd.read_csv("students.csv")
tps=pd.read_csv("tips.csv")
exp=pd.read_csv("expense_data.csv")
tit=pd.read_csv("titanic.csv")


# genre=mov2.groupby("Genre")
# print(genre.sum())
# print(genre["IMDB_Rating"].max())
# print(genre["IMDB_Rating"].mean())
# print(genre["IMDB_Rating"].std())
# print(genre.sum()["Gross"].sort_values(ascending=False))
# print(genre['IMDB_Rating'].mean().sort_values(ascending=False).head(1))

# dire=mov2.groupby("Director")["No_of_Votes"].sum().sort_values(ascending=False).head()
# print(dire)


# title=mov2.groupby("Series_Title")
# print(title.max()["IMDB_Rating"])

# print(mov2["Star1"].value_counts())
# print(mov2.columns)

# print(len(genre))
# print(mov2["Genre"].nunique())

# print(mov2["Genre"].value_counts())
# print(genre.size())

# print(genre.get_group("Action"))
# print(genre["Action"].first())/
# print(genre.get_group("Fantasy"))
# print(genre.groups)

# print(genre.describe())
# print(genre.sample(2,replace=True))
# print(genre.nunique())

# print(genre.agg(
#     {
#         "Runtime":"mean",
#         "IMDB_Rating":"mean",
#         "No_of_Votes":"sum",
#         "Metascore":"min",
#         "Gross":"max"
#     }
# ))

# print(genre.agg(['min','max']))

# print(genre.agg(
#     {
#         "Runtime":['min','max','mean'],
#         "IMDB_Rating":['min','max','mean'],
#     }
# ))
# df=pd.DataFrame(columns=mov2.columns)
# for group,data in genre:
#     df=df.append(data[data["IMDB_Rating"]==data["IMDB_Rating"].max()])    should done in cahtgpt

# def A_letter(group):
#     return group['Series_Title'].str.startswith('A').sum()
    
# print(genre.apply(A_letter))

# def group_rank(group):
#     group['genre_rank']=group['IMDB_Rating'].rank(ascending=False)
#     return group
# print(genre.apply(group_rank))

# def normal(group):
#     group["Normalize_rank"]=group["IMDB_Rating"]-group["IMDB_Rating"].min()/group["IMDB_Rating"].max()-group["IMDB_Rating"].min()
#     return group
# print(genre.apply(normal))

# duo=mov2.groupby(["Director","Star1"])
# duo=mov2.groupby(["Star1","Genre"])
# print(duo.size())
# print(duo.get_group(("Aamir Khan","Amole Gupte")))
# print(duo["Gross"].sum().sort_values(ascending=False).head(1))
# print(duo["Metascore"].mean().sort_values(ascending=False).reset_index())

# print(duo.agg(['min','max']))

# print(ipl2.head())
# print(ipl2.shape)
# run=ipl2.groupby('batsman')["batsman_runs"].sum()
# print(run.sort_values(ascending=False))
# six=ipl2[ipl2['batsman_runs']==6]
# print(six.groupby('batsman')['batsman'].count().sort_values(ascending=False))

# temp_df=ipl2[ipl2['over']>15]
# temp_df=temp_df[(temp_df["batsman_runs"]==6)|(temp_df["batsman_runs"]==4)]
# print(temp_df.groupby('batsman')['batsman'].count().sort_values(ascending=False))

# temp_df=ipl2[ipl2["batsman"]=="V Kohli"]
# print(temp_df.groupby("bowling_team")['batsman_runs'].sum().reset_index())

# def Highest_score(batsman):
#     temp_df=ipl2[ipl2['batsman']==batsman]
#     return temp_df.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False)

# print(Highest_score('DA Warner'))

# print(std)

# print(pd.concat([reg1,reg2],ignore_index=True))
# ml=pd.concat([reg1,reg2],keys=["November","December"])
# print(ml.loc[("December",0)])

# a1=pd.concat([reg1,reg2],ignore_index=True)
# print(a1)

# in_join=stdt.merge(reg1,how='inner',on='student_id')
# lft_join=crs.merge(reg1,how='left',on='course_id')
# print(lft_join)

# temp_df=pd.DataFrame({
#     'student_id':[26,27,28],
#     "name":["Nitish",'Ankit','Rahul'],
#     'partner':[28,26,17]
# })
# student=pd.concat([stdt,temp_df],ignore_index=True)
# print(student.merge(reg1,how='right',on="student_id"))
# print(student.merge(reg1,how='left',on="student_id"))
# print(student.merge(a1,how='outer',on="student_id"))

# print(a1.merge(crs,how='inner',on='course_id')['price'].sum())

# a2=pd.concat([reg1,reg2],keys=['Nov','Dec']).reset_index()
# print(a2.merge(crs,on='course_id').groupby('level_0')['price'].sum())

# print(a1.merge(stdt,on='student_id').merge(crs,on='course_id')[['name','course_name','price']].set_index('name'))

# grf=a1.merge(crs,on='course_id').groupby('course_name')['price'].sum()
# grf.plot(kind='bar')
# plt.show()
# comm_std_id=np.intersect1d(reg1['student_id'],reg1['student_id'])
# print(stdt[stdt['student_id'].isin(comm_std_id)])

# cid_list=np.setdiff1d(crs['course_id'],a1['course_id'])
# print(crs[crs['course_id'].isin(cid_list)])

# std_list=np.setdiff1d(stdt['student_id'],a1['student_id'])
# print(stdt[stdt["student_id"].isin(std_list)].shape[0])

# print(stdt.merge(stdt,how='inner',left_on='partner',right_on='student_id')[['name_x','name_y']])
# print(a1.merge(stdt,on="student_id").groupby(['student_id','name'])['name'].count().sort_values(ascending=False))

# print(stdt.merge(crs,left_on='student_id',right_on='course_id').groupby(['student_id','name'])['price'].sum().sort_values(ascending=False))

# temp_df=mchs.merge(ipl2,left_on='id',right_on='match_id')
# six_df=temp_df[temp_df['batsman_runs']==6]
# no_sixes=six_df.groupby('venue')['venue'].count()
# num_matches=mchs['venue'].value_counts()
# print((no_sixes/num_matches).sort_values(ascending=False).head(3))
# print(temp_df.groupby(['season','batsman'])['batsman_runs'].sum().reset_index().sort_values('batsman_runs',ascending=False).drop_duplicates(['season'],keep='first').sort_values('season'))


# index_val=[('cse',2019),('cse',2020),('cse',2021),('cse',2022),('ece',2019),('ece',2020),('ece',2021),('ece',2022)]
# multiindex=pd.MultiIndex.from_tuples(index_val)
# multiindex=pd.MultiIndex.from_product([['cse','ece'],[2019,2020,2021,2022]])
# s=pd.Series([1,2,3,4,5,6,7,8],index=multiindex)
# print(s['cse'])
# print(s.unstack())

# branch_df1=pd.DataFrame(
#     [
#         [1,2],
#         [3,4],
#         [5,6],
#         [7,8],
#         [9,10],
#         [11,12],
#         [13,14],
#         [15,16],
#     ],
#     index=multiindex,
#     columns=['avg_package','students']
# )
# print(branch_df1.unstack().unstack())
# print(branch_df1['avg_package'])
# print(branch_df1.loc['cse'])

# brancg_df2=pd.DataFrame([
#     [1,2,0,0],
#     [3,4,0,0],
#     [5,6,0,0],
#     [7,8,0,0],
# ],
#     index=[2019,2020,2021,2022],
#     columns=pd.MultiIndex.from_product([['Pew','Isb'],['avg_package','student']])
# )
# print(brancg_df2['Isb']['avg_package'])
# print(brancg_df2.loc[2021])

# brancg_df3=pd.DataFrame([
#     [1,2,0,0],
#     [3,4,0,0],
#     [5,6,0,0],
#     [7,8,0,0],
#     [9,10,0,0],
#     [11,12,0,0],
#     [13,14,0,0],
#     [15,16,0,0],
# ],
#     index=multiindex,
#     columns=pd.MultiIndex.from_product([['Pew','Isb'],['avg_package','student']])
# )
# print(brancg_df3.stack().stack())
# print(brancg_df3.unstack().unstack())
# print(brancg_df3.head())
# print(brancg_df3.shape)
# print(brancg_df3.duplicated())
# print(brancg_df3.isnull())
# print(brancg_df3.duplicated())
# print(brancg_df3.loc[('cse'),2021])
# print(brancg_df3.loc[('cse',2019):('ece',2020):2])
# print(brancg_df3.iloc[0])
# print(brancg_df3.iloc[0:5:2])
# print(brancg_df3['Pew']['avg_package'])
# print(brancg_df3.iloc[:,0:4:2])
# print(brancg_df3.iloc[[0,4,6],[1,2,3]])
# print(brancg_df3.sort_index(ascending=False))
# print(brancg_df3.sort_index(ascending=False))
# print(brancg_df3.sort_index(ascending=[False,True]))
# print(brancg_df3.sort_index(level=1,ascending=[False]))
# print(brancg_df3.transpose())
# print(brancg_df3.swaplevel().transpose())

# print(pd.DataFrame({
#     'branch':['cse','ece','mech'],
#     '2020':[100,150,60],
#     '2021':[120,140,50],
#     '2022':[130,145,65]
# }).melt(id_vars=['branch'],var_name='year',value_name='num_of_stds')) 

# death=pd.read_csv('time_series_covid19_deaths_global.csv')
# confirm=pd.read_csv('time_series_covid19_confirmed_global.csv')

# ldd=death.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_of_deaths')
# ldc=confirm.melt(id_vars=['Province/State','Country/Region','Lat','Long'],var_name='date',value_name='num_of_cases')
# print(ldc.merge(ldd,on=['Province/State','Country/Region','Lat','Long','date'])[['Country/Region','date','num_of_deaths','num_of_cases']])

# print(tps.groupby('sex')[['total_bill']].mean())
# print(tps.groupby(['sex','smoker'])[['total_bill']].mean().unstack())
# print(tps.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum'))
# a=tps.pivot_table(index='sex',columns='smoker')['size']

# print(tps.pivot_table(index=['sex','smoker'],columns=['day','time'],values='total_bill',aggfunc={'size':'mean','tip':'max','total_bill':'sum'}))

# print(tps.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum',margins=True))

# print(exp['Category'].value_counts())
# exp['Date']=pd.to_datetime(exp['Date'])
# exp['month']=exp['Date'].dt.month_name()
# print(exp.info())
# exp.pivot_table(index='month',columns='Category',values='INR',aggfunc='sum',fill_value=0).plot()
# exp.pivot_table(index='month',columns='Income/Expense',values='INR',aggfunc='sum',fill_value=0).plot()
# exp.pivot_table(index='month',columns='Account',values='INR',aggfunc='sum',fill_value=0).plot()
# plt.show()

# s=pd.Series(['cat','cow','cutie','queen','king','fast',None,'car',None])
# print(s[s.str.startswith('c')])
# print(tit['Name'].str.lower())
# print(tit['Name'].str.upper())
# print(tit['Name'].str.capitalize())
# print(tit['Name'].str.title())
# print(tit['Name'].str.len().max())
# print(tit['Name'][tit['Name'].str.len()==82].values[0])
# print(tit['Name'].str.strip())
# print(tit['Name'].str.split(',').str.get(1))
# tit['lastName']=tit['Name'].str.split(',').str.get(0)
# s=tit['title']=tit['Name'].str.split(',').str.get(1).str.strip().str.split(' ',n=1,expand=True)
# print(s)
# print(tit[tit['Name'].str.endswith('s')]['Name'])
# print(tit[tit['Name'].str.startswith('s')]['Name'])
# print(tit[tit['Name'].str.isdigit()]['Name'])
# print(tit[tit['Name'].str.contains('james',case=False)]['Name'].sum())
# print(tit[tit['Name'].str.contains('^[aeiouAEIOU].*[aeiouAEIOU]$')]['Name'])
# print(tit[tit['Name'].str.contains('^[^aeiouAEIOU].*[^aeiouAEIOU]$')]['Name'])

# print(tit['Name'].str[::2])
# print(tit['Name'].str[::-1])

# print(pd.Timestamp('11,2,2026 12:55AM'))
# print(pd.Timestamp('2nd October 2026 12:55AM'))
import datetime as dt
# x=pd.Timestamp(dt.datetime(2026,10,2,2,1))
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.hour)
# print(x.minute)
# print(x.second)

# print(pd.DatetimeIndex(['2023/1/1','2025/5/14','2026/10/4'])[0])
# print(pd.date_range(start='2024/12/31',end='2025/1/23',freq='4D'))
# print(pd.date_range(start='2024/12/31',end='2025/1/23',freq='B'))
# print(pd.date_range(start='2024/12/31',end='2025/1/23',freq='W'))
# print(pd.date_range(start='2024/12/31',end='2025/1/23',freq='W-SUN'))
# print(pd.date_range(start='2024/12/31',end='2025/1/23',freq='6H'))
# print(pd.date_range(start='2024/12/31',end='2029/1/23',freq='A'))
# print(pd.date_range(start='2024/12/31',periods=21,freq='D'))
# print(pd.date_range(start='2024/12/31',periods=21,freq='H'))