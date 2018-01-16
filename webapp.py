from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

#def get_state_options():
    #with open('drugs (1).json') as corgis_data:
        #rates = json.load(corgis_data)
    #state = rates[0]["State"]
    #pick = ""
    #for r in rates:
        #if state != r["State"]:
            #pick += Markup("<option value=" + state +">" + state + "</option>")
           # state = r["State"]
    #return pick 

@app.route("/")
def render_main():
    return render_template('home.html')

#@app.route("/p1")	
#def render_page1():
    #with open('drugs (1).json') as rates_data:
        #rates = json.load(rates_data)
    #return render_template('page1.html', option = get_state_options(rates))

@app.route("/p1")
def render_page1():
    with open('drugs (1).json') as rates_data:
        rates = json.load(rates_data)
    if 'state' in request.args:
        return render_template('page1.html', options = get_state_options(rates), total = totals(request.args['state']), state = request.args['state'])
    return render_template('page1.html', options = get_state_options(rates))

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
	
@app.route("/p3")
def render_page3():
    return render_template('page3.html')

def get_state_options(rates):
    states = []
    options = ""
    for r in rates:
        if r["State"] not in states:
            states.append(r["State"])
            options += Markup("<option value=\"" + r["State"] + "\">" + r["State"] + "</option>")
    return options

def totals(state):
    with open('drugs (1).json') as corgis_data:
        rates = json.load(corgis_data)
    total = 0
    for r in rates:
        if state == r["State"]:
            print(r["Totals"]["Illicit Drugs"]["Abuse Past Month"]["12-17"])    
	    total += r["Totals"]["Illicit Drugs"]["Abuse Past Month"]["12-17"]
    return total
	

#@app.route("/app", methods=['GET','POST'])
#def get_total():  
    #area = request.args['pickstate']
    #return render_template('page1.html', total = totals(area), option = get_state_options(rates))

if __name__=="__main__":
    app.run(debug=False)
