#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
total_score1 = int(input("Enter test score: "))
total_score2 = int(input("Enter test score: "))
total_score3 = int(input("Enter test score: "))

# calculate the total score
final_score = total_score1 + total_score2 + total_score3

# calculate average score
average_score = round(final_score / 3)

# format and display the result
print("======================")
print("Your Score: ", total_score1, total_score2, total_score3)
print("Total Score:  ", final_score,
      "\nAverage Score:", average_score)
print()
print("Bye")
