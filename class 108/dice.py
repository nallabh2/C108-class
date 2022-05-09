import random
import plotly.express as px
import plotly.figure_factory as ff

diceResults=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResults.append(dice1+dice2)

fig = ff.create_distplot([diceResults],["result"],show_hist=False)
fig.show()