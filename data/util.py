import pandas as pd

def get_data(PATH):
    df = pd.read_csv(PATH)
    return df

def get_games(PATH):
    df = get_data(PATH)
    return df