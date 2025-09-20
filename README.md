Cristine Piodo Explanation:

    Functions and Logic
normalize_direction(input_str):

This function takes a string input representing a direction.
It converts the input to lowercase and strips whitespace.
It then checks if the input matches any of the accepted directions:
'n' or 'north' → returns 'N'
's' or 'south' → returns 'S'
'e' or 'east' → returns 'E'
'w' or 'west' → returns 'W'
If the input doesn't match any of these, it returns None.
This function standardizes user input to a single uppercase letter representing the direction.
main():

Initializes the starting position at the origin (0, 0) on the Cartesian plane.
Enters an infinite loop where it:
Prompts the user to enter a direction (N, S, E, W) or STOP to end.
If the user types STOP (case-insensitive), the loop breaks and the program ends.
Otherwise, it normalizes the input using normalize_direction.
If the input is invalid (not a recognized direction), it prints an error message and asks again.
If valid, it updates the coordinates:
'N' increases the y-coordinate by 1 (move up).
'S' decreases the y-coordinate by 1 (move down).
'E' increases the x-coordinate by 1 (move right).
'W' decreases the x-coordinate by 1 (move left).
Prints the current position after each valid move.
After the loop ends, it prints the final position.
It also checks if the final position is back at the origin (0, 0) and prints a message accordingly.
Summary
The program simulates movement on a 2D grid starting at (0, 0).
The user inputs directions to move one step at a time.
The program keeps track of the current position and displays it after each move.
When the user stops, it reports the final position and whether the user returned to the origin.