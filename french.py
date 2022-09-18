# importing modules needed
import csv, random, re


# define functions
def select_random_word():
	English = []
	French = []
	article = []
	with open('french_nouns_final.csv', 'r', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in reader:
			English.append(row[0])
			French.append(row[2])
			article.append(row[1])
	# number of entries in the complete noun list
	n = reader.line_num
	i = random.randrange(1,n)
	return English[i], French[i], article[i]


# open the raw csv file with the french nouns and read the data
# french nouns come from http://frequencylists.blogspot.com/2015/12/the-2000-most-frequently-used-french.html
dictionary = {}
eng = []
fre = []
art = []


with open('french_nouns.csv', 'r', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

	# using regular expressions extract the number, english noun, article and french noun
	for row in spamreader:
		m = re.search(r'[a-z]+', row[0])
		n = re.search(r'[0-9]+', row[0])
		num = (n.group(0))
		eng.append(m.group(0))
		art.append(row[1])
		word = row[2]
		for i in range(3,len(row)): 
			word = word+' '+row[i]
		fre.append(word)




# write the selected words to a new csv file
with open('french_nouns_final.csv', 'w', newline='\n') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['English', 'article', 'French'])
	for word in range(len(eng)):
		spamwriter.writerow([eng[word], art[word], fre[word]])

# # call the function
# data = select_random_word()
# print (data)


