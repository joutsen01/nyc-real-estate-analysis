# nyc-real-estate-analysis
🏙️ New York Real Estate Data Analysis Project
This project analyzes a real estate dataset from New York City. The dataset includes sales information such as addresses, sale prices, dates, building sizes, and land areas. The goal of this project is to clean, normalize, and analyze the data, and then visualize important trends using Python libraries like pandas, matplotlib, and seaborn.

📌 Dataset
The dataset (realtor-data) was downloaded from Kaggle in ZIP format. It contains detailed real estate transaction records in New York.

🔧 Project Steps
1. Data Cleaning
- Renamed all column names to lowercase and replaced spaces with underscores.
- Replaced visually empty cells with NaN using regex.
- Dropped completely empty columns using dropna().
- Converted all string values to lowercase for consistency.
- Removed all duplicate records.

2. Data Normalization
- Converted object-type numeric columns (price, land_square_feet, gross_square_feet) to numeric format using pd.to_numeric().
- Converted the sale_date column to datetime using pd.to_datetime().

3. Feature Engineering
- Created a new column: price_per_sqft by dividing the price by gross square feet.
- Created a days_on_market column by subtracting sale_date from the current date using pd.to_datetime('today').

4. Data Visualization
Used matplotlib and seaborn to create several charts and visualizations:
- Distribution of sale prices
- Relationship between gross area and price
- Price trends over time
- Proportion of land used vs. total area via pie chart

🧰 Technologies Used
Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook / VS Code


