import pandas as pd
import plotly.express as px

myfile = "data.csv"
df = pd.read_csv(myfile)
fig = px.scatter(df,x = "date",y = "cases",color = "country")
fig.show()