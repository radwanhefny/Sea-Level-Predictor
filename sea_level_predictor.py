import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

def draw_plot():
    # Read data from file
    df = pd.read_csv(os.path.join(os.getcwd(), 'data/epa-sea-level.csv'))

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s= 15, label='Data Points')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_pred, color='red', label= 'Best Fit Line')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_extended2 = pd.Series(range(2000, 2051))
    sea_level_pred2 = slope2 * years_extended2 + intercept2
    plt.plot(years_extended2, sea_level_pred2, color='green', label= 'Best Fit Line (2000 onwards)')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()