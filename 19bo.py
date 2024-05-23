This function handles the countdown timer for the game.It checks if the game has ended (`end` is `True`), and if so, it stops the timer.
It decrements the `time` variable by 1 each second and updates the displayed time on the canvas.If the timer reaches zero, it clears the canvas and marks the game as ended.
It calls itself again after 1 second to continue the countdown.
import tkinter as tk
import random

def timer():#countdown     global time, end    if end:  #game has ended, stop the timer return
    time -= 1 #decrease the timer by one second  canvas.itemconfig(clock, text=time)  # update the timer display on the canvas  if time <= 0:  # If the timer reaches zero
        canvas.delete('all')  # Clear the canvas    end = True  # Mark the game as ended    return    canvas.after(1000, timer)  # Call the timer function again after 1 second
This function sets up the initial game UI elements. It creates the game title and instructions text on the canvas.It defines a list of colors for the cables and creates five cable rectangles on the canvas.
It randomly selects one of the cables as the correct cable. It displays the countdown timer on the canvas.It returns the correct cable and the timer display for further use.
This function checks if the user has clicked on the correct cable. It gets the ID of the clicked cable using the `find_overlapping` method.
If the clicked cable matches the correct cable, it displays a winning message. If the clicked cable is incorrect, it clears the canvas.
It marks the game as ended (`end` is set to `True`).

def setup():
    colors = ["green", 'red', 'grey', 'blue', 'orange']  # List of colors for the cables    canvas.create_text(WIDTH // 2, 50, text="Pyrotechnik", anchor='center', fill="blue", font="Arial 30 bold") canvas.create_text(WIDTH // 2, 80, text="oznac spravny kablik", font="Arial 10 bold")
    cables = []  # List to store the cable rectangles     for i in range(len(colors)):  cables.append(canvas.create_rectangle(50, 100 + 10 * i, 300, 100 + 10 * (i + 1), fill=colors[i], tags="cable"))  correct_cable = random.choice(cables)  # Randomly select the correct cable
    clock = canvas.create_text(320, 100, text=time, fill="red", anchor='nw', font="Arial 30 bold")
    print(correct_cable)  # Print the correct cable's ID for debugging   return correct_cable, clock  # Return the correct cable and the timer display
The main application window is created using `tk.Tk()`. The canvas is created with specified width and height, and its background color is set to white. The canvas is added to the main window using the `pack` method. The `end` variable is initialized to `False` to indicate the game is ongoing.
The `time` variable is set to 11 seconds for the countdown.

def check_cable(e): #if correct is clicked     global end     if end:  # If the game has ended, ignore the clicks
        return
    cable = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)[0]  # Get the ID of the clicked cable     if correct_cable == cable:  # If the clicked cable is correct         canvas.create_text(WIDTH // 2, 200, text="VYHRAL SI", font="Arial 30 bold")
    else:
        canvas.delete('all')  # Clear the canvas if the wrong cable is clicked nd = True  # Mark the game as ended

The `setup` function is called to create the initial game UI elements and get the correct cable and timer display.
The `timer` function is called to start the countdown timer. The `tag_bind` method is used to bind the click event on the cables (tagged as "cable") to the `check_cable` function.
The `mainloop` method is called to start the Tkinter event loop, allowing the application to respond to user interactions.
#root = tk.Tk() WIDTH = 500 HEIGHT = 300  canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white") canvas.pack()
# end = False  # Boolean to track if the game has ended time = 11  # Set the initial time for the countdown correct_cable, clock = setup()  # Set up the game UI and get the correct cable and timer display
timer()  # Start the countdown timer canvas.tag_bind("cable", "<Button-1>", check_cable)  # Bind the click event on the cables to the check_cable function

root.mainloop()






