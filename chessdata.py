import numpy as np
import pandas as pd
import matplotlib.pyplot as ptl

# Read file csv
_data = pd.read_csv("games.csv")

# Get Column winnner
_winner = list(_data["winner"])

# separate data on winnner
labels = set(_winner)

#Create Array 
sizes = np.array([])

# Get size for some value
for i in labels:
    sizes = np.append(sizes, _winner.count(i))
# Show equal pypolt

# fig, ax = ptl.subplots()
# ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#27d3d9', '#89e06e', '#e6917a'])
# ptl.show()

# ===========================================

_turns = _data["turns"]

_x = sorted(set(_turns))
_y = np.array([])
for i in _x:
    _y = np.append(_y, _x.count(i))

fig, ax = ptl.subplots()
ax.bar(_x, _y , color='#27d3d9')
ptl.show()

