import json
import os

# Define the notebook structure
notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Exploratory Data Analysis: Infectious Disease Trends & Healthcare Utilization\n",
                "\n",
                "This notebook performs exploratory data analysis on COVID-19 data to understand disease trends and healthcare utilization patterns across countries."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 1. Setup\n",
                "\n",
                "Import necessary libraries for data analysis and visualization."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "import numpy as np\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "from scipy import stats\n",
                "from datetime import datetime\n",
                "\n",
                "# Set plot style\n",
                "sns.set_style(\"darkgrid\")\n",
                "plt.rcParams['figure.figsize'] = (12, 8)\n",
                "plt.rcParams['font.size'] = 12"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Load Data\n",
                "\n",
                "Load the COVID-19 dataset and split it into train and test sets for analysis."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Load the COVID-19 dataset\n",
                "covid_df = pd.read_csv(\"../data/owid-covid-data.csv\")\n",
                "\n",
                "# Convert date to datetime\n",
                "covid_df['date'] = pd.to_datetime(covid_df['date'])\n",
                "\n",
                "# Split data into train and test sets (80% train, 20% test)\n",
                "# We'll use a time-based split to maintain temporal integrity\n",
                "train_cutoff_date = covid_df['date'].quantile(0.8)\n",
                "train_df = covid_df[covid_df['date'] < train_cutoff_date].copy()\n",
                "test_df = covid_df[covid_df['date'] >= train_cutoff_date].copy()\n",
                "\n",
                "print(f\"Training Data Shape: {train_df.shape}\")\n",
                "print(f\"Test Data Shape: {test_df.shape}\")\n",
                "print(f\"Train date range: {train_df['date'].min()} to {train_df['date'].max()}\")\n",
                "print(f\"Test date range: {test_df['date'].min()} to {test_df['date'].max()}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Data Overview\n",
                "\n",
                "Examine the structure and basic statistics of the datasets."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Display the first few rows of the training data\n",
                "train_df.head()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Check data types\n",
                "print(\"Data Types:\")\n",
                "train_df.dtypes"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Summary statistics for numerical columns\n",
                "train_df.describe()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Missing Values & Outliers\n",
                "\n",
                "Identify and handle missing values and outliers in the dataset."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Check missing values\n",
                "missing_values = train_df.isnull().sum()\n",
                "missing_values = missing_values[missing_values > 0]\n",
                "print(\"Missing values in dataset:\")\n",
                "print(missing_values.sort_values(ascending=False))"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Visualizing missing values\n",
                "plt.figure(figsize=(12, 6))\n",
                "sns.heatmap(train_df.isnull(), cmap='viridis', cbar=False, yticklabels=False)\n",
                "plt.title(\"Missing Values in Training Data\")\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Function to detect outliers using IQR method\n",
                "def detect_outliers(df, column):\n",
                "    Q1 = df[column].quantile(0.25)\n",
                "    Q3 = df[column].quantile(0.75)\n",
                "    IQR = Q3 - Q1\n",
                "    lower_bound = Q1 - 1.5 * IQR\n",
                "    upper_bound = Q3 + 1.5 * IQR\n",
                "    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]\n",
                "    print(f\"{column}: {len(outliers)} outliers detected\")\n",
                "    return outliers"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Select key numerical columns for outlier detection\n",
                "key_features = [\n",
                "    \"total_cases\", \"new_cases\", \"total_deaths\", \"new_deaths\",\n",
                "    \"total_cases_per_million\", \"new_cases_per_million\",\n",
                "    \"total_deaths_per_million\", \"new_deaths_per_million\",\n",
                "    \"hospital_beds_per_thousand\", \"life_expectancy\", \"human_development_index\"\n",
                "]\n",
                "\n",
                "# Detect outliers for all key features\n",
                "outlier_dict = {}\n",
                "for col in key_features:\n",
                "    if col in train_df.columns:\n",
                "        outlier_dict[col] = detect_outliers(train_df, col)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Handle missing values and outliers\n",
                "# For missing values in numerical columns, we'll use median imputation\n",
                "numerical_cols = train_df.select_dtypes(include=['float64', 'int64']).columns\n",
                "for col in numerical_cols:\n",
                "    if train_df[col].isnull().sum() > 0:\n",
                "        train_df[col] = train_df[col].fillna(train_df[col].median())\n",
                "        test_df[col] = test_df[col].fillna(train_df[col].median())\n",
                "\n",
                "# For missing values in categorical columns, we'll use mode imputation\n",
                "categorical_cols = train_df.select_dtypes(include=['object']).columns\n",
                "for col in categorical_cols:\n",
                "    if train_df[col].isnull().sum() > 0:\n",
                "        train_df[col] = train_df[col].fillna(train_df[col].mode()[0])\n",
                "        test_df[col] = test_df[col].fillna(train_df[col].mode()[0])\n",
                "\n",
                "# For outliers, we'll cap them at the 99th percentile\n",
                "def cap_outliers(df, col, percentile=99):\n",
                "    upper_limit = df[col].quantile(percentile / 100)\n",
                "    df[col] = df[col].apply(lambda x: upper_limit if x > upper_limit else x)\n",
                "\n",
                "# Apply capping for key features with many outliers\n",
                "for col in key_features:\n",
                "    if col in train_df.columns:\n",
                "        cap_outliers(train_df, col, 99)\n",
                "        cap_outliers(test_df, col, 99)\n",
                "\n",
                "print(\"Missing values and outliers handled.\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Distributions\n",
                "\n",
                "Analyze the distributions of key numerical and categorical variables."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Histograms for key numerical features\n",
                "plt.figure(figsize=(16, 10))\n",
                "for i, col in enumerate(key_features):\n",
                "    if col in train_df.columns:\n",
                "        plt.subplot(4, 3, i+1)\n",
                "        sns.histplot(train_df[col], kde=True)\n",
                "        plt.title(f\"Distribution of {col}\")\n",
                "        plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Boxplots for key numerical features\n",
                "plt.figure(figsize=(16, 10))\n",
                "for i, col in enumerate(key_features):\n",
                "    if col in train_df.columns:\n",
                "        plt.subplot(4, 3, i+1)\n",
                "        sns.boxplot(y=train_df[col])\n",
                "        plt.title(f\"Boxplot of {col}\")\n",
                "        plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Bar charts for categorical features\n",
                "# Top 10 countries by total cases\n",
                "top_countries = train_df.groupby('location')['total_cases'].max().sort_values(ascending=False).head(10)\n",
                "plt.figure(figsize=(12, 6))\n",
                "sns.barplot(x=top_countries.index, y=top_countries.values)\n",
                "plt.title(\"Top 10 Countries by Total Cases\")\n",
                "plt.xticks(rotation=45)\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Distribution of continents\n",
                "continent_counts = train_df['continent'].value_counts()\n",
                "plt.figure(figsize=(10, 6))\n",
                "sns.barplot(x=continent_counts.index, y=continent_counts.values)\n",
                "plt.title(\"Distribution of Continents\")\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 6. Correlations & Relationships\n",
                "\n",
                "Analyze correlations between numerical features and relationships between variables."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Select only numerical columns for correlation analysis\n",
                "numeric_df = train_df.select_dtypes(include=['int64', 'float64'])\n",
                "\n",
                "# Compute correlation matrix\n",
                "correlation_matrix = numeric_df.corr()\n",
                "\n",
                "# Plot heatmap of correlations\n",
                "plt.figure(figsize=(16, 12))\n",
                "sns.heatmap(correlation_matrix, cmap=\"coolwarm\", annot=False)\n",
                "plt.title(\"Feature Correlation Heatmap\")\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Display top correlated features with total_cases\n",
                "if 'total_cases' in correlation_matrix.columns:\n",
                "    top_correlations = correlation_matrix[\"total_cases\"].abs().sort_values(ascending=False)\n",
                "    print(\"Top correlations with total_cases:\")\n",
                "    print(top_correlations.head(15))"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Scatter plots for key relationships\n",
                "# Relationship between total cases and total deaths\n",
                "plt.figure(figsize=(10, 6))\n",
                "sns.scatterplot(x='total_cases', y='total_deaths', data=train_df, alpha=0.5)\n",
                "plt.title(\"Relationship between Total Cases and Total Deaths\")\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Relationship between hospital beds and deaths per million\n",
                "plt.figure(figsize=(10, 6))\n",
                "sns.scatterplot(x='hospital_beds_per_thousand', y='total_deaths_per_million', data=train_df, alpha=0.5)\n",
                "plt.title(\"Relationship between Hospital Beds and Deaths per Million\")\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 7. Time-Series Analysis\n",
                "\n",
                "Analyze trends and patterns over time."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Set date as index for time series analysis\n",
                "train_ts = train_df.set_index('date')\n",
                "\n",
                "# Plot global daily new cases over time\n",
                "global_daily_cases = train_ts.groupby('date')['new_cases'].sum()\n",
                "plt.figure(figsize=(14, 6))\n",
                "global_daily_cases.plot()\n",
                "plt.title(\"Global Daily New Cases Over Time\")\n",
                "plt.xlabel(\"Date\")\n",
                "plt.ylabel(\"New Cases\")\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Plot global daily deaths over time\n",
                "global_daily_deaths = train_ts.groupby('date')['new_deaths'].sum()\n",
                "plt.figure(figsize=(14, 6))\n",
                "global_daily_deaths.plot()\n",
                "plt.title(\"Global Daily Deaths Over Time\")\n",
                "plt.xlabel(\"Date\")\n",
                "plt.ylabel(\"New Deaths\")\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Plot 7-day moving average for new cases\n",
                "global_daily_cases_ma = global_daily_cases.rolling(window=7).mean()\n",
                "plt.figure(figsize=(14, 6))\n",
                "global_daily_cases_ma.plot()\n",
                "plt.title(\"Global Daily New Cases (7-day Moving Average)\")\n",
                "plt.xlabel(\"Date\")\n",
                "plt.ylabel(\"New Cases (7-day MA)\")\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Country Patterns\n",
                "\n",
                "Analyze patterns and trends across different countries."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Top 5 countries by total cases\n",
                "top_5_countries = train_df.groupby('location')['total_cases'].max().sort_values(ascending=False).head(5).index.tolist()\n",
                "\n",
                "# Plot daily new cases for top 5 countries\n",
                "plt.figure(figsize=(14, 6))\n",
                "for country in top_5_countries:\n",
                "    country_data = train_df[train_df['location'] == country]\n",
                "    plt.plot(country_data['date'], country_data['new_cases'], label=country)\n",
                "\n",
                "plt.title(\"Daily New Cases for Top 5 Countries\")\n",
                "plt.xlabel(\"Date\")\n",
                "plt.ylabel(\"New Cases\")\n",
                "plt.legend()\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Compare healthcare utilization across continents\n",
                "continent_healthcare = train_df.groupby('continent')[['hospital_beds_per_thousand', 'life_expectancy', 'human_development_index']].mean()\n",
                "continent_healthcare"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Visualize healthcare metrics by continent\n",
                "plt.figure(figsize=(12, 6))\n",
                "continent_healthcare['hospital_beds_per_thousand'].plot(kind='bar')\n",
                "plt.title(\"Average Hospital Beds per Thousand by Continent\")\n",
                "plt.xlabel(\"Continent\")\n",
                "plt.ylabel(\"Hospital Beds per Thousand\")\n",
                "plt.tight_layout()\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. Extra ML Insights\n",
                "\n",
                "Additional analyses to provide insights for machine learning models."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Feature importance for predicting total cases\n",
                "# We'll use a simple correlation-based approach\n",
                "if 'total_cases' in correlation_matrix.columns:\n",
                "    feature_importance = correlation_matrix[\"total_cases\"].abs().sort_values(ascending=False)\n",
                "    feature_importance = feature_importance.drop(\"total_cases\")  # Remove self-correlation\n",
                "    \n",
                "    plt.figure(figsize=(12, 6))\n",
                "    feature_importance.head(10).plot(kind='bar')\n",
                "    plt.title(\"Top 10 Features Correlated with Total Cases\")\n",
                "    plt.xlabel(\"Features\")\n",
                "    plt.ylabel(\"Absolute Correlation\")\n",
                "    plt.tight_layout()\n",
                "    plt.show()"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Clustering countries based on healthcare metrics\n",
                "from sklearn.preprocessing import StandardScaler\n",
                "from sklearn.cluster import KMeans\n",
                "\n",
                "# Select healthcare-related features\n",
                "healthcare_features = ['hospital_beds_per_thousand', 'life_expectancy', 'human_development_index']\n",
                "\n",
                "# Get the latest data for each country\n",
                "latest_data = train_df.sort_values('date').groupby('location').last()\n",
                "\n",
                "# Drop rows with missing values in healthcare features\n",
                "healthcare_data = latest_data[healthcare_features].dropna()\n",
                "\n",
                "# Scale the data\n",
                "scaler = StandardScaler()\n",
                "scaled_data = scaler.fit_transform(healthcare_data)\n",
                "\n",
                "# Perform K-means clustering\n",
                "kmeans = KMeans(n_clusters=4, random_state=42)\n",
                "healthcare_data['Cluster'] = kmeans.fit_predict(scaled_data)\n",
                "\n",
                "# Visualize clusters\n",
                "plt.figure(figsize=(10, 6))\n",
                "scatter = plt.scatter(healthcare_data['hospital_beds_per_thousand'], \n",
                "                     healthcare_data['human_development_index'], \n",
                "                     c=healthcare_data['Cluster'], cmap='viridis')\n",
                "plt.title(\"Country Clusters Based on Healthcare Metrics\")\n",
                "plt.xlabel(\"Hospital Beds per Thousand\")\n",
                "plt.ylabel(\"Human Development Index\")\n",
                "plt.colorbar(scatter, label='Cluster')\n",
                "plt.tight_layout()\n",
                "plt.show()\n",
                "\n",
                "# Display countries in each cluster\n",
                "for cluster in range(4):\n",
                "    print(f\"\\nCluster {cluster}:\")\n",
                "    print(healthcare_data[healthcare_data['Cluster'] == cluster].index.tolist())"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 10. Finalize & Export\n",
                "\n",
                "Prepare the data for modeling and export the cleaned datasets."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Add an ID column if it doesn't exist\n",
                "if 'Id' not in train_df.columns:\n",
                "    train_df['Id'] = range(1, len(train_df) + 1)\n",
                "    test_df['Id'] = range(1, len(test_df) + 1)\n",
                "\n",
                "# Rename and convert Id\n",
                "train_df.rename(columns={'remainder__Id':'Id'}, inplace=True)\n",
                "test_df.rename(columns={'remainder__Id':'Id'}, inplace=True)\n",
                "train_df['Id'] = train_df['Id'].astype('int32')\n",
                "test_df['Id'] = test_df['Id'].astype('int32')\n",
                "\n",
                "# Export cleaned data\n",
                "train_df.to_csv('../data/cleaned_train_data.csv', index=False)\n",
                "test_df.to_csv('../data/cleaned_test_data.csv', index=False)\n",
                "\n",
                "print(\"Data preparation complete. Cleaned datasets exported.\")"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "base",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.11.5"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
}

# Write the notebook to a file
with open("COVID-19 Analysis/eda_analysis.ipynb", "w") as f:
    json.dump(notebook, f, indent=1)

print("Notebook created successfully!") 