def main():
    # Ask the user for the input filename
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content (example: make uppercase)
        modified_content = content.upper ()

        # Create a new filename for output
        new_filename = "modified_" + filename

        # Write modified content to new file
        with open(new_filename, "w") as new_file: new_file.write(modified_content)
        print(f"File successfully modified and saved as '{new_filename}'.")
            
    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
         print("❌ Error: You don't have permission to view this file.")
    except Exception as e:
        print(f"❌ An unexpected error occured: {e}")
if __name__ == "__main__":
    main()