This function takes a line (`riadok`) from the image file as input and compresses it using run-length encoding.
It initializes a list `body` with characters '0' and '1' to alternate between them, an index `i` to traverse the line, a `count` to count consecutive characters, and `new_riadok` to store the compressed line.
It uses a while loop to traverse the line. Inside this loop, it counts the consecutive occurrences of the current character (either '0' or '1').
When a different character is encountered, it appends the count to `new_riadok`, resets the count, increments the index, and swaps the characters in `body`.
def spracuj_riadok(riadok):
    body = ['0', '1']  # Initialize the list to track alternating characters    i = 0  # Initialize the index to traverse the line    count = 0  # Initialize the count for consecutive characters    new_riadok = ""  # Initialize the compressed line
    while i < len(riadok):  # Traverse the entire line        while riadok[i] == body[0]:  # Count consecutive characters            count += 1            i += 1            if i == len(riadok):  # Break if end of the line is reached
                breakThe input file `kompresia_obrazka_1.txt` is opened for reading.
The first line, containing the dimensions of the image, is read and split into width and height.
The dimensions are printed to the console.

        new_riadok += str(count) + ' '  # Add the count to the compressed line        count = 1  # Reset count        i += 1  # Move to the next character        body = [body[1], body[0]]  # Swap to the other character ('0' to '1' or '1' to '0')
    return new_riadok[:-1] + '\n'  # Return the compressed line, removing the trailing space and adding a newline

The output file `kompresia_obrazka_vystup.txt` is opened for writing.
The dimensions are written to the output file.The compressed line returned by `spracuj_riadok` is written to the output file.
# Open the input file and read the dimensionsfr = open("file.txt", 'r', encoding="UTF-8") dimensions = fr.readline().strip().split()width, height = int(dimensions[0]), int(dimensions[1])print(f"sirka: {width}, vyska: {height}, pocet bodov: {width * height}")
# Open the output file and write the dimensions fw = open("filetxt", 'w', encoding="UTF-8")fw.write(' '.join(dimensions) + '\n')
# Process each line from the input file and write to the output file  for i in fr:    fw.write(spracuj_riadok(i))




