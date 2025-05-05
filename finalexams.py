from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

url = 'https://registrar.web.baylor.edu/exams-grading/spring-2025-final-exam-schedule'
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


tables = soup.findAll('table')
finals_table = tables[1] # regular finals table

tr = finals_table.findAll('tr')

infile = open('myclasses.csv', 'r')
csv_file = csv.reader(infile)

for rec in csv_file:
    my_class = rec[0]
    my_time = rec[1]

    for row in tr:
        td = row.findAll('td')
        if td:
            sch_class = td[0].text
            sch_time = td[1].text
            exam_day = td[2].text
            exam_time = td[3].text

            if my_class == sch_class and my_time == sch_time:
                print(f"My Class: {my_class},{my_time}, Exam: {exam_day},{exam_time}")



