import random

def matrix(n, init):
	new_lst = []
	new_sublst = []

	for i in range(n):
		new_sublst.append(init)

	for i in range(n):
		new_lst.append(new_sublst)

	return new_lst

def order(m):
	row_num = len(m)
	column_num = len(m[0])

	final = str(row_num) + " rows and " + str(column_num) + " columns."

	return final

def identity(n):
	new_lst = []
	new_sublst = []
	for i in range(n):
		new_lst.append(new_sublst)
		for j in range(n):
			if i == j:
				new_lst[i].append(1)
			else:
				new_lst[i].append(0)
		new_sublst = []

	return new_lst

def populate(mtrx, n, value):
	matrix_elements = len(mtrx) * len(mtrx)

	for i in range(0, n):
		index = random.randint(0, matrix_elements - 1)

		if index > len(mtrx) - 1:
			main_index = index // len(mtrx)
			sub_index = index % len(mtrx)

		else:
			main_index = 0
			sub_index = index

		mtrx[main_index][sub_index] = value

	return mtrx

def dist(lst1, lst2):
	distance = (((lst2[0] - lst1[0]) ** 2) + ((lst2[1] - lst1[1]) ** 2)) ** 0.5
	return distance

def shortest_dist(lst):
	shortest_distance = 0
	for i in range(0, len(lst)):
		for j in range(1, len(lst)):
			if i == j:
				shortest_distance = shortest_distance
			elif shortest_distance > dist(lst[i], lst[j]) or shortest_distance == 0:
				shortest_distance = dist(lst[i], lst[j])
	return shortest_distance

def neighbors(mtrx, r, c):
	current_cell = mtrx[r - 1][c - 1]

	cell1 = mtrx[r - 2][c - 2]
	if r - 2 not in range(0, len(mtrx)) or c - 2 not in range(0, len(mtrx[r])):
		cell1 = 0
	elif mtrx[r - 2][c - 2] == 1:
		cell1 = 1

	cell2 = mtrx[r - 2][c - 1]
	if r - 2 not in range(0, len(mtrx)) or c - 1 not in range(0, len(mtrx[r])):
		cell2 = 0
	elif mtrx[r - 2][c - 1] == 1:
		cell2 = 1

	cell3 = mtrx[r - 2][c]
	if r - 2 not in range(0, len(mtrx)) or c not in range(0, len(mtrx[r])):
		cell3 = 0
	elif mtrx[r - 2][c] == 1:
		cell3 = 1

	cell4 = mtrx[r - 1][c - 2]
	if r - 1 not in range(0, len(mtrx)) or c - 2 not in range(0, len(mtrx[r])):
		cell4 = 0
	elif mtrx[r - 1][c - 2] == 1:
		cell4 = 1

	cell6 = mtrx[r - 1][c]
	if r - 1 not in range(0, len(mtrx)) or c not in range(0, len(mtrx[r])):
		cell6 = 0
	elif mtrx[r - 1][c] == 1:
		cell6 = 1

	cell7 = mtrx[r][c - 2]
	if r not in range(0, len(mtrx)) or c - 2 not in range(0, len(mtrx[r])):
		cell7 = 0
	elif mtrx[r][c - 2] == 1:
		cell7 = 1

	cell8 = mtrx[r][c - 1]
	if r not in range(0, len(mtrx)) or c - 1 not in range(0, len(mtrx[r])):
		cell8 = 0
	elif mtrx[r][c - 1] == 1:
		cell8 = 1

	cell9 = mtrx[r][c]
	if r not in range(0, len(mtrx)) or c not in range(0, len(mtrx[r])):
		cell9 = 0
	elif mtrx[r][c] == 1:
		cell9 = 1

	neighbor_count = cell1 + cell2 + cell3 + cell4 + cell6 + cell7 + cell8 + cell9
	return neighbor_count

def update(mtrx):
	for i in range(0,len(mtrx)):
		for j in range(0, len(mtrx)):
			neighbor_count = neighbors(mtrx, i, j)
			if neighbor_count < 2 and mtrx[i][j] == 1:
				mtrx[i][j] = 0
			elif neighbor_count >= 2 and neighbor_count < 4 and mtrx[i][j] == 1:
				mtrx[i][j] = 1
			elif neighbor_count > 3 and mtrx[i][j] == 1:
				mtrx[i][j] = 0
			elif neighbor_count == 3 and mtrx[i][j] == 0:
				mtrx[i][j] = 1
	return mtrx

def life():
	mtrx = []
	sub_mtrx = []
	for i in range(0, 100):
		for j in range(0, 100):
			sub_mtrx.append(0)
		mtrx.append(sub_mtrx)
		sub_mtrx = []
	amount = int(random.randint(1, 10000))
	populate(mtrx, amount, 1)
	for i in range(0, 50):
		print("", flush=True)
		print(*mtrx,sep='\n')
		update(mtrx)
