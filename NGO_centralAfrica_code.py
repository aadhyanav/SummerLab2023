import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib3

urllib3.disable_warnings()
url = "https://www.spong-rca.org/ong-agreees/" #URL link
page = requests.get(url, verify=False) 
soup = BeautifulSoup(page.text, 'lxml') #HTML parser
tables = soup.find_all('table') 

data_rows = []  # List to store data rows

for table in tables:
    rows = table.find_all('tr')  # Find all rows within the table
    for row in rows[1:]:  # Skip the header row
        row_cells = row.find_all(['th', 'td'])  # Find cells within the row
        row_data = [cell.get_text(strip=True) for cell in row_cells]
        data_rows.append(row_data)

# Create a DataFrame using the collected data
headers = [cell.get_text(strip=True) for cell in tables[0].find('tr').find_all(['th', 'td'])]
mydata = pd.DataFrame(data_rows, columns=headers)

mydata.to_csv('NGODirectory_CentralAfrica_FRENCH.csv', index=False)
