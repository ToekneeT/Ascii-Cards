import unittest
from ascii_cards import ascii_cards


class TestDisplayCards(unittest.TestCase):
	def test_display_cards_10(self):
		expected = "┌─────┐ \n│10   │ \n│  ♤  │ \n│   10│ \n└─────┘ \n"
		self.assertEqual(ascii_cards.display_cards([["10", "♤"]]), expected)

	def test_display_cards(self):
		expected = "┌─────┐ \n│A    │ \n│  ♤  │ \n│    A│ \n└─────┘ \n"
		self.assertEqual(ascii_cards.display_cards([["A", "♤"]]), expected)

	def test_blank_card(self):
		expected = "┌─────┐ \n│░░░░░│\n│░░░░░│\n│░░░░░│\n└─────┘ \n"
		self.assertEqual(ascii_cards.display_blank_card(), expected)

	def test_display_cards_with_hidden(self):
		expected = "┌─────┐ ┌─────┐ \n│A    │ │░░░░░│ \n│  ♤  │ │░░░░░│ \n│    A│ │░░░░░│ \n└─────┘ └─────┘ \n"
		self.assertEqual(ascii_cards.display_cards([["A", "♤"], ["hidden", "hidden"]]), expected)

	def test_display_cards_7_height(self):
		expected = "┌───────┐ ┌───────┐ \n│A      │ │10     │ \n│       │ │       │ \n│   ♤   │ │   ♡   │ \n│       │ │       │ \n│      A│ │     10│ \n└───────┘ └───────┘ \n"
		self.assertEqual(ascii_cards.display_cards([["A", "♤"], ["10", "♡"]], 7), expected)


if __name__ == "__main__":
	unittest.main()