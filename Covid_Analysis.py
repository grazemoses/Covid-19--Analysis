# COVID-19 India Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# Filter data for India
india_df = df[df['location'] == 'India'].copy()
india_df['date'] = pd.to_datetime(india_df['date'])

# Keep only necessary columns
india_df = india_df[['date', 'new_cases', 'total_cases', 'new_deaths', 'total_deaths']]

# Basic info
print("Latest Date:", india_df['date'].max())
print(india_df.tail())

# Plot daily new cases
plt.figure(figsize=(12, 6))
sns.lineplot(data=india_df, x='date', y='new_cases', label='Daily New Cases', color='blue')
plt.title("Daily New COVID-19 Cases in India")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot total cases
plt.figure(figsize=(12, 6))
sns.lineplot(data=india_df, x='date', y='total_cases', label='Total Cases', color='green')
plt.title("Total COVID-19 Cases in India Over Time")
plt.xlabel("Date")
plt.ylabel("Cumulative Cases")
plt.grid(True)
plt.tight_layout()
plt.show()

# Moving average (7-day)
india_df['7_day_avg'] = india_df['new_cases'].rolling(window=7).mean()

plt.figure(figsize=(12, 6))
sns.lineplot(data=india_df, x='date', y='new_cases', label='Daily New Cases', alpha=0.4)
sns.lineplot(data=india_df, x='date', y='7_day_avg', label='7-Day Moving Average', color='red')
plt.title("Daily Cases and 7-Day Average - India")
plt.xlabel("Date")
plt.ylabel("Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Summary statistics
summary = india_df.describe()
print("\nSummary Statistics:")
print(summary[['new_cases', 'new_deaths']])
