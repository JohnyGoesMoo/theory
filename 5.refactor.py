`tkinter` for creating the graphical user interface (GUI).

Formats the input text into lines of notes, each line containing a fixed number of notes (`ALLinONE`).
If there are any remaining notes after forming complete lines, they are added as the last line.

Draws a muse staff with 5 horizontal lines at a specified y-coordinate on the canvas.

import tkinter as tk
Draws ovals representing musical n at specified positions on the staff.
The positions are calculated based on n and its index in the line.


def refactor(text):
    new_txt = []  # init empty list to hold lines  line = []  # init empty list to hold number of n
    for i in text:
        line.append(i)  # add current n to current line  if len(line) >= ALLinONE:  # if the current line has reached the maximum number of ns  new_txt.append(line)  # add current n to formatted text line = []  # reset current line
    if len(line) != 0:  # if there is anything remaining new_txt.append(line)  # add remaining as the last line  return new_txt

# create horizontal line to put n on def lines(y): for i in range(1, 6):  # loop to do 5 times canvas.create_line(0, y + nh * i, w, y + nh * i)

# put n onto lines with y coord
def n(y, notes): for x, note in enumerate(notes):  # through each note in current line  canvas.create_oval(
            (x + 1) * nw + x * nw // 2,  # x- left of oval  y + notes_as_number[note] * nh // 2,  # y-c top oval (x + 2) * nw + x * nw // 2,  # x-right oval y + notes_as_number[note] * nh // 2 + nh  # y-bottom oval
        )

text = open("file.txt", 'r', encoding="UTF-8").read()
root = tk.Tk()
Reads the input notes from the file `file.txt`.
Initializes the main tkinter window and the canvas with specified dimensions.
Formats the input text into lines of notes.
nw = 20  # Width nh = 10  # Height ALLinONE = 19  # Number of n in one line w = (ALLinONE + 1) * nw * 3 // 2  osh = 7 * nh h = 4 * osh

canvas = tk.Canvas(root, width=w, height=h)
canvas.pack()
Creates a dictionary to map each note to its position on the staff.
Draws the staves and inserts notes for each line of formatted text.
Starts the main loop of the tkinter application to display the window.


# Format the text into lines of notes text = refactor(text) # dictionary to map each n to a number (position on the staff) n_descending = 'hagfedc'  # descending order
n_as_number = {n_descending[i]: i for i in range(len(n_descending))}

#for each line of formatted text for i in range(len(text)):     lines(i * osh)  # lines at the current y-coordinate  n(i * osh + osh // 2 - nh, text[i])  # Insert n at the current y-coordinate

root.mainloop()




