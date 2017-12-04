#This is the entry file, like index.html
#First we should import Flask
#Next we import render_template to manage templates (need a templates/ folder)
from __future__ import print_function
from __future__ import division
import flask
from flask import Flask, render_template, request, flash, session
from flask.ext.session import Session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
import re
from nltk.tag import StanfordNERTagger
import ast
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.plotting import *
from numpy import pi
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

import sys
sys.path.insert(0,'/var/www/html/CapstoneI/code/application/scripts/')
from classify import predict_cluster
from nlp import analyze_sentiment

km = joblib.load('/var/www/html/CapstoneI/code/application/static/models/kmeans_model.pkl')
vectorizer = joblib.load('/var/www/html/CapstoneI/code/application/static/models/tf_vectorizer_obj.pkl')

app = Flask(__name__) #__name__ = Placeholder for current module
app.secret_key = 'secretsecret'

#database stuff
host = 'ec2-34-215-56-46.us-west-2.compute.amazonaws.com'
dbname = 'cap'
user = 'postgres'
password = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = str('postgresql://' + user + ':' + password + '@' + host + ':9000/' + dbname)
db = SQLAlchemy(app)
Bootstrap(app)
sess = Session()


# template for database cluster_labels table
class Cluster_labels(db.Model):
	cluster_num = db.Column(db.Integer, primary_key=True)
	cluster_label = db.Column(db.String(30))

# form for submitting text
class DisclosureForm(Form):
	article = TextAreaField('Article Text: ', validators=[validators.required(), validators.Length(min=250)])

#Use routes to define directories
@app.route('/')
def index():
	return render_template('index.html') #Normally return a template

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/disclosure', methods=['GET', 'POST'])
def disclosure():
	form = DisclosureForm(request.form)
	print(form.errors)
 
	if request.method == 'POST':
		text = request.form['article']
		text = text.encode("ascii", errors="ignore").decode()
		
		if form.validate():
			try:
				result = predict_cluster(text, km, vectorizer)
				data = Cluster_labels.query.get(int(result))
				sentiment = analyze_sentiment(text) 
				return render_template('disclosure.html', cluster=result, text=text, form=form, label=data.cluster_label, sentiment=sentiment)
			except Exception as e:
				return render_template('disclosure.html', form=form, text_error=True, exception=e, text=text)
		else:
			flash("Please provide body text of at least 250 characters")	

	return render_template('disclosure.html', form=form)

@app.route('/visuals')
def visuals():
	return render_template('visuals.html')

@app.route('/jan')
def jan():
	import json
	try:
		with open('/var/www/html/test_app/data4pie/jan.txt', 'r') as data:
    			jan = json.load(data)
			print("var www html test_app")
	except IOError:
		with open('./data4pie/jan.txt', 'r') as data:
                	jan = json.load(data)
			print(".")
	h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
	allofem=[]

	dates = [day for day in jan]
	dates.sort()

	for day in dates:
    		print(day)
    		perdiem = pd.DataFrame.from_dict(jan[day], orient="index")
    		perdiem.columns = ['count']
    		perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
    		denom = perdiem['count'].sum()
    		perdiem['percent'] =  perdiem['count']/denom
    		perdiem['cum_sum'] = perdiem['count'].cumsum()
    		perdiem['cum_perc'] = perdiem.cum_sum/denom
    		percents = [0]
    		percents.extend(perdiem.cum_perc.values)
    		starts = [p*2*pi for p in percents[:-1]]
    		ends = [p*2*pi for p in percents[1:]]
    
    		p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
    		source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
    		p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
    		allofem = allofem + [p]
	rc = gridplot([allofem[0:2], allofem[2:4], allofem[4:6], allofem[6:8], allofem[8:10], allofem[10:12], allofem[12:14], allofem[14:16], allofem[16:18]
	, allofem[18:20], allofem[20:22], allofem[22:24], allofem[24:26], allofem[26:28], allofem[28:30], allofem[30:]])
	script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='January', script=script, div=div)

@app.route('/feb')
def feb():
        import json
        try:
                with open('/var/www/html/test_app/data4pie/feb.txt', 'r') as data:
                        feb = json.load(data)
                        print("var www html test_app")
        except IOError:
                with open('./data4pie/feb.txt', 'r') as data:
                        feb = json.load(data)
                        print(".")
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]

	dates = [day for day in feb]
	dates.sort()

        for day in dates:

                perdiem = pd.DataFrame.from_dict(feb[day], orient="index")
                perdiem.columns = ['count']
                perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
                denom = perdiem['count'].sum()
                perdiem['percent'] =  perdiem['count']/denom
                perdiem['cum_sum'] = perdiem['count'].cumsum()
                perdiem['cum_perc'] = perdiem.cum_sum/denom
                percents = [0]
                percents.extend(perdiem.cum_perc.values)
                starts = [p*2*pi for p in percents[:-1]]
                ends = [p*2*pi for p in percents[1:]]

                p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
                source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
                p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
                allofem = allofem + [p]
        rc = gridplot([allofem[0:2], allofem[2:4], allofem[4:6], allofem[6:8], allofem[8:10], allofem[10:12], allofem[12:14], allofem[14:16], allofem[16:18]
        , allofem[18:20], allofem[20:22], allofem[22:24], allofem[24:26], allofem[26:28]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='February', script=script, div=div)

@app.route('/mar')
def mar():
        import json
	try:
                with open('/var/www/html/test_app/data4pie/march.txt', 'r') as data:
                        march = json.load(data)
                        print("var www html test_app")
        except IOError:
                with open('./data4pie/march.txt', 'r') as data:
                        march = json.load(data)
                        print(".")
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]

	dates = [day for day in march]
	dates.sort()	

        for day in dates:
                print(day)
                perdiem = pd.DataFrame.from_dict(march[day], orient="index")
                perdiem.columns = ['count']
                perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
                denom = perdiem['count'].sum()
                perdiem['percent'] =  perdiem['count']/denom
                perdiem['cum_sum'] = perdiem['count'].cumsum()
                perdiem['cum_perc'] = perdiem.cum_sum/denom
                percents = [0]
                percents.extend(perdiem.cum_perc.values)
                starts = [p*2*pi for p in percents[:-1]]
                ends = [p*2*pi for p in percents[1:]]

                p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
                source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
                p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
                allofem = allofem + [p]
        rc = gridplot([allofem[0:2], allofem[2:4], allofem[4:6], allofem[6:8], allofem[8:10], allofem[10:12], allofem[12:14], allofem[14:16], allofem[16:18]
        , allofem[18:20], allofem[20:22], allofem[22:24], allofem[24:26], allofem[26:28], allofem[28:30], allofem[30:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='March', script=script, div=div)

@app.route('/apr')
def apr():
        import json
        try:
                with open('/var/www/html/test_app/data4pie/april.txt', 'r') as data:
                        april = json.load(data)
                        print("var www html test_app")
        except IOError:
                with open('./data4pie/april.txt', 'r') as data:
                        april = json.load(data)
                        print(".")
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]

	dates = [day for day in april]
	dates.sort()	

        for day in dates:
                print(day)
                perdiem = pd.DataFrame.from_dict(april[day], orient="index")
                perdiem.columns = ['count']
                perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
                denom = perdiem['count'].sum()
                perdiem['percent'] =  perdiem['count']/denom
                perdiem['cum_sum'] = perdiem['count'].cumsum()
                perdiem['cum_perc'] = perdiem.cum_sum/denom
                percents = [0]
                percents.extend(perdiem.cum_perc.values)
                starts = [p*2*pi for p in percents[:-1]]
                ends = [p*2*pi for p in percents[1:]]

                p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
                source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
                p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
                allofem = allofem + [p]
        rc = gridplot([allofem[0:2], allofem[2:4], allofem[4:6], allofem[6:8], allofem[8:10], allofem[10:12], allofem[12:14], allofem[14:16], allofem[16:18]
        , allofem[18:20], allofem[20:22], allofem[22:24], allofem[24:26], allofem[26:28], allofem[28:30], allofem[30:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='April', script=script, div=div)

@app.route('/may')
def may():
        import json
        try:
                with open('/var/www/html/test_app/data4pie/may.txt', 'r') as data:
                        may = json.load(data)
                        print("var www html test_app")
        except IOError:
                with open('./data4pie/may.txt', 'r') as data:
                        may = json.load(data)
                        print(".")
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]

	dates = [day for day in may]
	dates.sort()

        for day in date:
                print(day)
                perdiem = pd.DataFrame.from_dict(may[day], orient="index")
                perdiem.columns = ['count']
                perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
                denom = perdiem['count'].sum()
                perdiem['percent'] =  perdiem['count']/denom
                perdiem['cum_sum'] = perdiem['count'].cumsum()
                perdiem['cum_perc'] = perdiem.cum_sum/denom
                percents = [0]
                percents.extend(perdiem.cum_perc.values)
                starts = [p*2*pi for p in percents[:-1]]
                ends = [p*2*pi for p in percents[1:]]

                p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
                source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
                p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
                allofem = allofem + [p]
        rc = gridplot([allofem[0:2], allofem[2:4], allofem[4:6], allofem[6:8], allofem[8:10], allofem[10:12], allofem[12:14], allofem[14:16], allofem[16:18]
        , allofem[18:20], allofem[20:22], allofem[22:24], allofem[24:26], allofem[26:28], allofem[28:30], allofem[30:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='May', script=script, div=div)

@app.route('/jun')
def jun():
        import json
        try:
                with open('/var/www/html/test_app/data4pie/june.txt', 'r') as data:
                        june = json.load(data)
                        print("var www html test_app")
        except IOError:
                with open('./data4pie/june.txt', 'r') as data:
                        june = json.load(data)
                        print(".")
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]

	dates = [day for day in june]
	dates.sort()
	
        for day in dates:
                print(day)
                perdiem = pd.DataFrame.from_dict(june[day], orient="index")
                perdiem.columns = ['count']
                perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
                denom = perdiem['count'].sum()
                perdiem['percent'] =  perdiem['count']/denom
                perdiem['cum_sum'] = perdiem['count'].cumsum()
                perdiem['cum_perc'] = perdiem.cum_sum/denom
                percents = [0]
                percents.extend(perdiem.cum_perc.values)
                starts = [p*2*pi for p in percents[:-1]]
                ends = [p*2*pi for p in percents[1:]]

                p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
                source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
                p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
                allofem = allofem + [p]
        rc = gridplot([allofem[0:2], allofem[2:4], allofem[4:6], allofem[6:8], allofem[8:10], allofem[10:12], allofem[12:14], allofem[14:16], allofem[16:18]
        , allofem[18:20], allofem[20:22], allofem[22:24], allofem[24:26], allofem[26:28], allofem[28:30], allofem[30:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='June', script=script, div=div)

@app.route('/jul')
def jul():
        import json
        try:
                with open('/var/www/html/test_app/data4pie/july.txt', 'r') as data:
                        july = json.load(data)
                        print("var www html test_app")
        except IOError:
                with open('./data4pie/july.txt', 'r') as data:
                        july = json.load(data)
                        print(".")
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]

	dates = [day for day in july]
	dates.sort()

        for day in dates:
                print(day)
                perdiem = pd.DataFrame.from_dict(july[day], orient="index")
                perdiem.columns = ['count']
                perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
                denom = perdiem['count'].sum()
                perdiem['percent'] =  perdiem['count']/denom
                perdiem['cum_sum'] = perdiem['count'].cumsum()
                perdiem['cum_perc'] = perdiem.cum_sum/denom
                percents = [0]
                percents.extend(perdiem.cum_perc.values)
                starts = [p*2*pi for p in percents[:-1]]
                ends = [p*2*pi for p in percents[1:]]

                p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
                source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
                p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
                allofem = allofem + [p]
        rc = gridplot([allofem[0:2], allofem[2:4], allofem[4:6], allofem[6:8], allofem[8:10], allofem[10:12], allofem[12:14], allofem[14:16], allofem[16:18]
        , allofem[18:20], allofem[20:22], allofem[22:24], allofem[24:26], allofem[26:28], allofem[28:30], allofem[30:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='July', script=script, div=div)

@app.route('/aug')
def aug():
        import json
        try:
                with open('/var/www/html/test_app/data4pie/aug.txt', 'r') as data:
                        aug = json.load(data)
                        print("var www html test_app")
        except IOError:
                with open('./data4pie/aug.txt', 'r') as data:
                        aug = json.load(data)
			print(".")
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]

	dates = [day for day in aug]
	dates.sort()

        for day in dates:
                print(day)
                perdiem = pd.DataFrame.from_dict(aug[day], orient="index")
                perdiem.columns = ['count']
                perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
                denom = perdiem['count'].sum()
                perdiem['percent'] =  perdiem['count']/denom
                perdiem['cum_sum'] = perdiem['count'].cumsum()
                perdiem['cum_perc'] = perdiem.cum_sum/denom
                percents = [0]
                percents.extend(perdiem.cum_perc.values)
                starts = [p*2*pi for p in percents[:-1]]
                ends = [p*2*pi for p in percents[1:]]

                p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
                source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
                p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
                allofem = allofem + [p]
        rc = gridplot([allofem[0:2], allofem[2:4], allofem[4:6], allofem[6:8], allofem[8:10], allofem[10:12], allofem[12:14], allofem[14:16], allofem[16:18]
        , allofem[18:20], allofem[20:22], allofem[22:24], allofem[24:26], allofem[26:28], allofem[28:30], allofem[30:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='August', script=script, div=div)

@app.route('/sep')
def sep():
        import json
        try:
                with open('/var/www/html/test_app/data4pie/sept.txt', 'r') as data:
                        sept = json.load(data)
                        print("var www html test_app")
        except IOError:
                with open('./data4pie/sept.txt', 'r') as data:
                        sept = json.load(data)
                        print(".")
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]

	dates = [day for day in sept]
	dates.sort()

        for day in dates:
                print(day)
                perdiem = pd.DataFrame.from_dict(sept[day], orient="index")
                perdiem.columns = ['count']
                perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
                denom = perdiem['count'].sum()
                perdiem['percent'] =  perdiem['count']/denom
                perdiem['cum_sum'] = perdiem['count'].cumsum()
                perdiem['cum_perc'] = perdiem.cum_sum/denom
                percents = [0]
                percents.extend(perdiem.cum_perc.values)
                starts = [p*2*pi for p in percents[:-1]]
                ends = [p*2*pi for p in percents[1:]]

                p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
                source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
                p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
                allofem = allofem + [p]
        rc = gridplot([allofem[0:2], allofem[2:4], allofem[4:6], allofem[6:8], allofem[8:10], allofem[10:12], allofem[12:14], allofem[14:16], allofem[16:18]
        , allofem[18:20], allofem[20:22], allofem[22:24], allofem[24:26], allofem[26:28], allofem[28:30], allofem[30:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='September', script=script, div=div)

@app.route('/oct')
def oct():
        import json
        try:
                with open('/var/www/html/test_app/data4pie/oct.txt', 'r') as data:
                        oct = json.load(data)
                        print("var www html test_app")
        except IOError:
                with open('./data4pie/oct.txt', 'r') as data:
                        oct = json.load(data)
                        print(".")
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]

	dates = [day for day in oct]
	dates.sort()

        for day in dates:
                print(day)
                perdiem = pd.DataFrame.from_dict(oct[day], orient="index")
                perdiem.columns = ['count']
                perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
                denom = perdiem['count'].sum()
                perdiem['percent'] =  perdiem['count']/denom
                perdiem['cum_sum'] = perdiem['count'].cumsum()
                perdiem['cum_perc'] = perdiem.cum_sum/denom
                percents = [0]
                percents.extend(perdiem.cum_perc.values)
                starts = [p*2*pi for p in percents[:-1]]
                ends = [p*2*pi for p in percents[1:]]

                p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
                source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
                p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
                allofem = allofem + [p]
        rc = gridplot([allofem[0:2], allofem[2:4], allofem[4:6], allofem[6:8], allofem[8:10], allofem[10:12], allofem[12:14], allofem[14:16], allofem[16:18]
        , allofem[18:20], allofem[20:22], allofem[22:24], allofem[24:26], allofem[26:28], allofem[28:30], allofem[30:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='October', script=script, div=div)

@app.route('/nov')
def nov():
        import json
        try:
                with open('/var/www/html/test_app/data4pie/nov.txt', 'r') as data:
                        nov = json.load(data)
                        print("var www html test_app")
        except IOError:
                with open('./data4pie/nov.txt', 'r') as data:
                        nov = json.load(data)
                        print(".")
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]

	dates = [day for day in nov]
	dates.sort()

        for day in dates:
                print(day)
                perdiem = pd.DataFrame.from_dict(nov[day], orient="index")
                perdiem.columns = ['count']
                perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
                denom = perdiem['count'].sum()
                perdiem['percent'] =  perdiem['count']/denom
                perdiem['cum_sum'] = perdiem['count'].cumsum()
                perdiem['cum_perc'] = perdiem.cum_sum/denom
                percents = [0]
                percents.extend(perdiem.cum_perc.values)
                starts = [p*2*pi for p in percents[:-1]]
                ends = [p*2*pi for p in percents[1:]]

                p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
                source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
                p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
                allofem = allofem + [p]
        rc = gridplot([allofem[0:2], allofem[2:4], allofem[4:6], allofem[6:8], allofem[8:10], allofem[10:12]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='November', script=script, div=div)

@app.route('/dec')
def dec():
        #import json
        #with open('./data4pie/dec.txt', 'r') as data:
        #        dec = json.load(data)
        #h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        #allofem=[]
        #for day in dec.keys():
         #       print(day)
          #      perdiem = pd.DataFrame.from_dict(dec[day], orient="index")
           #     perdiem.columns = ['count']
            #    perdiem = perdiem.sort_values(by='count', ascending = False)[:10]
             #   denom = perdiem['count'].sum()
              #  perdiem['percent'] =  perdiem['count']/denom
               # perdiem['cum_sum'] = perdiem['count'].cumsum()
               # perdiem['cum_perc'] = perdiem.cum_sum/denom
               # percents = [0]
               # percents.extend(perdiem.cum_perc.values)
               # starts = [p*2*pi for p in percents[:-1]]
               # ends = [p*2*pi for p in percents[1:]]
#
 #               p = figure(x_range=(-.6,.6), y_range=(-1,1), title=str(day))#", plot_height=100)
  #              source = ColumnDataSource(dict(colors=h, label=list(perdiem.index), x=[0]*10, y=[0]*10,radius=[1/2]*10, start_angle=starts,end_angle=ends))
   #             p.wedge(x='x',y='y' ,radius='radius' , start_angle='start_angle',end_angle='end_angle', color='colors', legend = 'label', source=source)
    #            allofem = allofem + [p]
     #   rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
      #  script, div = components(rc)
       # return render_template('monthVisualLayout.html', monthName='December', script=script, div=div)
	return render_template('monthVisualLayout.html', monthName='December')

#Run the app
if __name__ == '__main__':
	print(__doc__)
	app.config['SESSION_TYPE'] = 'filesystem'
	sess.init_app(app)
	app.debug = True	
	app.run() #Deubug is set to true
