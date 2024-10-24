import pandas as pd

def preprocess_data(data_path):
    print(f"Preprocessing data from {data_path}")
    # Add your data preprocessing logic here
    data = pd.read_csv(data_path)
    return data
