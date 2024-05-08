import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

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