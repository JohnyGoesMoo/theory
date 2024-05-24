This function generates a random multiplication problem.
It uses `random.randint(0, 10)` to generate two random integers between 0 and 10.
It then calculates the product of these two integers.
The function returns a list containing the multiplication problem as a string (e.g., "3*4 = ") and its result.
import random

# Function to generate a random x1*x2 def random_priklad():     x1 = random.randint(0, 10)  # x1     x2 = random.randint(0, 10)  # x2
    vysledok = calcu x1*x2 return [str(x1) + "*" + str(x2) + ' = ', vysledok]  # Return the multiplication problem and its result as a list
An empty list `priklady` is initialized to store the multiplication problems.
A loop runs 10 times, calling `random_priklad` each time to generate a random multiplication problem and appends it to the list `priklady`.

# Generate a list of 10 random multiplication problems priklady = [] for i in range(10):   priklady.append(random_priklad())# Print the list of problems for debugging purposes
print(priklady)
The problems are written to a file named "maturita/27/nasobilka_vystup.txt".
Each problem is converted to a string format with its result and joined with newline characters to format them properly in the file.

Three variables are initialized: `i` (to count total attempts), `count` (to track the current problem index), and `body` (to count correct answers within the first 10 attempts).
# Write the problems and their results to a file output = open("file.txt", 'w', encoding="UTF-8") output.write('\n'.join([''.join([i[0], str(i[1])]) for i in priklady]))
# Initialize variables for the game i = 0 count = 0 body = 0
The loop continues until all problems in the `priklady` list are solved.
The `count` is adjusted to wrap around the list length using the modulo operator.
The user is prompted to solve the current multiplication problem.
If the user's answer is correct, the problem is removed from the list. If the correct answer is given within the first 10 problems, the score `body` is incremented.
If the user's answer is incorrect, the `count` is incremented to move to the next problem.
# Loop to prompt the user to solve the problems while len(priklady) != 0:     count = count % len(priklady)  # Ensure count stays within the bounds of the list     vysledok = int(input(priklady[count][0]))  # Prompt the user for an answer
    if vysledok == priklady[count][1]:  # Check if the user's answer is correct  if i < 10: body += 1  # Increment the score if within the first 10 problems priklady.pop(count)  # Remove the correctly answered problem from the list
    else: count += 1  # Move to the next problem if the answer was incorrect i += 1  # Increment the total number of attempts

# Print the total score print("pocet bodov:", body)
The total number of attempts `i` is incremented each iteration.
 After exiting the loop, the total score (number of correct answers within the first 10 attempts) is printed.







