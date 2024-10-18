import PyPDF2
import tkinter as tk
from tkinter import filedialog
import os

# Function to merge selected PDFs
def merge_pdfs(pdf_files, output_name="result.pdf"):
    merger = PyPDF2.PdfMerger()

    # Append all selected PDF files to the merger
    for pdf in pdf_files:
        merger.append(pdf)

    # Write to the output file
    merger.write(output_name)
    merger.close()

# Function to allow user to select multiple PDF files
def select_pdfs():
    # Create a Tkinter root window (invisible)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select multiple PDF files ko select karne ke liye
    pdf_files = filedialog.askopenfilenames(
        title="Select karo PDF files ko...",
        filetypes=[("PDF Files", "*.pdf")],  # Filter for PDF files only
    )

    return pdf_files

if __name__ == "__main__":
    # Prompt user to select multiple PDFs
    selected_pdfs = select_pdfs()

    if selected_pdfs:
        # If user selected files, merge them
        merge_pdfs(selected_pdfs, "combined.pdf")
        print(f"PDF files merged successfully into 'combined.pdf'")
    else:
        print("No PDF files were selected.")
