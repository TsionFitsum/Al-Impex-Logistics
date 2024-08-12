from selenium import webdriver
from bs4 import BeautifulSoup

# Setup Selenium WebDriver
driver = webdriver.Chrome()
driver.get('https://combanketh.et/en/exchange-rate/')

# Get page source after rendering
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
# Find the correct HTML elements
# Replace 'your-table-class' with the actual class or ID for the table containing exchange rates
table = soup.find('table', {'class': 'text-left w-full'})

# If the table is found, extract the data
if table:
    rates = [] 
    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        if columns:
            currency = columns[0].get_text(strip=True)
            buy_rate = columns[1].get_text(strip=True)
            sell_rate = columns[2].get_text(strip=True)
            rates.append((currency, buy_rate, sell_rate))

    print(rates)
else:
    print("No table found. Check the table class or structure.")
