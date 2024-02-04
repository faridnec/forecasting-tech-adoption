import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the logistic function
def logistic_curve(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

def plot_s_curve(data, year_col, count_col, title):
    """
    Plot the S-curve for cumulative count of patent applications over years.

    Parameters:
    - data: DataFrame containing the data
    - year_col: Name of the column containing the years
    - count_col: Name of the column containing the cumulative count
    - title: Title of the plot
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data[year_col], data[count_col], marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Cumulative Patent Applications')
    plt.grid(True)
    plt.show()
    
def plot_model_curve(df, model_func, model_name):
    """
    Plot the model curve for the given DataFrame using the specified model function.

    Parameters:
    - df: DataFrame containing the data
    - model_func: Function representing the model
    - model_name: Name of the model for labeling the plot
    """
    # Provide initial guesses for the parameters
    initial_guess = [max(df['Cumulative_Count']), 0.1, np.median(df['Year'])]

    # Fit the model function to the cumulative count of patent applications per year
    popt, pcov = curve_fit(model_func, df['Year'], df['Cumulative_Count'], p0=initial_guess)

    # Generate points for the model curve
    x_values = np.linspace(min(df['Year']), max(df['Year']), 100)
    y_values = model_func(x_values, *popt)

    # Plot the model curve
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['Cumulative_Count'], color='blue', label='Data')
    plt.plot(x_values, y_values, color='red', label=model_name)
    plt.title(model_name)
    plt.xlabel('Year')
    plt.ylabel('Cumulative Count of Patent Applications')
    plt.legend()
    plt.grid(True)
    plt.show()