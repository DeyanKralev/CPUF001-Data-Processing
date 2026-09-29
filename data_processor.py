import sys
import os


def read_data(filename):
    """
    Reads numerical values from the given input file.
    Returns a list of float numbers.
    Includes error checking for missing file and invalid data.
    """
    numbers = []

    # Check if the input file exists
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    try:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        number = float(line)
                        numbers.append(number)
                    except ValueError:
                        print(f"Warning: Line {line_number} contains invalid data -> '{line}' (skipped)")
    except Exception as e:
        print(f"Error while reading the file: {e}")
        sys.exit(1)

    # Ensure at least 3 values are present (minimum requirement)
    if len(numbers) < 3:
        print("Error: The input file must contain at least 3 numerical values.")
        sys.exit(1)

    return numbers


def calculate_results(numbers):
    """
    Performs calculations on the list of numbers.
    Calculations: Sum, Average, Minimum, Maximum
    Returns a dictionary containing all results.
    """
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)

    results = {
        "count": count,
        "sum": total,
        "average": average,
        "minimum": minimum,
        "maximum": maximum
    }
    return results


def write_results(results, output_filename="results.txt"):
    """
    Writes the calculation results to an output file in a clear format.
    """
    try:
        with open(output_filename, "w") as file:
            file.write("==================================================\n")
            file.write("           DATA PROCESSING RESULTS\n")
            file.write("==================================================\n\n")
            file.write(f"Number of values processed : {results['count']}\n")
            file.write(f"Sum of all values          : {results['sum']:.2f}\n")
            file.write(f"Average value              : {results['average']:.2f}\n")
            file.write(f"Minimum value              : {results['minimum']:.2f}\n")
            file.write(f"Maximum value              : {results['maximum']:.2f}\n")
            file.write("\n==================================================\n")
            file.write("Processing completed successfully.\n")
            file.write("==================================================\n")
        
        print(f"Results successfully written to '{output_filename}'")
    except Exception as e:
        print(f"Error while writing the output file: {e}")
        sys.exit(1)


def main():
    """
    Main function that controls the program flow.
    1. Checks command-line argument
    2. Reads data from the input file
    3. Performs calculations
    4. Writes results to the output file
    """
    # Check if a filename was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python data_processor.py <input_filename>")
        print("Example: python data_processor.py sample_data.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    print(f"Reading data from: {input_file}")

    # Step 1: Read the data
    numbers = read_data(input_file)
    print(f"Successfully read {len(numbers)} values.")

    # Step 2: Perform calculations
    results = calculate_results(numbers)

    # Step 3: Write results to output file
    write_results(results)

    # Also display a short summary on the screen
    print("\n----- Summary -----")
    print(f"Sum      : {results['sum']:.2f}")
    print(f"Average  : {results['average']:.2f}")
    print(f"Minimum  : {results['minimum']:.2f}")
    print(f"Maximum  : {results['maximum']:.2f}")


# Program entry point
if __name__ == "__main__":
    main()