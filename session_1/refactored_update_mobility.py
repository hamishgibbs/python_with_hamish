import sys
import glob
import pandas as pd
from datetime import datetime

def dataframe_dates_to_datetime(df):
    df["date_time"] = pd.to_datetime(df["date_time"])
    return df

def get_latest_date(df):
    df = dataframe_dates_to_datetime(df)
    return df["date_time"].max()

def extract_date_from_filename(fn):
    return fn.split('Britain_')[-1].split('.csv')[0]

def parse_file_date(date_str):
    return datetime.strptime(date_str, '%Y_%m_%d_%H%M')

def parse_dates_from_filenames(fns):
    file_dates = [extract_date_from_filename(fn) for fn in fns]
    return [parse_file_date(date) for date in file_dates]

def new_file_indices(dates, threshold):
    return [i for i, x in enumerate(dates) if x > threshold]

def fns_later_than_date(input_files, threshold):
    input_file_dates = parse_dates_from_filenames(input_files)
    new_file_i = new_file_indices(input_file_dates, threshold)
    return [input_files[i] for i in new_file_i]

def concat_new_files(new_fns):
    return pd.concat(pd.read_csv(x) for x in new_fns)

def create_updated_data(old_data, new_fns):
    new_data = concat_new_files(new_fns)
    new_data = dataframe_dates_to_datetime(new_data)
    return pd.concat([old_data, new_data])

def main():
    """
    Update data by appending only new data to an existing file.
    """

    combined_fn = "./data/mobility.csv"
    input_path = "./data/raw/*.csv"
    out_fn = "./data/mobility_updated.csv"

    prev_data = pd.read_csv(combined_fn)
    input_files = glob.glob(input_path)

    latest_date = get_latest_date(prev_data)
    new_fns = fns_later_than_date(input_files, latest_date)

    updated_data = create_updated_data(prev_data, new_fns)

    updated_data.to_csv(out_fn, index=False)

if __name__ == '__main__':
    main()
