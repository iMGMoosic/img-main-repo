def sieve(n):
	lst = []
	prime_lst = []
	p = 2

	for i in range(n + 1):
		lst.append(i)

	lst[0] = False
	lst[1] = False

	while (p * p <= n):
		if lst[p] == True:
			for i in range(p ** 2, n + 1, p):
				lst[i] = False
		p += 1

	for p in range(n + 1):
		if lst[p]:
			prime_lst.append(p)

	return prime_lst
