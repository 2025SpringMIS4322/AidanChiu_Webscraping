import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


random_chapter = random.randrange(1,22) # pick random chapter from BOJ chapter 1 - 21

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter) # Convert to string



url = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)


# Grab all verses from page
page_verses = soup.findAll('div', class_ = 'p')

myverses = [] # list

for section_verses in page_verses: # Create list of verses and extract one at a time
    verse_list = section_verses.text.split('.')

    # Add one verse at a time
    for v in verse_list:
        myverses.append(v)

# Pick one, out of returned verses
my_choice = random.choice(myverses)
my_choice = f"Chapter: {random_chapter}    Verse: {my_choice}"
print(my_choice)


#  MY VONAGE REFUSES TO LET ME SIGN IN
#vonage_client = Vonage(auth=Auth(api_key=, api_secret=))
#message = SmsMessage(to='17148868113', from_=, text=my_choice)
#response: SmsResponse = vonage_client.sms.send(message)

#print(response.model_dump(exclude_unset=True))