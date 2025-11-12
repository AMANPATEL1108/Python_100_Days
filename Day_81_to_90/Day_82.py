import os
from PyPDF2 import PdfMerger

def merge_pdfs_alphabetically(input_folder, output_file):
    # Get all PDF files in the folder
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

    # Sort the list alphabetically
    pdf_files.sort()

    # Create a PdfMerger object
    merger = PdfMerger()

    # Add each PDF to the merger
    for pdf in pdf_files:
        pdf_path = os.path.join(input_folder, pdf)
        print(f"Merging: {pdf}")
        merger.append(pdf_path)

    # Write out the merged file
    merger.write(output_file)
    merger.close()
    print(f"\n✅ All PDFs merged successfully into '{output_file}'")

# Example usage
if __name__ == "__main__":
    input_folder = "Path_folder"            # Folder containing your PDFs
    output_file = "merged_output.pdf" # Output file name
    merge_pdfs_alphabetically(input_folder, output_file)
