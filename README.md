# PDF_Data_Summarizer
## Objective

The objective of this project is to create a Streamlit web application that allows users to upload PDF files, extract text content from them, and generate a summarized version of the extracted text using Natural Language Processing (NLP) techniques.

## Problem Statement

In the digital age, large volumes of information are stored in PDF documents. Manually reading and summarizing these documents can be time-consuming and labor-intensive. This project aims to simplify this process by providing an automated solution to extract and summarize text from PDF files.

## Workflow Diagram!
![PDF_Data_Summarizer drawio](https://github.com/Amrithagaja/PDF_Data_Summarizer/assets/98808900/f20997a6-1b40-4e71-b59c-9c57ce731505)

## Workflow Description
### 1. User Interface

- **File Uploader**: The user interface features a file uploader widget where users can upload their PDF files.
- **Instructions and Status Messages**: Provide clear instructions and status messages to guide the user through the process.

### 2. File Handling

- **File Upload**: When a user uploads a PDF file, the application saves the file in a designated directory for processing.
- **File Validation**: Validate the uploaded file to ensure it is a PDF and can be processed.

### 3. Text Extraction

- **PDF Reader**: Use `PyPDF2` to read the uploaded PDF file.
- **Extract Text**: Extract text from each page of the PDF document and concatenate the text into a single string.

### 4. Text Summarization

- **Tokenization**: Tokenize the extracted text into sentences and words using NLTK.
- **Summarization**: Apply the Latent Semantic Analysis (LSA) summarizer from the `sumy` library to generate a concise summary of the extracted text.

### 5. Display Results

- **Full Text Display**: Display the full extracted text on the web interface.
- **Summary Display**: Display the generated summary of the text on the web interface.

### 6. Save Uploaded File

- **File Saving**: Optionally, save the uploaded PDF file on the server for future reference.



