def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
        # Modify the content (let's just convert it to uppercase as an example)
        modified_content = content.upper()

        # Open the output file for writing the modified content
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read or write the file '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask the user for the input and output file names
    input_filename = input("Enter the name of the file you want to read: ")
    output_filename = input("Enter the name of the file where you want to save the modified content: ")

    # Call the function to read, modify, and write the file
    read_and_modify_file(input_filename, output_filename)

# Run the program
if __name__ == "__main__":
    main()
