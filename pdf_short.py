import PyPDF2
import os

# Function to extract the first three pages of a PDF
def extract_first_pages(pdf_input, pdf_output, pages_to_cut):
    with open(pdf_input, 'rb') as input_file:
        reader = PyPDF2.PdfFileReader(input_file)
        writer = PyPDF2.PdfFileWriter()
        
        # Extract the first pages
        for page_number in range(pages_to_cut):
            writer.addPage(reader.getPage(page_number))
        
        # Write the first three pages to a new PDF file
        with open(pdf_output, 'wb') as output_file:
            writer.write(output_file)

PAGES_TO_CUT = 8
# Ask the user to enter the directory containing the PDFs
pdfs_directory = input("Enter the directory path containing the PDFs: ")

# Create a subdirectory named "short_pdfs" if it doesn't exist
short_pdfs_directory = os.path.join(pdfs_directory, "short_pdfs")
os.makedirs(short_pdfs_directory, exist_ok=True)

# Iterate through all PDF files in the input directory
for file_name in os.listdir(pdfs_directory):
    if file_name.endswith('.pdf'):
        pdf_input = os.path.join(pdfs_directory, file_name)
        pdf_output = os.path.join(short_pdfs_directory, 'short_' + file_name)
        extract_first_pages(pdf_input, pdf_output, PAGES_TO_CUT)
