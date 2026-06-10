# File Backup Utility

# Function to copy file content
def backup_file(source, destination):

    try:
        # Open source file in read mode
        with open(source, "r") as src_file:
            data = src_file.read()   # Read full content

        # Open destination file in write mode
        with open(destination, "w") as dest_file:
            dest_file.write(data)    # Write content

        # Success message
        print("\nFile copied successfully.")
        print(f"All contents from '{source}' have been copied to '{destination}'.")

    except FileNotFoundError:
        print("Error: Source file not found!")

    except Exception as e:
        print("An error occurred:", e)


# Main program
source_file = input("Enter Source File Name      : ")
destination_file = input("Enter Destination File Name : ")

backup_file(source_file, destination_file)
