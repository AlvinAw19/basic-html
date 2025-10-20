import pandas as pd
import os

os.chdir(r'c:\Users\Alvin Aw\Downloads\basic-html\data')

# Load the poverty completion joined data
df = pd.read_csv('poverty_completion_joined.csv')

# Calculate national average for each year
national_avg = df.groupby('year')['poverty_absolute'].mean().reset_index()
national_avg['state'] = 'Malaysia (Average)'

# Combine with existing data
df_combined = pd.concat([df[['state', 'year', 'poverty_absolute']], 
                         national_avg[['state', 'year', 'poverty_absolute']]], 
                        ignore_index=True)

# Calculate rank for each year
df_combined['year'] = df_combined['year'].astype(int)
df_combined = df_combined.sort_values(['year', 'poverty_absolute'])
df_combined['poverty_rank'] = df_combined.groupby('year')['poverty_absolute'].rank(method='dense')

# Identify top 2 and bottom 2 states (averaged across all years)
state_avg = df_combined[df_combined['state'] != 'Malaysia (Average)'].groupby('state')['poverty_absolute'].mean()
top_2 = state_avg.nsmallest(2).index.tolist()  # Lowest poverty
bottom_2 = state_avg.nlargest(2).index.tolist()  # Highest poverty

print("Top 2 states (lowest poverty):", top_2)
print("Bottom 2 states (highest poverty):", bottom_2)

# Mark featured states
def get_category(state):
    if state == 'Malaysia (Average)':
        return 'featured'
    elif state in top_2:
        return 'featured'
    elif state in bottom_2:
        return 'featured'
    else:
        return 'other'

df_combined['category'] = df_combined['state'].apply(get_category)

# Save to CSV
df_combined.to_csv('poverty_rankings_enhanced.csv', index=False)

print("\nCreated poverty_rankings_enhanced.csv")
print(f"Total rows: {len(df_combined)}")
print("\nFeatured states:")
print(df_combined[df_combined['category'] == 'featured']['state'].unique())
