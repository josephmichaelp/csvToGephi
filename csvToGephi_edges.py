import pandas as pd
import numpy as np
import random as rd
print("ID,Source,Target,Weight")
id_edge = 0
df = pd.read_csv ('/Users/User/Downloads/ki_home.1_longest_paths.csv')
for index, value in df["SOLVERS_EDGE_PATH"].items():
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



