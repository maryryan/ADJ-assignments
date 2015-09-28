import csv

#open input and output files
csvfile = open('/Users/maryryan/Desktop/advanced-data-journalism/assignments/data-cleaning/data/cleanme.csv', 'r')
outfile = open('/Users/maryryan/Desktop/ADJ-assignments/data_cleaning_MaryRyan.csv', 'w')

#DictReader and DictWriter
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

#headers
writer.writeheader()


for row in reader:
	#make first_name text uppercase
	row['first_name'] = row['first_name'].upper()

	#add leading zeros to zip codes less than 5
	row['zip'] = row['zip'].zfill(5)

	#remove non-breaking spaces
	row['city'] = row['city'].replace("&nbsp;", " ")

	#only save contributions over $1,000
	if int(row['amount']) >= 1000:
		writer.writerow(row)

#This will make any text, regardless of column, uppercase but implementing this won't execute .zfill(), .replace() and int(row['amount'])
#for row in reader:
	#for col in row:
		#for thing in col:
			#if type(row[col]) == str:
				#row[col] = row[col].upper()
	#writer.writerow(row)