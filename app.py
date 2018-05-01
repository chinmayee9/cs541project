from flask import Flask, request, render_template, Response
from dbConnect import getDomains
from similarity import readPopularity
import json
from wtforms import TextField, Form
from getDataForFrontEnd import getDatabyCurrency
import os

# crypto flask app
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template("home.html")

# currency table
@app.route('/currencylist')
def currency_table():
    return render_template("currency_table.html")

# currency details
@app.route('/currency/<c_name>')
def currency_dashboard(c_name):
    params = getDatabyCurrency(c_name)
    return render_template("c_dashboard.html", c_name=c_name, params = params)


# currency domains
@app.route('/currency/<c_name>/domains')
def currency_domains(c_name):
    domains = getDomains(c_name)
    return render_template("c_domains.html", domains=domains, c_name=c_name)


# word cloud data
@app.route('/word_cloud')
def word_cloud():
    try:
        popular = readPopularity()
        words_json = [{'text': str(word[0]).capitalize(), 'weight': int(word[1]), 'link':'/currency/'+str(word[0]).lower()} for word in popular]
        return json.dumps(words_json)
        # return json.dumps(popular)
    except:
        return json.dumps({})


if __name__ == "__main__":
    app.debug(True)
    app.run()
