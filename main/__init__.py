"""
Contains main imports and the app instance.
Register the blueprints
"""
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']='7daf12b8731868c589b15b625907dd7b'

from main.bokeh_embed.routes import home_page

app.register_blueprint(home_page)
