import pandas as pd

# 1. Average Completion Rate
completion_df = pd.read_csv('state_school_completion.csv')
avg_completion = completion_df['completion'].mean()
print(f"Average Completion Rate: {avg_completion:.1f}%")

# 2. Average Teacher-Student Ratio (excluding post-secondary)
ratio_df = pd.read_csv('teacher_student_ratio.csv')
ratio_filtered = ratio_df[ratio_df['level'] != 'Post-Secondary']
avg_ratio = ratio_filtered['ratio'].mean()
print(f"Average Teacher-Student Ratio: {avg_ratio:.1f}:1")

# 3. Average Poverty Rate (2022 data - using latest year)
poverty_df = pd.read_csv('hh_poverty_state.csv')
poverty_df['date'] = pd.to_datetime(poverty_df['date'])
poverty_2022 = poverty_df[poverty_df['date'].dt.year == 2022]
if len(poverty_2022) > 0:
    avg_poverty = poverty_2022['poverty_absolute'].mean()
    print(f"Average Poverty Rate (2022): {avg_poverty:.1f}%")
else:
    # Use latest available year
    latest_year = poverty_df['date'].dt.year.max()
    poverty_latest = poverty_df[poverty_df['date'].dt.year == latest_year]
    avg_poverty = poverty_latest['poverty_absolute'].mean()
    print(f"Average Poverty Rate ({latest_year}): {avg_poverty:.1f}%")

# 4. Total Number of Schools
schools_df = pd.read_csv('schools_district.csv')
total_schools = schools_df['schools'].sum()
print(f"Total Schools: {total_schools:,}")

print("\n=== Summary for KPI Cards ===")
print(f"📘 Average Completion Rate: {avg_completion:.1f}%")
print(f"🧑‍🏫 Avg Teacher–Student Ratio: {avg_ratio:.1f}:1")
print(f"💰 Average Poverty Rate: {avg_poverty:.1f}%")
print(f"🏫 Total Schools: {total_schools:,}")
