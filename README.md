# superbattleships

I am building a game called "Super Battleships". It follows much of the same rules of normal Battleships.

There are two players, each of whom has 10 ships: 1 battleship (4 squares long), 2 cruisers (3 squares long), 3 destroyers (2 squares long) and 4 frigates (1 square long).

On each player's turn, a board is printed showing their own ships, any hits and misses that have been recorded, and any parts of the other player's ships that are touching their own ships. They are given the option of shooting or moving a ship. Vertically-aligned ships can move up or down, horizontally aligned ships can move left or right. Ships cannot move into a space already occupied.

When all parts of a ship have been hit, the ship can no longer be moved. The game ends when all of one player's ships have been sunk.

There are two play options: the "cheatmode" shows the entire playing board, allowing for easier debugging. Also, ships can be placed either manually (which obviously takes a bit longer) or automatically. Either way, ships will be placed either horizontally or vertically and will not be allowed to overlap one another.

This version of the game is written without using objects and classes so it is quite long. I would like to amend it.
