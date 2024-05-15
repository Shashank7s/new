import pandas as pd

data={
    'Name':['Jai','Princi','Gaurav','Anuj'],
    'Height':[5.1,6.2,5.1,5.2],
    'Qualification':['Msc','MA','Msc','Msc']
}
df=pd.DataFrame(data)
df.insert(2,"Age",[21,23,24,21],True)
print(df)