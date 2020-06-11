from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = "supersecret"

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		pass
	if request.mthod == 'POST':
		request.form.get('name')
		request.form.get('post')

	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True, port=5000, host='0.0.0.0')