from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def root():
	return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			print('did not write to database.')
	else:
		return 'something went wrong'


def write_to_csv(data):
	with open('database.csv', 'a', newline='') as db2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])



# @app.route('/index.html')
# def home():
# 	return render_template('index.html')

# @app.route('/works.html')
# def works():
# 	return render_template('works.html')

# @app.route('/about.html')
# def about_me():
# 	return render_template('about.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')

# @app.route('/components.html')
# def components():
# 	return render_template('components.html')

# @app.route('/work.html')
# def extra_work():
# 	return render_template('work.html')

# below text negates all above text.
# @app.route('/<string:page_name>')
# def html_page(page_name):
# 	return render_template(page_name)