from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        return render_template('home.html', city=city)

    elif request.method == 'GET':
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
