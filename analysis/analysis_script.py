import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'data/medical_raw_data.csv'
data = pd.read_csv(file_path)

# Drop rows with missing values in relevant columns
clean_data = data.dropna(subset=['State', 'Area', 'ReAdmis'])

# Calculate readmission rates by state
readmission_by_state = clean_data.groupby('State')['ReAdmis'].value_counts(normalize=True).unstack().fillna(0)
readmission_by_state['readmission_rate'] = readmission_by_state['Yes'] * 100

# Save the results to a CSV file
readmission_by_state[['readmission_rate']].to_csv('analysis/results/readmission_rates_by_state.csv')

# Calculate readmission rates by area type
readmission_by_area = clean_data.groupby('Area')['ReAdmis'].value_counts(normalize=True).unstack().fillna(0)
readmission_by_area['readmission_rate'] = readmission_by_area['Yes'] * 100

# Save the results to a CSV file
readmission_by_area[['readmission_rate']].to_csv('analysis/results/readmission_rates_by_area.csv')

# Plot readmission rates by state
plt.figure(figsize=(12, 8))
readmission_by_state[['readmission_rate']].sort_values(by='readmission_rate', ascending=False).plot(kind='bar', legend=None)
plt.title('Readmission Rates by State')
plt.xlabel('State')
plt.ylabel('Readmission Rate (%)')
plt.tight_layout()
plt.savefig('analysis/results/readmission_rates_by_state.png')
plt.close()

# Plot readmission rates by area type
plt.figure(figsize=(8, 6))
readmission_by_area[['readmission_rate']].sort_values(by='readmission_rate', ascending=False).plot(kind='bar', legend=None)
plt.title('Readmission Rates by Area Type')
plt.xlabel('Area Type')
plt.ylabel('Readmission Rate (%)')
plt.tight_layout()
plt.savefig('analysis/results/readmission_rates_by_area.png')
plt.close()

print("Analysis complete. Results and charts saved in 'analysis/results' directory.")

