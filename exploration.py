import pandas as pd
import numpy as np
import random
# Step 1: Load the dataset
file_path = 'data_set.csv'
data = pd.read_csv(file_path)

#  Step 1: Remove 2099 Data
cleaned_data = data[~data['event_date'].str.contains('2099')]

# Step 2: Handle Missing Values
# Drop rows where 'event_date' or 'venue_id' is missing
cleaned_data = cleaned_data.dropna(subset=['event_date', 'venue_id'])

# Fill missing values in 'availability_standard' with its median
cleaned_data['availability_standard'] = cleaned_data['availability_standard'].fillna(cleaned_data['availability_standard'].median())

# Fill missing values in 'availability_resale' with its median
cleaned_data['availability_resale'] = cleaned_data['availability_resale'].fillna(cleaned_data['availability_resale'].median())

# Fill missing values in 'capacity' with its median
cleaned_data['capacity'] = cleaned_data['capacity'].fillna(cleaned_data['capacity'].median())

# Step 3: Convert timestamp to datetime and standardize format
cleaned_data['timestamp'] = pd.to_datetime(cleaned_data['timestamp'], format='%Y_%m_%dT%H_%M_%S', errors='coerce')

# Step 4: Remove Outliers
# Define a threshold for availability
threshold = cleaned_data['availability_standard'].quantile(0.99)
cleaned_data = cleaned_data[cleaned_data['availability_standard'] < threshold]

# Print the dataset after outlier removal
print("After removing outliers:")
print(cleaned_data.head())

# Print dataset summary
print("\nDataset Summary:")
print(cleaned_data.describe())
print(cleaned_data.info())

# List of categories for events
categories = ['Concerts', 'Sports', 'Theater', 'Opera', 'Comedy Shows', 'Festivals', 'Miscellaneous']

# Get the unique show_ids
unique_show_ids = data['show_id'].unique()

# Randomly assign each show_id to a category
show_id_to_category = {show_id: random.choice(categories) for show_id in unique_show_ids}

# Create a new column for event categories
data['event_category'] = data['show_id'].map(show_id_to_category)

# Save the updated categorized dataset
data.to_csv('categorized_events_dataset_updated.csv', index=False)
print("\nThe dataset has been categorized and saved to 'categorized_events_dataset_updated.csv'.")

# Function to generate synthetic data for the next decade
def generate_synthetic_data(cleaned_data, years=10):
    num_entries = len(cleaned_data)  # Number of synthetic entries to generate

    # Generate random years in the next decade (2025-2034)
    random_years = np.random.randint(2025, 2025 + years, size=num_entries)

    # Adjust event_date to include random years in the future
    event_dates = pd.to_datetime(np.random.choice(cleaned_data['event_date'], size=num_entries))
    event_dates_with_random_years = [date.replace(year=random.choice(random_years)) for date in event_dates]

    # Generate the synthetic data DataFrame
    synthetic_data = pd.DataFrame({
        'show_id': np.random.choice(cleaned_data['show_id'], size=num_entries),
        'timestamp': pd.to_datetime(np.random.choice(cleaned_data['timestamp'], size=num_entries)).strftime('%Y-%m-%d %H:%M:%S'),
        'section_id': np.random.choice(cleaned_data['section_id'], size=num_entries),
        'availability_standard': np.random.choice(cleaned_data['availability_standard'], size=num_entries),
        'availability_resale': np.random.choice(cleaned_data['availability_resale'], size=num_entries),
        'capacity': np.random.choice(cleaned_data['capacity'], size=num_entries),
        'event_date': event_dates_with_random_years,
        'venue_id': np.random.choice(cleaned_data['venue_id'], size=num_entries),
        'event_time_zone': np.random.choice(cleaned_data['event_time_zone'], size=num_entries)
    })

    return synthetic_data

# Generate synthetic data for the next 10 years
synthetic_data = generate_synthetic_data(cleaned_data, years=10)
print(synthetic_data.head())

# Save synthetic data to a CSV file
synthetic_data.to_csv('synthetic_data_next_decade.csv', index=False)
print("Synthetic data for the next decade saved to 'synthetic_data_next_decade.csv'.")