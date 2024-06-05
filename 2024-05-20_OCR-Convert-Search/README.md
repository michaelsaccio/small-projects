# 2024-05-20_OCR-Convert-Search

## Overview
This Python script processes PDF and DOCX files to identify and extract documents containing specific keywords. It performs OCR on non-searchable PDFs, converts DOCX files to text, and searches for the defined keywords.

## Features
- **OCR Conversion**: Converts non-searchable PDFs to text using OCR.
- **Keyword Search**: Searches for specified keywords in PDF and DOCX files.
- **File Management**: Copies files containing keywords to an output directory.

## Requirements
- Python 3.x
- Packages: `pdf2image`, `pytesseract`, `shutil`, `docx2txt`, `re`, `fitz` (PyMuPDF)

## Usage
1. **Set Input and Output Directories**: Define the paths for the input directory containing the files to be processed and the output directory for storing the results.
   ```python
   input_dir = 'all_mous_and_memos'
   output_dir = 'output_mous_and_memos'
   ```

2. **Define Keywords**: Update the list of keywords to search within the documents.
   ```python
   keywords = ['John', 'Smith']
   ```

3. **Run the Script**: Execute the script to process the files.
   ```bash
   python script_name.py
   ```

## Functions
- `search_keywords_in_text(text)`: Searches for keywords in the given text.
- `is_pdf_searchable(file_path)`: Checks if a PDF is searchable.
- `ocr_convert_pdf(directory)`: Converts non-searchable PDFs to text using OCR.
- `extract_text_from_docx(file_path)`: Extracts text from DOCX files.
- `convert_and_search_docx(directory, output_dir)`: Searches for keywords in DOCX and converted PDF files and copies relevant files to the output directory.

## Main Execution
The `main` function orchestrates the OCR conversion and keyword search:
```python
def main(input_dir, output_dir):
    ocr_convert_pdf(input_dir)
    convert_and_search_docx(input_dir, output_dir)
```
Run `main(input_dir, output_dir)` to start the process.

## Notes
- Ensure Tesseract OCR is installed and configured properly for OCR functionality.
- The script handles errors in PDF processing and logs messages for troubleshooting.
