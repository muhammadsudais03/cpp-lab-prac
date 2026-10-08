import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mov=pd.read_csv("movies.csv")
ipl=pd.read_csv("ipl-matches.csv")

student_dict={
    "Name":['Sudais','Ilyas','Hisham','Faizan','Abdul Musawer','Abdul Mohaimin'],
    "Course":['SE','CS','SE','SE','CS','SE'],
    "Sem":['5th','5th','5th','5th','5th','5th'],
    "Fees":['50,000','45,000','39,000','49,000','42,000','40,000'],
    "Schol":['65%','70%','80%','66%','72%','75%'],
    "Gender":['M','M','M','M','M','M'],
    "Add":['Pew','Pew','Pew','Mar','Chr','Bun'],
    "Contt":['03705611331','03189606664','03302366272','03467238824','03425535546','03214423346'],
}

Std_info=pd.DataFrame(student_dict)
Std_info.set_index('Name',inplace=True)

# student_data=[
#     ['Sudais','SE','5th','50,000','70%','3.69','M','Pew','03705611331'],
#     ['Ilyas','CS','5th','45,000','70%','3.49','M','Pew','03189606664'],
#     ['Hisham','SE','5th','39,000','70%','3.35','M','Pew','03302366272'],
#     ['Faizan','SE','5th','49,000','70%','2.79','M','Mar','03467238824'],
#     ['Abdul Musawer','CS','5th','42,000','70%','3.31','M','Chr','03425535546'],
#     ['Abdul Mohaimin','SE','5th','40,000','70%','3.41','M','Bun','03214423346'],
# ]
# print(pd.DataFrame(student_data,columns=["Name","Course","Sem","Fees","Schol","CGpa","M/F","Add","Contt"]))

# country=['Pakistan','india','USA','China']
# a=pd.Series(country)
# print(pd.Series(country))
# print(a.dtype)

# babar_score=[56,78,45,89,98,67,85,88,34,60,55,90,103]
# teams=['Eng','Eng','Aus','Nz','WI','Sl','Sa','Zmb','Eng','Aus','Ind','Nep','Sa']
# a=pd.Series(babar_score,index=teams,name='Babar Azam ke Scores')
# print(a)


# marks={
#     "DBMS":78,
#     "DS":75,
#     "AOA":70,
#     "SDA":65,
#     "WEB":73,
# }
# marks_series=pd.Series(marks,name="4th Semester Subject marks")
# print(marks_series.size)
# print(marks_series.dtype)
# print(marks_series.name)
# print(marks_series.is_unique)
# print(marks_series.index)
# print(marks_series.values) 

# df=pd.read_csv('bollywood.csv',index_col="movie")["lead"]
# df=pd.read_csv('bollywood.csv',index_col="movie").squeeze("columns")
# vk=pd.read_csv('kohli_ipl.csv',index_col="match_no").squeeze("columns")
# subs=pd.read_csv('subs.csv',).squeeze("columns")
# print(type(df))
# print(df.head(12))
# print(df.tail(12))
# print(df.sample())
# print(df.value_counts())
# print(((vk>90) & (vk<100)).sum())
# print(vk.sort_values(ascending=False).head(1))
# print(vk.sort_values(ascending=False).head(1).values[0])
# print(vk.sort_values(inplace=True))
# print(vk)
# print(df.sort_index(ascending=False,inplace=True))
# print(df)
# print(vk.count())
# print(vk.sum())
# print(vk.median())
# print(vk.mode())
# print(vk.min())
# print(vk.max())
# print(vk.describe())
# print(subs.min())
# print(subs[subs==0])
# x=pd.Series([12,34,25,45,23,11,56])
# print(vk[-5:])
# print(df[::3])
# print(vk[[1,3,5,7,6,9]])
# a=vk[1501]=100
# a=vk[1]=100
# a=vk[1:3]=[100,43]
# a=vk[[1,3,4,6]]=[100,43,54,21]
# a=df["Awara Paagal Deewana"]="Aamir Khan"
# print(len(df))
# print(type(df))
# print(dir(df))
# print(sorted(df))
# print(min(df))
# print(max(df))
# print(list(df))
# print(dict(df))
# d='Ashok Insan' in df.values
# print(d)
 
# for i in df:
#     print(i)
# for i in df.index:
#     print(i)
# c=100+vk
# print(c)
# print(vk[vk>=50].size)
# print(vk[vk==0].size)
# print(subs[subs>=200].size)
# c=df.value_counts()
# print(c[c>20])
# print(vk.plot())
# print(df.plot())

# df=pd.read_csv('bollywood.csv',index_col="movie").squeeze("columns")
# vk=pd.read_csv('kohli_ipl.csv',index_col="match_no").squeeze("columns")
# subs=pd.read_csv('subs.csv',).squeeze("columns")


# subs.plot()
# vk.plot()
# df.value_counts().head(20).plot(kind="bar")
# df.value_counts().head(20).plot(kind="pie")
# plt.show()


# print(mov.shape)
# print(mov.dtypes)
# print(ipl.dtypes)
# print(mov.columns)
# print(ipl.columns)
# print(mov.values)
# print(ipl.values)
# print(mov.head())
# print(ipl.head())
# print(mov.tail(3))
# print(ipl.tail(2))
# print(mov.sample(3))
# print(ipl.sample(6))
# print(mov.info())
# print(ipl.info())
# print(mov.describe())
# print(ipl.describe())
# print(mov.isnull().sum())
# print(ipl.isnull().sum())
# print(mov.duplicated().sum())
# print(ipl.duplicated().sum())

# print(Std_info.rename(columns={"Schol":"Scholarship","Add":"Address","Contt":"Contact"}))
# print(Std_info.sum(axis=1))
# print(Std_info.mean(axis=1))
# print(Std_info.min(axis=1))
# print(Std_info.min(axis=0))
# print(Std_info.max(axis=0))
# print(Std_info.median(axis=0))

# print(mov[['title_x','actors','year_of_release','wins_nominations']])
# print(ipl[['City','Season','Player_of_Match','WinningTeam']])

# print(Std_info)

# print(mov.iloc[58])
# print(ipl.iloc[58])
# print(ipl.iloc[78:88])
# print(ipl.iloc[[4,6,3,8,9,5,34,]])

# print(Std_info.loc[['Sudais','Hisham']])
# print(Std_info.loc['Sudais':"Abdul Musawer"])
# print(Std_info.loc['Sudais':"Abdul Musawer":3])
# print(Std_info.iloc[0:5:2])

# print(mov.iloc[2:9,3:9])
# print(mov.loc[0:8,"title_x","actors","year_of_release","runtime","title_y"])
# print(mov.loc[0:8,"title_x":"actors"])

# Fm=ipl["MatchNumber"]=="Final"
# new_df=ipl[Fm]
# print(new_df[["Season","WinningTeam"]])

# print(ipl[ipl["MatchNumber"]=="Final"][["Season","WinningTeam"]])

# So=ipl["SuperOver"]=="Y"
# print(So.sum())

# kol=ipl["City"]=="Kolkata"
# chn=ipl["WinningTeam"]=="Chennai Super Kings"
# new_df=ipl[kol,chn]
# print(ipl.sum(new_df))

# print(ipl[(ipl["City"]=="Kolkata") & (ipl["WinningTeam"]=="Chennai Super Kings")].shape[0])

# print(ipl.columns)

# per=(ipl[ipl["TossWinner"]==ipl["WinningTeam"]].shape[0]/ipl["ID"].shape[0])*100
# print(per,"%")

# mrv=mov[(mov["imdb_rating"]>8) & (mov['imdb_votes']>10000)].shape[0]
# new_df=mov[mrv]
# print(new_df["title_x"])

# am=mov[(mov["genres"]=="Action") & (mov["imdb_rating"]>5)].shape[0]
# new_df=mov[am]
# print(new_df["title_x"])

# mov1=mov["genres"].str.split("|").apply(lambda x:"Action" in x)
# mov1=mov["genres"].str.contains("Action")
# mov2=mov["imdb_rating"]>7.5
# print(mov[mov1&mov2])


# def T1vsT2(Team1,Team2):
#     teams=ipl[(ipl["Team1"]==Team1)&(ipl["Team2"]==Team1)]
#     new_df=ipl[teams]
#     return print(new_df["WinningTeam"])
# T1vsT2("Chennai Super Kings","Mumbai Indians")

# new_col=mov["Industry"]="Bollywood"
# print(mov)

# ipl['ID']=ipl["ID"].astype('int16')
# ipl['Season']=ipl["Season"].astype('category')
# ipl['City']=ipl["City"].astype('category')
# ipl['Date']=ipl["Date"].astype('category')
# ipl['MatchNumber']=ipl["MatchNumber"].astype('category')
# ipl['Team1']=ipl["Team1"].astype('category')
# ipl['Team2']=ipl["Team2"].astype('category')
# ipl['Venue']=ipl["Venue"].astype('category')
# ipl['TossWinner']=ipl["TossWinner"].astype('category')
# ipl['TossDecision']=ipl["TossDecision"].astype('category')
# ipl['SuperOver']=ipl["SuperOver"].astype('category')
# ipl['WinningTeam']=ipl["WinningTeam"].astype('category')
# ipl['WonBy']=ipl["WonBy"].astype('category')
# ipl['Team1Players']=ipl["Team1Players"].astype('category')
# ipl['Team2Players']=ipl["Team2Players"].astype('category')
# ipl['Umpire1']=ipl["Umpire1"].astype('category')
# ipl['Umpire2']=ipl["Umpire2"].astype('category')
# ipl['Player_of_Match']=ipl["Player_of_Match"].astype('category')
# ipl['method']=ipl["method"].astype('category')
# ipl['Margin']=ipl["Margin"].astype('float16')
# print(ipl.info())


# print(ipl[~ipl['MatchNumber'].str.isdigit()]["Player_of_Match"].value_counts())

# ipl["TossDecision"].value_counts().plot(kind="pie")
# plt.show()

# print((ipl["Team1"].value_counts()+ipl["Team2"].value_counts()).sort_values(ascending=False))

# print(mov.sort_values("title_x",ascending=False))
# print(mov.sort_values("wins_nominations",na_position="last"))
# print(mov.sort_values("wins_nominations",na_position="first"))

# print(mov.sort_values(["year_of_release","title_x"],ascending=[True,False]))

# print(mov.sort_index(ascending=False))

# print(mov.set_index("title_x",inplace=True))
# print(mov)
# print(mov.reset_index())

# print(mov.set_index("title_x",inplace=True))
# print(mov.reset_index().set_index("wins_nominations",inplace=True))
# print(mov)

# print(mov.rename(columns={"imdb_id":"imdb","poster_path":"links"}))
# print(mov.set_index("title_x",inplace=True))
# print(mov.rename(index={"Uri: The Surgical Strike":"Uri","The Accidental Prime Minister (film)":"PM"}))
# print(mov.rename(index={"0":"Uri","1":"PM"}))
# x=ipl["Season"].unique()
# print(ipl["Season"].nunique())    nunique doesnt count the null values

# print(ipl[ipl.isnull()])
# print(ipl[ipl.notnull()])
# print(ipl["WinningTeam"].hasnans)
# print(ipl['WinningTeam'].dropna())
# print(ipl['WinningTeam'].dropna(how='any'))  remove the rows even have asingle nan value in a row
# print(ipl.dropna(how='all'))    remove if row have all value==nan
# print(ipl.dropna(subset='City'))    
# print(ipl.dropna(subset=['City','WinningTeam']))
    
# print(mov["wins_nominations"].fillna("unknown"))    
# print(mov["wins_nominations"].fillna("unknown").hasnans)    
# print(mov["wins_nominations"].fillna(method="ffill"))    
# print(mov["wins_nominations"].fillna(method="bfill"))    

marks={
    "name":["mohaimin","sudais","hisham","musawer","ilyas"],
    "iq":[100,90,120,80,80],
    "marks":[80,70,10,70,70],
    "package":[10,7,14,14,14]
}
marks=pd.DataFrame(marks)
# print(marks.duplicated().sum())
# print(marks.drop_duplicates(keep='last'))


# ipl["all_players"]=ipl["Team1Players"]+ipl["Team2Players"]

# def did_kohli_play(PlayerList):
#     return "V Kohli" in PlayerList

# ipl["did_kohli_play"]=ipl['all_players'].apply(did_kohli_play)

# last_match_at_delhi=ipl[(ipl['City']=="Delhi") & (ipl['did_kohli_play']==True)]

# print(last_match_at_delhi.drop_duplicates(subset=["City","did_kohli_play"],keep='first'))


# marks.drop(columns=['iq','package',],inplace=True)
# print(marks)

# marks.set_index("name",inplace=True)
# print(marks.drop(index=['hisham','musawer']))

# temp=pd.Series([23,65,43,98,48,32,84,93,49,23,11,30])

# def sigmoid(value):
#     return 1/1+np.exp(value)
# print(temp.apply(sigmoid)) 

point_df=pd.DataFrame({
    '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
    '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
})
print(point_df)

def euclidean(row):
    pt_A=row['1st point']
    pt_B=row['2nd point']
    return ((pt_A[0]-pt_B[1])**2+(pt_A[1]-pt_B[1])**2)**0.5

point_df['distance']=point_df.apply(euclidean,axis=1)
print(point_df)