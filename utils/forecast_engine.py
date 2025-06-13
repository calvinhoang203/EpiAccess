import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
import warnings
warnings.filterwarnings('ignore')

# Add PyTorch imports
import torch
import torch.nn as nn

class EpidemicTimeSeriesModel(nn.Module):
    """PyTorch neural network model for epidemic time series forecasting"""
    def __init__(self, input_size, hidden_size, output_size):
        super(EpidemicTimeSeriesModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

class EpidemicForecaster:
    """
    Epidemic forecasting engine using multiple approaches:
    - Exponential smoothing for stable trends
    - Linear trend for growth phases
    - Epidemic curve modeling for outbreak scenarios
    - PyTorch neural network for complex pattern recognition
    """
    
    def __init__(self):
        self.forecast_days = 180  # 6 months
        self.min_data_points = 14  # Minimum 2 weeks of data
        self.pytorch_models = {}  # Cache for trained PyTorch models
        
    def prepare_country_data(self, data: pd.DataFrame, disease: str, country: str, metric: str = 'new_cases') -> pd.DataFrame:
        """Prepare time series data for a specific country and disease"""
        country_data = data[
            (data['disease'] == disease) & 
            (data['country'] == country)
        ].copy()
        
        if len(country_data) < self.min_data_points:
            return pd.DataFrame()
            
        country_data = country_data.sort_values('date').reset_index(drop=True)
        country_data['date'] = pd.to_datetime(country_data['date'])
        
        # Ensure no negative values and handle missing data
        country_data[metric] = country_data[metric].fillna(0).clip(lower=0)
        
        return country_data[['date', metric]].rename(columns={metric: 'y'})
    
    def exponential_smoothing_forecast(self, ts_data: pd.DataFrame, alpha: float = 0.3) -> Tuple[List[float], List[float], List[float]]:
        """Simple exponential smoothing with trend adjustment"""
        values = ts_data['y'].values
        n = len(values)
        
        if n < 3:
            # Not enough data, return flat forecast
            last_value = values[-1] if n > 0 else 0
            forecast = [last_value] * self.forecast_days
            lower_bound = [max(0, last_value * 0.7)] * self.forecast_days
            upper_bound = [last_value * 1.3] * self.forecast_days
            return forecast, lower_bound, upper_bound
        
        # Calculate trend
        recent_values = values[-min(14, n):]  # Last 2 weeks or available data
        trend = np.polyfit(range(len(recent_values)), recent_values, 1)[0]
        
        # Exponential smoothing
        smoothed = [values[0]]
        for i in range(1, n):
            smoothed.append(alpha * values[i] + (1 - alpha) * smoothed[i-1])
        
        # Generate forecast
        last_smoothed = smoothed[-1]
        forecast = []
        
        for i in range(self.forecast_days):
            # Apply trend with dampening factor to prevent unrealistic growth
            damping = 0.98 ** i  # Exponential dampening
            trend_component = trend * i * damping
            
            # Ensure epidemic curves eventually decline
            epidemic_damping = 1.0
            if trend > 0 and i > 30:  # After 30 days, start dampening growth
                epidemic_damping = max(0.1, 0.95 ** (i - 30))
            
            forecast_value = max(0, last_smoothed + trend_component * epidemic_damping)
            forecast.append(forecast_value)
        
        # Calculate confidence intervals based on recent volatility
        recent_volatility = np.std(values[-min(21, n):]) if n > 1 else abs(values[-1]) * 0.2
        
        lower_bound = [max(0, f - 1.96 * recent_volatility * (1 + i/180)) for i, f in enumerate(forecast)]
        upper_bound = [f + 1.96 * recent_volatility * (1 + i/180) for i, f in enumerate(forecast)]
        
        return forecast, lower_bound, upper_bound
    
    def pytorch_forecast(self, ts_data: pd.DataFrame, input_size: int = 7, hidden_size: int = 16, epochs: int = 100) -> Tuple[List[float], List[float], List[float]]:
        """Generate forecast using a PyTorch neural network for epidemic time series"""
        values = ts_data['y'].values
        n = len(values)
        
        if n < input_size + 1:
            # Not enough data, return flat forecast
            last_value = values[-1] if n > 0 else 0
            forecast = [last_value] * self.forecast_days
            lower_bound = [max(0, last_value * 0.7)] * self.forecast_days
            upper_bound = [last_value * 1.3] * self.forecast_days
            return forecast, lower_bound, upper_bound
        
        # Prepare data for PyTorch
        X, y = [], []
        for i in range(len(values) - input_size):
            X.append(values[i:i+input_size])
            y.append(values[i+input_size])
        
        X = torch.tensor(X, dtype=torch.float32)
        y = torch.tensor(y, dtype=torch.float32).view(-1, 1)
        
        # Create and train model
        model = EpidemicTimeSeriesModel(input_size, hidden_size, 1)
        criterion = nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
        
        # Training loop
        model.train()
        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = model(X)
            loss = criterion(outputs, y)
            loss.backward()
            optimizer.step()
        
        # Generate forecast
        forecast = []
        current_input = values[-input_size:].copy()
        
        for i in range(self.forecast_days):
            # Prepare input tensor
            input_tensor = torch.tensor([current_input], dtype=torch.float32)
            
            # Get prediction
            model.eval()
            with torch.no_grad():
                prediction = model(input_tensor).item()
            
            # Ensure non-negative values
            prediction = max(0, prediction)
            forecast.append(prediction)
            
            # Update input for next prediction
            current_input = np.append(current_input[1:], prediction)
        
        # Calculate confidence intervals based on model error
        model.eval()
        with torch.no_grad():
            predictions = model(X).numpy().flatten()
            actuals = y.numpy().flatten()
            mae = np.mean(np.abs(predictions - actuals))
        
        # Wider confidence intervals for longer forecasts
        lower_bound = [max(0, f - 1.96 * mae * (1 + i/180)) for i, f in enumerate(forecast)]
        upper_bound = [f + 1.96 * mae * (1 + i/180) for i, f in enumerate(forecast)]
        
        return forecast, lower_bound, upper_bound
    
    def generate_forecast(self, data: pd.DataFrame, disease: str, country: str, metric: str = 'new_cases', use_pytorch: bool = False) -> Dict:
        """Generate 6-month forecast for a specific country and disease"""
        ts_data = self.prepare_country_data(data, disease, country, metric)
        
        if ts_data.empty:
            return {
                'success': False,
                'message': f'Insufficient data for {country} - {disease}',
                'forecast_dates': [],
                'forecast_values': [],
                'lower_bound': [],
                'upper_bound': []
            }
        
        # Generate forecast using selected method
        if use_pytorch:
            forecast_values, lower_bound, upper_bound = self.pytorch_forecast(ts_data)
            method = "PyTorch Neural Network"
        else:
            forecast_values, lower_bound, upper_bound = self.exponential_smoothing_forecast(ts_data)
            method = "Exponential Smoothing"
        
        # Create future dates
        last_date = ts_data['date'].max()
        forecast_dates = [last_date + timedelta(days=i+1) for i in range(self.forecast_days)]
        
        return {
            'success': True,
            'country': country,
            'disease': disease,
            'metric': metric,
            'last_date': last_date,
            'forecast_dates': forecast_dates,
            'forecast_values': forecast_values,
            'lower_bound': lower_bound,
            'upper_bound': upper_bound,
            'historical_data': ts_data.to_dict('records'),
            'forecast_method': method
        }
    
    def batch_forecast(self, data: pd.DataFrame, disease: str, countries: List[str], metric: str = 'new_cases', use_pytorch: bool = False) -> Dict[str, Dict]:
        """Generate forecasts for multiple countries"""
        results = {}
        
        for country in countries:
            try:
                forecast = self.generate_forecast(data, disease, country, metric, use_pytorch)
                results[country] = forecast
            except Exception as e:
                results[country] = {
                    'success': False,
                    'message': f'Error forecasting for {country}: {str(e)}',
                    'forecast_dates': [],
                    'forecast_values': [],
                    'lower_bound': [],
                    'upper_bound': []
                }
        
        return results

    def project_to_current_year(self, data: pd.DataFrame, disease: str, country: str, metric: str = 'new_cases', target_year: int = 2025, use_pytorch: bool = False) -> Dict:
        """Project historical epidemic patterns to a target year (e.g., 2025)"""
        ts_data = self.prepare_country_data(data, disease, country, metric)
        
        if ts_data.empty:
            return {
                'success': False,
                'message': f'Insufficient data for {country} - {disease}',
                'projected_dates': [],
                'projected_values': [],
                'forecast_dates': [],
                'forecast_values': [],
                'lower_bound': [],
                'upper_bound': []
            }
        
        # Get the original time series pattern
        original_dates = ts_data['date'].values
        original_values = ts_data['y'].values
        
        # Calculate the duration of the original outbreak
        start_date = ts_data['date'].min()
        end_date = ts_data['date'].max()
        duration_days = (end_date - start_date).days
        
        # Create new dates starting from target year
        new_start_date = datetime(target_year, 1, 1)
        projected_dates = [new_start_date + timedelta(days=i) for i in range(len(original_values))]
        
        # Keep the same values but with new dates
        projected_values = original_values.tolist()
        
        # Generate forecast from the end of projected data
        projected_ts_data = pd.DataFrame({
            'date': projected_dates,
            'y': projected_values
        })
        
        # Generate 6-month forecast from the projected data
        if use_pytorch:
            forecast_values, lower_bound, upper_bound = self.pytorch_forecast(projected_ts_data)
            method = "PyTorch Neural Network"
        else:
            forecast_values, lower_bound, upper_bound = self.exponential_smoothing_forecast(projected_ts_data)
            method = "Exponential Smoothing"
        
        # Create future dates from end of projected period
        last_projected_date = projected_dates[-1]
        forecast_dates = [last_projected_date + timedelta(days=i+1) for i in range(self.forecast_days)]
        
        return {
            'success': True,
            'country': country,
            'disease': disease,
            'metric': metric,
            'target_year': target_year,
            'original_period': f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}",
            'projected_dates': projected_dates,
            'projected_values': projected_values,
            'forecast_dates': forecast_dates,
            'forecast_values': forecast_values,
            'lower_bound': lower_bound,
            'upper_bound': upper_bound,
            'duration_days': duration_days,
            'forecast_method': method
        }
    
    def batch_project_to_current_year(self, data: pd.DataFrame, disease: str, countries: List[str], metric: str = 'new_cases', target_year: int = 2025, use_pytorch: bool = False) -> Dict[str, Dict]:
        """Project multiple countries to a target year"""
        results = {}
        
        for country in countries:
            try:
                projection = self.project_to_current_year(data, disease, country, metric, target_year, use_pytorch)
                results[country] = projection
            except Exception as e:
                results[country] = {
                    'success': False,
                    'message': f'Error projecting {country} to {target_year}: {str(e)}',
                    'projected_dates': [],
                    'projected_values': [],
                    'forecast_dates': [],
                    'forecast_values': [],
                    'lower_bound': [],
                    'upper_bound': []
                }
        
        return results

class InsightGenerator:
    """
    Generate human-readable insights from forecast data
    """
    
    def __init__(self):
        self.significance_threshold = 0.1  # 10% change threshold
    
    def calculate_trend_metrics(self, forecast_data: Dict) -> Dict:
        """Calculate trend metrics from forecast data"""
        if not forecast_data['success']:
            return {'trend': 'insufficient_data', 'confidence': 'low'}
        
        forecast_values = forecast_data['forecast_values']
        if not forecast_values:
            return {'trend': 'no_forecast', 'confidence': 'low'}
        
        # Calculate trends at different time horizons
        current_value = forecast_values[0]
        one_month = forecast_values[29] if len(forecast_values) > 29 else forecast_values[-1]
        three_month = forecast_values[89] if len(forecast_values) > 89 else forecast_values[-1]
        six_month = forecast_values[-1]
        
        # Calculate percentage changes
        one_month_change = ((one_month - current_value) / max(current_value, 1)) * 100
        three_month_change = ((three_month - current_value) / max(current_value, 1)) * 100
        six_month_change = ((six_month - current_value) / max(current_value, 1)) * 100
        
        # Determine trend direction
        if abs(one_month_change) < self.significance_threshold * 100:
            trend = 'stable'
        elif one_month_change > 0:
            trend = 'increasing'
        else:
            trend = 'decreasing'
        
        # Calculate confidence based on data quality
        historical_data = forecast_data.get('historical_data', [])
        data_points = len(historical_data)
        
        if data_points >= 30:
            confidence = 'high'
        elif data_points >= 14:
            confidence = 'medium'
        else:
            confidence = 'low'
        
        return {
            'trend': trend,
            'confidence': confidence,
            'one_month_change': one_month_change,
            'three_month_change': three_month_change,
            'six_month_change': six_month_change,
            'current_value': current_value,
            'peak_value': max(forecast_values),
            'peak_day': forecast_values.index(max(forecast_values)) + 1
        }
    
    def generate_insight_text(self, country: str, disease: str, metrics: Dict, metric_name: str = 'new cases') -> str:
        """Generate human-readable insight text"""
        if metrics['trend'] == 'insufficient_data':
            return f"{country}: Insufficient data for reliable {disease} forecast"
        
        if metrics['trend'] == 'no_forecast':
            return f"{country}: Unable to generate {disease} forecast"
        
        # Format the insight based on trend and timeframe
        change_1m = metrics['one_month_change']
        change_3m = metrics['three_month_change']
        
        # Choose the most relevant timeframe
        if abs(change_1m) > abs(change_3m):
            primary_change = change_1m
            timeframe = "next month"
        else:
            primary_change = change_3m
            timeframe = "next 3 months"
        
        # Format percentage
        change_str = f"{abs(primary_change):.0f}%"
        direction = "increase" if primary_change > 0 else "decrease"
        
        # Add confidence indicator
        confidence_text = ""
        if metrics['confidence'] == 'low':
            confidence_text = " (low confidence)"
        elif metrics['confidence'] == 'high':
            confidence_text = " (high confidence)"
        
        # Generate insight
        if abs(primary_change) < self.significance_threshold * 100:
            return f"{country}: {disease} {metric_name} expected to remain stable in {timeframe}{confidence_text}"
        else:
            return f"{country}: {change_str} {direction} in {disease} {metric_name} forecast for {timeframe}{confidence_text}"
    
    def generate_batch_insights(self, forecast_results: Dict[str, Dict], disease: str, metric_name: str = 'new cases') -> List[Dict]:
        """Generate insights for multiple countries"""
        insights = []
        
        for country, forecast_data in forecast_results.items():
            metrics = self.calculate_trend_metrics(forecast_data)
            insight_text = self.generate_insight_text(country, disease, metrics, metric_name)
            
            insights.append({
                'country': country,
                'disease': disease,
                'insight': insight_text,
                'trend': metrics['trend'],
                'confidence': metrics['confidence'],
                'change_1m': metrics.get('one_month_change', 0),
                'change_3m': metrics.get('three_month_change', 0)
            })
        
        # Sort by significance (largest absolute change first)
        insights.sort(key=lambda x: abs(x['change_1m']), reverse=True)
        
        return insights 