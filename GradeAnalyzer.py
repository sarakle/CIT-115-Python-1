Name = input("What is the name for calculating the grades: ")

test1 = int(input("Test Score 1: "))
test2 = int(input("Test Score 2: "))
test3 = int(input("Test Score 3: "))
test4 = int(input("Test Score 4: "))

LOW_SCORE = input("Drop The Lowest Grade? Y or N: ")

# This determines if the test score that was inputted is less than 0
if test1 <= 0 or test2 <= 0 or test3 <= 0 or test4 <= 0:
    print("Test scores must be greater than 0.")
    raise SystemExit

# Finding the lowest test score
lowest_score = test1
if test2 < lowest_score:
    lowest_score = test2
if test3 < lowest_score:
    lowest_score = test3
if test4 < lowest_score:
    lowest_score = test4

# Calculates average with dropping the lowest score
if LOW_SCORE == "Y" or LOW_SCORE == "y":
    if lowest_score == test1:
        average = (test2 + test3 + test4)/3
    elif lowest_score == test2:
        average = (test1 + test3 + test4)/3
    elif lowest_score == test3:
        average = (test1 + test2 + test4)/3
    elif lowest_score == test4:
        average = (test1 + test2 + test3)/3
# Calculates the average without dropping the lowest
elif LOW_SCORE == "N" or LOW_SCORE == "n":
    average = (test1 + test2 + test3 + test4)/4
else:
# Stops the program from continuing because of incorrect input
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

# Determines the letter for the grade
if average >= 97.0:
    letter_grade = "A+"
elif average >= 94.0:
    letter_grade = "A"
elif average >= 90.0:
    letter_grade = "A-"
elif average >= 87.0:
    letter_grade = "B+"
elif average >= 84.0:
    letter_grade = "B"
elif average >= 80.0:
    letter_grade = "B-"
elif average >= 77.0:
    letter_grade = "C+"
elif average >= 74.0:
    letter_grade = "C"
elif average >= 70.0:
    letter_grade = "C-"
elif average >= 67.0:
    letter_grade = "D+"
elif average >= 64.0:
    letter_grade = "D"
elif average >= 60.0:
    letter_grade = "D-"
else:
    letter_grade = "F"

# Prints the test average with the user's name and letter grade of the average formatting it by .1 decimal point
print(f"{Name} test average is: {average:.1f}")
print(f"Letter Grade for the test is: {letter_grade}")
