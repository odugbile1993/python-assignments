# File Creation: Creating a new text file and writing to it

# Open the file in write mode ('w')
with open("my_file.txt", 'w') as file:
    file.write("This is the first line of text.\n")
    file.write("The second line contains a number: 123\n")
    file.write("The third line is a string with mixed data: Hello 456\n")

# File Reading and Display: Reading the file content and displaying it

# Open the file in read mode ('r')
with open("my_file.txt", 'r') as file:
    content = file.read()  # Read the entire content of the file
    print("File Content:")
    print(content)

# File Appending: Appending new lines of text to the existing file

# Open the file in append mode ('a')
with open("my_file.txt", 'a') as file:
    file.write("The fourth line with more data.\n")
    file.write("Another line with an integer: 789\n")
    file.write("Final line: Text completed.\n")

# To verify the appended content, we can read the file again
with open("my_file.txt", 'r') as file:
    content = file.read()  # Read the entire content again
    print("Updated File Content after Appending:")
    print(content)
