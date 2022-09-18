import csv, random
from flask import Flask, render_template, request
app = Flask(__name__)


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


# @app.route('/index.html')
# def index():
# 	return render_template('index.html') 


@app.route('/')
def home():
	data = select_random_word()
	return render_template('french.html', English = data[0], French = data[1]) 








# @app.route('/<string:page_name>')
# def page(page_name):
# 	if page_name in ['index','about','works', 'contact', 'components']:
# 		return render_template(page_name + '.html')
# 	elif page_name in ['index.html','about.html', 'works.html','contact.html','components.html','thankyou.html']:
# 		return render_template(page_name)
# 	else:
# 		return 'uh oh, no such page'

# def write_to_file(data):
# 	with open('database.txt', mode='a') as database:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		file = database.write(f'\n{email},{subject},{message}')

# def write_to_csv(data):
# 	with open('database.csv', newline='', mode='a') as database2:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		csv_writer = csv.writer(database2, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
# 		csv_writer.writerow([email,subject,message])

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
# 	if request.method == 'POST':
# 		try: 
# 			data = request.form.to_dict()
# 			write_to_csv(data)
# 			return redirect('/thankyou.html')
# 		except:
# 			return 'did not save to database'
# 	else:
# 		return 'error'