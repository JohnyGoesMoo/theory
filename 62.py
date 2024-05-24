import tkinter as tk
`tkinter` is imported to create the graphical user interface (GUI).

Flips the image horizontally by moving each '1' pixel to its new position.
The `canvas.coords(i)[0]` function retrieves the current x-coordinate of the pixel, and the calculation `(WIDTH // 2 - canvas.coords(i)[0]) * 2` determines the distance to move the pixel horizontally to flip it.

Draws the image on the canvas by creating rectangles for each '1' pixel.
The `canvas.create_rectangle` function is used to draw a black rectangle at the calculated position.
def horizon(): #horizontal flip    for i in range(1, count_jedn + 1):  # through each pix  x = (WIDTH // 2 - canvas.coords(i)[0]) * 2  # horizontal distance to flip pix
        canvas.move(i, x, 0)  # move pixel to new pos

# draw the image def draw():  for y in range(len(pixels)):  # each row for x in range(0, len(pixels[y]), 2):  # each pix in row, step by 2
            if pixels[y][x] == '1':  # if pix=1  # black rext in cores pos canvas.create_rectangle( x // 2 * str, y * str, x // 2 * str + str, y * str + str,fill="black"
                )

# count 1 pixs on page def ones():  counter = 0  # Initialize a counter for i in pixels:  # each row for j in i:  # each pix in row if j == '1':  # if pix=1 counter += 1
    return counter  # num of 1 pix
Counts the number of '1' pixels in the image.
Loops through each row and each pixel in the row, incrementing the counter for each '1' pixel.

Initializes the main tkinter window.
Reads the image dimensions (width and height) from the file.
Defines the size of each pixel (`str`).
Creates a canvas widget with the calculated width and height and adds it to the main window.
root = tk.Tk()
fr = open("file.txt", 'r', encoding="UTF-8") WIDTH, HEIGHT = fr.readline().strip().split()  # Read the width and height of the image str = 4  # def size of each pix WIDTH, HEIGHT = int(WIDTH) * str, int(HEIGHT) * str  #calc canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT) canvas.pack()

# Read the pixel data from the file and strip any whitespace pixels = fr.readlines() pixels = [i.strip() for i in pixels]
#number of pixels in the image print("pocet pixelov:", WIDTH // str * HEIGHT // str)
# Count and print the number of '1' pixels in the image count_jedn = ones() print("count ones:", count_jedn)
Reads the pixel data from the file and strips any whitespace.
Prints the total number of pixels and the number of '1' pixels in the image.
Creates a button to flip the image and adds it to the main window.
Draws the initial image on the canvas.
Starts the main loop of the tkinter application to display the window.

This step-by-step explanation simplifies the code's functionality for easier understanding.
# button to flip the image button = tk.Button(root, text="reverse", command=horizon) button.pack()

# initial image
draw()





