import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3

urllib3.disable_warnings()
def scrape_and_save(url, filename):
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')

    table = soup.find('table')

    headers = []
    for th in table.find_all('th'):
        title = th.text
        headers.append(title)

    data = []

    for row in table.find_all('tr')[1:]:
        row_data = row.find_all('td')
        row_values = [td.text for td in row_data]
        data.append(row_values)
    print("Headers:", headers)
    print("Row Values:", row_values)

    df = pd.DataFrame(data, columns=headers)

    df.to_csv(filename, index=False)
    print(f"Data from {url} has been scraped and saved as {filename}")

# Scrape and save data from the second URL
international_url = "https://www.spong-rca.org/ong-agreees/"
international_filename = "CentralAfrica_NGOs.csv"
scrape_and_save(international_url, international_filename)
