import pandas as pd

data={
    'Name':['johnn','Alice','Bob'],
      'Age':[25,30,34],
      'city':['New York','London','Paris']
}
df=pd.DataFrame(data)
print(df)