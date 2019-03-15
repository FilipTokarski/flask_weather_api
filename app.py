from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from api_request import ApiRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)

# class Cities(db.Model):
#     pass


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city_name = request.form['city']
        api_data = ApiRequest(city_name) 
        context = api_data.get_data()
        return render_template('home.html', context=context)

    elif request.method == 'GET':
        return render_template('home.html')


@app.route('/delete_city', methods=['GET', 'POST'])
def delete_city():
    if request.method == 'POST':
        modal = request.form['modal']
        return redirect('/')

    elif request.method == 'GET':
        return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
