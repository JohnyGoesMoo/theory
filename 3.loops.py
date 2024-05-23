v = open('file1.txt', 'r', encoding="UTF-8") f = open("file2.txt", 'r', encoding="UTF-8").readlines()
The file `hlasovanie_1.txt` is opened to read the votes for contestants.
The file `hlasovanie_vypadnuti.txt` is opened to read the list of eliminated contestants.
A dictionary `points` is initialized to count the votes for each contestant. The keys are the contestant numbers as strings from "5220" to "5229", all starting with 0 votes.

# dict to count points, keys from 5220 to 5229, initial set 0 points = {str(i): 0 for i in range(5220, 5230)}
Each line in the `v` file is read and processed:
Whitespace is stripped from the line to get the contestant number.
The vote count for this contestant is incremented in the dictionary.

for i in v: # strip  whitespace from the line to get the x  x = i.strip()  # increments the vote count for the respective member in the dict
    points[x] += 1
The total number of votes is calculated by summing the values in the dictionary and printed.
The vote count for each contestant is printed.
The contestant with the fewest votes is found and printed using the `min` function on the dictionary.

# sum of values in dict print("v num:", sum(points.values()))

# v for each member print("v to member:\n", '\n'.join([f"{i}: {points[i]}" for i in points]))
# Find and print the lowest v, along with el print("smallest v, el:", min(points, key=lambda x: points[x]))

# loop el
for i in f:   # remove the v for each eli from the dictionary    points.pop(i.strip())

# Find and print the lowest v, exc el print("najmenej hlasov bez vypadnutych:", min(points, key=lambda x: points[x]))

Each eliminated contestant's number from the `vypadnuti` list is used to remove their vote count from the dictionary.
The contestant with the fewest votes, excluding those who were eliminated, is found and printed.









