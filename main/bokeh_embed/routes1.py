"""
Blueprint for home module.
Contains: 
1. The route to the home page
2. 
"""
import os, pandas as pd
from flask import Blueprint
from flask import redirect, render_template
home_page = Blueprint('home_page',__name__)

# BOKEH IMPORTS
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import ColumnDataSource

# TOOLTIPS IMPORT
from main.tooltips.tooltips import Tooltips

def read_file():
	"""
	read the csv file from location (main->static->file) using pandas.
	we use the os.getcwd() to get the current working directory and then concat with the file location.
	finally return the dataframe
	"""
	cwd = os.getcwd()
	try:
		file_loc = r'\main\static\file\DATA1.csv' # for windows systems
		file_path = cwd+file_loc
		df = pd.read_csv(file_path)
	except FileNotFoundError:
		file_loc = r'/main/static/file/DATA1.csv' # for linux
		file_path = cwd+file_loc
		df = pd.read_csv(file_path, sep=',', parse_dates=[
		                 'UTC'], infer_datetime_format=True) # UTC is the datetime column
	return df

def generate_bokeh_graph():
	"""
	use the pdf file to plot a bokeh time line.
	"""
	df = read_file()
	# PLOT THE FIGURE
	source = ColumnDataSource(data=df)
	# INITIALIZE TOOLTIPS CLASS
	tooltip = Tooltips
	tools = [tooltip.profile_2d(None), 'tap', 'save', 'pan',
          'wheel_zoom', 'reset']

	# CREATE FIGURE INSTANCE WITH DATETIME AS X AXIS
	# PASS THE TOOLS OBJECT IN THE FIGURE OBJECT
	fig = figure(x_axis_type='datetime', plot_width=900,
	             plot_height=600, tools=tools)

	# SOME FIGURE SETTINGS
	fig.title.text = "BOKEH PLOT"
	fig.title.text_font_size = "20px"
	fig.title.align = "center"
	fig.yaxis.axis_label = "Altitude"
	fig.xaxis.axis_label = "Datetime"

	# CREATE LINE PLOT PASSING THE X & Y-AXIS COLUMN DATA
	fig.line('UTC', 'Altitude', source=source, line_width=2, color='green')

	# GET THE JS SCRIPT AND HTML DIV OF THE PLOT
	line_script, line_div = components(fig)

	return line_script, line_div

@home_page.route("/")
def home():
	"""
	call the generate bokeh graph method and pass to a variable.
	it contains two objects: line_script and line_div at indices 0 & 1 respectively
	"""
	line_graph = generate_bokeh_graph()

	# PASS THE GRAPH OBJECT TO THE CONTEXT
	context = {'line_script':line_graph[0],'line_div':line_graph[1]}
	return render_template("home/home.html",title="Home", **context)
