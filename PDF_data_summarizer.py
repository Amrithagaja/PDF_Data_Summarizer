# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:09:52 2024

@author: Jai
"""

import streamlit as st
import PyPDF2
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lsa import LsaSummarizer
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import os


# Ensure NLTK data is downloaded
nltk.download('punkt') 

st.set_page_config(page_title="PDF Data Summarizer",page_icon="C://Users//Jai//Downloads//data.PNG")


# CSS to center the file uploader
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(176, 224, 230, 0.5), rgba(176, 224, 230, 0.5)), 
                    url("https://thumbs.dreamstime.com/z/vector-data-analysis-pattern-big-seamless-background-117577846.jpg?ct=jpeg") no-repeat center center fixed;
        
        background-size: cover;
    
        
        }
    .block-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: auto;
        background-color: rgba(176, 224, 230, 0.8); /* Optional: Add a white overlay for readability */
        padding: 20px;
        border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("PDF Data Summarizer")

# Create 'uploads' directory if it doesn't exist
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# File uploader widget
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

class NLTKTokenizer:
    @staticmethod
    def to_sentences(text):
        return sent_tokenize(text)

    @staticmethod
    def to_words(text):
        return word_tokenize(text)

def summarize_text(text, num_sentences=5):
    parser = PlaintextParser.from_string(text, NLTKTokenizer)
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    summary_text = "\n".join([str(sentence) for sentence in summary])
    return summary_text

if uploaded_file is not None:
    try:
        # Open the PDF file
        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        # Print the number of pages in the PDF
        st.write(f'The PDF document has {len(pdf_reader.pages)} pages.')

        # Extract text from each page
        full_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            full_text += text

        # Display the full text
        st.subheader("Full Text")
        st.write(full_text)

        # Summarize the text
        summary = summarize_text(full_text)
        st.subheader("Summary")
        st.write(summary)

        # Optionally save the uploaded file
        with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File saved successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("No file uploaded yet. Please upload a PDF file.")
