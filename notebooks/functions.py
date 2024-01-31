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


def df_grouping (df: pd.DataFrame, objective: str, sum_func: str):
    
    platform_group = df.groupby(['year', objective]).agg({sum_func : 'sum'}).sort_values(sum_func, ascending=False)
    platform_group = pd.DataFrame(platform_group).reset_index()
    return platform_group

def lineplot(df_list: list = None, names_list: list = None, objective: str = None, width: int = 30, height: int = 5, x:str = 'year', y: str = 'global'):
    for elem, name in zip(df_list, names_list):
        fig, ax = plt.subplots(figsize=(width, height))
        sns.lineplot(data = elem, x = x, y = y, hue = objective)
        plt.title(f'{name} sales through the years')
        plt.show()

def barplot(df_list: list = None, names_list: list = None, objective: str = None, width: int = 30, height: int = 5, y: str = 'global', palette: str = 'light:#5A9'):
    for elem, name in zip(df_list, names_list):
        fig, ax = plt.subplots(figsize=(width, height))
        sns.barplot(data = elem, x = objective, y = y, hue = objective, palette = palette)
        plt.title(f'{name}  Top-selling')
        plt.xticks(rotation=45)
        plt.show()
