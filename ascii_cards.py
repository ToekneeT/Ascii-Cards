# Rethink size, needs to be something that makes sense
# consistently able to math it
# for example width of card edge to edge.
def display_cards(cards: list[[str, str]]):
	top: str = f"┌{"-"*(5)}┐"
	bottom: str = f"└{"-"*(5)}┘"
	side: str = f"│{" "*(2)}│"

	suit_line_left: str = f"|{" "*(2)}"
	suit_line_right: str = f"{" "*(2)}|"
	left_rank_left: str = f"|"
	left_rank_right: str = f"{" "*(3)}|"
	right_rank_left: str = f"|{" "*(4)}"
	right_rank_right: str = f"|"
	hidden_side: str = f"|{"░"*(5)}|"

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
			result_str += f"|{cards[idx][0]}{left_rank_right}"
		else:
			result_str += f"{left_rank_left}{cards[idx][0]} {left_rank_right}"
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


def display_blank_card():
	top: str = "┌─────┐"
	bottom: str = "└─────┘"
	side: str = "│░░░░░│"
	return f"{top}\n{side}\n{side}\n{side}\n{bottom}"


def main():
	deck = [["A", "♤"], ["10", "♤"], ["8", '♡'], ["2", "♧"], ["4", "♢"], ["T", "♢"], ["hidden", "hidden"]]
	print("Multiple Cards: ")
	print(display_cards(deck))
	print("Single blank: ")
	print(display_blank_card())


if __name__ == "__main__":
	main()