def rank_suit_count(cards):
	rank = {}
	suit = {}
	for i in range(len(cards)):
		if cards[i][0] in rank:
			rank[cards[i][0]] += 1
		else:
			rank[cards[i][0]] = 1
		if cards[i][1] in suit:
			suit[cards[i][1]] += 1
		else:
			suit[cards[i][1]] = 1
	return (rank, suit)