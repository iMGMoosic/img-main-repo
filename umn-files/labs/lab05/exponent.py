def expo(x, y):
	add_x = x
	new_x = x
	for i in range(0, y - 1):
		for j in range(0, x - 1):
			new_x += add_x
		add_x = new_x

	return new_x
