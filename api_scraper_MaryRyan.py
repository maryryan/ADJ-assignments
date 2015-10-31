import re, urllib2, json
#write function to clean the json
def clean_json(json):
    '''
    Turn dirty State Department JSON into clean JSON.
    '''
    return re.sub(r'new Date\(.*?\)', '""', json)

#Q1
CASE = 'F-2014-20439'
#Q2
SEARCH = 'Benghazi'
#Q3
dirty_json = urllib2.urlopen('https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?searchText=%s&beginDate=false&endDate=false&postedBeginDate=false&postedEndDate=false&caseNumber=%s&collectionMatch=false&page=1&start=0&limit=500' % (SEARCH, CASE)).read()
clean = clean_json(dirty_json)
data = json.loads(clean)

for info in data['Results']:
    print info['pdfLink']