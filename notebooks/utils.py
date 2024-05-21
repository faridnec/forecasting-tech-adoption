import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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

# Define the logistic function
def logistic_curve(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

def drop_rows_with_nan(df, column_name):
    """
    Drop rows containing NaN values in the specified column.

    Parameters:
    - df: DataFrame to operate on
    - column_name: Name of the column to check for NaN values

    Returns:
    - DataFrame with rows containing NaN values in the specified column dropped
    """
    nan_indices = df[df[column_name].isna()].index
    return df.drop(index=nan_indices)

def calculate_cumulative_count(data: pd.DataFrame, categories: list):
    """
    Calculate the cumulative count of patent applications per year for each unique category.

    Parameters:
    - data: DataFrame containing the patent application data
    - categories: List of unique categories

    Returns:
    - DataFrame with the cumulative count of patent applications per year for each category
    """
    result = []
    for category in categories:
        category_data = data[data['CATEGORY'] == category]
        applications_per_year = category_data.groupby('YEAR').size().reset_index(name='Applications_Per_Year')
        applications_per_year['Cumulative_Count'] = applications_per_year['Applications_Per_Year'].cumsum()
        applications_per_year['CATEGORY'] = category
        result.append(applications_per_year)
    
    return pd.concat(result, ignore_index=True)

def calculate_cumulative_count_per_category(data: pd.DataFrame, categories: list):
    """
    Calculate the cumulative count of patent applications per year for each unique category.

    Parameters:
    - data: DataFrame containing the patent application data
    - categories: List of unique categories

    Returns:
    - DataFrame with the cumulative count of patent applications per year for each category
    """
    result = []
    for category in categories:
        category_data = data[data['CATEGORY'] == category]
        applications_per_year = category_data.groupby('YEAR').size().reset_index(name='Applications_Per_Year')
        applications_per_year['Cumulative_Count'] = applications_per_year['Applications_Per_Year'].cumsum()
        applications_per_year['CATEGORY'] = category
        result.append(applications_per_year)
    
    return pd.concat(result, ignore_index=True)


def plot_cumulative_s_curves(data: pd.DataFrame):
    """
    Plot the cumulative S-curves of patent applications for different categories.

    Parameters:
    - data: DataFrame containing the cumulative count of patent applications per year for each category
    """ 
    plt.figure(figsize=(10, 6))
    categories = data['CATEGORY'].unique()

    for category in categories:
        category_data = data[data['CATEGORY'] == category]
        plt.plot(category_data['YEAR'], category_data['Cumulative_Count'], marker='o', linestyle='-', label=category)

    plt.title('Cumulative S-curves of Patent Applications for Different Categories')
    plt.xlabel('Year')
    plt.ylabel('Cumulative Patent Applications')
    plt.grid(True)
    plt.legend()
    plt.show()
    

def plot_one_cumulative_s_curves(data, year_col, count_col, category_col, category_values, plot_title):
    """
    Plot cumulative S-curves of patent applications over years for multiple categories.

    Parameters:
    - data: DataFrame containing the data
    - year_col: Name of the column containing the years
    - count_col: Name of the column containing the cumulative count
    - category_col: Name of the column containing the category
    - category_values: List of category values to plot
    - plot_title: Title of the plot
    """
    plt.figure(figsize=(10, 6))
    
    for category_value in category_values:
        # Filter data for the specified category value
        filtered_data = data[data[category_col] == category_value]
        
        # Group by 'YEAR' and count occurrences
        applications_per_year = filtered_data.groupby(year_col)[count_col].count().cumsum()
        
        # Plot the cumulative S-curve for the current category
        plt.plot(applications_per_year.index, applications_per_year.values, marker='o', linestyle='-', label=category_value)
    
    plt.title(plot_title)
    plt.xlabel('Year')
    plt.ylabel('Cumulative Patent Applications')
    plt.grid(True)
    plt.legend()
    plt.show()
