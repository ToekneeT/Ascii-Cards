# Ascii Cards
A Python script that generates ASCII art playing cards. Can print out multiple cards in one line, allowing for more flexibility with text based card games.
Suits and ranks are adjustable.

Returns a string of playing cards when given a 2D list containing a card's rank and suit.

Due to the cards needing to stay proportional, cards only work when the passed height parameter is an odd number.

## Features
- Displays an ASCII art version of playing cards.
- Supports any single or double character value for rank.
- Supports any single character value for Suits.
- Adjustable size of cards.
- Displays a blank card.

## Requirements
Python 3.x.

## Install
`pip install py-ascii-cards`

## How to use

To display cards.
```
import ascii_cards

print(ascii_cards.display_cards([["A", "♣"]]))

┌─────┐
│A    │
│  ♣  │
│    A│
└─────┘

print(ascii_cards.display_cards([["A", "♠"], ["10", "♥"]]))

┌─────┐ ┌─────┐
│A    │ │10   │
│  ♠  │ │  ♥  │
│    A│ │   10│
└─────┘ └─────┘

```

Can also display a single blank card.
```
print(ascii_cards.display_blank_card())

┌─────┐
│░░░░░│
│░░░░░│
│░░░░░│
└─────┘

```

Can also display a blank card in the `display_cards` function if passed a rank of the value "hidden".

```
print(ascii_cards.display_cards([["2", "♠"], ["hidden", "hidden"], ["8", '♥']]))

┌─────┐ ┌─────┐ ┌─────┐
│2    │ │░░░░░│ │8    │
│  ♠  │ │░░░░░│ │  ♥  │
│    2│ │░░░░░│ │    8│
└─────┘ └─────┘ └─────┘

```

Can adjust the size of the cards by passing it a height after the cards to display. **Important to note** that to stay proportional, the cards will only work if the passed height parameter is an odd number above 5.

```
print(ascii_cards.display_cards([["2", "♠"], ["hidden", "hidden"], ["8", '♥']], 7))

┌───────┐ ┌───────┐ ┌───────┐
│2      │ │░░░░░░░│ │8      │
│       │ │░░░░░░░│ │       │
│   ♠   │ │░░░░░░░│ │   ♥   │
│       │ │░░░░░░░│ │       │
│      2│ │░░░░░░░│ │      8│
└───────┘ └───────┘ └───────┘

```