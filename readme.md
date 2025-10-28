# Ascii Cards
A Python script that generates ASCII art playing cards. Can print out multiple cards in one line, allowing for more flexibility with text based card games.
Suits and ranks are adjustable.

Returns a string of playing cards when given a 2D list containing a card's rank and suit.

## Features
- Displays an ASCII art version of playing cards.
- Supports any single or double character value for rank.
- Supports any single character value for Suits.

## Requirements
Python 3.x.

## Install
`pip install ascii-cards`

## How to use

To display cards.
```
display_cards([["A", "♣"]])

┌-----┐
|A    |
|  ♣  |
|    A|
└-----┘

display_cards([["A", "♠"], ["10", "♥"]])

┌-----┐ ┌-----┐
|A    | |10   |
|  ♠  | |  ♥  |
|    A| |   10|
└-----┘ └-----┘

```

Can also display a single blank card.
```
display_blank_card()

┌─────┐
│░░░░░│
│░░░░░│
│░░░░░│
└─────┘

```

Can also display a blank card in the `display_cards` function if passed a rank of the value "hidden".

```
display_cards([["2", "♠"], ["hidden", "hidden"], ["8", '♥']])

┌-----┐ ┌-----┐ ┌-----┐
|2    | |░░░░░| |8    |
|  ♠  | |░░░░░| |  ♥  |
|    2| |░░░░░| |    8|
└-----┘ └-----┘ └-----┘

```