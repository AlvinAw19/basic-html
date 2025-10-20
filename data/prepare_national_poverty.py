import pandas as pd
import os

os.chdir(r'c:\Users\Alvin Aw\Downloads\basic-html\data')

# Load poverty data
poverty_df = pd.read_csv('hh_poverty_state.csv')

# Convert date to year
poverty_df['date'] = pd.to_datetime(poverty_df['date'])
poverty_df['year'] = poverty_df['date'].dt.year

# Filter for years 2016-2022 and exclude Malaysia if it exists
poverty_df = poverty_df[
    (poverty_df['year'] >= 2016) & 
    (poverty_df['year'] <= 2022) &
    (poverty_df['state'] != 'Malaysia')
]

# Calculate national average for each year
national_avg = poverty_df.groupby('year')['poverty_absolute'].mean().reset_index()
national_avg.columns = ['year', 'poverty_rate']
national_avg = national_avg.round(2)

print("National Average Poverty Rate by Year:")
print(national_avg)

# Save to CSV
national_avg.to_csv('malaysia_poverty_national.csv', index=False)
print("\nCreated: malaysia_poverty_national.csv")
