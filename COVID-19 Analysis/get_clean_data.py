import pandas as pd
import numpy as np

# Load the dataset
covid_df = pd.read_csv("./data/owid-covid-data.csv")

# Convert 'date' to datetime
covid_df['date'] = pd.to_datetime(covid_df['date'])

# Handle missing values
numerical_cols = covid_df.select_dtypes(include=['float64', 'int64']).columns
for col in numerical_cols:
    covid_df[col] = covid_df[col].fillna(covid_df[col].median())

categorical_cols = covid_df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    covid_df[col] = covid_df[col].fillna(covid_df[col].mode()[0])

# Cap outliers in key numerical features
def cap_outliers(df, col, percentile=99):
    upper = df[col].quantile(percentile / 100)
    df[col] = df[col].apply(lambda x: min(x, upper))

key_features = [
    "total_cases", "new_cases", "total_deaths", "new_deaths",
    "total_cases_per_million", "new_cases_per_million",
    "total_deaths_per_million", "new_deaths_per_million",
    "hospital_beds_per_thousand", "life_expectancy", "human_development_index"
]

for col in key_features:
    if col in covid_df.columns:
        cap_outliers(covid_df, col)

# Save the cleaned full dataset
covid_df.to_csv("./data/cleaned_covid_data.csv", index=False)

print("Cleaned full dataset saved as 'cleaned_covid_data.csv'")