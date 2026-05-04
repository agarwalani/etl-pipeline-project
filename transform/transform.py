import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)
    df = df[['id', 'name', 'email']]
    df.rename(columns={'id': 'user_id'}, inplace=True)
    return df