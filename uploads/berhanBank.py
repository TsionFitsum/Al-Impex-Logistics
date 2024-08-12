from selenium import webdriver
from bs4 import BeautifulSoup

# Setup Selenium WebDriver
driver = webdriver.Chrome()
driver.get('https://berhanbanksc.com/exchange-rates/')

# Get page source after rendering
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# Extract exchange rate data
rates = []
rows = soup.find_all('div', class_='row customRow mb-2')

for row in rows:
    columns = row.find_all('div', class_='col-6')
    if columns:
        currency = columns[0].find_all('span')[1].get_text(strip=True)
        buy_rate = row.find_all('div', class_='col-3')[0].get_text(strip=True)
        sell_rate = row.find_all('div', class_='col-3')[1].get_text(strip=True)
        rates.append((currency, buy_rate, sell_rate)) 

print(rates)
