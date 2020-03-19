"""
Blueprint for home module.
Contains: 
1. The route to the home page
2. 
"""
from flask import Blueprint
from flask import redirect, render_template
home_page = Blueprint('home_page',__name__)

# TOOLTIPS TEST
#from products.tooltips import tooltips

@home_page.route("/")
def home():
	context = {}
	return render_template("base/base.html",title="Home", **context)