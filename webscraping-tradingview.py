from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'

url = 'https://webull.com/quote/us/gainers'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers) # Request returns back entire webpage

webpage = urlopen(req).read() # Load entire contents of URL. Pass to BeautifulSoup Library
soup = BeautifulSoup(webpage, 'html.parser') # Use BeautifulSoup Class to begin scraping
# '.parser' = split apart entire webpage based on website TAGS

print(soup.title.text)

# Get stock data only
stock_data = soup.findAll('div', class_ = 'table-cell') # findAll() function finds tags and classes.  class_ is a function, not an actual class
#print(stock_data[1])

# get names of companies
counter = 1 # why use counter? Must work down each row. Makes life easier
for x in range(5):
    name = stock_data[counter]
    name = name.findAll('p', class_ = 'txt')[1].text
    change = float(stock_data[counter+2].text.strip('+').strip('%'))/100 
    last_price = float(stock_data[counter+3].text)
    prev_price = round(last_price / (1 + change), 2)
    print(f"Company name: {name}")
    print(f"Change: {change}")
    print(f"Last Price: {last_price}")
    print(f"Previous Price: {prev_price}")
    print()
    print()

    counter += 11 # utilizes counter to move down to next row, after running through indexes [1-12] for first row on website.
    # Ex. Since there are 12 indexes for all of the first row on the website URL, we'll have the for loop run thru all 12 of those indexes before moving down to row 2

# FInd vs findAll:
    # Find --> gives FIRST occurrance of a tag
    # FindAll --> Gives EVERY occurrance in every tag. Returns list