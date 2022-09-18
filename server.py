import csv, random, os
from flask import Flask, render_template, request
app = Flask(__name__)


# define functions
def select_random_word():
	English = []
	French = []
	article = []
	THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
	my_file = os.path.join(THIS_FOLDER, 'french_nouns_final.csv')

	
	with open(new_path, 'r', newline='') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in reader:
			English.append(row[0])
			French.append(row[2])
			article.append(row[1])
	# number of entries in the complete noun list
	n = reader.line_num
	i = random.randrange(1,n)
	return English[i], French[i], article[i]


@app.route('/')
def home():
	data = select_random_word()
	return render_template('french.html', English = data[0], French = data[1], Article = data[2]) 

