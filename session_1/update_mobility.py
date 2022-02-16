import sys
import glob
import pandas as pd
from datetime import datetime

print('Reading existing mobility file...')
prev_data = pd.read_csv("data/mobility.csv")
max_date = max([datetime.strptime(x, '%Y-%m-%d %H%M') for x in prev_data['date_time'].unique()])
fn_df = pd.DataFrame({'fn':glob.glob('data/raw/*.csv')})
fn_df['date'] = [datetime.strptime(x.split('Britain_')[-1].split('.csv')[0], '%Y_%m_%d_%H%M') for x in fn_df['fn'].values]
new_fns = list(fn_df.loc[fn_df['date'] > max_date, 'fn'])

#open and concat all mobility files
print('Reading mobility files...')
mobility = pd.concat([pd.read_csv(file) for file in new_fns])

#write updated mobility data
print('Writing data...')
mobility = pd.concat([prev_data, mobility])
mobility.to_csv("data/mobility_updated.csv", index=False)
print('Success.')
exit()
