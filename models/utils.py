import pandas as pd

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