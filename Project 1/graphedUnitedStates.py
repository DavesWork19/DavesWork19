import pandas as pd
from datetime import datetime
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.models import LinearAxis, Range1d, HoverTool, CustomJS
from bokeh.models.widgets import CheckboxGroup
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

#import info from .csv and store in data frame
file = "us.csv"
df = pd.read_csv(file)

#Figure graph
graphs = figure(title = "United States", x_axis_label='DATE', y_axis_label='CONFIRMED CASES OF COVID-19', x_axis_type='datetime',y_range=(0,2100000),tools='pan,box_zoom,zoom_in,zoom_out,reset,save',plot_width=1000, plot_height=500)
graphs.extra_y_ranges = {"foo": Range1d(start=0, end=210000)}
graphs.add_layout(LinearAxis(y_range_name="foo", axis_label='DEATHS FROM COVID-19'), 'right')
graphs.left[0].formatter.use_scientific = False
graphs.right[0].formatter.use_scientific = False
#convert string dates to datetime
dates = []
count = 0
for item in df['date']:
    dates.append(datetime.strptime(item, '%Y-%m-%d'))


#graph for all of us 
graphs.line(dates,df['cases'],line_width=2,line_color='blue',legend_label="Confirmed")
graphs.line(dates,df['deaths'],line_width=2,line_dash='dashed',line_color='blue', y_range_name="foo",legend_label="Deaths")

graphs.sizing_mode = 'scale_both'
graphs.legend.location = 'top_left'
graphs.add_tools(HoverTool(tooltips=[("","$x{%F}: $y{int}")],formatters = {"$x": "datetime"},mode='mouse',toggleable=False)) 


print("niice, graph 45 location: UnitedStatesGraph.txt")
output_file("US.html")
#show(graphs)
html = file_html(graphs, CDN, "US States")
fa = open("UnitedStatesGraph.txt","w")
fa.write(html)
