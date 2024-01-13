import PyPDF2
import os

# Function to display PDF files and get user input for order
def get_pdf_order(pdf_files):
    print("PDF files found:")
    for i, file in enumerate(pdf_files, start=1):
        print(f"{i}. {file}")
        
    while True:
        try:
            order_input = input("Enter the order of files to merge (e.g., 2 1 3): ")
            order_indexes = [int(i) for i in order_input.split()]

            # Check if any index is out of range
            if any(i < 1 or i > len(pdf_files) for i in order_indexes):
                raise ValueError("Index out of range.")

            return [pdf_files[i-1] for i in order_indexes]

        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid indexes.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Main
def main():
    pdf_files = [file for file in os.listdir(os.curdir) if file.endswith(".pdf")]
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return

    ordered_files = get_pdf_order(pdf_files)

    merger = PyPDF2.PdfMerger()

    for file in ordered_files:
        try:
            print(f"Adding {file}...")
            merger.append(file)
        except PyPDF2.errors.PdfReadError as e:
            print(f"Error merging {file}: {e}")

    output_name = input("Enter the name of the combined PDF file: ")
    merger.write(output_name + ".pdf")
    merger.close()

    print(f"Files combined in {output_name}.pdf")

if __name__ == "__main__":
    main()
