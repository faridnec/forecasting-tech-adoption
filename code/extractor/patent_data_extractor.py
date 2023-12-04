#problem with KeyBert Installation
#still figuring out to matches with the Turkish Taxonomy and extracting key product/topic from patent data

import os
import PyPDF2
from keybert import KeyBert
import pandas as pd

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader
        text = ""
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text

def process_files(input_directory, output_directory):
    model = KeyBERT("distilbert-base-nli-mean-tokens")  # different model can be tried

    for filename in os.listdir(input_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_directory, filename)
            text = extract_text_from_pdf(pdf_path)

            keywords = model.extract_keywords(text, keyphrase_ngram_range=(1, 1), stop_words="english", use_maxsum=True)

            # Create a DataFrame for each file
            df = pd.DataFrame({"Keyword": keywords})
            df["Filename"] = filename
            df["PDF_Text"] = text
            # df["Title"] = 

            # Save the DataFrame to a CSV file
            output_filename = os.path.splitext(filename)[0] + "_output.csv"
            output_path = os.path.join(output_directory, output_filename)
            df.to_csv(output_path, index=False)

def main():
    input_directory = "input_pdfs"
    output_directory = "output_datasets"
    process_files(input_directory, output_directory)

if __name__ == "__main__":
    main()