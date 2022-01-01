from bs4 import BeautifulSoup
import time 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def get_data(url):
    s = Service('C:\\selenium\\chromedriver_win32\\chromedriver.exe')
    option = Options()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service = s,chrome_options=option)
    driver.maximize_window()
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source , 'html.parser')
    return soup

'''Extracting Product Lists'''
def all_pages():
    base_url = "https://www.toolstation.com/search?q=dewalt&promo_name=StaticPage&promo_id=DeWaltSP&promo_creative=DeWaltViewAll&promo_position=DeWaltTopBanner"
    pages = [base_url]
    for x in range(2,3):
        str = f"https://www.toolstation.com/search?q=dewalt&promo_name=StaticPage&promo_id=DeWaltSP&promo_creative=DeWaltViewAll&promo_position=DeWaltTopBanner&page={x}"
        pages.append(str)
    return pages

total_pages = all_pages()

products = []
links = []
for page in total_pages:
    soup = get_data(page)
    data = soup.find_all('div' ,class_='product-name')
    for y in data:
        name = y.find('a').get_text().strip()
        link = y.find('a')
        products.append(name)
        links.append(link['href'])
    
Product_list = {'name' :products , 'url':links}
df = pd.DataFrame(Product_list)
df.to_csv('data.csv')
print(df.head())



