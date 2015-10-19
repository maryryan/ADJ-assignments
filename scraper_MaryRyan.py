import urllib2, mechanize, csv
from bs4 import BeautifulSoup
#set default encoding to utf-8 to deal with \xa0
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#set up the output csv
output = open('election2014.csv', 'w')
writer = csv.writer(output)

#open the page
br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/')

#select the form to choose the auditor race
formcount=0
for frm in br.forms():  
    if str(frm.attrs["id"])=="Form1":
        break
    formcount=formcount+1
br.select_form(nr=formcount)

#find the drop down menu and value
control = br.form.find_control(id='MainContent_cboRaces')
control.value = ["460006719"]
br[control.name] = ["460006719"]

#select submit for second menu
br.submit(nr=1)

#get the HTML
html = br.response().read()

# Transform the HTML into a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

#find the table
main_table = soup.find('table',
    {'id': 'MainContent_dgrdCountyRaceResults'}
)

#get the table headers
for row in main_table.find_all('tr'):
    data1 = [cell.text for cell in row.find_all('th')]
    writer.writerow(data1)
    break

#get the data from each row of the table
for row in main_table.find_all('tr'):
    data = [cell.text for cell in row.find_all('td')]
    writer.writerow(data)