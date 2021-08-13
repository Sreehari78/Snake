# Snake
Snake game created using python tkinter

# Snake's Body
The body is made up of various segments of 'square shaped turtles'. All of these segments are stored in a list in-order to take account of the collision with the snake's head with any part of its body.

# Snake's Movement
Suppose the snake's body constitutes of 3 blocks of 'square shaped turtles' (head, body, and tail), and when the snake moves the tail block moves to the body block's position from the body to head and the head can move in 3 directions. based on the head block this process continues and I hide this entire concept using screen.update() (screen being my object for Screen() class)and sleep() (which i imported from the package 'time').

# Food
The snake's food keeps randomly appearing in the screen which is implemented using the package random

# Highscore
The highscore is being written into a .txt file which gets updated once the user breaks the previous highscore and dies. This ensures that the highscore to retain its data even after terminating the game
