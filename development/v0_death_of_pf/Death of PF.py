# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Function to scrape usage rates for power forwards
def scrape_usage_rates(start_year, end_year, position='PF'):
    all_data = []

    for year in range(start_year, end_year + 1):
        url = f"https://www.basketball-reference.com/leagues/NBA_{year}_advanced.html"
        print(f"Scraping data for year: {year}")
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve data for year {year}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'id': 'advanced_stats'})

        if table is None:
            print(f"Table not found for year {year}")
            continue

        rows = table.find_all('tr')

        for row in rows[1:]:
            cells = row.find_all('td')
            if cells:
                player_position = cells[3].text  # Position column
                if position in player_position:
                    data = [cell.text for cell in cells]
                    data.append(year)
                    all_data.append(data)

        # Be respectful to the website by adding a delay
        time.sleep(2)

    # Create DataFrame
    if all_data:
        columns = [th.text for th in table.find('thead').find_all('th')][1:]
        columns.append('Year')
        df = pd.DataFrame(all_data, columns=columns)
    else:
        df = pd.DataFrame()

    return df

# Scrape PF usage rates for 1990-2005 and 2020-2023
pf_usage_90s_00s = scrape_usage_rates(1990, 2005)
pf_usage_20s = scrape_usage_rates(2020, 2023)

print("1990-2005 DataFrame:")
print(pf_usage_90s_00s.head())

print("2020-2023 DataFrame:")
print(pf_usage_20s.head())


# Save to CSV if DataFrames are not empty
if not pf_usage_90s_00s.empty:
    pf_usage_90s_00s.to_csv('pf_usage_90s_00s.csv', index=False)
    print("Saved pf_usage_90s_00s.csv")

if not pf_usage_20s.empty:
    pf_usage_20s.to_csv('pf_usage_20s.csv', index=False)
    print("Saved pf_usage_20s.csv")

# Load the CSV files into DataFrames
pf_usage_90s_00s = pd.read_csv('pf_usage_90s_00s.csv')
pf_usage_20s = pd.read_csv('pf_usage_20s.csv')

# Display the first few rows of each DataFrame
print("Power Forwards Usage Rates (1990-2005):")
print(pf_usage_90s_00s.head())

print("\nPower Forwards Usage Rates (2020-2023):")
print(pf_usage_20s.head())

# Drop rows with missing values
pf_usage_90s_00s.dropna(inplace=True)
pf_usage_20s.dropna(inplace=True)

# Ensure the data types are correct
print("\nData Types for 1990-2005 Data:")
print(pf_usage_90s_00s.dtypes)

print("\nData Types for 2020-2023 Data:")
print(pf_usage_20s.dtypes)

# Visualization of Average Usage Rate Over Time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='USG%', data=pf_usage_90s_00s, label='1990-2005')
sns.lineplot(x='Year', y='USG%', data=pf_usage_20s, label='2020-2023')

plt.title('Average Usage Rate of Power Forwards Over Time')
plt.xlabel('Year')
plt.ylabel('Usage Rate (USG%)')
plt.legend()
plt.grid(True)
plt.show()

# Distribution of Heights for Power Forwards
plt.figure(figsize=(10, 6))
sns.histplot(pf_usage_90s_00s['Ht'], label='1990-2005', color='blue', kde=True)
sns.histplot(pf_usage_20s['Ht'], label='2020-2023', color='orange', kde=True)

plt.title('Distribution of Heights for Power Forwards')
plt.xlabel('Height')
plt.legend()
plt.show()

# Distribution of Weights for Power Forwards
plt.figure(figsize=(10, 6))
sns.histplot(pf_usage_90s_00s['Wt'], label='1990-2005', color='blue', kde=True)
sns.histplot(pf_usage_20s['Wt'], label='2020-2023', color='orange', kde=True)

plt.title('Distribution of Weights for Power Forwards')
plt.xlabel('Weight')
plt.legend()
plt.show()

# Comment out these lines for now
# pf_usage_90s_00s = pd.read_csv('pf_usage_90s_00s.csv')
# pf_usage_20s = pd.read_csv('pf_usage_20s.csv')

# Leave the scraping part to run
pf_usage_90s_00s = scrape_usage_rates(1990, 2005)
pf_usage_20s = scrape_usage_rates(2020, 2023)

# Save the scraped data
if not pf_usage_90s_00s.empty:
    pf_usage_90s_00s.to_csv('pf_usage_90s_00s.csv', index=False)
    print("Saved pf_usage_90s_00s.csv")

if not pf_usage_20s.empty:
    pf_usage_20s.to_csv('pf_usage_20s.csv', index=False)
    print("Saved pf_usage_20s.csv")



# %%



