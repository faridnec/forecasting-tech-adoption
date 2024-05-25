import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import re

from scipy.optimize import curve_fit



# Preprocessing

def load_patent_data(data_path, sheet_name):
    """
    Load patent data from Excel file into a DataFrame.
    
    Args:
    - data_path (str): Path to the Excel file containing the patent data.
    - sheet_name (str): Name of the sheet containing the patent data in the Excel file.
    
    Returns:
    - patent_data (pd.DataFrame): DataFrame containing the loaded patent data.
    """
    patent_data = pd.read_excel(data_path, sheet_name=sheet_name)
    return patent_data

def clean_text(text):
  """
  This function cleans text data by converting to lowercase, removing punctuation,
  and performing optional stemming or lemmatization.

  Args:
      text (str): The text data to be cleaned.

  Returns:
      str: The cleaned text data.
  """
  # Convert to lowercase
  text = text.lower()

  # Remove punctuation
  import string
  punctuations = string.punctuation
  text = text.translate(str.maketrans('', '', punctuations))

  return text

def preprocess_date_column(df, date_col):
    """
    Preprocesses the specified date column to convert it to datetime format.
    
    Args:
    - df: DataFrame containing the date column.
    - date_col: Name of the date column to preprocess.
    
    Returns:
    - df: DataFrame with the date column converted to datetime format.
    """
    df[date_col] = pd.to_datetime(df[date_col])
    return df

def preprocess_cpc_data(relevant_patents_df, cpc_col):
    # Filter rows where 'CPC' column is not null and not empty
    relevant_patents_df = relevant_patents_df.dropna(subset=[cpc_col])
    relevant_patents_df = relevant_patents_df[relevant_patents_df[cpc_col] != '']

    # Preprocess CPC data to handle multiple CPC codes
    relevant_patents_df[cpc_col] = relevant_patents_df[cpc_col].astype(str)

    # Extract the section, class, and subclass for each CPC code
    relevant_patents_df[cpc_col] = relevant_patents_df[cpc_col].str.replace(r'[^A-Z0-9/]', '')
    relevant_patents_df[cpc_col] = relevant_patents_df[cpc_col].str.split(';| \| ')

    # Create a list to store extracted CPC codes
    cpc_list = []

    # Iterate through each row and extract section, class, and subclass for each CPC code
    for row in relevant_patents_df.itertuples(index=False):
        for cpc_code in row.CPC:
            cpc_code = cpc_code.strip()
            if len(cpc_code) >= 4:  # Check if the CPC code is at least 4 characters long
                section = cpc_code[:4]
                cpc_list.append(section)

    cpc_df = pd.DataFrame(cpc_list, columns=[cpc_col])

    cpc_counts = cpc_df[cpc_col].value_counts()

    return cpc_counts


# Semantic Search

def semantic_search(query, query_embedding, text_embeddings, patent_data, threshold, top_matches,
                    patent_id_col, pub_number_col, title_col, abstract_col, date_col, cpc_col):
    
    distances = scipy.spatial.distance.cdist(query_embedding, text_embeddings, "cosine")[0]
    
    results = sorted(zip(range(len(distances)), distances), key=lambda x: x[1])

    relevant_patents = []
    for idx, distance in results[:top_matches]:
        if 1 - distance > threshold:
            relevant_patent = {
                patent_id_col: patent_data.index[idx],
                "Score": 1 - distance,
                pub_number_col: patent_data.iloc[idx][pub_number_col],
                title_col: patent_data.iloc[idx][title_col],
                abstract_col: patent_data.iloc[idx][abstract_col],
                date_col: patent_data.iloc[idx][date_col],
                cpc_col: patent_data.iloc[idx][cpc_col]
            }
            relevant_patents.append(relevant_patent)
    
    return pd.DataFrame(relevant_patents)


# S-Curves

def logistic_growth(x, a, b, c):
    return a / (1 + np.exp(-b * (x - c)))

def gompertz_growth(x, a, b, c):
    return a * np.exp(-np.exp(-b * (x - c)))

def plot_s_curves(relevant_patents_df, cpc_counts, time_col, top_n=5, year_range=(1990, 2070), growth_model=None, growth_model_label=None):
    if growth_model is None or growth_model_label is None:
        raise ValueError("Both growth_model and growth_model_label must be specified.")
    
    top_cpc_codes = cpc_counts.head(top_n).index
    
    for cpc_code in top_cpc_codes:
        cpc_relevant_patents = relevant_patents_df[relevant_patents_df['CPC'].str.contains(cpc_code)]
        year_counts = cpc_relevant_patents.groupby(cpc_relevant_patents[time_col].dt.year).size()
        
        if not year_counts.empty:
            future_years = np.arange(*year_range)
            patent_cumulative_counts = year_counts.cumsum()

            try:
                initial_guess = (max(patent_cumulative_counts), 0.1, year_range[0])
                popt, pcov = curve_fit(growth_model, patent_cumulative_counts.index, patent_cumulative_counts, p0=initial_guess)
                future_counts = growth_model(future_years, *popt)

                print(f"For CPC {cpc_code}: Estimated Parameters (a, b, c): {popt}")

                plt.figure(figsize=(10, 6))
                plt.plot(year_counts.index, year_counts.cumsum(), 'o', label=f'CPC {cpc_code} - Actual')
                if future_years is not None and future_counts is not None:
                    plt.plot(future_years, future_counts, label=f'CPC {cpc_code} - Predicted')

                plt.xlabel('Years')
                plt.ylabel('Cumulative Number of Patents')
                plt.title(f'S-Curve for CPC {cpc_code} ({growth_model_label})')
                plt.legend()
                plt.grid(True)
                plt.show()
            except RuntimeError:
                print(f"Failed to fit {growth_model_label} growth model for CPC {cpc_code}")
        else:
            print(f"No data available for CPC {cpc_code}")


def calculate_application_per_month(data: pd.DataFrame, date_column: str):
    """
    Calculate the cumulative count of patent applications per month.

    Parameters:
    - data: DataFrame containing the patent application data

    Returns:
    - DataFrame with the cumulative count of patent applications per month
    """
    # Convert date column to datetime format
    data[date_column] = pd.to_datetime(data[date_column])

    # Extract year and month from the date
    data['Time'] = data[date_column].dt.to_period('M')

    # Group by year and month, and count the number of applications in each group
    applications_per_month = data.groupby('Time').size().reset_index(name='Applications')
    
    return applications_per_month

def calculate_application_per_week(data: pd.DataFrame, date_column: str):
    """
    Calculate the cumulative count of patent applications per week.

    Parameters:
    - data: DataFrame containing the patent application data
    - date_column: Name of the column containing the date information

    Returns:
    - DataFrame with the cumulative count of patent applications per week
    """
    # Convert date column to datetime format
    data[date_column] = pd.to_datetime(data[date_column])

    # Extract year and week number from the date
    data['Week'] = data[date_column].dt.to_period('W')

    # Group by week and count the number of applications in each group
    applications_per_week = data.groupby('Week').size().reset_index(name='Applications')

    return applications_per_week