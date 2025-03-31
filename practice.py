try:
    # Get filenames
    input_file = input("Enter input filename: ")
    output_file = input("Enter output filename: ")

    # Read, modify, and write
    with open(input_file, 'r') as infile:
        with open(output_file, 'w') as outfile:
            for line in infile:
                outfile.write(line.upper())

    print(f"Success! Modified content written to {output_file}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"Error: {e}")