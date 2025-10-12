### General

Returns a string of playing cards when given a 2D list containing a card's rank and suit.

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