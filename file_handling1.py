#read
file = open("notes.txt", "r")      # Opens the file in read mode
content = file.read()              # Reads the entire content of the file
print("File Content:\n", content)  # Prints what was read
file.close()                       # Closes the file
