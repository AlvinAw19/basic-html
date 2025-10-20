import pandas as pd
import os

# Change to data directory
os.chdir(r'c:\Users\Alvin Aw\Downloads\basic-html\data')

# Load completion data
df = pd.read_csv('completion_school_state.csv')

# Convert date to datetime and extract year
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

# Filter for 'both' sexes only and exclude Malaysia aggregate
df_filtered = df[(df['sex'] == 'both') & (df['state'] != 'Malaysia')]

# Calculate average completion rate by state and year across all stages
avg_completion = df_filtered.groupby(['state', 'year'])['completion'].mean().reset_index()
avg_completion.columns = ['state', 'year', 'avg_completion']

# Round to 2 decimal places
avg_completion['avg_completion'] = avg_completion['avg_completion'].round(2)

# Save to CSV
avg_completion.to_csv('completion_by_year.csv', index=False)

print('Created completion_by_year.csv')
print(f'Total rows: {len(avg_completion)}')
print('\nSample data:')
print(avg_completion.head(10))
print('\nYears available:', sorted(avg_completion['year'].unique()))
print('States:', sorted(avg_completion['state'].unique()))
