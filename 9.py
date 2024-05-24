draw_original_image()`: This function reads image data from a file and draws rectangles on the canvas to represent the original image.
draw_negative_image()`: This function clears the canvas, reads the image data again, and draws rectangles with inverted colors to represent the negative of the image.
the script opens the image file  in read mode and reads the dimensions of the image.

import tkinter as tk

def draw():
    color = ["black", "white"] #def drawing colors     y = 0      for i in obrazok: #each element x = 0  line = i.split(' ')  # split into individual elements
        for j in line: # Draw rectangles based on the element values   for k in range(int(j)): canvas.create_rectangle(x, y, x, y, fill=color[0], outline=color[0])
                x += 1  # Move to the next column  color = [color[1], color[0]]  # Swap colors for the next iteration
        y += 1  # Move to the next row
The Tkinter window (`root`) is initialized using `tk.Tk()`. This creates the main window for the application.
A canvas widget (`canvas`) is created within the Tkinter window to display the image. The dimensions of the canvas are set based on the dimensions of the image read from the file.
A button widget (`button`) is created within the Tkinter window. This button is used to trigger the drawing of the negative image when clicked.

def negative():
    canvas.delete('all')  # Clear the canvas obrazok.seek(0)  # Reset the file pointer to the beginning obrazok.readline()  # Skip the first line (image dimensions)  color = ["white", "black"]  # Start with white color for fill
    y = 0    # Loop through each line of the image data  for i in obrazok: x = 0 line = i.split(' ')  # Split the line into individual elements
        # Loop through each element in the line for j in line:    # Draw rectangles based on the element values for k in range(int(j)):
                canvas.create_rectangle(x, y, x, y, fill=color[0], outline=color[0])
                x += 1  # Move to the next column color = [color[1], color[0]]  # Swap colors for the next iteration y += 1  # Move to the next row

# Open the image file and read its dimensions obrazok = open("file.txt", 'r', encoding="UTF-8") dimensions = obrazok.readline().strip().split()
WIDTH, HEIGHT = int(dimensions[0]), int(dimensions[1])

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
button = tk.Button(root, text="negativ", command=negative)
button.pack()
The `draw_original_image()` function is called to draw the original image on the canvas. This function reads the image data from the file and draws rectangles on the canvas based on the pixel values.
Event handlers are defined for the button: When the button is clicked, the `draw_negative_image()` function is called to draw the negative image.
Finally, the Tkinter event loop (`root.mainloop()`) is started. This loop listens for events such as button clicks and updates the GUI accordingly. It keeps the application running until the user closes the window or exits the program.

draw()
root.mainloop()




