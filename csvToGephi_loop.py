import pandas as pd
import numpy as np
import random as rd
print("Id,Source,Target,Weight")
id_edge = 0
df = pd.read_csv ('/Users/User/Downloads/ki_home.5_loops_2_5.csv')
for index, value in df["LOOP"].items():
	arr = value.split(',')
	i = 0
	for item in arr:
		node = item.strip()
		if i == 0:
			last_node = node
		else:
			print("{},{},{},{}".format(id_edge, last_node, node, 1))
			last_node = node
		i = i + 1
		id_edge = id_edge + 1