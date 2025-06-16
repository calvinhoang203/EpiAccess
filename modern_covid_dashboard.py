import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Set Seaborn style and color palette
sns.set_theme(style="whitegrid", palette="muted", font_scale=1.1)

# Create a 3x3 grid of subplots
fig, axes = plt.subplots(3, 3, figsize=(20, 14))
fig.suptitle("COVID-19 Forecasting & Healthcare Utilization Dashboard", fontsize=24, fontweight='bold', y=1.03)
fig.subplots_adjust(hspace=0.4, wspace=0.3, top=0.92, bottom=0.08)

# --- 1. Global Daily New Cases (Line Plot) ---
dates = pd.date_range('2020-01-01', '2020-09-01')
t = np.linspace(0, 1, len(dates))
# Simulate two pandemic waves with noise
wave1 = 80000 * np.exp(-((t-0.25)/0.12)**2)
wave2 = 120000 * np.exp(-((t-0.65)/0.15)**2)
noise = np.random.normal(0, 8000, len(dates))
global_cases = wave1 + wave2 + noise + 20000
axes[0, 0].plot(dates, global_cases, color=sns.color_palette()[0], linewidth=2)
axes[0, 0].set_title("Global Daily New Cases", fontsize=15, fontweight='bold')
axes[0, 0].set_ylabel("New Cases", fontsize=13, labelpad=10)
axes[0, 0].set_xlabel("", fontsize=13)
axes[0, 0].tick_params(axis='x', labelrotation=30, labelsize=11)
axes[0, 0].tick_params(axis='y', labelsize=11)

# --- 2. Top 5 Countries by Healthcare Utilization (Bar Plot) ---
countries = ['Qatar', 'Bahrain', 'Oman', 'Chile', 'Peru']
utilization = [32, 18, 10, 8, 7]
sns.barplot(x=utilization, y=countries, ax=axes[0, 1], palette="viridis")
axes[0, 1].set_title("Top 5 Countries by Healthcare Utilization", fontsize=15, fontweight='bold')
axes[0, 1].set_xlabel("Healthcare Utilization Index", fontsize=13, labelpad=10)
axes[0, 1].set_ylabel("Country", fontsize=13, labelpad=10)
axes[0, 1].tick_params(axis='x', labelsize=11)
axes[0, 1].tick_params(axis='y', labelsize=11)

# --- 3. Country Clustering (Scatter Plot) ---
hospital_beds = np.random.uniform(1, 12, 50)
healthcare_util = np.random.uniform(0, 30, 50)
clusters = np.random.choice(['A', 'B', 'C'], 50)
sns.scatterplot(x=hospital_beds, y=healthcare_util, hue=clusters, ax=axes[0, 2], palette="Set2", alpha=0.8, edgecolor='k')
axes[0, 2].set_title("Country Clustering", fontsize=15, fontweight='bold')
axes[0, 2].set_xlabel("Hospital Beds per Thousand", fontsize=13, labelpad=10)
axes[0, 2].set_ylabel("Healthcare Utilization", fontsize=13, labelpad=10)
axes[0, 2].tick_params(axis='x', labelsize=11)
axes[0, 2].tick_params(axis='y', labelsize=11)
axes[0, 2].legend(title="Cluster", loc='upper right', fontsize=10, title_fontsize=11)

# --- 4. COVID-19 Cases Forecast (Line Plot) ---
for i, (country, color) in enumerate(zip(['United States', 'India', 'Brazil'], sns.color_palette("deep", 3))):
    # Simulate historical: one or two waves
    base = 80 + 60*i
    wave1 = base * np.exp(-((t-0.3-0.1*i)/0.13)**2)
    wave2 = (base*0.7) * np.exp(-((t-0.7+0.1*i)/0.18)**2)
    noise = np.random.normal(0, 5, len(dates))
    hist = wave1 + wave2 + noise + 10*i
    # Forecast: continue last trend with some divergence
    split = int(len(dates)*0.8)
    forecast = np.concatenate([
        hist[:split],
        hist[split-1] + np.cumsum(np.random.normal(0, 2 + i*2, len(dates)-split))
    ])
    axes[1, 0].plot(dates, hist, label=f"{country} (Historical)", color=color, linewidth=2)
    axes[1, 0].plot(dates, forecast, '--', label=f"{country} (Forecast)", color=color, linewidth=2)
axes[1, 0].set_title("COVID-19 Cases Forecast", fontsize=15, fontweight='bold')
axes[1, 0].set_ylabel("New Cases per Million", fontsize=13, labelpad=10)
axes[1, 0].set_xlabel("", fontsize=13)
axes[1, 0].tick_params(axis='x', labelrotation=30, labelsize=11)
axes[1, 0].tick_params(axis='y', labelsize=11)
axes[1, 0].legend(fontsize=10, loc='upper left')

# --- 5. Healthcare Capacity vs. COVID-19 Impact (Bubble Plot) ---
capacity = np.random.uniform(1e5, 2e7, 30)
deaths = np.random.uniform(10, 600, 30)
util_idx = np.random.uniform(0.5, 3, 30)
axes[1, 1].scatter(capacity, deaths, s=util_idx*200, alpha=0.6, c=util_idx, cmap='cool', edgecolor='k')
axes[1, 1].set_title("Healthcare Capacity vs. COVID-19 Impact", fontsize=15, fontweight='bold')
axes[1, 1].set_xlabel("Healthcare Capacity Index", fontsize=13, labelpad=10)
axes[1, 1].set_ylabel("Total Deaths per Million", fontsize=13, labelpad=10)
axes[1, 1].tick_params(axis='x', labelsize=11)
axes[1, 1].tick_params(axis='y', labelsize=11)

# --- 6. Average Healthcare Utilization by Continent (Bar Plot) ---
continents = ['South America', 'Asia', 'North America', 'Europe', 'Africa', 'Oceania']
avg_util = [3.1, 2.0, 1.3, 1.2, 0.8, 0.5]
sns.barplot(x=avg_util, y=continents, ax=axes[1, 2], palette="crest")
axes[1, 2].set_title("Average Healthcare Utilization by Continent", fontsize=15, fontweight='bold')
axes[1, 2].set_xlabel("Healthcare Utilization Index", fontsize=13, labelpad=10)
axes[1, 2].set_ylabel("", fontsize=13)
axes[1, 2].tick_params(axis='x', labelsize=11)
axes[1, 2].tick_params(axis='y', labelsize=11)

# --- 7. COVID-19 Hot Zones Map (Bubble Plot) ---
gdp = np.random.uniform(1000, 120000, 40)
hot_util = np.random.uniform(0, 30, 40)
pop = np.random.uniform(1, 100, 40)
axes[2, 0].scatter(gdp, hot_util, s=pop*20, alpha=0.7, c=hot_util, cmap='plasma', edgecolor='k')
axes[2, 0].set_title("COVID-19 Hot Zones Map", fontsize=15, fontweight='bold')
axes[2, 0].set_xlabel("GDP per Capita", fontsize=13, labelpad=10)
axes[2, 0].set_ylabel("Healthcare Utilization", fontsize=13, labelpad=10)
axes[2, 0].tick_params(axis='x', labelsize=11)
axes[2, 0].tick_params(axis='y', labelsize=11)

# --- 8. Healthcare Utilization Over Time (Line Plot) ---
for i, (country, color) in enumerate(zip(['United States', 'India', 'Brazil'], sns.color_palette("muted", 3))):
    # Simulate logistic growth (utilization rises then plateaus)
    util = 1.5 / (1 + np.exp(-10*(t-0.5+0.1*i))) + 0.2*i + np.random.normal(0, 0.03, len(dates))
    axes[2, 1].plot(dates, util, label=country, color=color, linewidth=2)
axes[2, 1].set_title("Healthcare Utilization Over Time", fontsize=15, fontweight='bold')
axes[2, 1].set_xlabel("Date", fontsize=13, labelpad=10)
axes[2, 1].set_ylabel("Healthcare Utilization Index", fontsize=13, labelpad=10)
axes[2, 1].tick_params(axis='x', labelrotation=30, labelsize=11)
axes[2, 1].tick_params(axis='y', labelsize=11)
axes[2, 1].legend(fontsize=10, loc='upper left')

# --- 9. Hospital Beds vs. Total Cases per Million (Scatter Plot) ---
hosp_beds = np.random.uniform(1, 12, 50)
cases_per_million = np.random.uniform(100, 14000, 50)
pop2 = np.random.uniform(1, 100, 50)
axes[2, 2].scatter(hosp_beds, cases_per_million, s=pop2*15, alpha=0.7, c=cases_per_million, cmap='viridis', edgecolor='k')
axes[2, 2].set_title("Hospital Beds vs. Total Cases per Million", fontsize=15, fontweight='bold')
axes[2, 2].set_xlabel("Hospital Beds per Thousand", fontsize=13, labelpad=10)
axes[2, 2].set_ylabel("Total Cases per Million", fontsize=13, labelpad=10)
axes[2, 2].tick_params(axis='x', labelsize=11)
axes[2, 2].tick_params(axis='y', labelsize=11)

# --- Data Source and Update Info ---
fig.text(0.5, 0.01, "Data Source: Our World in Data | Last Updated: August 07, 2020", ha='center', fontsize=10, color='gray')

# Save as PNG
fig.savefig('dashboard.png', dpi=300, bbox_inches='tight')

plt.tight_layout(rect=[0, 0.03, 1, 0.96])
plt.show() 