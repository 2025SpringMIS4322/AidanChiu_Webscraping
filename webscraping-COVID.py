# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

##############FOR MACS THAT HAVE CERTIFICATE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

##############FOR PCs THAT HAVE CERTIFICATE ERRORS LOOK HERE################
## https://support.chainstack.com/hc/en-us/articles/9117198436249-Common-SSL-Issues-on-Python-and-How-to-Fix-it

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers) # Request returns back entire webpage

webpage = urlopen(req).read() # Load entire contents of URL. Pass to BeautifulSoup Library
soup = BeautifulSoup(webpage, 'html.parser') # Use BeautifulSoup Class to begin scraping
# '.parser' = split apart entire webpage based on website TAGS

print(soup.title.text) # Returns '<title>' from website --> "view page source". Extracts text from '<title>' tag as viewed on 'view page source'
print()

# Return table rows for "california"
table_rows = soup.findAll("tr") 
#print(table_rows[2])            



#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)              RETURNS ONLY FIRST OCCURANCE OF SOMETHING
# findAll(tag, attributes, recursive, text, limit, keywords)    RETURNS ALL OCCURANCES OF SOMETHING (Output is an iterable LIST)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

# Display the states with the highest and lowest death ratios
state_highest_death_ratio = '' #Pennsylvania
highest_death_ratio = 0.0
state_lowest_death_ratio = '' #Alaska
lowest_death_ratio = 1000.0


for row in table_rows[2:53]: # Covers from row 3 (California) through the rest of the 50 states
    td = row.findAll("td") #Search thru <td> tags
    #print(td)'
    try:
        state = td[1].text.strip() # State name location on website at index[1]. '.strip' removes unnecessary spaces
        total_cases = int(td[2].text.replace(',',''))   # '.replace' replaces something with something else. I.e. here: Replace ',' with nothing ''
        total_deaths = int(td[3].text.replace(',',''))
        total_recovered = int(td[4].text.replace(',',''))
        population = td[7].text.replace(',','').strip()
    except:
        print(f"{state} is missing data")  # This Try/Except function removes states with data that doesn't match parameters.

    print(f"State: {state}")
    print(f"Total cases: {total_cases}")
    print(f"Total deaths: {total_deaths}")
    print(f"Total recovered: {total_recovered}")
    print(f"Population: {population}")

    death_ratio = (total_deaths) / (total_cases)
    recovery_ratio = (total_recovered) / (total_cases)

    print(f"State death ratio: {death_ratio}")
    print(f"State recovery ratio: {recovery_ratio}")
    print()

    # Check for highest death ratio
    if death_ratio > highest_death_ratio:
        highest_death_ratio = death_ratio
        state_highest_death_ratio = state

    # Check for highest death ratio
    if death_ratio < lowest_death_ratio:
        lowest_death_ratio = death_ratio
        state_lowest_death_ratio = state

# Display the states with the highest and lowest death ratios
print(f"The state with the highest death ratio is: {state_highest_death_ratio}")
print(f"Death ratio: {highest_death_ratio:.2%}\n")
print(f"The state with the lowest death ratio is: {state_lowest_death_ratio}")
print(f"Death ratio: {lowest_death_ratio:.2%}\n")

