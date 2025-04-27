# Function to determine the grade based on the score
def get_grade(score):
    # Check if the score is in the range for an A grade (90-100)
    if 90 <= score <= 100:
        print("Grade: A")
    # Check if the score is in the range for a B grade (80-89)
    elif 80 <= score < 90:
        print("Grade: B")
    # Check if the score is in the range for a C grade (70-79)
    elif 70 <= score < 80:
        print("Grade: C")
    # Check if the score is in the range for a D grade (60-69)
    elif 60 <= score < 70:
        print("Grade: D")
    # Check if the score is in the range for an F grade (0-59)
    elif 0 <= score < 60:
        print("Grade: F")
    # If the score is not in the valid range (negative or above 100)
    else:
        print("Invalid score entered.")

# Example usage: Take user input and call the get_grade function
grade = float(input("Enter your score: "))  # Prompt user to enter a score
get_grade(grade)  # Call the function to determine and print the grade
