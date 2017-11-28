#This is the entry file, like index.html
#First we should import Flask
#Next we import render_template to manage templates (need a templates/ folder)
from __future__ import print_function
from __future__ import division
import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
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

app = Flask(__name__) #__name__ = Placeholder for current module
Bootstrap(app)

#Use routes to define directories
@app.route('/')
def index():
	return render_template('index.html') #Normally return a template

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/disclosure')
def disclosure():
	return render_template('disclosure.html')

@app.route('/visuals')
def visuals():
	return render_template('visuals.html')

@app.route('/visuals/jan')
def jan():
	import json
	with open('./data4pie/jan.txt', 'r') as data:
    		jan = json.load(data)
	h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
	allofem=[]
	for day in jan.keys():
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
	rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
	script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='January', script=script, div=div)

@app.route('/visuals/feb')
def feb():
        import json
        with open('./data4pie/feb.txt', 'r') as data:
                feb = json.load(data)
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]
        for day in feb.keys():
                print(day)
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
        rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='February', script=script, div=div)

@app.route('/visuals/mar')
def mar():
        import json
        with open('./data4pie/march.txt', 'r') as data:
                march = json.load(data)
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]
        for day in march.keys():
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
        rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='March', script=script, div=div)

@app.route('/visuals/apr')
def apr():
        import json
        with open('./data4pie/april.txt', 'r') as data:
                april = json.load(data)
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]
        for day in april.keys():
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
        rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='April', script=script, div=div)

@app.route('/visuals/may')
def may():
        import json
        with open('./data4pie/may.txt', 'r') as data:
                may = json.load(data)
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]
        for day in may.keys():
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
        rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='May', script=script, div=div)

@app.route('/visuals/jun')
def jun():
        import json
        with open('./data4pie/june.txt', 'r') as data:
                june = json.load(data)
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]
        for day in june.keys():
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
        rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='June', script=script, div=div)

@app.route('/visuals/jul')
def jul():
        import json
        with open('./data4pie/july.txt', 'r') as data:
                july = json.load(data)
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]
        for day in july.keys():
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
        rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='July', script=script, div=div)

@app.route('/visuals/aug')
def aug():
        import json
        with open('./data4pie/aug.txt', 'r') as data:
                aug = json.load(data)
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]
        for day in aug.keys():
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
        rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='August', script=script, div=div)

@app.route('/visuals/sep')
def sep():
        import json
        with open('./data4pie/sept.txt', 'r') as data:
                sept = json.load(data)
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]
        for day in sept.keys():
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
        rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='September', script=script, div=div)

@app.route('/visuals/oct')
def oct():
        import json
        with open('./data4pie/oct.txt', 'r') as data:
                oct = json.load(data)
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]
        for day in oct.keys():
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
        rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='October', script=script, div=div)

@app.route('/visuals/nov')
def nov():
        import json
        with open('./data4pie/nov.txt', 'r') as data:
                nov = json.load(data)
        h = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "red", "green"]
        allofem=[]
        for day in nov.keys():
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
        rc = gridplot([allofem[0:7], allofem[7:14], allofem[14:21], allofem[21:28], allofem[28:]])
        script, div = components(rc)
        return render_template('monthVisualLayout.html', monthName='November', script=script, div=div)

@app.route('/visuals/dec')
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
	app.run(debug=True) #Deubug is set to true
