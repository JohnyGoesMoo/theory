
The script imports the Tkinter library, allowing for the creation of a graphical user interface.

Functions**: Several functions are defined to handle different tasks:
   - `open_text()`: Reads data from a text file and processes it.
   - `start()`: Initializes the canvas by drawing buildings and streets based on the processed data.
import tkinter as tk

def open_text():   text = open("file", 'r', encoding="UTF-8").readlines()  new_text = []     for i in text: #each line
        line = i.strip().split() #remove whispace and split in indiv values  line[0], line[1] = int(line[0]), int(line[1]) #width, height to int  new_text.append(line) #processed line
    return new_text

def start():#start drawing     data = open_text()    # Obtain processed building data  y = 170    # Initial coordinates for drawing x = 20
    ids = []# List to store item IDs of drawn objects on canvas     for i in data:#each building street data if i[1] == 0:#if height 0 canvas.create_line(x, y, x+i[0], y, width=3, fill="green") # Draw a street line
            x += i[0] # Update x-coordinate for next object ids.append('trava') # Append 'trava' to the ids list to skip it later
            continue
        temp = canvas.create_rectangle(x, y, x+i[0], y-i[1], fill="grey")# Draw a building rectangle  x += i[0]  # Update x-coordinate for next object
        ids.append(temp)# Append the item ID to the ids list  return ids

# Event handler for button press
def on_button_press():
    text = entry.get() # Get the maximum height difference specified by the user
    vykresli(int(text))# Call the vykresli function with the maximum height difference as argument
`on_button_press()`: Event handler for the button press event, which triggers the drawing function.
`vykresli()`: Redraws the canvas based on the maximum height difference specified by the user.

The Tkinter window (`root`) is created.

A canvas widget (`canvas`) is created to display buildings and streets.
An entry widget (`entry`) allows the user to input the maximum height difference.
A button widget (`button`) triggers the drawing function when clicked.

The `start()` function is called to draw the initial layout of buildings and streets on the canvas.
def vykresli(max_height):# Function to redraw canvas based on maximum height difference  global ids, red_lines  for i in red_lines:# Delete previously drawn red lines (if any) canvas.delete(i)
        red_lines.pop(0)# Remove the item ID from the red_lines list   for i in range(len(ids) - 1): # Iterate over each pair of adjacent buildings   if ids[i] != "trava" and ids[i+1] != "trava": # Check if both buildings are not streets
            my_building = canvas.coords(ids[i])# Get coordinates of the current building next_building = canvas.coords(ids[i + 1])# Get coordinates of the next building  height_difference = abs(my_building[1] - my_building[3] - next_building[1] + next_building[3]) # Calculate the height difference between the buildings
            if height_difference > max_height:  # If the height difference exceeds the maximum allowed height
                # Draw a red line between the buildings red_lines.append(canvas.create_line(my_building[2], my_building[1], my_building[2], next_building[1], width=5, fill='red'))

#root = tk.Tk() WIDTH = 800 HEIGHT = 200 canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()
# entry widget for user input entry = tk.Entry(root) entry.pack()
# Create button widget to trigger drawing function
button = tk.Button(root, text="vykresli", command=on_button_press)
button.pack()
# Initialize variables
red_lines = []
ids = start()
root.mainloop()



