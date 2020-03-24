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

# TOOLTIPS TEST
#from products.tooltips import tooltips
def read_file():
	"""
	read the csv file from location (main->static->file) using pandas.
	we use the os.getcwd() to get the current working directory and the concat with the location.
	return the dataframe
	"""
	cwd = os.getcwd()
	file_loc = r'\main\static\file\DATA1.csv'
	file_path = cwd+file_loc
	df = pd.read_csv(file_path)
	return df

@home_page.route("/")
def home():
	read_file()
	context = {}
	return render_template("home/home.html",title="Home", **context)