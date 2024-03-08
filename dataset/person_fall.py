import pandas as pd
import numpy as np

N=21

df = pd.DataFrame({
   #'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   #'x': np.linspace(0,stop=N-1,num=N),
   #'y': np.random.rand(N),
   #'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   #'D': np.random.normal(100, 10, size=(N)).tolist()
   'Counter': np.linspace(0,stop=N-1,num=N),
   'In_time': pd.date_range(start='2023-04-23 00:09:00', end='2023-04-23 00:50:00', freq='2T'),
   'Elapsed_time':np.random.normal(20,5,size=(N)).tolist()

})
print(df)

N=28
df1 = pd.DataFrame({
   #'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   #'x': np.linspace(0,stop=N-1,num=N),
   #'y': np.random.rand(N),
   #'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   #'D': np.random.normal(100, 10, size=(N)).tolist()
   'Counter': np.linspace(20,stop=N-1,num=9),
   'In_time': pd.date_range(start='2023-04-23 00:09:00', end='2023-04-23 00:50',freq='5T'),
   'Elapsed_time':np.random.normal(20,5,size=9).tolist()
})
df=df.append(df1)
df['Counter']=df['Counter'].astype(int)
df['Elapsed_time']=df['Elapsed_time'].astype(int)  
  
df = df.reset_index(drop=True)
print(df)
#print()
#reindex the DataFrame
#df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
#print(df_reindexed)
df.to_csv('person_fall.csv', index=False)
