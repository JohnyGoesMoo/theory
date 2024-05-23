The end variable is initialized to False to indicate the game is ongoing.
The time variable is set to 11 seconds for the countdown.
Setting Up the Game UI:

import tkinter as tk
import random

def lodicka(x, y): #draw boats position     # Generate a random number between -3 and 3 to simulate waves
    plachta = random.randint(-3, 3)    # Draw the boat using lines and a polygon on the canvas canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

def setup():    for i in range(15):# Draw boats at fixed x position and incrementing y position        lodicka(20, i * 40 + 40)        # Store boat IDs in a list for later referencelode.append(1 + 2 * i)
    # Draw a red line as a separator    canvas.create_line(650, 0, 650, 800, fill='red')

# Start the game when the left mouse button is clicked def start(e):    global starter    if starter:        mover()        starter = False
The setup function is called to create the initial game UI elements and get the correct cable and timer display.
Starting the Countdown Timer:The timer function is called to start the countdown timer.inding Events:The tag_bind method is used to bind the click event on the cables (tagged as "cable") to the check_cable function.
Starting the Tkinter Main Loop:
# Move the boats and check for collisions def mover():    global first, counter    for i, j in enumerate(lode):
        # Get the current coordinates of the boat        line_coord = canvas.coords(j) # Generate a random move between 1 and 10 move = random.randint(1, 10)
        # Delete the boat and its wake        canvas.delete(j)        canvas.delete(j+1)
        # Draw a new boat at the updated position  lodicka(line_coord[0] + move, line_coord[1])
        # Move the boat's ID in the list  if first:  lode[i] += 31   else:            lode[i] += 30 # Check if any boats have reached the finish line if len(canvas.find_overlapping(650, 0, 650, 800)) > 1:
            # Calculate the winning boat and store it     winner.append((j - 30 * counter - 1)//2 + 1) # If any boat reaches the finish line, display the winner
        if len(canvas.find_overlapping(700, 0, 700, 800)):  canvas.create_text(350, 400, text='Vyhrala lodicka: ' + str(winner[0]), font=('Helvetica', '30', 'bold'), fill='red', anchor=tk.CENTER)
            return
    # Increment the counter and continue moving boats first = False
    counter += 1 # Call mover() again after 100 milliseconds  canvas.after(100, mover)

his function checks if the user has clicked on the correct cable.It gets the ID of the clicked cable using the find_overlapping method.
If the clicked cable matches the correct cable, it displays a winning message.If the clicked cable is incorrect, it clears the canvas.It marks the game as ended (end is set to True).Setting Up the Main Application Window:

root = tk.Tk()
canvas = tk.Canvas(root, width=700, height=800)
canvas.pack()

The main application window is created using tk.Tk().The canvas is created with specified width and height, and its background color is set to white.
The canvas is added to the main window using the pack method.Initializing Game Variables:

#lode = []  winner = []  first = True starter = True  counter = 0  setup() # Bind the left mouse button click event to the start function
canvas.bind('<Button-1>', start) # Start the tkinter event loop root.mainloop()






The mainloop method is called to start the Tkinter event loop, allowing the application to respond to user interactions.
