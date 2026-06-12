# Open source file in read mode
src = open("notes.txt", "r")

# Read content
content = src.read()

# Open backup file in write mode
dest = open("backup.txt", "w")

# Copy content
dest.write(content)

# Close files
src.close()
dest.close()

# Success message
print("File copied successfully")