file = open("notes.txt", "w")
file.write("This is my first Python file\n")
file.write("File handling\n")
file.close()
print("File created and data written successfully.")

file = open("notes.txt", "r")
content = file.read()
print("File content:")
file.close()

file = open("notes.txt", "a")
file.write("Appending a new line to the file.\n")
file.close()