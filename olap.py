import pandas as pd

# Load the dataset
file_path = 'agriculture_dataset.csv'
df = pd.read_csv(file_path)

# Display the dataset
print("Original Dataset:")
print(df)

### 1. Roll-up: Aggregate monthly data into yearly data (e.g., sum of yields and revenue by year)
roll_up = df.groupby('year').agg({'yield': 'sum', 'total_revenue': 'sum'})
print("\nRoll-up (Yearly Aggregation):")
print(roll_up)

### 2. Drill-down: Show detailed monthly data for a specific year (e.g., 2020)
drill_down = df[df['year'] == 2020]
print("\nDrill-down (Monthly Data for 2020):")
print(drill_down)

### 3. Slice: Select data for a specific year (e.g., only data for 2021)
slice_op = df[df['year'] == 2021]
print("\nSlice (Data for 2021):")
print(slice_op)

### 4. Dice: Select data for specific months and years (e.g., Jan and Feb of 2021 and 2022)
dice_op = df[(df['month'].isin(['January', 'February'])) & (df['year'].isin([2021, 2022]))]
print("\nDice (Jan and Feb of 2021 and 2022):")
print(dice_op)

### 5. Pivot: Pivot the data to see yields as rows and total revenue as columns
pivot_op = df.pivot_table(index='yield', columns='year', values='total_revenue', aggfunc='sum')
print("\nPivot (Yields as Rows, Total Revenue by Year):")
print(pivot_op)
