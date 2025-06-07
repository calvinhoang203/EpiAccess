import pandas as pd
import numpy as np
from datetime import datetime
import json
import os

class EpidemicDataProcessor:
    """
    Processes and unifies COVID-19, SARS, and Monkeypox datasets 
    for the epidemic dashboard
    """
    
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.unified_data = None
        self.metadata = {}
        
        # Country name standardization mapping
        self.country_mapping = {
            "Hong Kong SAR, China": "Hong Kong",
            "Taiwan, China": "Taiwan", 
            "Republic of Ireland": "Ireland",
            "United States": "United States",
            "England": "United Kingdom",
            "Scotland": "United Kingdom", 
            "Wales": "United Kingdom",
            "Northern Ireland": "United Kingdom",
            "Democratic Republic Of The Congo": "Democratic Republic of Congo",
            "Republic of Congo": "Republic of the Congo"
        }
    
    def load_covid_data(self):
        """Load and process COVID-19 dataset"""
        print("Processing COVID-19 data...")
        
        try:
            covid_df = pd.read_csv(f"{self.data_dir}/cleaned_covid_data.csv")
            
            # Select relevant columns and rename for consistency
            covid_processed = covid_df[['location', 'date', 'total_cases', 'new_cases', 
                                      'total_deaths', 'new_deaths', 'continent']].copy()
            
            # Add disease identifier
            covid_processed['disease'] = 'COVID-19'
            
            # Rename columns to match unified schema
            covid_processed = covid_processed.rename(columns={
                'location': 'country',
                'continent': 'region'
            })
            
            # Convert date to datetime
            covid_processed['date'] = pd.to_datetime(covid_processed['date'])
            
            # Fill NaN values with 0 for numeric columns
            numeric_cols = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths']
            covid_processed[numeric_cols] = covid_processed[numeric_cols].fillna(0)
            
            # Apply country name mapping
            covid_processed['country'] = covid_processed['country'].map(
                lambda x: self.country_mapping.get(x, x)
            )
            
            self.metadata['COVID-19'] = {
                'start_date': covid_processed['date'].min().strftime('%Y-%m-%d'),
                'end_date': covid_processed['date'].max().strftime('%Y-%m-%d'),
                'countries': covid_processed['country'].unique().tolist(),
                'total_records': len(covid_processed)
            }
            
            print(f"✅ COVID-19 data processed: {len(covid_processed)} records")
            return covid_processed
            
        except Exception as e:
            print(f"❌ Error processing COVID-19 data: {e}")
            return pd.DataFrame()
    
    def load_sars_data(self):
        """Load and process SARS dataset"""
        print("Processing SARS data...")
        
        try:
            sars_df = pd.read_csv(f"{self.data_dir}/sars_2003_complete_dataset_clean.csv")
            
            # Rename columns to match unified schema
            sars_processed = sars_df.rename(columns={
                'Date': 'date',
                'Country': 'country',
                'Cumulative number of case(s)': 'total_cases',
                'Number of deaths': 'total_deaths',
                'Number recovered': 'total_recovered'
            })
            
            # Add disease identifier
            sars_processed['disease'] = 'SARS'
            
            # Convert date to datetime
            sars_processed['date'] = pd.to_datetime(sars_processed['date'])
            
            # Calculate new cases (daily difference in total cases)
            sars_processed = sars_processed.sort_values(['country', 'date'])
            sars_processed['new_cases'] = sars_processed.groupby('country')['total_cases'].diff().fillna(0)
            sars_processed['new_deaths'] = sars_processed.groupby('country')['total_deaths'].diff().fillna(0)
            
            # Add region mapping for SARS countries
            region_mapping = {
                'China': 'Asia',
                'Hong Kong SAR, China': 'Asia',
                'Taiwan, China': 'Asia',
                'Singapore': 'Asia',
                'Thailand': 'Asia',
                'Viet Nam': 'Asia',
                'Canada': 'North America',
                'United States': 'North America',
                'Germany': 'Europe',
                'United Kingdom': 'Europe',
                'France': 'Europe',
                'Italy': 'Europe',
                'Spain': 'Europe',
                'Switzerland': 'Europe',
                'Republic of Ireland': 'Europe',
                'Slovenia': 'Europe',
                'Romania': 'Europe',
                'Belgium': 'Europe',
                'Sweden': 'Europe',
                'Australia': 'Oceania'
            }
            
            sars_processed['region'] = sars_processed['country'].map(region_mapping)
            
            # Apply country name mapping
            sars_processed['country'] = sars_processed['country'].map(
                lambda x: self.country_mapping.get(x, x)
            )
            
            # Fill NaN values
            numeric_cols = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths']
            sars_processed[numeric_cols] = sars_processed[numeric_cols].fillna(0)
            
            # Ensure non-negative new cases/deaths
            sars_processed['new_cases'] = sars_processed['new_cases'].clip(lower=0)
            sars_processed['new_deaths'] = sars_processed['new_deaths'].clip(lower=0)
            
            self.metadata['SARS'] = {
                'start_date': sars_processed['date'].min().strftime('%Y-%m-%d'),
                'end_date': sars_processed['date'].max().strftime('%Y-%m-%d'),
                'countries': sars_processed['country'].unique().tolist(),
                'total_records': len(sars_processed)
            }
            
            print(f"✅ SARS data processed: {len(sars_processed)} records")
            return sars_processed[['disease', 'country', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'region']]
            
        except Exception as e:
            print(f"❌ Error processing SARS data: {e}")
            return pd.DataFrame()
    
    def load_monkeypox_data(self):
        """Load and process Monkeypox dataset"""
        print("Processing Monkeypox data...")
        
        try:
            mpx_df = pd.read_csv(f"{self.data_dir}/Daily_Country_Monkeypox_Confirmed_Cases.csv")
            
            # Transform from wide to long format
            id_vars = ['Country']
            date_cols = [col for col in mpx_df.columns if col.startswith('2022-')]
            
            mpx_melted = mpx_df.melt(id_vars=id_vars, value_vars=date_cols, 
                                   var_name='date', value_name='new_cases')
            
            # Rename and process
            mpx_processed = mpx_melted.rename(columns={'Country': 'country'})
            mpx_processed['disease'] = 'Monkeypox'
            
            # Convert date to datetime
            mpx_processed['date'] = pd.to_datetime(mpx_processed['date'])
            
            # Sort by country and date to calculate cumulative cases
            mpx_processed = mpx_processed.sort_values(['country', 'date'])
            mpx_processed['total_cases'] = mpx_processed.groupby('country')['new_cases'].cumsum()
            
            # For Monkeypox, we don't have death data, so set to 0
            mpx_processed['total_deaths'] = 0
            mpx_processed['new_deaths'] = 0
            
            # Add region mapping for major Monkeypox countries
            region_mapping = {
                'United States': 'North America',
                'Canada': 'North America',
                'Brazil': 'South America',
                'Argentina': 'South America',
                'Chile': 'South America',
                'Colombia': 'South America',
                'Peru': 'South America',
                'Spain': 'Europe',
                'France': 'Europe',
                'Germany': 'Europe',
                'United Kingdom': 'Europe',
                'England': 'Europe',
                'Portugal': 'Europe',
                'Italy': 'Europe',
                'Netherlands': 'Europe',
                'Belgium': 'Europe',
                'Switzerland': 'Europe',
                'Nigeria': 'Africa',
                'Democratic Republic Of The Congo': 'Africa',
                'Cameroon': 'Africa',
                'Central African Republic': 'Africa',
                'Ghana': 'Africa',
                'South Africa': 'Africa'
            }
            
            mpx_processed['region'] = mpx_processed['country'].map(region_mapping).fillna('Other')
            
            # Apply country name mapping
            mpx_processed['country'] = mpx_processed['country'].map(
                lambda x: self.country_mapping.get(x, x)
            )
            
            # Fill NaN values
            mpx_processed['new_cases'] = mpx_processed['new_cases'].fillna(0)
            mpx_processed['total_cases'] = mpx_processed['total_cases'].fillna(0)
            
            self.metadata['Monkeypox'] = {
                'start_date': mpx_processed['date'].min().strftime('%Y-%m-%d'),
                'end_date': mpx_processed['date'].max().strftime('%Y-%m-%d'),
                'countries': mpx_processed['country'].unique().tolist(),
                'total_records': len(mpx_processed)
            }
            
            print(f"✅ Monkeypox data processed: {len(mpx_processed)} records")
            return mpx_processed[['disease', 'country', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'region']]
            
        except Exception as e:
            print(f"❌ Error processing Monkeypox data: {e}")
            return pd.DataFrame()
    
    def create_unified_dataset(self):
        """Combine all disease datasets into unified format"""
        print("\n🔄 Creating unified epidemic dataset...")
        
        # Load individual datasets
        covid_data = self.load_covid_data()
        sars_data = self.load_sars_data()
        mpx_data = self.load_monkeypox_data()
        
        # Combine all datasets
        datasets = [df for df in [covid_data, sars_data, mpx_data] if not df.empty]
        
        if not datasets:
            print("❌ No data loaded successfully!")
            return None
        
        self.unified_data = pd.concat(datasets, ignore_index=True)
        
        # Final data cleaning
        self.unified_data = self.unified_data.sort_values(['disease', 'country', 'date'])
        
        # Ensure numeric columns are proper types
        numeric_cols = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths']
        self.unified_data[numeric_cols] = self.unified_data[numeric_cols].astype(float)
        
        print(f"✅ Unified dataset created: {len(self.unified_data)} total records")
        print(f"📊 Diseases: {self.unified_data['disease'].unique().tolist()}")
        print(f"🌍 Countries: {len(self.unified_data['country'].unique())} unique countries")
        print(f"📅 Date range: {self.unified_data['date'].min()} to {self.unified_data['date'].max()}")
        
        return self.unified_data
    
    def save_processed_data(self, output_dir="data/processed"):
        """Save processed datasets and metadata"""
        if self.unified_data is None:
            print("❌ No unified data to save. Run create_unified_dataset() first.")
            return
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Save unified dataset
        unified_path = f"{output_dir}/unified_epidemic_data.csv"
        self.unified_data.to_csv(unified_path, index=False)
        print(f"💾 Unified dataset saved: {unified_path}")
        
        # Save individual processed datasets
        for disease in self.unified_data['disease'].unique():
            disease_data = self.unified_data[self.unified_data['disease'] == disease]
            disease_path = f"{output_dir}/{disease.lower().replace('-', '_')}_processed.csv"
            disease_data.to_csv(disease_path, index=False)
            print(f"💾 {disease} dataset saved: {disease_path}")
        
        # Save metadata
        metadata_path = f"{output_dir}/disease_metadata.json"
        with open(metadata_path, 'w') as f:
            json.dump(self.metadata, f, indent=2)
        print(f"💾 Metadata saved: {metadata_path}")
        
        # Save summary statistics
        summary = self.generate_summary_stats()
        summary_path = f"{output_dir}/data_summary.json"
        with open(summary_path, 'w') as f:
            json.dump(summary, f, indent=2)
        print(f"📈 Summary statistics saved: {summary_path}")
    
    def generate_summary_stats(self):
        """Generate summary statistics for the dashboard"""
        if self.unified_data is None:
            return {}
        
        summary = {}
        
        for disease in self.unified_data['disease'].unique():
            disease_data = self.unified_data[self.unified_data['disease'] == disease]
            
            summary[disease] = {
                'total_countries': len(disease_data['country'].unique()),
                'date_range': {
                    'start': disease_data['date'].min().strftime('%Y-%m-%d'),
                    'end': disease_data['date'].max().strftime('%Y-%m-%d')
                },
                'peak_cases': {
                    'total_cases': int(disease_data['total_cases'].max()),
                    'daily_cases': int(disease_data['new_cases'].max())
                },
                'total_deaths': int(disease_data['total_deaths'].max()),
                'top_affected_countries': disease_data.groupby('country')['total_cases'].max().nlargest(5).to_dict()
            }
        
        return summary

def main():
    """Main function to process all epidemic data"""
    print("🦠 EPIDEMIC DATA PROCESSOR")
    print("=" * 50)
    
    processor = EpidemicDataProcessor()
    
    # Create unified dataset
    unified_data = processor.create_unified_dataset()
    
    if unified_data is not None:
        # Save processed data
        processor.save_processed_data()
        
        print("\n✅ Data processing completed successfully!")
        print("\nFiles created:")
        print("📁 data/processed/")
        print("  ├── unified_epidemic_data.csv")
        print("  ├── covid_19_processed.csv") 
        print("  ├── sars_processed.csv")
        print("  ├── monkeypox_processed.csv")
        print("  ├── disease_metadata.json")
        print("  └── data_summary.json")
    else:
        print("❌ Data processing failed!")

if __name__ == "__main__":
    main() 