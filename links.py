import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the main URL of the website to scrape
main_url = "https://www.9awmya.tn/"

# Define the list of paths to include in the scraped links
include_paths = [
    "https://www.9awmya.tn/category/home/ajs/",
    "https://www.9awmya.tn/category/eco/",
    "https://www.9awmya.tn/category/estoir/",
    "https://www.9awmya.tn/category/%d8%b3%d9%8a%d8%a7%d8%b3%d8%a9/",
    "https://www.9awmya.tn/category/commun/",
    "https://www.9awmya.tn/category/library/"
]

# Initialize an empty list to store all the links
all_links = []

# Create a function to extract links
def extract_links(url):
    # Send a GET request to the URL and get the HTML content of the page
    response = requests.get(url)
    html = response.text

    # Use BeautifulSoup to parse the HTML content and extract all the links
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            for path in include_paths:
                if path in href:
                    links.add(href)
                    break

    return links

# Create a function to scrape a URL and all its links
def scrape(url):
    # Print a message to indicate which URL is being scraped
    print(f"Scraping {url}")

    # Extract all the links on the page
    links = extract_links(url)

    # Loop through each link on the page
    for link in links:
        # If the link is not already in the list and starts with the main URL, add it to the list and scrape it
        if link not in all_links and link.startswith(main_url):
            all_links.append(link)
            scrape(link)
        # If the link is outside the domain of the main URL, ignore it and continue with the next link
        elif not link.startswith(main_url):
            continue

# Start scraping the main URL and all its links
scrape(main_url)

# Create a Pandas dataframe from the list of links
df = pd.DataFrame(all_links, columns=["Links"])

# Save the dataframe to an Excel file
file_path = "links.xlsx"
df.to_excel(file_path, index=False)

# Print the number of links saved to the file
print(f"{len(all_links)} links saved to {file_path}")

