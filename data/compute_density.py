import csv
from collections import defaultdict

# Read schools data (2022, All Districts)
schools = defaultdict(lambda: defaultdict(int))
with open('schools_district.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['date'] == '2022-01-01' and row['district'] == 'All Districts' and row['state'] != 'Malaysia':
            state = row['state']
            stage = row['stage']
            schools[state][stage] += int(row['schools'])

# Read enrolment data (2022, All Districts, both sexes)
students = defaultdict(lambda: defaultdict(int))
with open('enrolment_school_district.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['date'] == '2022-01-01' and row['district'] == 'All Districts' and row['sex'] == 'both' and row['state'] != 'Malaysia':
            state = row['state']
            stage = row['stage']
            students[state][stage] += int(row['students'])

# Compute density per 100k students
densities = []
for state in schools:
    primary_schools = schools[state].get('primary', 0)
    secondary_schools = schools[state].get('secondary', 0)
    tertiary_schools = schools[state].get('tertiary', 0)
    
    primary_students = students[state].get('primary', 0)
    secondary_students = students[state].get('secondary', 0)
    post_secondary_students = students[state].get('post_secondary', 0)
    
    total_students = primary_students + secondary_students + post_secondary_students
    
    if total_students > 0:
        primary_density = (primary_schools / primary_students * 100000) if primary_students > 0 else 0
        secondary_density = (secondary_schools / secondary_students * 100000) if secondary_students > 0 else 0
        tertiary_density = (tertiary_schools / post_secondary_students * 100000) if post_secondary_students > 0 else 0
        
        total_density = primary_density + secondary_density + tertiary_density
        
        densities.append({
            'state': state,
            'primary': round(primary_density, 2),
            'secondary': round(secondary_density, 2),
            'post_secondary': round(tertiary_density, 2),
            'total': round(total_density, 2)
        })

# Sort by total density descending
densities.sort(key=lambda x: x['total'], reverse=True)

# Output results
print('State,Primary,Secondary,Post-Secondary,Total')
for d in densities:
    print(f"{d['state']},{d['primary']},{d['secondary']},{d['post_secondary']},{d['total']}")

# Print top 3 and bottom 3 summary
print()
print('TOP 3 STATES (Schools per 100k students):')
for i in range(min(3, len(densities))):
    d = densities[i]
    print(f"{i+1}. {d['state']}: {d['total']:.2f} total (Primary: {d['primary']:.2f}, Secondary: {d['secondary']:.2f}, Post-Secondary: {d['post_secondary']:.2f})")

print()
print('BOTTOM 3 STATES (Schools per 100k students):')
for i in range(max(0, len(densities)-3), len(densities)):
    d = densities[i]
    print(f"{len(densities)-i}. {d['state']}: {d['total']:.2f} total (Primary: {d['primary']:.2f}, Secondary: {d['secondary']:.2f}, Post-Secondary: {d['post_secondary']:.2f})")

# Write CSV for Vega-Lite
with open('school_density_computed.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['state', 'primary', 'secondary', 'post_secondary', 'total'])
    writer.writeheader()
    writer.writerows(densities)

print()
print('CSV file created: school_density_computed.csv')
