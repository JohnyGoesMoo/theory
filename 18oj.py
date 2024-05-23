This function is called when a rectangle representing a food item is clicked.
It uses the `find_overlapping` method to determine which rectangle was clicked based on the click coordinates `(e.x, e.y)`.
The `jedlo_id` is derived from the clicked rectangle's ID. import tkinter as tk

def zapis_obed(e): #selection when clicked jedlo_id = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)[0] - 1#what was clickedjedla = ["z", "c", "m", "o"] #idetifiers objednavka = str(entry.get()) + ' ' + jedla[jedlo_id] + '\n'# Create the order string with the student code and selected food identifier
    objednavky.write(objednavka)# Write the order to the file print(objednavka)
It maps the `jedlo_id` to a corresponding food identifier from the `jedla` list (`z`, `c`, `m`, `o`).
It constructs an order string containing the student's code (from the entry widget) and the selected food identifier.
This order string is written to the `objednavky` file and printed to the console.

def setup(): #gui     color = ["green", "red", "blue", "orange"]    for i in range(4):canvas.create_rectangle(100 * i, 100, 100 * (i + 1), 200, fill=color[i], tags="jedlo") # rectangle=food  canvas.create_text(WIDTH // 2, 50, text="VYBER JEDLA", font="Arial 40 bold", fill="red")objednavky = open("maturita/18/vyber_jedla.txt", 'w', encoding="UTF-8")# Open a file to save the orders
root = tk.Tk()This function sets up the initial UI elements on the canvas.
It defines a list of colors for the food rectangles (`green`, `red`, `blue`, `orange`).
It creates four rectangles on the canvas, each representing a different food item, using the `create_rectangle` method.
It adds a title text "VYBER JEDLA" at the top of the canvas using the `create_text` method.
# WIDTH = 400 HEIGHT = 230  canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white") canvas.pack()
#label = tk.Label(root, text="kod studenta") label.pack() entry = tk.Entry(root) entry.pack() setup() canvas.tag_bind("jedlo", "<Button-1>", zapis_obed) root.mainloop()

The `objednavky` file is opened in write mode (`'w'`) to save the food orders. The file is named
The main application window is created using `tk.Tk()`.
The canvas is created with specified width and height, and its background color is set to white.
The canvas is added to the main window using the `pack` method.





