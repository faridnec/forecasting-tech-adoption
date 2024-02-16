import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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


def logistic_growth_function(t, L, k, t0):
    """
    Logistic growth function.

    Parameters:
    - t: Time variable
    - L: Carrying capacity
    - k: Growth rate
    - t0: Midpoint of growth

    Returns:
    - Value of the logistic growth function at time t
    """
    return L / (1 + np.exp(-k * (t - t0)))

def fit_logistic_growth(data):
    """
    Fit logistic growth function to data.

    Parameters:
    - data: DataFrame containing time (YEAR) and cumulative count data

    Returns:
    - Tuple (L, k, t0) representing the fitted parameters for logistic growth function
    """
    # Initial guesses for parameters
    initial_guesses = [data['Cumulative_Count'].max(), 0.1, data['YEAR'].median()]
    popt, pcov = curve_fit(logistic_growth_function, data['YEAR'], data['Cumulative_Count'], p0=initial_guesses)
    return tuple(popt)

def plot_logistic_growth(data, L, k, t0, title):
    """
    Plot observed data points and the fitted logistic growth curve.

    Parameters:
    - data: DataFrame containing time (YEAR) and cumulative count data
    - L: Carrying capacity
    - k: Growth rate
    - t0: Midpoint of growth
    - title: Title of the plot
    """
    # Generate time values for plotting the curve
    t_values = np.linspace(data['YEAR'].min(), data['YEAR'].max(), 100)
    # Calculate predicted counts using the logistic growth function
    predicted_counts = logistic_growth_function(t_values, L, k, t0)

    # Plot observed data points
    plt.scatter(data['YEAR'], data['Cumulative_Count'], label='Observed Data')
    # Plot fitted logistic growth curve
    plt.plot(t_values, predicted_counts, label='Fitted Logistic Growth Curve', color='red')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Cumulative Count')
    plt.legend()
    plt.grid(True)
    plt.show()
