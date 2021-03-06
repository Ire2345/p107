import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv("data1.csv")
df=df.loc[df['student_id']=="TRL_987"]

print(df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(
    x=df.groupby("level")["attempt"].mean(),
    y=["level1","level2","level3","level4"], orientation='h'
    
))
fig.show()
