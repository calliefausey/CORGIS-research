from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    with open('drugs (1).json') as rates_data:
        rates = json.load(rates_data)
    if 'state' in request.args:
        return render_template('page1.html', soptions = get_state_options(rates), abuseTotal = get_total(rates, request.args['state']), state = request.args['state'])
    return render_template('page1.html', soptions = get_state_options(rates))

@app.route("/p2")
def render_page2():
    with open('drugs (1).json') as rates_data:
        rates = json.load(rates_data)
    if 'state' in request.args:
        return render_template('page2.html', soptions = get_state_options(rates), abuseRate = get_rate(rates, request.args['state']), state = request.args['state'])
    return render_template('page2.html', soptions = get_state_options(rates))
	
@app.route("/p3")
def render_page3():
    with open('drugs (1).json') as rates_data:
        rates = json.load(rates_data)
    if 'state' in request.args:
        return render_template('page3.html', soptions = get_state_options(rates), earlyRate = get_early_rate(rates, request.args['state']), earlyTotal = get_early_total(rates, request.args['state']), state = request.args['state'])
    return render_template('page3.html', soptions = get_state_options(rates))

def get_state_options(rates):
    states = []
    soptions = ""
    for r in rates:
        if r["State"] not in states:
            states.append(r["State"])
            soptions += Markup("<option value=\"" + r["State"] + "\">" + r["State"] + "</option>")
    return soptions

def get_total(rates, get_state):
    abuseTotal = 0
    for r in rates:
        if r["State"] == get_state and r["Year"] == 2014:
            abuseTotal += r["Totals"]["Alcohol"]["In Minors"]["Abuse"]
    return abuseTotal

def get_rate(rates, get_state):
    abuseRate = 0
    for r in rates:
        if r["State"] == get_state and r["Year"] == 2014:
            abuseRate += r["Rates"]["Illicit Drugs"]["Abuse Past Month"]["12-17"]
    return abuseRate 

def get_early_total(rates, get_state):
    earlyTotal = 0
    for r in rates:
        if r["State"] == get_state and r["Year"] == 2002:
            earlyTotal += r["Totals"]["Alcohol"]["In Minors"]["Abuse"]
    return earlyTotal

def get_early_rate(rates, get_state):
    earlyRate = 0
    for r in rates:
        if r["State"] == get_state and r["Year"] == 2002:
            earlyRate += r["Rates"]["Illicit Drugs"]["Abuse Past Month"]["12-17"]
    return earlyRate 

if __name__=="__main__":
    app.run(debug=False)
