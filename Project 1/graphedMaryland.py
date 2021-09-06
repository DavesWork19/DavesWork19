import pandas as pd
from datetime import datetime
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.models import LinearAxis, Range1d, HoverTool, CustomJS
from bokeh.models.widgets import CheckboxGroup
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html
import random

#import info from .csv and store in data frame
file = "us-counties.csv"
df = pd.read_csv(file)
#print(df)

#store index associated with state row into list
count = 0
c = 0
countList = []
plots_Conf = []
plots_Dead = []

state = "Maryland"
for place in df['state']:
    if(place == state):
        countList.append(count)
    count = count + 1
    
#get colors from colors.txt
colorList = []
cL = open("colors.txt","r")
for line in cL:
    colorList.append(line)
    
#use list of indexs to create new updated data frame with only specified state
updatedDF = pd.DataFrame(df.iloc[countList])


#Figure graph
title = "Maryland Counties"
graphs = figure(title = title, x_axis_label='DATE', y_axis_label='CONFIRMED CASES OF COVID-19', x_axis_type='datetime',y_range=(0,14500),tools='pan,box_zoom,zoom_in,zoom_out,reset,save',plot_width=1000, plot_height=500)
graphs.extra_y_ranges = {"foo": Range1d(start=0, end=1450)}
graphs.add_layout(LinearAxis(y_range_name="foo", axis_label='DEATHS FROM COVID-19'), 'right')
graphs.left[0].formatter.use_scientific = False
graphs.right[0].formatter.use_scientific = False


#collect data for graph and graph each county
uniqueCounties = sorted(updatedDF['county'].unique())
length = len(updatedDF)
for place in uniqueCounties:
    date = []
    conf = []
    dead = []
    
    #get color from colors.txt for graph line
    color = random.choice(colorList)
    color = color.strip('\n')
    
    for i in range(0,length):
        if (updatedDF.iloc[i,1] == place):
            date.append(datetime.strptime(updatedDF.iloc[i,0], '%Y-%m-%d'))
            conf.append(updatedDF.iloc[i,4])
            dead.append(updatedDF.iloc[i,5])

    #graph for all of us 
    if(c == 0):
        plots_Conf.append(graphs.line(date,conf,line_width=2,line_color='blue',legend_label="Confirmed",name=place))
        plots_Dead.append(graphs.line(date,dead,line_width=2,line_dash='dashed',line_color='blue', y_range_name="foo",legend_label="Deaths",name=place))
    else:
        plots_Conf.append(graphs.line(date,conf,line_width=2,line_color=color,name=place,visible=False))
        plots_Dead.append(graphs.line(date,dead,line_width=2,line_dash='dashed',line_color=color,name=place, y_range_name="foo",visible=False))
    c = c + 1
        

graphs.sizing_mode = 'scale_both'
graphs.legend.location = 'top_left'
graphs.add_tools(HoverTool(tooltips=[("", "$name"),("","$x{%F}: $y{int}")],formatters = {"$x": "datetime"},mode='mouse',toggleable=False)) 

checkboxes = CheckboxGroup(labels=uniqueCounties, active=[0])

#Linking with JavaScript
callback = CustomJS(code="""
                            var i;
                            for (i = 0; i < 25; i++)
                            {
                                if (cb_obj.active.includes(i))
                                {
                                    lineC[i].visible = true;
                                    lineD[i].visible = true;
                                }
                                else
                                {
                                    lineC[i].visible = false;
                                    lineD[i].visible = false;
                                }
                            }
                            """,
                    args={'lineC': plots_Conf, 'lineD': plots_Dead})


checkboxes.js_on_click(callback)


print("niice, graph 20 location: countiesMaryland.txt")
output_file("countiesMaryland.html")
#show(row(graphs,checkboxes))

html = file_html(row(graphs,checkboxes), CDN, "US States")
fa = open("countiesMaryland.txt","w")
fa.write(html)
