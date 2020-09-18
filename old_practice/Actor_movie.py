# Import pandas package
import pandas as pd
data = pd.read_csv("data.csv")
df = pd.DataFrame(data)
print(df.sort_values("Actor", axis = 0, ascending = True, nplace = True, na_position ='last'))
df
unidf = (df.Actor.unique())
unidf[0]
unidf[1]
unidf[2]
