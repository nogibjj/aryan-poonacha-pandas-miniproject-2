"""CLI interface for ids_706_python_template project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test():
    return 'test'

def main():
    """
    The main function executes on commands:
    `python -m ids_706_python_template` and `$ ids_706_python_template `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    df = pd.read_csv("data/cars.csv")
    print(df.describe())

    # Create the scatter plot
    plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
    plt.scatter(df['mpg'], df['hp'], c='b', marker='o', edgecolors='k', alpha=0.6)
    plt.title('Scatter Plot of MPG vs. HP')
    plt.xlabel('MPG')
    plt.ylabel('HP')

    # Save the visualization as an image file
    plt.savefig('output/scatter_plot.png', dpi=300, bbox_inches='tight')

    # Display the plot (optional)
    plt.show()