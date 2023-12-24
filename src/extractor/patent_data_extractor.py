import os
import PyPDF2
import keybert
import pandas as pd
from typing import Dict, List


class PDFExtractor:
    def __init__(self, input_folder: str, kw_model: keybert.KeyBERT):
        self.input_folder = input_folder
        self.kw_model = kw_model
        self.extracted_data: List[Dict] = []

    def extract_all(self):
        for filename in os.listdir(self.input_folder):
            print(f"Processing file: {filename}")
            self.extract_from_file(filename)

    def extract_from_file(self, filename: str):
        text = self.read_pdf_text(filename)
        extracted_info = self.extract_information(text)
        self.extracted_data.append(extracted_info)

    def read_pdf_text(self, filename: str) -> str:
        with open(os.path.join(self.input_folder, filename), "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extractText()
        return text

    def extract_information(self, text: str) -> Dict:
        # Define extraction functions for desired information
        def extract_patent_number(text: str) -> str:
            return re.findall(r"Patent Number: (\d+)", text)[0]

        def extract_application_date(text: str) -> str:
            return re.findall(r"Application Date: (\d{4}-\d{2}-\d{2})", text)[0]

        def extract_title(text: str) -> str:
            return re.findall(r"Title: (.+)", text)[0]

        def extract_abstract(text: str) -> str:
            # Use regex or specific markers to identify abstract section
            # ...
            pass

        # Extract information using defined functions
        info = {
            "patent_number": extract_patent_number(text),
            "application_date": extract_application_date(text),
            "title": extract_title(text),
            "abstract": extract_abstract(text),
        }

        # Use KeyBERT for relevant keywords
        keywords = self.kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 3))

        # Extract product, classification, and taxonomy from keywords
        info["product"] = keywords[0]
        # Customize logic based on your needs
        # ...

        return info

    def get_extracted_data(self) -> List[Dict]:
        return self.extracted_data


# Customize the following parameters
input_folder = "../input_files"
kw_model = keybert.KeyBERT(model="distiluse-base-multilingual-cased")

# Initialize and extract data
extractor = PDFExtractor(input_folder, kw_model)
extractor.extract_all()
extracted_data = extractor.get_extracted_data()

# Create Pandas DataFrame and set column names
df = pd.DataFrame(extracted_data)
df.columns = ["patent_number", "application_date", "title", "abstract",
              "product", "technology_classification", "taxonomy"]

# Save or further process the DataFrame
df.to_csv("extracted_data.csv", index=False)
