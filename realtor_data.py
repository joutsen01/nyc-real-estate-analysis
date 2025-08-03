import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('nyc-rolling-sales.csv')

#lowercased and replaced spaces with an underscore
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

#normalized the data format
df['sale_price'] = pd.to_numeric(df['sale_price'], errors='coerce')
df['sale_date'] = pd.to_datetime(df['sale_date'])
df['land_square_feet'] = pd.to_numeric(df['land_square_feet'], errors='coerce')
df['gross_square_feet'] = pd.to_numeric(df['gross_square_feet'], errors='coerce')

#eliminated or replaced empty columns
pd.set_option('future.no_silent_downcasting', True)
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
df = df.dropna(axis=1, how='all')

#lower cased all
df['neighborhood'] = df['neighborhood'].str.lower().str.strip()
df['building_class_category'] = df['building_class_category'].str.lower().str.strip()
df['tax_class_at_present'] = df['tax_class_at_present'].astype(str).str.lower().str.strip()
df['building_class_at_present'] = df['building_class_at_present'].astype(str).str.lower().str.strip()
df['address'] = df['address'].str.lower().str.strip()
df['building_class_at_time_of_sale'] = df['building_class_at_time_of_sale'].astype(str).str.lower().str.strip()

#removing duplicates
df = df.drop_duplicates()

#created new field to calculate price for per square foot
df['Price_per_sqft']=df['sale_price']/df['land_square_feet']

#calculated for how many days the real estate is on market
today = pd.to_datetime('today')
df['Days_on_market'] = today - df['sale_date']

#df.to_csv("cleaned_nyc-rolling-sales.csv", index=False)

#average price
print('Average price of real estate in NY:', df['sale_price'].mean())    

#visualize

fig, axes = plt.subplots(2, 2, figsize=(14, 8))

# Monthly average price for real estate
df = df.dropna(subset=['sale_date', 'sale_price'])
df['Month'] = df['sale_date'].dt.month
monthly_price_trend = df.groupby('Month')['sale_price'].mean()

# first row - first column
monthly_price_trend.plot(marker='o', color='pink', ax=axes[0][0])
axes[0][0].set_title('Average Property Price by Month')
axes[0][0].set_xlabel('Month')
axes[0][0].set_ylabel('Average Price')
axes[0][0].grid(True)

# Building age category
df = df[df['year_built'].notna()]
df = df[df['year_built'] > 0]
df['building_age_category'] = df['year_built'].apply(
    lambda x: 'Old (Before 1950)' if x < 1950 else 'Normal (1950-1999)' if x < 2000 else 'New (2000 or After)'
)
age_counts = df['building_age_category'].value_counts()

# first row - second column
age_counts.plot(kind='bar', color=['pink', 'orange', 'grey'], ax=axes[0][1])
axes[0][1].set_title('Building Age Distribution')
axes[0][1].set_xlabel('Building Age Category')
axes[0][1].set_ylabel('Number of Buildings')
axes[0][1].tick_params(axis='x', rotation=0)

# The busiest neighborhoods
neighborhood_options = df['neighborhood'].value_counts().sort_values(ascending=True).head(10)

# second row - first column
neighborhood_options.plot(kind='barh', color='orange', ax=axes[1][0])
axes[1][0].set_title('Top 10 Busiest Neighborhoods')
axes[1][0].set_xlabel('Number of Listings')
axes[1][0].set_ylabel('Neighborhood')

# Portion of usable gross area
df_clean = df[['land_square_feet', 'gross_square_feet']].dropna()
df_clean = df_clean[(df_clean['land_square_feet'] > 0) & (df_clean['gross_square_feet'] > 0)]

total_land = df_clean['land_square_feet'].sum()
total_gross = df_clean['gross_square_feet'].sum()

# Ensure values are positive
usable_area = min(total_land, total_gross)
unused_area = max(0, total_gross - total_land)

# second row - second column
axes[1][1].pie([usable_area, unused_area], labels=['Total build-up area', 'Open space'], colors=['pink', 'lightgray'])
axes[1][1].set_title('Portion of Built Land')

# Final plot
plt.tight_layout()
plt.show()



