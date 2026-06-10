# Write a program to copy entire content from one file into another
f = open("file1.txt",  "r")
data = f.read()
f.close()

f = open("file2.txt", "w")
f.write(data)
f.close()
print ("data copied  succesfull")