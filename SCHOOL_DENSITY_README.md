# School Density Stacked Bar Chart - Implementation Summary

## Overview
Created a stacked bar chart showing school density per 100,000 students by state in Malaysia (2022), with visual hierarchy highlighting the top 3 states and detailed annotations for top/bottom 3.

## Data Processing
- **Source Files**: 
  - `schools_district.csv` (school counts by state and stage)
  - `enrolment_school_district.csv` (student enrollment by state and stage)
- **Computation Script**: `data/compute_density.py`
- **Formula**: (Schools / Students) × 100,000 per stage
- **Output**: `data/school_density_computed.csv`

## Key Findings

### Top 3 States (Highest School Density)
1. **Sarawak**: 652.7 schools per 100k students
   - Primary: 537.6 | Secondary: 101.8 | Post-Secondary: 13.3
2. **Perak**: 598.3 schools per 100k students
   - Primary: 424.9 | Secondary: 157.7 | Post-Secondary: 15.7
3. **Pahang**: 579.4 schools per 100k students
   - Primary: 358.1 | Secondary: 194.5 | Post-Secondary: 26.8

### Bottom 3 States (Lowest School Density)
1. **W.P. Putrajaya**: 167.3 schools per 100k students
2. **Selangor**: 249.9 schools per 100k students
3. **Pulau Pinang**: 367.1 schools per 100k students

## Visualization Features

### Chart Design
- **Type**: Horizontal stacked bar chart
- **Dimensions**: 900×550 pixels
- **Color Scheme**: 
  - Primary: Blue (#3498db)
  - Secondary: Red (#e74c3c)
  - Post-Secondary: Orange (#f39c12)

### Visual Hierarchy
- **Top 3 States**: 
  - Bold, dark labels (#2c3e50)
  - Full opacity (1.0)
  - Total values displayed on bars
- **Middle States**: 
  - Normal weight, grey labels (#666666)
  - Reduced opacity (0.75)
- **Bottom 3 States**: 
  - Normal weight, grey labels (#666666)
  - Reduced opacity (0.75)
  - Total values displayed on bars

### Interactive Elements
- Tooltips showing state, stage, and exact density value
- Clear legend for school stages
- Grid lines for easier reading

## Files Created/Modified

### New Files
1. `data/compute_density.py` - Python script for density calculations
2. `data/school_density_computed.csv` - Processed density data
3. `js/school_density_stacked.json` - Vega-Lite specification

### Modified Files
1. `index.html` - Added new section with detailed caption
2. `css/styles.css` - Added styling for school_density_chart

## Insights

The data reveals that **rural states have higher school densities** while **urban states have lower densities**:

- **Rural Pattern** (High Density): Sarawak, Perak, Pahang
  - Dispersed populations require more schools
  - Smaller schools serving local communities
  
- **Urban Pattern** (Low Density): Putrajaya, Selangor, Pulau Pinang
  - Concentrated populations allow for larger schools
  - Fewer schools serving more students efficiently
  - Better infrastructure enables larger school capacities

This pattern reflects the efficiency of urban education systems versus the accessibility challenges in rural areas.

## How to View

1. Ensure the HTTP server is running:
   ```powershell
   cd "c:\Users\Alvin Aw\Downloads\basic-html"
   python -m http.server 8080
   ```

2. Open browser to: `http://localhost:8080`

3. Scroll to the "School Density per 100,000 Students by State (2022)" section

The chart will display 8 selected states sorted by total density, with top 3 prominently highlighted and all annotations clearly visible.
