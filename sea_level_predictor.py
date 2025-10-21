import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress



def draw_plot():
    # Read data from file
    df = pd.read_csv("https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/refs/heads/main/epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 5))
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x,y)
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    x_pred = pd.Series(range(1880, 2051))
    y_pred = intercept + slope * x_pred
    plt.plot(x_pred, y_pred, color='b', label='Best fit line (1880–2018)')
    

    # Create second line of best fit

    df_recent = df[df['Year'] >= 2000]

    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = intercept_recent + slope_recent * x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, color='red', label='Best fit line (2000–2018)')

    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()