# File Content Analyzer

# Function to analyze file content
def analyze_file(filename):

    # Open file in read mode
    with open(filename, "r") as file:
        content = file.read()   # Read entire file content

    # Initialize counters
    vowels = 0
    characters = 0

    # Define vowels
    vowel_list = "aeiouAEIOU"

    # Count characters and vowels
    for ch in content:
        characters += 1
        if ch in vowel_list:
            vowels += 1

    # Count number of lines
    lines = len(content.splitlines())

    # Display report
    print("\nFile Analysis Report")
    print("Total Number of Vowels     :", vowels)
    print("Total Number of Characters :", characters)
    print("Total Number of Lines      :", lines)


# Main program
filename = input("Enter file name: ")
analyze_file(filename)
