import pandas as pd

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