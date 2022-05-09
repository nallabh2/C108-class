import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

data = pd.read_csv("data.csv")

fig=ff.create_distplot([data["Height(Inches)"].to_list()],["Height"],show_hist=False)
fig.show()

fig2=ff.create_distplot([data["Weight(Pounds)"].to_list()],["Weight"],show_hist=False)
fig2.show()