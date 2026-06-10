import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. The target website URL
url = "https://toscrape.com"

print("Connecting to the website...")
response = requests.get(url)

# 2. Check if the website responded successfully (Status Code 200 means OK)
if response.status_code == 200:
    print("Connection successful! Parsing HTML...")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Storage lists for our scraped data
    quotes_list = []
    authors_list = []
    
    # 3. Find all quote elements on the page
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    
    # 4. Clean the data and loop through it
    for q, a in zip(quotes, authors):
        quotes_list.append(q.text.strip())
        authors_list.append(a.text.strip())
        
    # 5. Structure the data into a table using Pandas
    data = {
        'Famous Quote': quotes_list, 
        'Author Name': authors_list
    }
    df = pd.DataFrame(data)
    
    # 6. Save the table directly to an Excel file
    excel_filename = 'scraped_quotes.xlsx'
    df.to_excel(excel_filename, index=False)
    
    print(f"🎉 Success! Data cleanly saved to '{excel_filename}' inside your folder.")
else:
    print(f"❌ Failed to fetch data. Error code: {response.status_code}")
