import pandas as pd
import os

os.chdir(r'c:\Users\Alvin Aw\Downloads\basic-html\data')

# Load data
teachers = pd.read_csv('teachers_district.csv')
students = pd.read_csv('enrolment_school_district.csv')

# Filter for 2022, All Districts, both sexes, exclude Malaysia aggregate
teachers_2022 = teachers[
    (teachers['district'] == 'All Districts') & 
    (teachers['date'] == '2022-01-01') & 
    (teachers['sex'] == 'both') & 
    (teachers['state'] != 'Malaysia')
][['state', 'stage', 'teachers']]

students_2022 = students[
    (students['district'] == 'All Districts') & 
    (students['date'] == '2022-01-01') & 
    (students['sex'] == 'both') & 
    (students['state'] != 'Malaysia')
][['state', 'stage', 'students']]

# Merge and calculate ratio
merged = pd.merge(students_2022, teachers_2022, on=['state', 'stage'])
merged['ratio'] = merged['students'] / merged['teachers']

# Create readable level names
merged['level'] = merged['stage'].map({
    'primary': 'Primary',
    'secondary': 'Secondary',
    'post_secondary': 'Post-Secondary'
})

# Select and save
result = merged[['state', 'level', 'ratio', 'students', 'teachers']]
result.to_csv('teacher_student_ratio.csv', index=False)

print('Created teacher_student_ratio.csv')
print(f'Total rows: {len(result)}')
print('\nFirst 10 rows:')
print(result.head(10))
print('\nSample data:')
print(result[result['state'] == 'Johor'])
