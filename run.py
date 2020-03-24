"""
used to run the flask app
"""
from main import app

def main():
	app.run(debug=True)
	
if __name__ == "__main__":
	main()