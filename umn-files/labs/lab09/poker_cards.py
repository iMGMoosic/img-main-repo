from playing_cards import *

def poker_hand(cards):
	rank_sequence = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
	rank, suit = rank_suit_count(cards)

	if len(rank) == 5:
		if len(suit) == 1:
			for i in range(len(rank_sequence)):
				card_1 = rank_sequence[i]

				if i + 1 > 12:
					card_2 = rank_sequence[i + 1 - 13]
				else:
					card_2 = rank_sequence[i + 1]

				if i + 2 > 12:
					card_3 = rank_sequence[i + 2 - 13]
				else:
					card_3 = rank_sequence[i + 2]

				if i + 3 > 12:
					card_4 = rank_sequence[i + 3 - 13]
				else:
					card_4 = rank_sequence[i + 3]

				if i + 4 > 12:
					card_5 = rank_sequence[i + 4 - 13]
				else:
					card_5 = rank_sequence[i + 4]

				if card_1 in rank and card_2 in rank and card_3 in rank and card_4 in rank and card_5 in rank:
					return "Straight Flush"
			return "Flush"
		else:
			for i in range(len(rank_sequence)):
				card_1 = rank_sequence[i]

				if i + 1 > 12:
					card_2 = rank_sequence[i + 1 - 13]
				else:
					card_2 = rank_sequence[i + 1]

				if i + 2 > 12:
					card_3 = rank_sequence[i + 2 - 13]
				else:
					card_3 = rank_sequence[i + 2]

				if i + 3 > 12:
					card_4 = rank_sequence[i + 3 - 13]
				else:
					card_4 = rank_sequence[i + 3]

				if i + 4 > 12:
					card_5 = rank_sequence[i + 4 - 13]
				else:
					card_5 = rank_sequence[i + 4]

				if card_1 in rank and card_2 in rank and card_3 in rank and card_4 in rank and card_5 in rank:
					return "Straight"
			return "High Card"
	elif len(rank) == 4:
		return "One Pair"
	elif len(rank) == 3:
		for key in rank:
			if rank[key] == 2:
				return "Two Pair"
			if rank[key] == 3:
				return "Three-Of-A-Kind"
	else:
		for key in rank:
			if rank[key] == 4:
				return "Four-Of-A-Kind"
			if rank[key] == 2 or rank[key] == 3:
				return "Full House"
