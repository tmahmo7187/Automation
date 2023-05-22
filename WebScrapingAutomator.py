import requests
from bs4 import BeautifulSoup

# URL of the web page to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract specific data from the web page
    # Example: Scraping all the headlines from an HTML page
    headlines = soup.find_all('h1')

    # Print the extracted headlines
    for headline in headlines:
        print(headline.text)
else:
    print(f"Request failed with status code: {response.status_code}")
