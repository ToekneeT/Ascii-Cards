# Rethink size, needs to be something that makes sense
# consistently able to math it
# for example width of card edge to edge.
# Possibly making it so that the size is vertical lines.
# Minimum being 5, which makes it a 7x5, smallest that looks normal.

# Given as Rank, Suit
def display_cards(cards: list[[str, str]], height = 5):
	# Length should typically be two higher than the height in order to keep a 
	# proportionate looking playing card.
	# Given that the suit needs to be in the middle of the card, making the height an even number severely breaks the ascii.
	length = height + 2
	top: str = f"┌{"─"*(length-2)}┐"
	bottom: str = f"└{"─"*(length-2)}┘"
	side: str = f"│{" "*(length-2)}│"

	# Needs an even amount of characters on the left and the right.
	# Always has an extra character on the left and right due to the side of the card.

	# Loop that increments by 2, starting at 7, each increment adds 1 to the amount of spaces that gets added on each side?

	suit_line_spacing = 2
	for _ in range(7, length, 2):
		suit_line_spacing += 1

	extra_vertical = 0
	for _ in range(5, height, 2):
		extra_vertical += 1

	suit_line_left: str = f"│{" "*(suit_line_spacing)}"
	suit_line_right: str = f"{" "*(suit_line_spacing)}│"

	left_rank_left: str = f"│"
	left_rank_right: str = f"{" "*(length-4)}│"
	right_rank_left: str = f"│{" "*(length-3)}"
	right_rank_right: str = f"│"
	hidden_side: str = f"│{"░"*(length-2)}│"

	result_str: str = ""

	# Top of the card.
	for _ in range(len(cards)):
		result_str += f"{top} "

	result_str += "\n"

	# Rank of the card on the top left side.
	for idx in range(len(cards)):
		if cards[idx][0] == "hidden":
			result_str += hidden_side
		elif cards[idx][0] == "10":  # Ten is the only rank with two digits
			result_str += f"│{cards[idx][0]}{left_rank_right}"
		else:
			result_str += f"{left_rank_left}{cards[idx][0]} {left_rank_right}"
		result_str += " "

	result_str += "\n"

	if height > 5:
		for _ in range(extra_vertical):
			for idx in range(len(cards)):
				if cards[idx][0] == "hidden":
					result_str += hidden_side
				else:
					result_str += side
				result_str += " "
			
			result_str += "\n"

	# Suit of the card in the middle.
	for idx in range(len(cards)):
		if cards[idx][0] == "hidden":
			result_str += hidden_side
		else:
			result_str += f"{suit_line_left}{cards[idx][1]}{suit_line_right}"
		result_str += " "

	result_str += "\n"

	if height > 5:
		for _ in range(extra_vertical):
			for idx in range(len(cards)):
				if cards[idx][0] == "hidden":
					result_str += hidden_side
				else:
					result_str += side
				result_str += " "
			
			result_str += "\n"

	# Rank of the card on the bottom right side.
	for idx in range(len(cards)):
		if cards[idx][0] == "hidden":
			result_str += hidden_side
		elif cards[idx][0] == "10":
			result_str += f"{right_rank_left[:len(right_rank_left)-1]}{cards[idx][0]}{right_rank_right}"
		else:
			result_str += f"{right_rank_left}{cards[idx][0]}{right_rank_right}"
		result_str += " "

	result_str += "\n"

	# Bottom of the card
	for _ in range(len(cards)):
		result_str += f"{bottom} "

	result_str += "\n"

	return result_str


def display_blank_card(height = 5):
	length = height + 2
	top: str = f"┌{"─"*(length-2)}┐"
	bottom: str = f"└{"─"*(length-2)}┘"
	side: str = f"│{" "*(length-2)}│"

	# Needs an even amount of characters on the left and the right.
	# Always has an extra character on the left and right due to the side of the card.

	# Loop that increments by 2, starting at 7, each increment adds 1 to the amount of spaces that gets added on each side?

	suit_line_spacing = 2
	for _ in range(7, length, 2):
		suit_line_spacing += 1

	extra_vertical = 0
	for _ in range(5, height, 2):
		extra_vertical += 1

	hidden_side: str = f"│{"░"*(length-2)}│"

	result_str: str = ""

	# Top of the card.
	result_str += f"{top} "
	result_str += "\n"
	result_str += hidden_side
	result_str += "\n"

	# If the height is larger than 5, needs to add more of lines.
	if height > 5:
		for _ in range(extra_vertical):
			result_str += hidden_side
			result_str += "\n"

	result_str += hidden_side
	result_str += "\n"

	if height > 5:
		for _ in range(extra_vertical):
			result_str += hidden_side
			result_str += "\n"

	result_str += hidden_side
	result_str += "\n"
	result_str += f"{bottom} "
	result_str += "\n"

	return result_str


def main():
	deck = [["A", "♤"], ["10", "♤"], ["8", '♡'], ["2", "♧"], ["4", "♢"], ["T", "♢"], ["hidden", "hidden"]]
	print("Multiple Cards: ")
	print(display_cards(deck))
	print("Single blank: ")
	print(display_blank_card())
	print(display_blank_card(7))
	print(display_blank_card(9))
	print(display_blank_card(11))
	print(display_cards(deck, 7))
	print(display_cards(deck, 9))
	print(display_cards(deck, 11))

	print(display_cards([["A", "♤"]]))
	print(display_cards([["A", "♠"], ["10", "♥"]]))
	print(display_cards([["2", "♠"], ["hidden", "hidden"], ["8", '♥']]))


if __name__ == "__main__":
	main()