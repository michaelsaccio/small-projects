import os
from pdf2image import convert_from_path
import pytesseract
import shutil
import docx2txt
import re
import fitz  # PyMuPDF


# Input and output directories
input_dir = 'all_mous_and_memos'
output_dir = '2024-05-20_search/output_mous_and_memos'

# Define keywords
keywords = ['OtP', 'Scholz', 'Phillips', 'Jamie', 'Moffitt', 'Schill', 'Coltrane', 'Gottfredson', 'Berdahl', 'Lariviere', 'Frohnmayer', 'KCASI', 'Knight Campus', 'VPFA', 'HR', 'IS']

# Function to search for keywords in a text using regular expressions
def search_keywords_in_text(text):
    for keyword in keywords:
        pattern = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)
        if re.search(pattern, text):
            return True
    return False

# Function to check if a PDF is searchable/readable
def is_pdf_searchable(file_path):
    try:
        doc = fitz.open(file_path)
        for page in doc:
            text = page.get_text()
            if text.strip():
                return True
        return False
    except Exception as e:
        print(f"Error checking PDF: {e}")
        return False

# OCR conversion function for PDFs
def ocr_convert_pdf(directory):
    total_files = 0
    converted_files = 0
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.pdf'):
                total_files += 1
                file_path = os.path.join(root, file_name)
                if not is_pdf_searchable(file_path):
                    output_path = os.path.splitext(file_path)[0] + '_OCR.txt'
                    images = convert_from_path(file_path)
                    pdf_text = ""
                    for image in images:
                        text = pytesseract.image_to_string(image)
                        pdf_text += text
                    if not pdf_text.strip():
                        print(f"Error: No text extracted from PDF: {file_path}")
                    else:
                        converted_files += 1
                        with open(output_path, 'w', encoding='utf-8') as f:
                            f.write(pdf_text)
                        print(f"Searchable text saved to {output_path}")

    if total_files > 0:
        print(f"\nFiles converted : {converted_files}")
        print(f"Total files : {total_files}")
    else:
        print("No PDF files found in the directory.")

# Function to extract text from DOCX files
def extract_text_from_docx(file_path):
    text = docx2txt.process(file_path)
    return text

# Function to convert DOCX files and search for keywords
def convert_and_search_docx(directory, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.docx'):
                file_path = os.path.join(root, file_name)
                text = extract_text_from_docx(file_path)
                if search_keywords_in_text(text):
                    shutil.copy(file_path, output_dir)
            elif file_name.endswith('_OCR.txt'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    if search_keywords_in_text(text):
                        shutil.copy(file_path.replace('_OCR.txt', '.pdf'), output_dir)  # Copy the corresponding PDF file

# Main function
def main(input_dir, output_dir):
    ocr_convert_pdf(input_dir)
    convert_and_search_docx(input_dir, output_dir)

# Execute the script
main(input_dir, output_dir)