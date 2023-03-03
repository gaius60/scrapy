import pandas as pd
import requests
from bs4 import BeautifulSoup

# Replace the file name and sheet name with your Excel file and sheet name
df = pd.read_excel("links.xlsx", sheet_name="Sheet1")

# Initialize an empty list to store all the words
all_words = []

# Loop through all the links in the Excel file
for link in df["Links"]:
    # Send a GET request to the link and get the HTML content
    response = requests.get(link)
    html_content = response.text

    # Use BeautifulSoup to parse the HTML content and extract the words
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()
    words = text.split()

    # Add the words to the list of all words
    all_words.extend(words)

# Join all the words into a comma-separated string
text = ",".join(all_words)

# Save the text to a text file
with open("words.doc", "w") as f:
    f.write(text)

