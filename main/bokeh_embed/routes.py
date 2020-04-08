"""
Blueprint for home module.
Contains: 
1. The route to the home page
"""
import os
from flask import Blueprint
from flask import redirect, render_template
home_page = Blueprint('home_page', __name__)

def read_file():
	"""
	read the csv file from location (main->static->file) using pandas.
	we use the os.getcwd() to get the current working directory and then concat with the file location.
	finally return the dataframe
	"""
	cwd = os.getcwd()
	try:
		file_loc = r'\main\static\file\DATA1.csv'  # for windows systems
		file_path = cwd+file_loc
		df = pd.read_csv(file_path)
	except FileNotFoundError:
		file_loc = r'/main/static/file/DATA1.csv'  # for linux
		file_path = cwd+file_loc
		df = pd.read_csv(file_path, sep=',', parse_dates=[
		                 'UTC'], infer_datetime_format=True)  # UTC is the datetime column
	return df

@home_page.route("/")
def home():
	"""
	call the generate bokeh graph method and pass to a variable.
	it contains two objects: line_script and line_div at indices 0 & 1 respectively
	"""
	return "Hello home from blueprint"
