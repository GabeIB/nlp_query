from flask import render_template, request
from app import app
from app.forms import LoginForm
from app.process import lproc
import sqlite3

@app.route('/')
@app.route('/index', methods=['GET'])
def login():
    form = LoginForm()
    if 'search' in request.args:
        con = sqlite3.connect("app/data.db")
        cursor = con.cursor()
        dbsearch = lproc(request.args['search']) #lproc should take natural language and convert to sql
        try:
            cursor.execute(dbsearch)#this syntax prevents sql injection
            results = cursor.fetchmany(20)
        except:
            print("dblookup error")
            results = ["invalid query"]
        
    else:
        dbsearch = ''
        results = []

    return render_template('login.html', form=form, search=dbsearch, results=results)

