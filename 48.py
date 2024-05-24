def spracuj_riadok(riadok): #processes a line of input, str as argument
    # Initialize a list `body` with two elements, "0" and '1'.  body = ["0", '1']  The input string `riadok` is stripped of leading and trailing whitespace, then split into a list of strings using a space as the delimiter.
    riadok = riadok.strip().split(' ')   # Initialize an empty string `new_riadok`. new_riadok = ""   # Iterate over each element `i` in the list `riadok`.
    for i in riadok: # Convert the element `i` to an integer and multiply it by the first element of `body`. # The result is concatenated to `new_riadok`.        new_riadok += int(i)*body[0]
        # The elements of `body` are swapped.        body = [body[1], body[0]]
    # The processed line `new_riadok` is returned, followed by a newline character.    return new_riadok + '\n'
# Open the file "maturita/21/dekompresia_obrazka_1.txt" for reading. fr = open("file", 'r', encoding="UTF-8")

# Read the first line of the file and split it into a list of strings.dimensions = fr.readline().strip().split()
# The first and second elements of `dimensions` are converted to integers and assigned to `width` and `height`. width, height = int(dimensions[0]), int(dimensions[1])

# Print the width, height, and total number of points.print(f"sirka: {width}, vyska: {height}, pocet bodov: {width*height}")# Open the file "maturita/21/dekompresia_obrazka_vystup.txt" for writing.
fw = open("file.txt", 'w', encoding="UTF-8")

# Write the dimensions to the output file, followed by a newline character.fw.write(' '.join(dimensions) + '\n')# Iterate over each line `i` in the input file.for i in fr:    # Write the processed line to the output file.
    fw.write(spracuj_riadok(i))
