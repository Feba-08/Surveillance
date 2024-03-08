import pandas as pd
import numpy as np
df  = pd.DataFrame()
N=2
"""
df1 = pd.DataFrame({
   #'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   #'x': np.linspace(0,stop=N-1,num=N),
   #'y': np.random.rand(N),
   #'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   #'D': np.random.normal(100, 10, size=(N)).tolist()
   #'Counter': np.linspace(0,stop=N-1,num=N),
   'In_time': pd.date_range(start='2023-04-23 09:00:00', end='2023-04-23 10:00:00', freq='2T'),
   'Gender':  np.random.choice(['Abhin','Geo'],N).tolist()

})
df1= df1.sample(n = 2).drop_duplicates()
#print(df)"""
for i in range(11):
   df[i] = pd.DataFrame({
   #'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   #'x': np.linspace(0,stop=N-1,num=N),
   #'y': np.random.rand(N),
   #'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   #'D': np.random.normal(100, 10, size=(N)).tolist()
   #'Counter': np.linspace(0,stop=N-1,num=N),
   #'In_time': pd.date_range(start='2023-04-23 09:00:00', end='2023-04-23 10:00:00', freq='2T'),
   'Gender':  np.random.choice(['Abhin','Geo'],N).tolist()

   })
   df[i]= df[i].sample(n = 2).drop_duplicates()
   #df = df.append(df[i],ignore_index=True) 
   #df.join(df[i])
   
   #df = df.append(df[i], ignore_index = True).dropna()
   df=pd.concat(df,df[i],axis=0)
   
"""
N=28
df1 = pd.DataFrame({
   #'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   #'x': np.linspace(0,stop=N-1,num=N),
   #'y': np.random.rand(N),
   #'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   #'D': np.random.normal(100, 10, size=(N)).tolist()
   'Counter': np.linspace(20,stop=N-1,num=9),
   'In_time': pd.date_range(start='2023-04-23 00:09:00', end='2023-04-23 00:50',freq='5T'),
   'Gender':np.random.choice(['Abhin','Geo'],9).tolist()
})
df=df.append(df1)
df['Counter']=df['Counter'].astype(int)
#df['Gender']=df['Elapsed_time'].astype(int)  
""" 
df = df.reset_index(drop=True)
print(df)
#print()
#reindex the DataFrame
#df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
#print(df_reindexed)
df.to_csv('person_face_attendence.csv', index=False)
