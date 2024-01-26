import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def update_year(df: pd.DataFrame="video_games_df", indices: list=None, year: float=None):
    """
    Update the 'Year' column for specified rows in the video_games_df DataFrame.

    Parameters:
    - indices (list): List of row indices to be updated.
    - year (float): New year value to be assigned.
    """
    for elem in indices:
        df.iloc[elem, df.columns.get_loc('Year')] = year


def rename_columns(df: pd.DataFrame):
    """ 
    Rename columns in a DataFrame by converting them to lowercase and replacing spaces with underscores.

    Parameters:
    - df (pd.DataFrame): The DataFrame with columns to be renamed.
    """
    df.columns = df.columns.str.lower().str.replace(' ', '_')

def countplot_categorical_variables(df: pd.DataFrame, figsize_height: int = 16, figsize_width: int = 16):
    """This functions takes as:
    Input: a df with categorical variables, and figsizes with a default value each of 16
    Output: countplot for each column of the df sorted by frequency. Whenever the nº unique values > 6, bars will be placed in the y-axis"""

    for col in df:
        if len(df[col].unique()) >= 6:
            fig, ax = plt.subplots(figsize=(figsize_width, figsize_height))
            sns.countplot(data=df, y=col, order=df[col].value_counts().index, ax=ax)
            ax.set_title(f'Countplot for {col}')
        else:
            fig, ax = plt.subplots(figsize=(figsize_width, figsize_height))
            sns.countplot(data=df, x=col, order=df[col].value_counts().index, ax=ax)
            ax.set_title(f'Countplot for {col}')

        plt.show()